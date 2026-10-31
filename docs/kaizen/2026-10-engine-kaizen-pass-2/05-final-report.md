# Digital Research Engine: kaizen pass 2, final report

Date: 2026-10-31 (Africa/Kampala)
Starting branch: `main`, HEAD `d350ce2`, clean tree.
Working branch: `kaizen/2026-10-pass2`. At the end of the cycle the checkout was
returned to `main`, so the live checkout is as it was found; the work is on the
working branch, unpushed.

Raw score: **59.5/100**. Published under the Standard cap: `min(59.5, 65) = 59.5/100`.
Frozen baseline for this pass: 56.3 (capped 56.3). The 29 October final was 58.2.
The target of 95/100 is not reached, and the cap is a reporting ceiling, not a
rating.

Ten backlog items were selected and ten kept; none was reverted. One planned
change (a description rewrite in R2-05) was not made after its diagnosis proved
wrong, and one scope item (generated "Evidence Notes" headings in R2-07) was left
out. No critical defect was found. No canonical doctrine, protected document or
other engine was edited. `AGENTS.md`, the router, received pointers and gate
documentation only (workflow step 1, the machine-error gate options, the register
gate), not a change to any rule. No paid model call, archive write, push or pull
request was made.

## Scores by dimension

| Dimension | 29 Oct final | Baseline (31 Oct) | After | Evidence for the change |
|---|---:|---:|---:|---|
| Doctrine | 64 | 62 | 65 | A named owner and a premise check now exist for single-claim questions, reachable from the router and four skills (R2-03). The archive-snapshot gate is unchanged. |
| Taxonomy and routing | 55 | 54 | 57 | Rank-1 36/40 (90.0%) from 30/34 (88.2%); top-3 still 100%; skills with three positives and two owned negatives 3 of 59 from 1; skills with an owned negative 10 from 6; 19 repeated headings removed; current-state questions now have routing vocabulary (R2-05, R2-07). The proxy still lets a proper noun in a skill name win. |
| Skill depth | 56 | 55 | 58 | Premise check, undated-page rule, statute-consolidation rule and denominator check (R2-03, R2-04, R2-08). |
| Applied proof | 40 | 40 | 43 | Two checked single-claim records and one checked denominator example, each over 60 words with traceable figures; one held-out premise handled by the procedure. 55 of 59 skill worked examples are still under 60 words. |
| Standards currency | 74 | 70 | 77 | Older register passes through a machine-checked supersession; every real register is now gated as of today in `validate_engine.py` and CI; ten records re-read from primary pages, with ICD 203 corrected to partial and ICD 206 honestly `NOT_ASSESSED` (R2-02, R2-10). |
| Output readiness | 55 | 55 | 56 | Market brief now records denominators with definitions and quarantines a vendor count that fails arithmetic; market size remains a gap. |
| Accessibility and inclusion | 45 | 45 | 45 | No assistive-technology, locale or rendered-document check was in scope. |
| Production and handoff | 59 | 56 | 59 | The cross-engine machine-error gate runs on this host: PASS for 11 bound engines (was 12 of 12 missing); 94 unit tests (was 50). Archive handoff, remote CI, the unbound political target and the sibling register schemas are still open (R2-01). |
| Hygiene | 70 | 64 | 72 | Scanner now catches repository-escaping and dead links and covers the author-facing guides; broken link 1 to 0; host paths in the guides 3 files to 0; repeated headings 19 skills to 0; retired skill name 15 mentions to 0 (R2-06, R2-07, R2-09). Seven history links, nine generated headings and the two protected files remain. |
| Safety and integrity | 64 | 62 | 63 | A false premise is now stated before answering, and a vendor figure is arithmetic-checked before use. The provenance lines in D-13 stay unresolved pending Peter's decision; archive and independent review are absent. |
| **Raw mean** | **58.2** | **56.3** | **59.5** | |

After arithmetic: `(65 + 57 + 58 + 43 + 77 + 56 + 45 + 59 + 72 + 63) / 10 = 595 / 10 = 59.5`.
Baseline arithmetic: `563 / 10 = 56.3`, in `01-baseline-scorecard.md`. Ratings are
reviewer judgements tied to the named evidence; no measure in the frozen baseline
is worse now (see the check below).

No measure is worse than its frozen baseline:

| Measure | Baseline | Now |
|---|---|---|
| Routing top-3 / rank-1 | 34/34, 30/34 (88.2%) | 40/40, 36/40 (90.0%) |
| Owned negatives pass / fail / `NOT_ASSESSED` | 9 / 0 / 2 | 15 / 0 / 2 |
| Contract compliance | 59 of 59 | 59 of 59 |
| Unit tests in `validate_engine.py` | 50 | 94 |
| Overdue source records in a real register | 6 | 0 (6 superseded by a validated successor) |
| Broken relative links, active scope | 1 | 0 |
| Skills with duplicate headings | 19 | 0 |
| Machine-error gate targets resolved on this host | 0 of 12 | 11 of 12 (9 by default roots) |
| Worked examples under 60 words | 55 of 59 | 55 of 59 (unchanged) |

## Kept changes

| Item | Commit | Evidence |
|---|---|---|
| R2-01, machine-error gate resolves targets by portfolio root | `00bdc44` | 12 tests; fixture holds no host path (17 before); 11 engines PASS on this host; live tests pass |
| R2-02, register supersession and a gate for real registers | `d581e01` | 13 tests; older register exit 1 to exit 0; 3 registers checked in `validate_engine.py` and CI |
| R2-03, premise check and single-claim owner | `4f73c9c`, `81970a4` | grep for the premise phrases 0 hits to present; source-evaluation fully fixtured; worked example checked against the primary notice |
| R2-04, undated page and stale consolidation rules | `b81c727` | grep for "undated" 0 to present; online-legal-research fully fixtured; Uganda record checked against the Act text |
| R2-05, routing vocabulary for current-state questions | `fb4dfee` | plain NSSF prompt: `source-evaluation` rank 55 to 1; four fixtures; rank-1 90.0% |
| R2-06, scanner link rules and wider scope | `f610ce7` | 5 findings on the unrepaired tree, 0 after; 7 tests |
| R2-07, repeated headings | `b9648f6` | `duplicate_heading` 19 on the pre-fix tree, 0 after; 5 tests; no non-blank line lost |
| R2-08, denominator check | `9621cc6` | arithmetic re-done; 336-word example; fixtures unchanged and passing |
| R2-09, unresolved companion names | `d094054` | 4 findings on the pre-fix tree, 0 after; 7 tests; 15 mentions repaired |
| R2-10, currency re-verification | `aeceb5a` | 10 sources and 11 claims; validator exit 0; three honest downgrades |

Evidence files are committed on the same branch in separate commits (baseline
`436dd70`, backlog `a822fc6`, then this record set).

## Scope corrections made during the cycle

- R2-05: the baseline's diagnosis (country-heavy descriptions) was wrong. The probe was scored with and without the country word; the descriptions are already academic-scoped, and nothing in the catalogue spoke of a current rate or status. The planned rewrite was dropped and a different change made. The baseline file is left as frozen; the correction is in `03-experiment-log.md`.
- The 29 October social-media mismatch no longer reproduces: that engine passes the identifier check at its current HEAD. It had its own commits after 29 October.
- The oracle `055-route-release-evidence-mirror` is not in this repository; it lives in `chwezi-engine-agents` and is evaluated in union mode there. It is `NOT_ASSESSED` here.
- R2-07's nine generated "Evidence Notes" headings were left out because one holds a table that the contract reads as its evidence section.

## Readiness and residual risk

- **CI will turn red on a date.** The register gate checks as of today. The four OpenAI platform records in the 29 October register fall overdue on 2026-11-30 and the two in the 31 October register on 2026-12-01. That is the stated policy, but someone must re-read the pages first. `06-next-cycle.md` sets the re-audit before that date.
- **Archive snapshots** remain the principal release-evidence blocker for live web research. The universal gate is doctrine and is unchanged.
- **Two standards cannot be fully checked here.** ICD 206 is an image-only PDF and no OCR tool is installed; the latest ICD 203 amendment date is unreadable and its printed date conflicts with a memorandum it cites.
- **Routing evidence is lexical.** The proxy shows a vocabulary gap closed; it does not show a live agent choosing correctly. Tier 3 was not run.
- **Semantic support** in the new registers is the agent's reading of each page; no independent reviewer has signed any row.
- **D-13** (provenance lines naming a personal path and unofficial book-copy markers in `docs/continuous-improvement/english-collocations-and-lexical-precision-2026-09-02.md`, lines 146 and 147) needs Peter's decision. It was not edited.
- **Remote CI, marketplace readiness and installed-plugin discovery** were not checked this pass.

See `06-next-cycle.md` for the follow-up, the proposed text for the two protected
documents, the cross-engine mismatches and the review date.
