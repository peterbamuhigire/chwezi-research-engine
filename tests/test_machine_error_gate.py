"""Local identifier checks and opt-in installed-adapter integration gates.

SKILL_ENGINE_TARGETS selects textual adapters only. The all-visual integration
gate checks every declared visual adapter independently of that selection;
neither gate establishes semantic, editorial or rendered visual quality.
"""

import json
import os
import tempfile
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "machine-error-gate-baseline.json"
PRESSURE_FIXTURE = ROOT / "tests" / "fixtures" / "machine-error-pressure-fixture.md"
OVERLAY_PRESSURE_FIXTURE = ROOT / "tests" / "fixtures" / "anti-slop-overlay-pressure-fixture.md"


class MachineErrorGateCoverageTests(unittest.TestCase):
    @unittest.skipUnless(os.environ.get("SKILL_ENGINE_LIVE_TESTS") == "1", "requires installed portfolio; opt in explicitly")
    def test_shared_reference_and_all_engine_adapters_expose_every_check(self):
        from scripts.validate_machine_error_gate import resolve_roots, resolve_target, validate
        contract = json.loads(FIXTURE.read_text(encoding="utf-8"))
        selected = os.environ.get("SKILL_ENGINE_TARGETS")
        chosen = set(selected.split(",")) if selected else None
        roots = resolve_roots()
        self.assertEqual(validate(contract, chosen, roots), [])
        required_ids = contract["required_ids"]
        shared_reference = ROOT / contract["shared_reference"]
        self.assertTrue(shared_reference.exists(), shared_reference)
        shared_text = shared_reference.read_text(encoding="utf-8")
        for check_id in required_ids:
            self.assertIn(check_id, shared_text)

        missing = []
        for target in contract["targets"]:
            if chosen and target["engine"] not in chosen:
                continue
            path, description = resolve_target(contract, target, roots)
            if path is None:
                missing.append(f"{target['engine']}: missing {description}")
                continue
            text = path.read_text(encoding="utf-8")
            for check_id in required_ids:
                if check_id not in text:
                    missing.append(f"{target['engine']}: missing {check_id}")
        self.assertEqual([], missing, "\n".join(missing))

    def test_pressure_fixture_covers_each_machine_error_and_exceptions(self):
        text = PRESSURE_FIXTURE.read_text(encoding="utf-8")
        for check_id in [f"ME{i}" for i in range(1, 8)]:
            self.assertIn(f"{check_id}:", text)
        self.assertIn("functional exception", text.lower())

    def test_overlay_pressure_fixture_covers_each_overlay_and_exceptions(self):
        contract = json.loads(FIXTURE.read_text(encoding="utf-8"))
        fixture = ROOT / contract["overlay_pressure_fixture"]
        self.assertEqual(fixture, OVERLAY_PRESSURE_FIXTURE)
        text = fixture.read_text(encoding="utf-8")
        for check_id in contract["overlay_ids"]:
            self.assertIn(f"{check_id}:", text)
        self.assertIn("functional exception", text.lower())

    @unittest.skipUnless(os.environ.get("SKILL_ENGINE_LIVE_TESTS") == "1", "requires all installed visual adapters; separate all-visual integration gate")
    def test_all_visual_adapters_declare_hard_bans_integration(self):
        from scripts.validate_machine_error_gate import resolve_roots, resolve_target
        contract = json.loads(FIXTURE.read_text(encoding="utf-8"))
        roots = resolve_roots()
        for target in contract["visual_targets"]:
            path, description = resolve_target(contract, target, roots)
            self.assertIsNotNone(path, f"{target['engine']}: missing {description}")
            text = path.read_text(encoding="utf-8").lower()
            for phrase in contract["visual_hard_ban_phrases"]:
                self.assertIn(phrase.lower(), text, f"{target['engine']}: missing {phrase}")

    def test_local_contract_and_explicit_scope_fail_closed(self):
        from scripts.validate_machine_error_gate import validate
        contract = json.loads(FIXTURE.read_text(encoding="utf-8"))
        shared = (ROOT / contract["shared_reference"]).read_text(encoding="utf-8")
        for check_id in contract["required_ids"]:
            self.assertIn(check_id, shared)
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "adapter.md"
            target.write_text(shared, encoding="utf-8")
            contract["targets"] = [{"engine": "local", "path": str(target)},
                                   {"engine": "missing", "path": str(target.parent / "absent.md")}]
            self.assertEqual(validate(contract, {"local"}), [])
            self.assertTrue(validate(contract))
            self.assertTrue(validate(contract, {"unknown"}))
            self.assertTrue(validate(contract, set()))
            target.write_text("No gate identifiers", encoding="utf-8")
            self.assertTrue(validate(contract, {"local"}))


if __name__ == "__main__":
    unittest.main()
