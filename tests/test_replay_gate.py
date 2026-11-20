import json
from pathlib import Path
import unittest

from tools.evaluation.replay_gate import evaluate


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "evals/seek-research/replay-gate/synthetic_historical_regression.json"


def load_record():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def passing_record():
    record = load_record()
    record["synthetic"] = False
    record["candidate"]["synthetic"] = False
    record["replay"]["regressions"] = 0
    record["controls"].update({
        "reviewed_labels_verified": True,
        "independent_review": True,
        "semantic_review_complete": True,
        "uncertainty_reported": True,
    })
    record["ambiguous"] = {"cases": 1, "critical_false_ready": 0, "noninferiority_pass": True}
    return record


def paired_cases():
    required_evidence = (
        ("emerging", "critical_failures"),
        ("emerging", "critical_false_ready"),
        ("replay", "critical_failures"),
        ("replay", "critical_false_ready"),
        ("replay", "regressions"),
        ("ambiguous", "critical_false_ready"),
        ("candidate", "protected_labels_seen"),
    )
    for section, key in required_evidence:
        record = passing_record()
        del record[section][key]
        yield f"missing {section}.{key}", record, "not_assessed", f"{section}.{key}"

    record = passing_record()
    record["candidate"]["protected_labels_seen"] = "false"
    yield "malformed attestation", record, "rejected", "candidate.protected_labels_seen"

    record = passing_record()
    record["emerging"]["improved"] = 4
    yield "overstated improvement", record, "rejected", "emerging.improved"

    yield "explicit zeroes", passing_record(), "eligible_for_authorized_review", "all supplied gates pass"

    record = passing_record()
    del record["candidate"]["protected_labels_seen"]
    record["emerging"]["critical_failures"] = 1
    yield "critical failure with missing attestation", record, "rejected", "critical failure observed"

    record = passing_record()
    del record["replay"]["regressions"]
    record["candidate"]["protected_labels_seen"] = True
    yield "label exposure with missing count", record, "rejected", "candidate author saw protected labels"

    record = passing_record()
    del record["ambiguous"]["critical_false_ready"]
    record["controls"]["evaluation_contract_unchanged"] = False
    yield "denied control with missing count", record, "rejected", "evaluation contract changed"


class ReplayGateTests(unittest.TestCase):
    def assert_disposition(self, record, expected, reason):
        result = evaluate(record)
        self.assertEqual(expected, result["status"])
        self.assertTrue(any(reason in item for item in result["reasons"]), result["reasons"])
        self.assertIs(result["promotion_performed"], False)
        self.assertIs(result["canonical_guidance_written"], False)
        self.assertIs(result["semantic_truth_certified"], False)
        return result

    def test_malformed_review_attestations_are_rejected(self):
        for section, key in (
            ("controls", "reviewed_labels_verified"),
            ("controls", "authorized_maintainer_decision"),
            ("controls", "semantic_review_complete"),
            ("controls", "uncertainty_reported"),
            ("ambiguous", "noninferiority_pass"),
        ):
            for value in ("false", 0, None):
                with self.subTest(section=section, key=key, value=value):
                    record = passing_record()
                    record[section][key] = value
                    self.assert_disposition(record, "rejected", f"{section}.{key}")

    def test_unchanged_controls_distinguish_missing_denied_and_malformed(self):
        for key in (
            "routing_description_unchanged",
            "model_runtime_unchanged",
            "evaluation_contract_unchanged",
        ):
            with self.subTest(key=key):
                record = passing_record()
                del record["controls"][key]
                self.assert_disposition(record, "not_assessed", f"missing controls.{key}")

                record["emerging"]["critical_failures"] = 1
                self.assert_disposition(record, "rejected", "critical failure observed")
                record["emerging"]["critical_failures"] = 0

                record["controls"][key] = False
                self.assert_disposition(record, "rejected", f"controls.{key}")

                record["controls"][key] = "false"
                self.assert_disposition(record, "rejected", f"controls.{key} must be a boolean")

    def test_malformed_synthetic_markers(self):
        for section in ("record", "candidate"):
            for value in ("true", "false", 1, 0, None):
                with self.subTest(section=section, value=value):
                    record = passing_record()
                    target = record if section == "record" else record["candidate"]
                    target["synthetic"] = value
                    self.assert_disposition(record, "rejected", f"{section}.synthetic")

    def test_paired_replay_dispositions(self):
        for name, record, expected, reason in paired_cases():
            with self.subTest(case=name):
                self.assert_disposition(record, expected, reason)

    def test_missing_candidate_synthetic_marker(self):
        for top_level_marker_present in (False, True):
            with self.subTest(top_level_marker_present=top_level_marker_present):
                record = passing_record()
                del record["candidate"]["synthetic"]
                if not top_level_marker_present:
                    del record["synthetic"]
                self.assert_disposition(record, "not_assessed", "missing candidate.synthetic")

    def test_critical_failure_takes_precedence_over_missing_candidate_synthetic_marker(self):
        record = passing_record()
        del record["candidate"]["synthetic"]
        record["emerging"]["critical_failures"] = 1
        self.assert_disposition(record, "rejected", "critical failure observed")

    def test_malformed_independent_review_is_rejected(self):
        for value in ("false", 0, None):
            with self.subTest(value=value):
                record = passing_record()
                record["controls"]["independent_review"] = value
                self.assert_disposition(record, "rejected", "controls.independent_review")

    def test_missing_or_negative_independent_review_is_not_assessed(self):
        record = passing_record()
        record["controls"]["independent_review"] = False
        self.assert_disposition(record, "not_assessed", "independent review absent")

        del record["controls"]["independent_review"]
        self.assert_disposition(record, "not_assessed", "independent review absent")

    def test_invalid_count_values_and_cohort_bounds(self):
        for section, key, value in (
            ("emerging", "cases", True),
            ("emerging", "improved", -1),
            ("emerging", "critical_failures", 4),
            ("emerging", "critical_false_ready", 4),
            ("replay", "critical_failures", 3),
            ("replay", "critical_false_ready", 3),
            ("replay", "regressions", 3),
            ("replay", "regressions", False),
            ("replay", "regressions", -1),
            ("ambiguous", "critical_false_ready", 2),
            ("ambiguous", "critical_false_ready", None),
        ):
            with self.subTest(section=section, key=key, value=value):
                record = passing_record()
                record[section][key] = value
                result = self.assert_disposition(record, "rejected", f"{section}.{key}")
                self.assertFalse(any("observed" in reason for reason in result["reasons"]))

    def test_attestation_requires_boolean(self):
        for value in (0, 1, None, [], {}):
            with self.subTest(value=value):
                record = passing_record()
                record["candidate"]["protected_labels_seen"] = value
                self.assert_disposition(record, "rejected", "candidate.protected_labels_seen")

    def test_historical_regression_rejects_despite_emerging_improvement(self):
        result = evaluate(load_record())
        self.assertEqual("rejected", result["status"])
        self.assertTrue(any("historical replay regression" in reason for reason in result["reasons"]))
        self.assertFalse(result["promotion_performed"])
        self.assertFalse(result["canonical_guidance_written"])

    def test_synthetic_no_regression_still_cannot_be_promoted(self):
        record = load_record()
        record["replay"]["regressions"] = 0
        result = evaluate(record)
        self.assertEqual("not_assessed", result["status"])
        self.assertTrue(any("synthetic" in reason for reason in result["reasons"]))

    def test_changed_routing_description_rejects_guidance_only_candidate(self):
        record = load_record()
        record["controls"]["routing_description_unchanged"] = False
        result = evaluate(record)
        self.assertEqual("rejected", result["status"])
        self.assertTrue(any("routing description changed" in reason for reason in result["reasons"]))

    def test_mixed_cause_cannot_enter_revision_gate(self):
        record = load_record()
        record["candidate"]["primary_cause"] = "mixed"
        record["replay"]["regressions"] = 0
        result = evaluate(record)
        self.assertEqual("not_assessed", result["status"])
        self.assertTrue(any("cause is unresolved" in reason for reason in result["reasons"]))

    def test_passing_evidence_only_yields_human_review_handoff(self):
        record = passing_record()
        record["controls"]["authorized_maintainer_decision"] = True
        self.assert_disposition(record, "eligible_for_authorized_review", "all supplied gates pass")

    def test_malformed_count_rejects_instead_of_crashing(self):
        record = load_record()
        record["replay"]["regressions"] = "one"
        result = evaluate(record)
        self.assertEqual("rejected", result["status"])
        self.assertTrue(any("non-negative integer" in reason for reason in result["reasons"]))


if __name__ == "__main__":
    unittest.main()
