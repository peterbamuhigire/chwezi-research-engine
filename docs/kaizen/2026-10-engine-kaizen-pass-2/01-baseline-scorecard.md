# Digital Research Engine: frozen baseline, kaizen pass 2

As of: 2026-10-31 (Africa/Kampala)
Repository HEAD at measurement: `d350ce2` on `main`; branch `kaizen/2026-10-pass2` created from it.
Status: frozen. This file was committed before any engine content changed. Later
results go in `03-experiment-log.md`, `04-validation-record.md` and `05-final-report.md`.

The repository has not changed since the 29 October cycle ended. Where a score
below differs from the 29 October final, the cause is a defect that this cycle's
fresh observation found and that the earlier scoring did not reflect. It is not a
regression in the code. The evidence for each difference is in
`00-scope-and-evidence.md` (defect IDs D-01 to D-15).

## The ten dimensions

Ratings are reviewer judgements against the Portfolio Kaizen Standard's minimum
evidence table, equal weight. The September audit's weighted 51.6 and the
29 October equal-weight 58.2 are context, not inputs.

| Dimension | 29 Oct final | Raw now | Named evidence | One-line deficiency |
|---|---:|---:|---|---|
| Doctrine | 64 | 62 | `AGENTS.md`, `rules/common/core.md`, `evidence-discipline.md`; three task answers kept evidence, inference and gaps apart | No rule asks the agent to test the premise of a question (0 grep hits), and single-claim lookups are excluded by three skills with no owner (D-03, D-04). |
| Taxonomy and routing | 55 | 54 | 59 skills; precision@1 30/34 (88.2%), top-3 34/34; 11 owned negatives, 9 pass, 0 fail, 2 `NOT_ASSESSED`; 1 of 59 skills fully fixtured; lexical probe of three task prompts | Two country-named academic skills outrank every evidence skill for non-academic country questions (D-06); coverage is 1 of 59. |
| Skill depth | 56 | 55 | Three task outputs; `source-evaluation` and `source-verification` read in full | Nothing covers an undated first-party page or a statute consolidation that lists unapplied amendments (D-05); no archive-unavailable branch (carried). |
| Applied proof | 40 | 40 | 55 of 59 worked examples under 60 words; 1 of 59 fully fixtured; three fresh task outputs with checked figures | Applied evidence rests on three tasks and one fully fixtured skill; no Tier 3 behavioural run. |
| Standards currency | 74 | 70 | `docs/source-registers/kaizen-currentness-2026-10.json` valid (0 findings); standards records reviewable to 2027-01-29; four platform records due 2026-11-29 | The older register still exits 1 with six overdue records (D-02); CI checks only a fixture at a fixed 2026-08-06 date, so no real register can block release. |
| Output readiness | 55 | 55 | Task 1 answer dated and bounded; Task 2 stopped at a gap instead of inventing a size; Task 3 corrected the premise | No archive snapshots; no priced, product-matched market figure; Task 1 relied on an undated first-party page. |
| Accessibility and inclusion | 45 | 45 | Plain-language outputs with country context; Uganda and Kenya academic skills exist | No assistive-technology, locale or rendered-document check was part of any observation. |
| Production and handoff | 59 | 56 | `validate_engine.py` exit 0 with 50 tests; file cap 1268/5000 and 987/5000; plugin install evidence from 29 October | The cross-engine machine-error gate cannot run off the original Windows host (12 of 12 targets missing, D-01); the gate document and validator name evidence fields differently (D-15). |
| Hygiene | 70 | 64 | Portable-reference scan 376 files, 0 findings; contract 59/59 | Scanner false negatives (D-08); 1 broken link (D-09); 7 links leave the repository (D-10); 19 skills with duplicate headings and 9 with generated "Evidence Notes N" headings (D-11); 3 dangling companion names (D-12). |
| Safety and integrity | 64 | 62 | Source-ingestion guard 0 findings; no-book check OK; bounded claims in all outputs | A provenance record carries a personal path and filenames that suggest unlawful book copies (D-13); archive and independent human review still absent. |
| **Raw mean** | **58.2** | **56.3** | | |

Arithmetic, raw now: `(62 + 54 + 55 + 40 + 70 + 55 + 45 + 56 + 64 + 62) / 10 = 563 / 10 = 56.3`.
Arithmetic, 29 October final: `(64 + 55 + 56 + 40 + 74 + 55 + 45 + 59 + 70 + 64) / 10 = 582 / 10 = 58.2`.

Published score under the Standard cap: `min(56.3, 65) = 56.3/100`.
The improvement plan still targets 95/100; the cap is a reporting ceiling and
neither changes a raw rating nor hides a defect.

## Blockers

None of the safety, legal, financial, privacy or release kind is a blocker for
the engine's research outputs. Two items need an owner decision and are flagged
rather than scored away:

- D-13: provenance lines with a personal path and unofficial-copy markers in a
  user-authored record. Peter decides whether to redact.
- Release currentness: the older source register fails its own validator today.
  Under `AGENTS.md` ("overdue records block release") this is a release-gate
  failure for that register until it is superseded or re-verified. It is item
  R2-02 in the backlog and is not a content-safety issue.

## Measured inputs, fresh

| Measure | Value | Command or method |
|---|---|---|
| Skill contract | 59 active, 59 compliant, exit 0 | `python3 -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json` |
| Routing | 34/34 top-3; precision@1 30/34 = 88.2% (lexical proxy, not live routing) | `python3 -X utf8 scripts/routing_smoke_test.py` |
| Owned negatives | 11 rows: 9 pass, 0 fail, 2 `NOT_ASSESSED` | same run |
| Fixture coverage (three positives and two owned negatives) | 1 of 59; 29 skills with a positive, 6 with an owned negative | scripted recount of `tests/skill-engine/routing-fixtures.json` |
| Worked-example depth | 55 of 59 under 60 words; median 26 | scripted word count |
| Broken relative links, active scope | 1 (`skills/doc-standards.md:446`) | read-only scan, 376 files |
| Relative links leaving the repository | 0 in active scope; 7 in `docs/continuous-improvement` | same scan, plus 40 `docs/` files |
| Machine-specific paths | Active scope 0 (scanner); outside scanner scope 3 repairable files and the protected pair | `git grep -lIE` and scanner |
| Dangling cross-engine references | 3 companion names (7 mentions); 6 sibling routers hard-code a Windows path to this engine | scripted count; grep over siblings |
| Duplicate headings | 19 skills; 9 with generated "Evidence Notes N" | scripted count |
| Expired source records | 6, all in one register | `python3 -X utf8 scripts/validate_source_currency.py docs/source-registers/skills-kaizen-wave2-2026-09.json --as-of 2026-10-31`, exit 1 |
| Native engine validator | exit 0; 50 tests | `python3 -X utf8 scripts/validate_engine.py` |
| File cap | 1268/5000 full; 987/5000 package-oriented | `python3 -X utf8 scripts/check_file_count_cap.py` |
| Machine-error gate | exit 1; 12 of 12 targets missing | `python3 -X utf8 scripts/validate_machine_error_gate.py` |
| System pytest | `NOT_ASSESSED`: no module | not installed, per the brief |

## Source currency review, accessed 2026-10-31

Re-verification of the named standards happens in Step 5 and is recorded in
`04-validation-record.md` and `docs/source-registers/kaizen-currentness-2026-10-31.json`.
The baseline carries the 29 October register state: eight standards records
valid to 2027-01-29, four OpenAI platform records valid to 2026-11-29 and six
historical records superseded in prose but not in machine-readable form (D-02).
