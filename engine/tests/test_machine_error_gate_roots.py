from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "validate_machine_error_gate", ROOT / "scripts" / "validate_machine_error_gate.py"
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

FIXTURE = ROOT / "tests" / "fixtures" / "machine-error-gate-baseline.json"
HOST_PATH = re.compile(r"(?i)(?:^[A-Z]:[\\/]|^/|[\\/]wamp64[\\/]|[\\/]Users[\\/]|[\\/]home[\\/])")


def base_contract() -> dict:
    contract = json.loads(FIXTURE.read_text(encoding="utf-8"))
    contract["targets"] = []
    contract["engine_aliases"] = {"canonical-name": ["local-name"]}
    return contract


def write_target(root: Path, directory: str, relative: str, text: str) -> None:
    path = root / directory / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class MachineErrorGateRootTests(unittest.TestCase):
    def setUp(self) -> None:
        self.contract = base_contract()
        self.all_ids = " ".join(self.contract["required_ids"])

    def test_shipped_fixture_holds_no_host_path(self) -> None:
        contract = json.loads(FIXTURE.read_text(encoding="utf-8"))
        for group in ("targets", "visual_targets"):
            for target in contract[group]:
                self.assertNotRegex(target["path"], HOST_PATH, f"{group}/{target['engine']}")
                self.assertTrue(target.get("engine_dir") or target.get("self"), f"{group}/{target['engine']}")

    def test_resolves_through_alias_under_explicit_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_target(root, "local-name", "skills/x.md", self.all_ids)
            self.contract["targets"] = [{"engine": "a", "engine_dir": "canonical-name", "path": "skills/x.md"}]
            resolved: list[str] = []
            self.assertEqual(MODULE.validate(self.contract, None, [root], resolved), [])
            self.assertEqual(resolved, ["a: local-name/skills/x.md"])

    def test_canonical_name_wins_over_alias(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_target(root, "canonical-name", "skills/x.md", self.all_ids)
            write_target(root, "local-name", "skills/x.md", "no identifiers")
            self.contract["targets"] = [{"engine": "a", "engine_dir": "canonical-name", "path": "skills/x.md"}]
            self.assertEqual(MODULE.validate(self.contract, None, [root]), [])

    def test_second_root_is_searched(self) -> None:
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            write_target(Path(second), "canonical-name", "skills/x.md", self.all_ids)
            self.contract["targets"] = [{"engine": "a", "engine_dir": "canonical-name", "path": "skills/x.md"}]
            self.assertEqual(MODULE.validate(self.contract, None, [Path(first), Path(second)]), [])

    def test_unresolvable_target_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            self.contract["targets"] = [{"engine": "a", "engine_dir": "canonical-name", "path": "skills/x.md"}]
            errors = MODULE.validate(self.contract, None, [Path(directory)])
            self.assertEqual(len(errors), 1)
            self.assertIn("a: target missing", errors[0])
            self.assertIn("local-name", errors[0])

    def test_missing_identifier_is_reported_with_engine_name(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_target(root, "canonical-name", "skills/x.md", "ME1 only")
            self.contract["targets"] = [{"engine": "a", "engine_dir": "canonical-name", "path": "skills/x.md"}]
            errors = MODULE.validate(self.contract, None, [root])
            self.assertEqual(len(errors), 1)
            self.assertTrue(errors[0].startswith("a: missing ME2"))

    def test_engine_selection_skips_an_unbound_target(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_target(root, "canonical-name", "skills/x.md", self.all_ids)
            self.contract["targets"] = [
                {"engine": "a", "engine_dir": "canonical-name", "path": "skills/x.md"},
                {"engine": "unbound", "engine_dir": "absent-engine", "path": "skills/y.md"},
            ]
            self.assertEqual(MODULE.validate(self.contract, {"a"}, [root]), [])
            self.assertTrue(MODULE.validate(self.contract, None, [root]))

    def test_self_target_resolves_inside_this_checkout(self) -> None:
        self.contract["targets"] = [{"engine": "me", "self": True, "path": "skills/anti-ai-slop/SKILL.md"}]
        self.assertEqual(MODULE.validate(self.contract, None, []), [])

    def test_explicit_absolute_path_is_still_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "adapter.md"
            path.write_text(self.all_ids, encoding="utf-8")
            self.contract["targets"] = [{"engine": "a", "path": str(path)}]
            self.assertEqual(MODULE.validate(self.contract, None, []), [])

    def test_relative_path_without_engine_dir_fails_closed(self) -> None:
        self.contract["targets"] = [{"engine": "a", "path": "skills/x.md"}]
        errors = MODULE.validate(self.contract, None, [ROOT])
        self.assertEqual(len(errors), 1)
        self.assertIn("no engine_dir", errors[0])

    def test_roots_from_environment_follow_explicit_roots(self) -> None:
        separator = MODULE.os.pathsep
        roots = MODULE.resolve_roots([Path("first")], {MODULE.ENV_ROOTS: f"second{separator}third"})
        self.assertEqual([root.name for root in roots], ["first", "second", "third"])

    def test_default_root_is_parent_of_checkout(self) -> None:
        self.assertEqual(MODULE.resolve_roots(None, {}), [ROOT.parent])


if __name__ == "__main__":
    unittest.main()
