# Digital Research Engine — October 2026 Kaizen report

Date: 2026-10-29 (Africa/Kampala)

Branch: `kaizen/2026-10`

Raw score: 58.2/100

Portfolio Standard cap: `min(58.2, 65) = 58.2/100`

User-requested initial cap: `min(58.2, 45) = 45/100`

The cycle assessed the engine against the three full practitioner outputs and
the frozen repository evidence, then kept four bounded changes. The market
brief still has no defensible Uganda/Kenya commercial school-administration
software TAM in the consulted evidence; the change makes that evidence
boundary explicit and prevents public-system coverage or adjacent learning
products from filling the gap. [Task outputs](00-scope-and-evidence.md).
**(synthesis)**

## Scores by dimension

| Dimension | Baseline | After | Evidence of change or reason unchanged |
|---|---:|---:|---|
| Doctrine | 64 | 64 | The source and evidence rules remain sound; the archive-snapshot limitation remains open. |
| Taxonomy and routing | 53 | 55 | New market-sizing route tests lift rank-1 from 25/29 (86.2%) to 30/34 (88.2%) and provide complete positive/owned-negative fixtures for one of 59 skills; routing remains a lexical proxy ([validation record](04-validation-record.md)). |
| Skill depth | 54 | 56 | Quantitative modelling now has an explicit product/buyer/geography/period/revenue boundary and a source-linked example. |
| Applied proof | 36 | 40 | Three independent positive and two owned-negative fixtures were added for the affected skill; all three original task outputs remain documented ([fixtures](../../../tests/skill-engine/routing-fixtures.json); [task outputs](00-scope-and-evidence.md)). |
| Standards currency | 52 | 74 | A dated claim-level source register was added, six overdue historical records received explicit dispositions, and the academic-reporting claim was refreshed from official current sources ([currentness register](../../source-registers/kaizen-currentness-2026-10.json); [backlog](02-improvement-backlog.md)). |
| Output readiness | 53 | 55 | The worked market example now distinguishes relevant evidence and returns unmatched market inputs as gaps; actual TAM remains unassessed because product-matched inputs were not found. |
| Accessibility and inclusion | 45 | 45 | No end-to-end accessibility or rendered-document evaluation was conducted. |
| Production and handoff | 58 | 59 | The engine validator now runs portable-reference and full/package capacity gates and has 48 passing tests; archive-backed source handoff remains incomplete ([validation record](04-validation-record.md)). |
| Hygiene | 42 | 70 | The new recurrence check reports zero findings across 376 active Markdown files; the frozen-tree retrospective found 52 absolute-path occurrences before repair ([validation record](04-validation-record.md)). |
| Safety and integrity | 64 | 64 | Bounded claims, gaps and inference labels remain; archival verification and independent source review are still open. |
| **Mean** | **52.1** | **58.2** | Equal-weight mean of the ten dimension ratings; exact arithmetic shown below. |

After score arithmetic: `(64 + 55 + 56 + 40 + 74 + 55 + 45 + 59 + 70 + 64) / 10 = 58.2`.
The baseline arithmetic is recorded in [01-baseline-scorecard.md](01-baseline-scorecard.md).
Dimension ratings are reviewer judgements tied to the named evidence in the
table and task records. The
Portfolio Standard cap of 65 and the user's requested initial cap of 45 are
reporting ceilings; neither changes raw ratings. The target of 95/100 is not
achieved.

## Kept changes

- **R-KZ-01 — currentness:** `bd5a693` adds a claim-linked 2026 register,
  disposition of six overdue records, and a correction to the academic
  reporting standards description. Metadata validation passes; semantic
  support still requires human review and archived locators remain absent.
- **R-KZ-02 — portability:** `d02f841 fix(research-kaizen): reject nonportable skill references`; follow-up `aa8ba37 fix(research-kaizen): cover host root path variants`
  adds a scanner to the normal validator path and removes machine-specific
  paths from active router/skill Markdown. Its clean-tree check and synthetic
  failure path both behave as intended. The foreign-checkout machine-error
  validator still fails on missing external targets; this is not counted as
  passing cross-engine evidence.
- **R-KZ-03 — market boundary:** `68d9747 fix(research-kaizen): bound school software market sizing`; the market boundary rule/example and five
  routing fixtures make the product distinction testable. Top-3 stays 100%,
  rank-1 improves above baseline, and the TAM conclusion remains a gap.
- **R-KZ-05 — capacity guard:** `72bc019 feat(research-kaizen): enforce checkout package file cap`; `check_file_count_cap.py` is part of the
  standard engine validator. It checks full-checkout and package-oriented
  counts, includes exact-limit/over-limit tests, and fails closed when the
  filesystem walk cannot complete. The current inventory is below the task
  ceiling; a future built ZIP still needs archive-level validation.

R-KZ-05's planned production/handoff target of 60 was not applied to the
rating: the new preflight does not prove actual archive contents or archived
source handoff.

No experiment was reverted. No canonical doctrine or another engine was
edited. No paid model call or public submission was made.

## Readiness and residual risk

The two native plugin installations and the offline runtime path inspection
provide install/discovery evidence for Codex and Claude; exact validator
results and limitations are in [04-validation-record.md](04-validation-record.md).
This does not
establish model answer quality, live-service credentials, remote CI status,
independent human source review, or marketplace publication status. Source
archive snapshots remain the principal release-evidence blocker for live web
research. The machine-error gate's missing foreign paths remain a portfolio
handoff gap, not a research-engine code failure.

See `06-next-cycle.md` for the scoped follow-up and review date.
