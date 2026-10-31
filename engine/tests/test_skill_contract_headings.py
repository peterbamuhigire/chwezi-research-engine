from __future__ import annotations

import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "skill_contract_validator", ROOT / "scripts" / "skill_contract_validator.py"
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

SOURCE_SKILL = ROOT / "skills" / "source-verification" / "SKILL.md"


class DuplicateHeadingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.skill = self.root / "skills" / "source-verification" / "SKILL.md"
        self.skill.parent.mkdir(parents=True)
        shutil.copyfile(SOURCE_SKILL, self.skill)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def codes(self) -> list[str]:
        return [code for code, _ in MODULE.assess(self.root, self.skill)]

    def test_shipped_skill_has_no_repeated_heading(self) -> None:
        self.assertNotIn("duplicate_heading", self.codes())

    def test_repeated_non_contract_heading_is_reported(self) -> None:
        with self.skill.open("a", encoding="utf-8") as handle:
            handle.write("\n## Companion Skills\n\n- `evidence-claim-graph`\n")
        findings = [detail for code, detail in MODULE.assess(self.root, self.skill) if code == "duplicate_heading"]
        self.assertEqual(len(findings), 1)
        self.assertIn("'companion skills' appears 2 times", findings[0])

    def test_heading_case_does_not_hide_a_repeat(self) -> None:
        with self.skill.open("a", encoding="utf-8") as handle:
            handle.write("\n## See also\n\n- a\n\n## See Also\n\n- b\n")
        self.assertIn("duplicate_heading", self.codes())

    def test_repeated_contract_heading_keeps_its_own_code(self) -> None:
        with self.skill.open("a", encoding="utf-8") as handle:
            handle.write("\n## Anti-Patterns\n\n- again\n")
        codes = self.codes()
        self.assertIn("duplicate_contract_section", codes)
        self.assertNotIn("duplicate_heading", codes)

    def test_third_level_headings_are_not_counted(self) -> None:
        with self.skill.open("a", encoding="utf-8") as handle:
            handle.write("\n### Notes\n\ntext\n\n### Notes\n\ntext\n")
        self.assertNotIn("duplicate_heading", self.codes())


if __name__ == "__main__":
    unittest.main()
