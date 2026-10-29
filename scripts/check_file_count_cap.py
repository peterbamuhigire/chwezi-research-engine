#!/usr/bin/env python3
"""Enforce the current 5,000-entry release ceiling for checkout/package trees."""
from __future__ import annotations

import os
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
ENTRY_LIMIT = 5_000
PACKAGE_EXCLUDED_DIRS = {
    ".git",
    ".cache",
    "cache",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
}


def count_entries(root: Path, *, package_oriented: bool) -> int:
    """Count files and symlink entries, pruning symlink directories and package exclusions."""
    count = 0
    walk_errors: list[OSError] = []
    for current, dirs, files in os.walk(root, followlinks=False, onerror=walk_errors.append):
        current_path = Path(current)
        if package_oriented:
            dirs[:] = [name for name in dirs if name not in PACKAGE_EXCLUDED_DIRS]
        retained_dirs: list[str] = []
        for name in dirs:
            child = current_path / name
            if child.is_symlink():
                if not package_oriented or not any(part in PACKAGE_EXCLUDED_DIRS for part in child.relative_to(root).parts):
                    count += 1
            else:
                retained_dirs.append(name)
        dirs[:] = retained_dirs
        for name in files:
            path = current_path / name
            if package_oriented and any(part in PACKAGE_EXCLUDED_DIRS for part in path.relative_to(root).parts):
                continue
            if path.is_file() or path.is_symlink():
                count += 1
    if walk_errors:
        raise OSError(f"could not count all entries under {root}: {walk_errors[0]}")
    return count


def count_violations(full_checkout: int, package_oriented: int, limit: int = ENTRY_LIMIT) -> list[str]:
    violations = []
    if full_checkout > limit:
        violations.append(f"full checkout has {full_checkout} entries; limit is {limit}")
    if package_oriented > limit:
        violations.append(f"package-oriented tree has {package_oriented} entries; limit is {limit}")
    return violations


def main() -> int:
    root = ROOT
    try:
        full_count = count_entries(root, package_oriented=False)
        package_count = count_entries(root, package_oriented=True)
    except OSError as exc:
        print(f"[FAIL] file-count-cap could not complete: {exc}")
        return 1
    print(f"file-count-cap: full-checkout {full_count}/{ENTRY_LIMIT}; package-oriented {package_count}/{ENTRY_LIMIT}")
    violations = count_violations(full_count, package_count)
    if violations:
        for violation in violations:
            print(f"[FAIL] {violation}")
        return 1
    print("PASS: both measured trees are within the configured release ceiling")
    return 0


if __name__ == "__main__":
    sys.exit(main())
