"""Check textual gate identifier presence, not semantic, editorial or visual quality.

Targets live in other engines' checkouts. Each target names the engine directory
and a path inside it; the directory is looked up under one or more portfolio
roots, so the same fixture works on every host. Roots come from ``--engines-root``
(repeatable), then the ``CHWEZI_ENGINES_ROOT`` environment variable (separated by
the platform path separator), and default to the directory that holds this
checkout. A target that cannot be resolved is an error, never a pass.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = ROOT / "tests" / "fixtures" / "machine-error-gate-baseline.json"
ENV_ROOTS = "CHWEZI_ENGINES_ROOT"


def load_contract(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_roots(explicit: list[Path] | None = None, environ: dict[str, str] | None = None) -> list[Path]:
    """Return the portfolio roots to search, in priority order."""
    environment = os.environ if environ is None else environ
    roots = [Path(item).expanduser() for item in (explicit or [])]
    roots.extend(Path(item).expanduser() for item in environment.get(ENV_ROOTS, "").split(os.pathsep) if item)
    return roots or [ROOT.parent]


def candidate_names(contract: dict, target: dict) -> list[str]:
    engine_dir = target.get("engine_dir")
    if not engine_dir:
        return []
    aliases = contract.get("engine_aliases", {}).get(engine_dir, [])
    return [engine_dir, *[alias for alias in aliases if alias != engine_dir]]


def resolve_target(contract: dict, target: dict, roots: list[Path]) -> tuple[Path | None, str]:
    """Return (path, description). The path is None when the target cannot be found."""
    relative = target["path"]
    if target.get("self"):
        path = ROOT / relative
        return (path if path.is_file() else None), f"this checkout/{relative}"
    names = candidate_names(contract, target)
    if not names:
        absolute = Path(relative)
        if absolute.is_absolute():
            return (absolute if absolute.is_file() else None), "explicit absolute path"
        return None, f"no engine_dir and path is not absolute: {relative}"
    for root in roots:
        for name in names:
            path = root / name / relative
            if path.is_file():
                return path, f"{name}/{relative}"
    return None, f"{names[0]}/{relative} (tried names: {', '.join(names)}; {len(roots)} root(s))"


def validate(
    contract: dict,
    engines: set[str] | None = None,
    roots: list[Path] | None = None,
    resolved: list[str] | None = None,
) -> list[str]:
    required_ids = contract["required_ids"]
    errors: list[str] = []
    known = {target["engine"] for target in contract["targets"]}
    if not contract["targets"]:
        return ["targets must not be empty"]
    if engines is not None and (not engines or engines - known):
        return ["engine selection must be non-empty and contain only registered engines"]
    search_roots = roots if roots is not None else resolve_roots()
    shared = ROOT / contract["shared_reference"]
    if not shared.exists():
        errors.append(f"shared reference missing: {shared}")
        return errors

    shared_text = shared.read_text(encoding="utf-8")
    for check_id in required_ids:
        if check_id not in shared_text:
            errors.append(f"shared reference missing {check_id}: {shared}")

    for target in contract["targets"]:
        if engines is not None and target["engine"] not in engines:
            continue
        path, description = resolve_target(contract, target, search_roots)
        if path is None:
            errors.append(f"{target['engine']}: target missing: {description}")
            continue
        if resolved is not None:
            resolved.append(f"{target['engine']}: {description}")
        text = path.read_text(encoding="utf-8")
        missing = [check_id for check_id in required_ids if check_id not in text]
        if missing:
            errors.append(f"{target['engine']}: missing {', '.join(missing)}: {description}")

    overlay_fixture_value = contract.get("overlay_pressure_fixture")
    overlay_ids = contract.get("overlay_ids", [])
    if overlay_fixture_value and overlay_ids:
        overlay_fixture = ROOT / overlay_fixture_value
        if not overlay_fixture.exists():
            errors.append(f"overlay pressure fixture missing: {overlay_fixture}")
        else:
            fixture_text = overlay_fixture.read_text(encoding="utf-8")
            for check_id in overlay_ids:
                if f"{check_id}:" not in fixture_text:
                    errors.append(f"overlay pressure fixture missing {check_id}: {overlay_fixture}")
            if "functional exception" not in fixture_text.lower():
                errors.append(f"overlay pressure fixture missing functional exception: {overlay_fixture}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--engine", action="append", help="Select textual gate targets only; repeat for each engine. Omit to require all textual targets. Visual hard-ban adapters have a separate all-visual integration gate.")
    parser.add_argument("--engines-root", action="append", type=Path, help=f"Directory holding engine checkouts; repeat for several. Falls back to ${ENV_ROOTS}, then to the parent of this checkout.")
    args = parser.parse_args()
    contract = load_contract(args.fixture)
    selected = set(args.engine) if args.engine else None
    resolved: list[str] = []
    errors = validate(contract, selected, resolve_roots(args.engines_root), resolved)
    if errors:
        print("MACHINE_ERROR_GATE: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("MACHINE_ERROR_GATE: PASS (identifier presence only)")
    print("- semantic, editorial and visual verification: NOT ASSESSED")
    print("- visual hard-ban adapters: separate all-visual integration gate; not checked by this command")
    print(f"- checks: {', '.join(contract['required_ids'])}")
    print(f"- engines: {len(selected) if selected is not None else len(contract['targets'])}")
    print("- textual scope: " + (", ".join(sorted(selected)) if selected is not None else "all registered textual targets"))
    for line in resolved:
        print(f"- resolved {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
