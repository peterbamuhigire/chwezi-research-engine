# Experiment log

Cycle: `2026-10-engine-kaizen`  
Baseline frozen in `01-baseline-scorecard.md` before these experiments.  
No Tier-3 model calls, external archive writes, plugin submissions, or public
publication were performed.

## PDSA-1 — currentness record refresh (R-KZ-01)

- **Plan:** Recheck the standards named by the prompt and TOP against current
  primary sources, then replace only the obsolete TOP statement and add a
  dated, claim-linked source register. Keep old source snapshots immutable.
- **Do:** Added the dated claim register; directly refreshed PRISMA, GRADE,
  Cochrane, ICD 203, ICD 206, RFC 9309 and TOP from official publisher sources;
  corrected the TOP count and provenance wording in the academic-reporting
  skill. Six due source records are dispositioned in the new register while
  the old register remains unchanged.
- **Study:** `validate_source_currency.py
  docs/source-registers/kaizen-currentness-2026-10.json --as-of 2026-10-29`
  exits 0 with zero metadata findings. Contract validator: 59/59 compliant;
  routing remains 29/29 top-3, 25/29 rank-1, with 7 negative passes, 0
  failures, 2 NOT_ASSESSED; `validate_engine.py` exits 0 with 37 tests; the
  source-ingestion guard exits 0 with zero findings. Source limitations are
  recorded per row in the JSON register.
- **Act:** Kept. The new register validates and the skill now separates EQUATOR
  guidance from independently governed GRADE, Cochrane and TOP sources. The
  metadata pass does not certify semantic support; archive snapshots remain
  unassessed.
- **Stop/rollback:** If a source cannot be opened or its scope is ambiguous,
  keep that claim `NOT_ASSESSED`; historical source records remain immutable.

## PDSA-2 — portable-path recurrence check (R-KZ-02)

- **Plan:** Remove only confirmed machine-specific paths from active routers
  and skills; add a small scanner with synthetic positive and negative cases.
- **Do:** Pending.
- **Study:** Pending clean-checkout run, CI-equivalent validator result, and
  failure-path check.
- **Act:** Pending; keep only if the scanner detects prohibited examples and
  passes on the cleaned tree without unrelated warnings.
- **Stop/rollback:** Revert pattern or integration if it flags public URLs,
  historical evidence, or allowed relative paths.

## PDSA-3 — market boundary and routing proof (R-KZ-03)

- **Plan:** Add the smallest quantitative-modelling rule/example that separates
  government MIS, adjacent EdTech spending and commercial school-administration
  software; add three positive and two owned-negative fixtures for that route.
- **Do:** Pending.
- **Study:** Pending fixture lint, p@1/p@3, owned-negative statuses, task
  evidence review, and native validators.
- **Act:** Pending; keep only if the target route wins each positive, the owned
  negative owner outranks it, and aggregate routing results do not regress.
- **Stop/rollback:** Remove any fixture that uses its target skill name,
  copies the skill description, or fails ranking rather than weakening the
  smoke-test threshold.
