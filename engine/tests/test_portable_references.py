from __future__ import annotations

import importlib.util
from pathlib import Path
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


if __name__ == "__main__":
    unittest.main()
