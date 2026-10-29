#!/usr/bin/env python3
"""Reject host-specific absolute paths and sibling-checkout links in active docs."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FILES = [ROOT / "AGENTS.md", ROOT / "README.md"]
DEFAULT_FILES.extend(sorted((ROOT / "skills").rglob("*.md")))
ABSOLUTE_PATH = re.compile(
    r"(?i)(?:\b[A-Z]:[\\/][^\s`<>]+|(?<![:/A-Za-z0-9.])/(?:home|Users|mnt|tmp|root|opt|workspace|private|Volumes)(?:/|$)[^\s`<>]*)"
)
SIBLING_CHECKOUT = re.compile(
    r"(?i)(?:\.\.[\\/])+chwezi-[a-z0-9-]+(?:[\\/]|$)[^\s`<>]*"
)


def find_nonportable_references(text: str) -> list[tuple[int, str, str]]:
    """Return (line, code, match) for absolute paths or sibling-checkout links."""
    findings: list[tuple[int, str, str]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for match in ABSOLUTE_PATH.finditer(line):
            findings.append((line_number, "host-absolute-path", match.group(0)))
        for match in SIBLING_CHECKOUT.finditer(line):
            findings.append((line_number, "sibling-checkout-link", match.group(0)))
    return findings


def check_files(paths: list[Path]) -> list[tuple[Path, int, str, str]]:
    findings: list[tuple[Path, int, str, str]] = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            findings.append((path, 0, "unreadable-file", str(exc)))
            continue
        findings.extend((path, *finding) for finding in find_nonportable_references(text))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="Markdown files to scan; defaults to active router, README and skills")
    args = parser.parse_args()
    paths = [path if path.is_absolute() else ROOT / path for path in args.paths] if args.paths else DEFAULT_FILES
    findings = check_files(paths)
    print(f"portable-reference-check: {len(paths)} files, {len(findings)} findings")
    for path, line, code, match in findings:
        print(f"[FAIL] {path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}:{line}: {code}: {match}")
    if not findings:
        print("PASS: no host-specific absolute paths or sibling-checkout links in scanned active documents")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
