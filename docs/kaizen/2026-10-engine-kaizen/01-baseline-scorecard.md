# Digital Research Engine — frozen October 2026 baseline

As of: 2026-10-29 (Africa/Kampala)  
Repository: `digital-research-engine`, pre-change HEAD `444b7ce`

Assessment date: 2026-10-29
Status: the initial scorecard was committed before implementation; its first
draft leaned on prior-audit judgements. This correction was made after the
first implementation commit. It reconstructs the pre-change state of HEAD
`444b7ce` from the three full task outputs and repository evidence, including a
retrospective portability scan against that frozen tree. It does not claim the
correction itself was recorded before changes or use post-change results as a
baseline. Prior September scores are context only, not the scoring basis.

## Standard dimensions

Each score is a reviewer judgement against the Standard's minimum evidence
table, informed by the three full task outputs and the pre-change
validator/repository state recorded in `00-scope-and-evidence.md`.
The September audit's weighted score of 51.6/100 is comparison context only;
it is not averaged into this baseline. The ten dimension ratings use an equal
weight arithmetic mean because the Standard names ten dimensions and requires
each to be scored; the Standard does not prescribe different weights.

| Dimension | Raw | Named evidence | Current deficiency |
|---|---:|---|---|
| Doctrine | 64 | Current `AGENTS.md`, common research rules, source-evaluation and source-verification workflows, and currentness gate were read; all three task answers kept evidence, gaps and inference distinct | Doctrine is comprehensive but its universal archive gate had no operational branch for the three live-source tasks; one freshness register was overdue. |
| Taxonomy and routing | 53 | Inventory of 59 skills; pre-change router test 29/29 top-3 and 25/29 rank-1; 0/59 skills met 3-positive/2-owned-negative coverage; three observed routes reviewed | Existing lexical evidence covers fewer than half of the inventory and does not establish live-agent selection quality. |
| Skill depth | 54 | Three task outputs: current legal-rate lookup cited official sources; market brief separated public EMIS/NEMIS from paid SaaS but could not size the market; false-premise task corrected the outdated premise | The observed market-sizing route lacked an explicit product/buyer boundary and source-matched example; source-verification lacks an archive-unavailable handling branch. |
| Applied proof | 36 | Pre-change count: 56/59 examples under 60 words; 0/59 fixture-complete skills; three full task outputs expose one supported lookup, one market-size gap, and one corrected premise | Applied evidence is limited to three tasks and short examples; Tier-3 behavioural evaluation was not run. |
| Standards currency | 52 | Standards register review date was 2026-10-08; six dated wave-2 records returned overdue in the validator; TOP description in academic-reporting skill conflicted with current official COS material reviewed for this cycle | The register lacked current dated claim-level coverage for named standards, and several old model/catalogue records had not been dispositioned. |
| Output readiness | 53 | The current-rate output included source tier, date and limitation; the market brief had a compact claim/evidence/limit table but no defensible TAM; the false-premise answer supplied a corrected question | Product outputs show usable structure but no archival verification or commercial market input evidence for release-grade analysis. |
| Accessibility and inclusion | 45 | Three outputs used plain language and country context; route inventory includes Uganda/Kenya academic skills; no assistive-technology or rendered-document check was part of these observations | Accessibility, language-access, and rendered-output behavior were not demonstrated end-to-end. |
| Production and handoff | 58 | Pre-change `validate_engine.py`: exit 0, 37 tests; source-ingestion guard: exit 0, zero findings; native package installation evidence was inspected separately from the task outputs | Local checks pass, but the observed source handoff omitted required archive snapshots; no rendered research deliverable was produced. |
| Hygiene | 42 | Pre-change targeted check found host-specific paths in three skills and `AGENTS.md`; repository included two previously reported sibling-checkout links already repaired at `9ab4eb0`; a later retrospective whole-scope scan identified 52 absolute-path occurrences in the frozen tree | No recurrence guard existed; the initial targeted scope missed path occurrences in reference notes. The 52-count is a retrospective diagnostic, not a pre-change run. |
| Safety and integrity | 64 | Task outputs used bounded claims, cited sources, stated gaps, and labelled inference; pre-change source-ingestion guard and no-book check returned zero findings | No archival snapshots or independent semantic source review were available for the three tasks; paid Tier-3 evaluation remained unrun. |

Simple mean: **52.1/100**. Published cap: `min(52.1, 65) = 52.1/100`.
This is the ten-dimension arithmetic mean, not the prior audit's weighted
overall result of 51.6/100. Any safety, legal, privacy, or release blocker
remains independent of the numerical score.

For continuity with the user's initial-cycle reporting instruction, the same
raw score under the requested initial cap is `min(52.1, 45) = 45/100`. The
Portfolio Kaizen Standard's 65-point reporting cap remains the controlling
standard cap; neither cap changes the underlying dimension ratings.

## Measured inputs

| Measure | Baseline result | Evidence / limitation |
|---|---|---|
| Skill contract | 59 active skills; 59 fully compliant; exit 0 | `python -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json`; automated contract result only. |
| Routing | 29/29 top-3; 25/29 rank-1 = 86.2%; lexical proxy | `python -X utf8 scripts/routing_smoke_test.py`; top-3 threshold 1.000. Not live agent routing. |
| Owned negatives | 9 rows: 7 pass, 0 fail, 2 not assessed; 5 distinct skills have negatives | Same routing run; two not-assessed rows are not passes. |
| Fixture coverage | 0/59 skills have ≥3 positives and ≥2 owned negatives | Recomputed directly from `tests/skill-engine/routing-fixtures.json`. Current distribution: 28 skills with positive rows; five with owned negatives. |
| Worked-example length | 56/59 below 60 words, 0/59 missing a Worked example heading | Read-only heuristic counts words from example heading to next heading; length is only a proxy, not quality. |
| Machine-specific paths | Three skill files and `AGENTS.md` contain workstation-specific absolute references | `skills/skill-writing/SKILL.md`, `skills/skill-taxonomy-and-routing/SKILL.md`, `skills/skill-safety-audit/SKILL.md`, `AGENTS.md`. |
| Cross-engine links from prior CI finding | No longer present in the previously failing locations at current HEAD | Prior failure referenced `skills/ai-slop-audit/SKILL.md:146` and `skills/anti-ai-slop/SKILL.md:129`; commit `9ab4eb0` says portable cross-engine links. Remote CI state was not checked in this preflight. |
| Source-currency, delayed source register | 6 overdue records; exit 1 | `python -X utf8 scripts/validate_source_currency.py docs/source-registers/skills-kaizen-wave2-2026-09.json --as-of 2026-10-29`; all six are model/catalogue/pricing or Claude manifest records due 2026-10-03. |
| Deterministic source-currency fixture | 0 findings; exit 0; support NOT_ASSESSED | `python -X utf8 scripts/validate_source_currency.py tests/fixtures/source-currency.json --as-of 2026-10-29`; metadata/date check only. |
| Source-ingestion guardrail | 0 findings; exit 0 | `python -X utf8 scripts/source_ingestion_guardrail.py`. |
| Native engine validator | exit 0; 37 tests passed | `python -X utf8 scripts/validate_engine.py`; includes contract/routing reruns, no-book check, doctor, and engine unit tests. |
| Cross-engine relative links | Earlier two CI failures were addressed; ad hoc scan found two unrelated legacy/demo links | `skills/doc-standards.md` demo path and `skills/osint-investigation/references/social-source-extraction.md` literal ellipsis; scanner was not the validator and these findings require manual disposition. |
| Expired standard/source records | Standard register review date passed 2026-10-08; all six wave-2 records are overdue | Currentness evidence is in the source-currentness prep notes; no repository metadata has been changed. |

## Source currency review, accessed 2026-10-29

These are direct observations from official/current publisher pages and the
local register, not an exhaustive literature review.

| Item | Observed official state | Disposition |
|---|---|---|
| PRISMA | Official PRISMA site continues to present PRISMA 2020 as the core statement/checklists and lists extensions. It identifies a PRISMA-C 2026 extension. | Core version currentness supported for PRISMA 2020; extension scope has expanded. Record extension by study population and verify any applicable extension. |
| GRADE | GRADE Book is an official living resource; the GRADE Handbook is being replaced as chapters are updated, with coverage still being developed. | Do not describe the old Handbook alone as the current complete source; exact chapter-level currency is partial and must be checked per use. |
| Cochrane Handbook | Cochrane's official page identifies intervention handbook version 6.5, last updated 2024-08-22. | Version/status verified on access date; a 2024 content date remains the publisher's listed update. |
| ICD 203 | Official ODNI PDF contains the 2015 directive and a 2022 technical amendment signed 2022-01-21. | Register source should capture base directive plus amendment; currentness within IC jurisdiction only. |
| ICD 206 | Official ODNI PDF contains the 2015 directive and technical amendment dated 2025-12-18; source statement points to ICS 206-01. | Missing from current standards register; needs a claim-scoped row and direct check of ICS 206-01 before implementation claims. |
| RFC 9309 | RFC Editor labels it an Internet Standards Track document, published September 2022; Datatracker metadata updated 2026-05-20 and an errata record exists. | Current specification status observed; check errata/updates before normative crawler claims. |
| TOP Guidelines | The local skill still states “8 modular standards × 3 implementation levels”; the prior independent audit found that COS TOP 2025 material uses a different count/structure. | Treat the current skill text as stale pending a new dated direct COS source record; do not use its numeric framing. |
| OpenAI / Claude platform source records | The wave-2 register has six overdue entries. Separate packaging research dated 2026-10-29 checked official release/catalogue documentation and local model-cache IDs. | Reuse that dated source evidence only in its stated scope. Comparative quality, latency, cost per task, and active-session/account entitlement remain **NOT_ASSESSED**. |

## Validator evidence and commands

| Exact command | Exit | Relevant output |
|---|---:|---|
| `python --version` | 0 | Python 3.14.8 observed in this environment. |
| `python .codex/ensure_model_policy.py --runtime codex --check` | 0 | `PASS: Codex model policy is correct`. |
| `python -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json` | 0 | 59 active, 59 compliant, no failures. |
| `python -X utf8 scripts/routing_smoke_test.py` | 0 | 29/29 top-3, 25/29 rank-1, owned negatives 7 pass / 0 fail / 2 not assessed. |
| `python -X utf8 scripts/validate_engine.py` | 0 | contract/routing pass; no-book check OK; Engine doctor OK; 37 tests OK. |
| `python -X utf8 scripts/validate_source_currency.py docs/source-registers/skills-kaizen-wave2-2026-09.json --as-of 2026-10-29` | 1 | 6 overdue records. |
| `python -X utf8 scripts/validate_source_currency.py tests/fixtures/source-currency.json --as-of 2026-10-29` | 0 | 0 metadata findings; claim support not assessed. |
| `python -X utf8 scripts/source_ingestion_guardrail.py` | 0 | 0 findings. |

The table above is the pre-change measurement snapshot. The cycle then began
after the portfolio coordinator released the accounting-cycle hold. Later
changes and their checks are recorded in `03-experiment-log.md` and
`04-validation-record.md`.


## Installation and runtime evidence available at baseline

- The engine's Claude-compatible marketplace install succeeded offline in a
  disposable environment. The loader reports the `research@chwezi-research`
  plugin installed and enumerates all 59 skill directories. Its output says one
  user configuration option is unset (`hooks_enabled`); hook execution is
  therefore **NOT_ASSESSED**. Operator installation output was reviewed during
  baseline preparation; a later runtime path check is recorded in the
  validation record.
- Codex local-marketplace installation succeeded in an offline disposable
  environment. The plugin inventory reports `installed: true`, `enabled: true`,
  source `/engine`, and `authPolicy: ON_INSTALL`. This records install state,
  not active-session identity or public-directory acceptance. Operator
  installation output was reviewed during baseline preparation.
- The prior direct plugin validation at baseline passed with warnings: plugin
  description/author absent from the plugin manifest, root `CLAUDE.md` not
  loaded as project context, and icon missing. Marketplace metadata does contain
  attribution and a description. No manifest rebuild is selected based only on
  these warnings. No unsupported manifest change is claimed in this cycle.
- Checkout file count at baseline: 1,041 regular files including `.git`, 1,007
  after excluding `.git`; both are far below the 5,000-file ceiling. Counting
  method: `find . -type f | wc -l` and
  `find . -type f -not -path './.git/*' -not -path './.venv/*' -not -path './__pycache__/*' | wc -l`.
