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


class CompanionNameTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.skill = self.root / "skills" / "source-verification" / "SKILL.md"
        self.skill.parent.mkdir(parents=True)
        shutil.copyfile(SOURCE_SKILL, self.skill)
        self.known = {"source-verification", "source-evaluation", "evidence-claim-graph", "agentic-research-operations"}

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def unresolved(self) -> list[str]:
        return [detail for code, detail in MODULE.assess(self.root, self.skill, self.known) if code == "unresolved_companion_name"]

    def test_names_that_resolve_pass(self) -> None:
        self.assertEqual(self.unresolved(), [])

    def test_retired_skill_name_in_a_companion_list_is_reported(self) -> None:
        text = self.skill.read_text(encoding="utf-8").replace("- `source-evaluation` defines source credibility.", "- `data-quality-assessment` scores datasets.")
        self.skill.write_text(text, encoding="utf-8")
        findings = self.unresolved()
        self.assertEqual(len(findings), 1)
        self.assertIn("`data-quality-assessment`", findings[0])

    def test_declared_external_skill_is_accepted(self) -> None:
        text = self.skill.read_text(encoding="utf-8").replace("- `source-evaluation` defines source credibility.", "- `world-class-engineering` sets the bar.")
        self.skill.write_text(text, encoding="utf-8")
        self.assertEqual(len(self.unresolved()), 1)
        self.known.add("world-class-engineering")
        self.assertEqual(self.unresolved(), [])

    def test_no_check_without_a_known_skill_set(self) -> None:
        text = self.skill.read_text(encoding="utf-8").replace("- `source-evaluation` defines source credibility.", "- `data-quality-assessment` scores datasets.")
        self.skill.write_text(text, encoding="utf-8")
        codes = [code for code, _ in MODULE.assess(self.root, self.skill)]
        self.assertNotIn("unresolved_companion_name", codes)

    def test_names_outside_companion_sections_are_not_checked(self) -> None:
        with self.skill.open("a", encoding="utf-8") as handle:
            handle.write("\n## Notes\n\n- `made-up-skill` is mentioned in passing.\n")
        self.assertEqual(self.unresolved(), [])

    def test_external_registry_is_well_formed(self) -> None:
        names, findings = MODULE.load_external_skills(ROOT)
        self.assertEqual(findings, [])
        self.assertIn("world-class-engineering", names)

    def test_registry_entry_without_engine_is_reported(self) -> None:
        directory = self.root / "tests" / "skill-engine"
        directory.mkdir(parents=True)
        (directory / "external-skills.json").write_text('{"checked": "2026-10-31", "skills": [{"name": "x-y"}]}', encoding="utf-8")
        names, findings = MODULE.load_external_skills(self.root)
        self.assertEqual(names, set())
        self.assertEqual([code for code, _ in findings], ["external_skill_registry"])


if __name__ == "__main__":
    unittest.main()
