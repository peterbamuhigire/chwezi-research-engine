"""Read-only gate for proposed skill guidance revisions; never promotes or writes."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any


FAILURE_CAUSES = {"routing", "knowledge", "execution", "source/tool", "gold-label", "mixed", "unknown"}


def evaluate(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    missing: list[str] = []
    candidate = record.get("candidate", {})
    controls = record.get("controls", {})
    emerging = record.get("emerging", {})
    replay = record.get("replay", {})
    ambiguous = record.get("ambiguous", {})

    def count(
        section: dict[str, Any], key: str, label: str, *,
        required: bool = False, cohort_size: int | None = None,
    ) -> int | None:
        if key not in section:
            if required:
                missing.append(f"missing {label}.{key}")
            return None
        value = section[key]
        if type(value) is not int or value < 0:
            errors.append(f"{label}.{key} must be a non-negative integer")
            return None
        if cohort_size is not None and value > cohort_size:
            errors.append(f"{label}.{key} exceeds {label}.cases")
            return None
        return value

    cause = candidate.get("primary_cause")
    if cause not in FAILURE_CAUSES:
        errors.append("unknown primary cause")
    protected_labels_seen = candidate.get("protected_labels_seen")
    if "protected_labels_seen" not in candidate:
        missing.append("missing candidate.protected_labels_seen")
    elif type(protected_labels_seen) is not bool:
        errors.append("candidate.protected_labels_seen must be a boolean")
    elif protected_labels_seen:
        errors.append("candidate author saw protected labels")
    if not candidate.get("rollback_target"):
        errors.append("missing rollback target")
    for key, description in (
        ("routing_description_unchanged", "routing description"),
        ("model_runtime_unchanged", "model/runtime"),
        ("evaluation_contract_unchanged", "evaluation contract"),
    ):
        if key not in controls:
            missing.append(f"missing controls.{key}")
        elif type(controls[key]) is not bool:
            errors.append(f"controls.{key} must be a boolean")
        elif controls[key] is False:
            errors.append(f"controls.{key}: {description} changed")

    for key in (
        "independent_review",
        "reviewed_labels_verified",
        "authorized_maintainer_decision",
        "semantic_review_complete",
        "uncertainty_reported",
    ):
        if key in controls and type(controls[key]) is not bool:
            errors.append(f"controls.{key} must be a boolean")
    if "noninferiority_pass" in ambiguous and type(ambiguous["noninferiority_pass"]) is not bool:
        errors.append("ambiguous.noninferiority_pass must be a boolean")

    reviewed_cases = count(record, "distinct_reviewed_cases", "record")
    source_clusters = count(record, "distinct_source_clusters", "record")
    emerging_cases = count(emerging, "cases", "emerging")
    replay_cases = count(replay, "cases", "replay")
    ambiguous_cases = count(ambiguous, "cases", "ambiguous")
    improved = count(emerging, "improved", "emerging", cohort_size=emerging_cases)
    critical = (
        count(emerging, "critical_failures", "emerging", required=True, cohort_size=emerging_cases),
        count(replay, "critical_failures", "replay", required=True, cohort_size=replay_cases),
    )
    false_ready = (
        count(emerging, "critical_false_ready", "emerging", required=True, cohort_size=emerging_cases),
        count(replay, "critical_false_ready", "replay", required=True, cohort_size=replay_cases),
        count(ambiguous, "critical_false_ready", "ambiguous", required=True, cohort_size=ambiguous_cases),
    )
    regressions = count(replay, "regressions", "replay", required=True, cohort_size=replay_cases)
    if "synthetic" not in candidate:
        missing.append("missing candidate.synthetic")
    for section, label in ((record, "record"), (candidate, "candidate")):
        if "synthetic" in section and type(section["synthetic"]) is not bool:
            errors.append(f"{label}.synthetic must be a boolean")
    reasons = list(errors)
    if any(critical):
        reasons.append("critical failure observed")
    if any(false_ready):
        reasons.append("critical false-ready transition observed")
    if regressions:
        reasons.append("historical replay regression observed")

    if reasons:
        status = "rejected"
    elif cause in {"mixed", "unknown"}:
        status = "not_assessed"
        reasons.append("cause is unresolved; do not create a guidance-only revision")
    elif cause != "knowledge":
        status = "not_assessed"
        reasons.append("primary cause belongs to a non-knowledge repair path")
    else:
        if record.get("synthetic") is True or candidate.get("synthetic") is True:
            missing.append("evidence is synthetic")
        if controls.get("reviewed_labels_verified") is not True:
            missing.append("reviewed labels not verified")
        if (reviewed_cases or 0) < 3:
            missing.append("fewer than three reviewer-confirmed recurrence cases")
        if (source_clusters or 0) < 3:
            missing.append("fewer than three distinct source-origin clusters")
        if not emerging_cases or not improved:
            missing.append("no measured emerging-case improvement")
        if not replay_cases:
            missing.append("no historical replay evidence")
        if controls.get("independent_review") is not True:
            missing.append("independent review absent")
        if controls.get("semantic_review_complete") is not True:
            missing.append("semantic review incomplete")
        if controls.get("uncertainty_reported") is not True:
            missing.append("paired uncertainty evidence absent")
        if not ambiguous_cases:
            missing.append("ambiguous/needs-work slice is not assessed")
        if ambiguous.get("noninferiority_pass") is not True:
            missing.append("predeclared ambiguous-slice noninferiority gate not passed")
        if missing:
            status = "not_assessed"
        else:
            status = "eligible_for_authorized_review"
            reasons.append("all supplied gates pass; maintainer must review this handoff")

    reasons.extend(missing)
    return {
        "candidate_id": candidate.get("candidate_id", ""),
        "status": status,
        "reasons": reasons,
        "rollback_target": candidate.get("rollback_target"),
        "promotion_performed": False,
        "canonical_guidance_written": False,
        "semantic_truth_certified": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    try:
        record = json.loads(args.record.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"replay-gate input error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(evaluate(record), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
