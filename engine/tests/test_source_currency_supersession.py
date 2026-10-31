from __future__ import annotations

from datetime import date
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "validate_source_currency", ROOT / "scripts" / "validate_source_currency.py"
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

AS_OF = date(2026, 10, 31)


def source(source_id: str, review_after: str) -> dict:
    return {
        "id": source_id,
        "accessed": "2026-09-01",
        "verified_at": "2026-09-01",
        "review_after": review_after,
        "freshness_class": "platform",
        "as_of": "2026-09-01",
    }


def register(*sources: dict, **extra: object) -> dict:
    return {"register_id": "test", "sources": list(sources), "claims": [], **extra}


def disposition(old_id: str) -> dict:
    return {"old_source_id": old_id, "state": "superseded", "reason": "test"}


class SupersessionTests(unittest.TestCase):
    def write(self, directory: Path, name: str, payload: dict) -> Path:
        path = directory / name
        path.write_text(json.dumps(payload), encoding="utf-8")
        return path

    def test_overdue_register_without_supersession_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write(Path(tmp), "old.json", register(source("A", "2026-10-03")))
            findings = MODULE.validate_manifest(path, AS_OF)
            self.assertEqual(len(findings), 1)
            self.assertIn("overdue", findings[0])

    def test_valid_successor_with_full_dispositions_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            self.write(directory, "new.json", register(source("N", "2027-01-01"), dispositions=[disposition("A"), disposition("B")]))
            old = self.write(directory, "old.json", register(source("A", "2026-10-03"), source("B", "2026-10-03"), superseded_by="new.json"))
            findings, notes = MODULE.validate_manifest_with_notes(old, AS_OF)
            self.assertEqual(findings, [])
            self.assertTrue(any(note.startswith("SUPERSEDED: 2 overdue") for note in notes))

    def test_missing_successor_keeps_overdue_findings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            old = self.write(Path(tmp), "old.json", register(source("A", "2026-10-03"), superseded_by="absent.json"))
            findings = MODULE.validate_manifest(old, AS_OF)
            self.assertTrue(any("overdue" in item for item in findings))
            self.assertTrue(any("superseded_by not accepted" in item and "not found" in item for item in findings))

    def test_overdue_successor_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            self.write(directory, "new.json", register(source("N", "2026-10-05"), dispositions=[disposition("A")]))
            old = self.write(directory, "old.json", register(source("A", "2026-10-03"), superseded_by="new.json"))
            findings = MODULE.validate_manifest(old, AS_OF)
            self.assertTrue(any("successor new.json has 1 finding" in item for item in findings))
            self.assertTrue(any("overdue" in item and item.startswith("A:") for item in findings))

    def test_undispositioned_old_record_is_rejected_and_named(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            self.write(directory, "new.json", register(source("N", "2027-01-01"), dispositions=[disposition("A")]))
            old = self.write(directory, "old.json", register(source("A", "2026-10-03"), source("B", "2026-10-03"), superseded_by="new.json"))
            findings = MODULE.validate_manifest(old, AS_OF)
            self.assertTrue(any("no disposition for: B" in item for item in findings))

    def test_unsafe_superseded_by_values_are_rejected(self) -> None:
        for value in ("../new.json", "/tmp/new.json", "", None, 7):
            with self.subTest(value=value), tempfile.TemporaryDirectory() as tmp:
                old = self.write(Path(tmp), "old.json", register(source("A", "2026-10-03"), superseded_by=value))
                findings = MODULE.validate_manifest(old, AS_OF)
                self.assertTrue(any("must be a relative file name" in item for item in findings), findings)

    def test_other_finding_in_a_superseded_register_still_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            self.write(directory, "new.json", register(source("N", "2027-01-01"), dispositions=[disposition("A")]))
            broken = source("A", "2026-10-03")
            del broken["verified_at"]
            old = self.write(directory, "old.json", register(broken, superseded_by="new.json"))
            findings = MODULE.validate_manifest(old, AS_OF)
            self.assertTrue(any("missing verified_at" in item for item in findings), findings)

    def test_supersession_cycle_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            first = self.write(directory, "a.json", register(source("A", "2026-10-03"), superseded_by="b.json", dispositions=[disposition("B")]))
            self.write(directory, "b.json", register(source("B", "2026-10-03"), superseded_by="a.json", dispositions=[disposition("A")]))
            findings = MODULE.validate_manifest(first, AS_OF)
            self.assertTrue(any("superseded_by not accepted" in item for item in findings), findings)


class RegistersDirectoryTests(unittest.TestCase):
    def test_non_register_json_is_skipped_by_name(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "good.json").write_text(json.dumps(register(source("A", "2027-01-01"))), encoding="utf-8")
            (directory / "verifier-output.json").write_text(json.dumps({"results": []}), encoding="utf-8")
            findings, notes = MODULE.validate_registers_dir(directory, AS_OF)
            self.assertEqual(findings, [])
            self.assertIn("skipped verifier-output.json: not a register (no `sources` key)", notes)
            self.assertIn("registers checked: 1", notes)

    def test_findings_carry_the_register_file_name(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "stale.json").write_text(json.dumps(register(source("A", "2026-10-03"))), encoding="utf-8")
            findings, _ = MODULE.validate_registers_dir(directory, AS_OF)
            self.assertEqual(len(findings), 1)
            self.assertTrue(findings[0].startswith("stale.json: A:"))

    def test_directory_with_no_register_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            findings, _ = MODULE.validate_registers_dir(Path(tmp), AS_OF)
            self.assertEqual(findings, ["no register with a `sources` key found"])

    def test_unreadable_json_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "bad.json").write_text("{not json", encoding="utf-8")
            findings, _ = MODULE.validate_registers_dir(directory, AS_OF)
            self.assertTrue(any(item.startswith("bad.json: cannot read") for item in findings))

    def test_shipped_registers_are_current_on_the_cycle_date(self) -> None:
        findings, notes = MODULE.validate_registers_dir(ROOT / "docs" / "source-registers", AS_OF)
        self.assertEqual(findings, [])
        self.assertTrue(any(note.startswith("registers checked:") for note in notes))


if __name__ == "__main__":
    unittest.main()
