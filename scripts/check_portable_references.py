#!/usr/bin/env python3
"""Reject host-specific absolute paths, links that leave the repository, and dead relative links.

Findings: ``host-absolute-path``, ``sibling-checkout-link`` (a ``../chwezi-*`` pattern),
``link-escapes-repository`` (any relative Markdown link that resolves outside the
repository root, whatever the sibling is called) and ``broken-relative-link`` (a
relative link whose target does not exist). Fenced code blocks and inline code are
not scanned for links.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SCOPE_FILES = ("AGENTS.md", "README.md", "CLAUDE.md", "CONTRIBUTING.md", "PROJECT_BRIEF.md", "docs/skill-authoring-standard.md")
SCOPE_TREES = ("skills", "rules", "templates", "docs/quality-gates", "docs/ai-prompting")


def default_files(root: Path = ROOT) -> list[Path]:
    files = [root / name for name in SCOPE_FILES if (root / name).is_file()]
    for tree in SCOPE_TREES:
        files.extend(sorted((root / tree).rglob("*.md")))
    return files


DEFAULT_FILES = default_files()
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
INLINE_CODE = re.compile(r"`[^`\n]*`")
SCHEME = re.compile(r"^[a-z][a-z0-9+.-]*:", re.IGNORECASE)
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


def find_link_problems(path: Path, text: str, root: Path = ROOT) -> list[tuple[int, str, str]]:
    """Return (line, code, target) for relative links that leave the repository or do not resolve."""
    findings: list[tuple[int, str, str]] = []
    resolved_root = root.resolve()
    in_fence = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in MARKDOWN_LINK.finditer(INLINE_CODE.sub("", line)):
            target = match.group(1)
            if SCHEME.match(target) or target.startswith(("#", "<")):
                continue
            clean = unquote(target.split("#", 1)[0])
            if not clean or ABSOLUTE_PATH.match(clean):
                continue
            beside = (path.parent / clean).resolve()
            from_root = (resolved_root / clean).resolve()
            candidates = [item for item in (beside, from_root) if item.is_relative_to(resolved_root)]
            if any(item.exists() for item in candidates):
                continue
            code = "broken-relative-link" if candidates else "link-escapes-repository"
            findings.append((line_number, code, target))
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
        findings.extend((path, *finding) for finding in find_link_problems(path, text))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="Markdown files to scan; defaults to the active router, top-level guides, authoring standard, skills, rules, templates and quality gates")
    args = parser.parse_args()
    paths = [path if path.is_absolute() else ROOT / path for path in args.paths] if args.paths else DEFAULT_FILES
    findings = check_files(paths)
    print(f"portable-reference-check: {len(paths)} files, {len(findings)} findings")
    for path, line, code, match in findings:
        print(f"[FAIL] {path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}:{line}: {code}: {match}")
    if not findings:
        print("PASS: no host-specific absolute paths, repository-escaping links or dead relative links in scanned active documents")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
