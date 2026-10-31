from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "check_portable_references", ROOT / "scripts" / "check_portable_references.py"
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PortableReferenceTests(unittest.TestCase):
    def test_rejects_windows_machine_path(self) -> None:
        findings = MODULE.find_nonportable_references(r"Use C:\wamp64\www\engine\AGENTS.md")
        self.assertEqual(findings[0][1], "host-absolute-path")

    def test_rejects_windows_forward_slash_path(self) -> None:
        findings = MODULE.find_nonportable_references("Read C:/Users/Peter/engine/SKILL.md")
        self.assertEqual(findings[0][1], "host-absolute-path")

    def test_rejects_unix_checkout_path(self) -> None:
        findings = MODULE.find_nonportable_references("Open /home/peter/skill-engines/engine/SKILL.md")
        self.assertEqual(findings[0][1], "host-absolute-path")

    def test_rejects_other_rooted_unix_paths(self) -> None:
        findings = MODULE.find_nonportable_references("Open /opt/runtime/engine/SKILL.md")
        self.assertEqual(findings[0][1], "host-absolute-path")

    def test_rejects_sibling_checkout_relative_link(self) -> None:
        findings = MODULE.find_nonportable_references("See ../../../chwezi-dev-engine/skills/example/SKILL.md")
        self.assertEqual(findings[0][1], "sibling-checkout-link")

    def test_rejects_windows_sibling_checkout_relative_link(self) -> None:
        findings = MODULE.find_nonportable_references(r"See ..\..\chwezi-dev-engine\skills\example\SKILL.md")
        self.assertEqual(findings[0][1], "sibling-checkout-link")

    def test_keeps_public_url_and_local_relative_path(self) -> None:
        findings = MODULE.find_nonportable_references(
            "See https://github.com/peterbamuhigire/chwezi-dev-engine and ../references/check.md"
        )
        self.assertEqual(findings, [])


class LinkProblemTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "repo"
        (self.root / "skills" / "a").mkdir(parents=True)
        (self.root / "docs").mkdir()
        (self.root / "docs" / "present.md").write_text("x", encoding="utf-8")
        (self.root / "docs" / "with space.md").write_text("x", encoding="utf-8")
        (self.root / "skills" / "a" / "SKILL.md").write_text("x", encoding="utf-8")
        self.page = self.root / "skills" / "a" / "SKILL.md"

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def problems(self, text: str) -> list[tuple[int, str, str]]:
        return MODULE.find_link_problems(self.page, text, self.root)

    def test_link_that_leaves_the_repository_under_any_sibling_name(self) -> None:
        text = "See [standard](../../../skills-web-dev/references/standard.md)."
        self.assertEqual(MODULE.find_nonportable_references(text), [], "the name pattern alone misses this")
        self.assertEqual([item[1] for item in self.problems(text)], ["link-escapes-repository"])

    def test_dead_link_inside_the_repository(self) -> None:
        self.assertEqual([item[1] for item in self.problems("[x](../../docs/absent.md)")], ["broken-relative-link"])

    def test_existing_links_pass_from_the_file_or_from_the_root(self) -> None:
        text = "[a](../../docs/present.md) [b](docs/present.md) [c](docs/with%20space.md#anchor)"
        self.assertEqual(self.problems(text), [])

    def test_external_anchor_and_mail_links_are_ignored(self) -> None:
        text = "[a](https://example.org/x.md) [b](#top) [c](mailto:a@example.org) [d](<angle>)"
        self.assertEqual(self.problems(text), [])

    def test_fenced_and_inline_code_are_not_scanned(self) -> None:
        text = "```\n[x](docs/absent.md)\n```\nInline `[y](docs/absent.md)` stays.\n"
        self.assertEqual(self.problems(text), [])

    def test_line_number_is_reported(self) -> None:
        findings = self.problems("one\ntwo [x](docs/absent.md)\n")
        self.assertEqual(findings, [(2, "broken-relative-link", "docs/absent.md")])

    def test_default_scope_covers_author_facing_guides(self) -> None:
        names = {path.relative_to(ROOT).as_posix() for path in MODULE.default_files(ROOT)}
        for expected in ("AGENTS.md", "CONTRIBUTING.md", "docs/skill-authoring-standard.md", "skills/source-evaluation/SKILL.md"):
            self.assertIn(expected, names)


if __name__ == "__main__":
    unittest.main()
