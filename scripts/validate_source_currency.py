#!/usr/bin/env python3
"""Fail-closed validation for source freshness and review metadata.

A register may carry an optional top-level ``superseded_by`` key naming a newer
register in the same directory. Its overdue records are then accepted as history
only when the successor exists, passes this validator on the same date, and lists
every old source id in its ``dispositions``. Any other finding still fails, and a
failed supersession leaves the overdue findings in place.

``--registers-dir`` checks every JSON file that has a ``sources`` key; other JSON
files in the directory (for example verifier output) are skipped by name.
"""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path, PureWindowsPath
from typing import Any

REQUIRED = {"id", "accessed", "verified_at", "review_after", "freshness_class"}
CURRENT_CLASSES = {"volatile", "current", "regulatory", "market", "platform", "context-bound"}


def parse_date(value: Any, field: str, source_id: str, findings: list[str]) -> date | None:
    if not isinstance(value, str) or not value.strip():
        findings.append(f"{source_id}: {field} is required as ISO date")
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        findings.append(f"{source_id}: {field} is not ISO date: {value}")
        return None


def _validate_manifest(path: Path, as_of: date | None = None) -> tuple[list[str], dict[str, Any] | None]:
    """Return (findings, parsed manifest or None when it could not be read)."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"cannot read manifest: {exc}"], None
    if not isinstance(data, dict):
        return ["manifest must be an object"], None
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        return ["sources must be a nonempty list"], None
    findings: list[str] = []
    source_map: dict[str, dict[str, Any]] = {}
    check_date = as_of or date.today()
    for source in sources:
        if not isinstance(source, dict):
            findings.append("source entries must be objects")
            continue
        source_id = source.get("id")
        if not isinstance(source_id, str) or not source_id.strip():
            findings.append("source id must be a nonempty string")
            continue
        if source_id in source_map:
            findings.append(f"duplicate source id: {source_id}")
            continue
        source_map[source_id] = source
        for field in sorted(REQUIRED):
            if field not in source:
                findings.append(f"{source_id}: missing {field}")
        accessed = parse_date(source.get("accessed"), "accessed", source_id, findings)
        verified = parse_date(source.get("verified_at"), "verified_at", source_id, findings)
        review_after = parse_date(source.get("review_after"), "review_after", source_id, findings)
        freshness_value = source.get("freshness_class")
        freshness = freshness_value.strip().lower() if isinstance(freshness_value, str) else ""
        if freshness not in CURRENT_CLASSES | {"static", "historical"}:
            findings.append(f"{source_id}: unsupported freshness_class: {freshness}")
        if freshness in CURRENT_CLASSES and not (source.get("publication_date") or source.get("revision_date") or source.get("as_of")):
            findings.append(f"{source_id}: current source requires publication_date, revision_date, or as_of")
        if freshness == "context-bound" and (
            not isinstance(source.get("scope"), str) or not source["scope"].strip()
        ):
            findings.append(f"{source_id}: context-bound source requires nonempty scope")
        for field in ("publication_date", "revision_date", "as_of"):
            if field in source:
                parse_date(source.get(field), field, source_id, findings)
        if accessed and verified and verified < accessed:
            findings.append(f"{source_id}: verified_at precedes accessed")
        for field, value in (("accessed", accessed), ("verified_at", verified)):
            if value and value > check_date:
                findings.append(f"{source_id}: {field} is in the future as of {check_date.isoformat()}")
        if verified and review_after and review_after < verified:
            findings.append(f"{source_id}: review_after precedes verified_at")
        if review_after and review_after < check_date:
            findings.append(f"{source_id}: review_after is overdue as of {check_date.isoformat()}")
    claims = data.get("claims", [])
    if not isinstance(claims, list):
        findings.append("claims must be a list")
        return findings, data
    claim_ids: set[str] = set()
    for claim in claims:
        if not isinstance(claim, dict):
            findings.append("claim entries must be objects")
            continue
        claim_id = claim.get("id")
        if not isinstance(claim_id, str) or not claim_id.strip():
            findings.append("claim id must be a nonempty string")
            continue
        if claim_id in claim_ids:
            findings.append(f"duplicate claim id: {claim_id}")
        claim_ids.add(claim_id)
        current = claim.get("requires_currentness")
        if not isinstance(current, bool):
            findings.append(f"{claim_id}: requires_currentness must be boolean")
        source_ids = claim.get("source_ids")
        if not isinstance(source_ids, list):
            findings.append(f"{claim_id}: source_ids must be a list")
            continue
        if current is True and not source_ids:
            findings.append(f"{claim_id}: current claim requires nonempty source_ids")
        seen_sources: set[str] = set()
        for source_id in source_ids:
            if not isinstance(source_id, str) or not source_id.strip():
                findings.append(f"{claim_id}: source_ids entries must be nonempty strings")
                continue
            if source_id in seen_sources:
                findings.append(f"{claim_id}: duplicate source id: {source_id}")
            seen_sources.add(source_id)
            source = source_map.get(source_id)
            if source is None:
                findings.append(f"{claim_id}: unknown source {source_id}")
            elif current is True and (
                not isinstance(source.get("freshness_class"), str)
                or source["freshness_class"].strip().lower() not in CURRENT_CLASSES
            ):
                findings.append(f"{claim_id}: source {source_id} is not currentness-qualified")
    return findings, data


OVERDUE_SUFFIX = "review_after is overdue as of"


def _supersession_findings(
    path: Path, data: dict[str, Any], as_of: date | None, seen: frozenset[Path]
) -> tuple[bool, list[str]]:
    """Decide whether this register's successor accepts its overdue records.

    Returns (accepted, reasons). Reasons explain a rejection or describe the
    acceptance for the printed notes.
    """
    target = data.get("superseded_by")
    if (
        not isinstance(target, str)
        or not target.strip()
        or PureWindowsPath(target).anchor
        or ":" in target
        or ".." in target.replace("\\", "/").split("/")
    ):
        return False, ["superseded_by must be a relative file name in the same directory tree"]
    successor = (path.parent / target).resolve()
    if not successor.is_relative_to(path.parent.resolve()):
        return False, ["superseded_by must be a relative file name in the same directory tree"]
    if successor == path.resolve() or successor in seen:
        return False, ["superseded_by points back to a register already in the chain"]
    if not successor.is_file():
        return False, [f"superseded_by register not found: {target}"]
    findings, notes = _validate_with_notes(successor, as_of, seen | {path.resolve()})
    if findings:
        return False, [f"successor {target} has {len(findings)} finding(s)"]
    try:
        successor_data = json.loads(successor.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return False, [f"successor {target} is unreadable: {exc}"]
    dispositions = successor_data.get("dispositions", [])
    covered = {item.get("old_source_id") for item in dispositions if isinstance(item, dict)}
    old_ids = [source.get("id") for source in data.get("sources", []) if isinstance(source, dict)]
    missing = [source_id for source_id in old_ids if source_id not in covered]
    if missing:
        return False, [f"successor {target} has no disposition for: {', '.join(map(str, missing))}"]
    return True, [f"accepted: successor {target} validates and dispositions all {len(old_ids)} record(s)"]


def _validate_with_notes(path: Path, as_of: date | None, seen: frozenset[Path]) -> tuple[list[str], list[str]]:
    findings, data = _validate_manifest(path, as_of)
    notes: list[str] = []
    if data is None or "superseded_by" not in data:
        return findings, notes
    accepted, reasons = _supersession_findings(path, data, as_of, seen)
    if accepted:
        kept = [item for item in findings if OVERDUE_SUFFIX not in item]
        dropped = len(findings) - len(kept)
        notes.append(f"SUPERSEDED: {dropped} overdue record finding(s) accepted as history; {reasons[0]}")
        return kept, notes
    return findings + [f"superseded_by not accepted: {reason}" for reason in reasons], notes


def validate_manifest(path: Path, as_of: date | None = None) -> list[str]:
    """Return findings for one register; the supersession rule is applied."""
    return _validate_with_notes(path.resolve(), as_of, frozenset())[0]


def validate_manifest_with_notes(path: Path, as_of: date | None = None) -> tuple[list[str], list[str]]:
    """Return (findings, notes) for one register."""
    return _validate_with_notes(path.resolve(), as_of, frozenset())


def validate_registers_dir(directory: Path, as_of: date | None = None) -> tuple[list[str], list[str]]:
    """Check every register in a directory; return (findings, notes)."""
    findings: list[str] = []
    notes: list[str] = []
    if not directory.is_dir():
        return [f"registers directory not found: {directory}"], notes
    checked = 0
    for path in sorted(directory.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            findings.append(f"{path.name}: cannot read: {exc}")
            continue
        if not isinstance(data, dict) or "sources" not in data:
            notes.append(f"skipped {path.name}: not a register (no `sources` key)")
            continue
        checked += 1
        register_findings, register_notes = validate_manifest_with_notes(path, as_of)
        findings.extend(f"{path.name}: {item}" for item in register_findings)
        notes.extend(f"{path.name}: {item}" for item in register_notes)
    if checked == 0:
        findings.append("no register with a `sources` key found")
    notes.append(f"registers checked: {checked}")
    return findings, notes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", nargs="?", type=Path)
    parser.add_argument("--registers-dir", type=Path, help="Check every register (JSON file with a `sources` key) in this directory.")
    parser.add_argument("--as-of", type=date.fromisoformat, default=date.today())
    args = parser.parse_args()
    if bool(args.manifest) == bool(args.registers_dir):
        parser.error("give exactly one of a manifest path or --registers-dir")
    if args.registers_dir:
        label = str(args.registers_dir)
        findings, notes = validate_registers_dir(args.registers_dir.resolve(), args.as_of)
    else:
        label = str(args.manifest)
        findings, notes = validate_manifest_with_notes(args.manifest.resolve(), args.as_of)
    print("source-currency-validator:")
    print(f"- manifest: {label}")
    print(f"- as-of: {args.as_of.isoformat()}")
    print(f"- findings: {len(findings)}")
    for note in notes:
        print(f"- note: {note}")
    for finding in findings:
        print(f"[FAIL] {finding}")
    if not findings:
        print("PASS: metadata/date checks only; claim support NOT ASSESSED")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
