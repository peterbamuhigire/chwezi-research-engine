from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "check_file_count_cap", ROOT / "scripts" / "check_file_count_cap.py"
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class FileCountCapTests(unittest.TestCase):
    def test_boundary_fixture_passes_at_limit_and_fails_one_over_for_each_tree(self) -> None:
        fixture = json.loads((ROOT / "tests" / "fixtures" / "file-count-cap.json").read_text(encoding="utf-8"))
        limit = fixture["limit"]
        self.assertEqual(limit, MODULE.ENTRY_LIMIT)
        self.assertEqual(MODULE.count_violations(fixture["at_limit"], fixture["at_limit"], limit), [])
        self.assertEqual(len(MODULE.count_violations(fixture["one_over"], fixture["at_limit"], limit)), 1)
        self.assertEqual(len(MODULE.count_violations(fixture["at_limit"], fixture["one_over"], limit)), 1)

    def test_caller_cannot_raise_the_hard_ceiling(self) -> None:
        with self.assertRaisesRegex(ValueError, "hard ceiling 5000"):
            MODULE.count_violations(5001, 0, limit=6000)

    def test_caller_cannot_set_a_negative_limit(self) -> None:
        with self.assertRaisesRegex(ValueError, "between 0 and the hard ceiling"):
            MODULE.count_violations(0, 0, limit=-1)

    def test_package_count_excludes_named_cache_directories_only(self) -> None:
        with tempfile.TemporaryDirectory(prefix="file-count-cap-") as temp:
            root = Path(temp)
            (root / "skill.md").write_text("x", encoding="utf-8")
            cache = root / "__pycache__"
            cache.mkdir()
            (cache / "compiled.pyc").write_text("x", encoding="utf-8")
            self.assertEqual(MODULE.count_entries(root, package_oriented=False), 2)
            self.assertEqual(MODULE.count_entries(root, package_oriented=True), 1)

    def test_symlinked_directories_are_counted_without_following_them(self) -> None:
        with tempfile.TemporaryDirectory(prefix="file-count-symlink-") as temp:
            root = Path(temp)
            target = root / "target"
            target.mkdir()
            (target / "inside.txt").write_text("x", encoding="utf-8")
            try:
                (root / "alias").symlink_to(target, target_is_directory=True)
            except OSError as exc:
                self.skipTest(f"directory symlink unavailable: {exc}")
            self.assertEqual(MODULE.count_entries(root, package_oriented=False), 2)

    def test_unreadable_walk_fails_closed(self) -> None:
        def failed_walk(root: Path, *, followlinks: bool, onerror):
            onerror(PermissionError("denied"))
            return iter(())

        with patch.object(MODULE.os, "walk", side_effect=failed_walk):
            with self.assertRaises(OSError):
                MODULE.count_entries(ROOT, package_oriented=False)


if __name__ == "__main__":
    unittest.main()
