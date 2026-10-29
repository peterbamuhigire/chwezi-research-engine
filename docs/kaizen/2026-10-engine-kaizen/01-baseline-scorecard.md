# Digital Research Engine — baseline preparation

As of: 2026-10-29 (Africa/Kampala)  
Repository: `digital-research-engine`, HEAD `444b7ce`  
Status: prepared outside the repository before any edit; final scorecard remains
to be frozen on root-agent go-ahead.

## Standard dimensions

Scores carry forward the latest full audit's named judgement evidence unless a
new measure below directly updates it. Taxonomy/routing combines the prior
taxonomy score (48) and measured discovery/routing score (57.5), rounded to
53. This is a transparent average for the Standard's combined dimension, not
the old report's weighted engine score. The simple mean is shown for the ten
Standard dimensions; the prior weighted audit score (51.6) remains separately
reported and is not arithmetically comparable.

| Dimension | Raw | Named evidence | Current deficiency |
|---|---:|---|---|
| Doctrine | 64 | `AGENTS.md`; source-evaluation and source-verification skills; currentness gate; evidence discipline | Guidance is distributed across router, rules, skills, and references; freshness/archival obligations are difficult to satisfy consistently. |
| Taxonomy and routing | 53 | Prior audit: taxonomy 48; routing fixture 29/29 top-3, 25/29 rank-1, 0/59 coverage at 3 positives + 2 owned negatives | Discovery performance is measurable but sparse coverage means it does not yet demonstrate reliable routing for most skills. |
| Skill depth | 54 | Prior audit records repeated headings and thin specialist workflows; the quantitative-modelling route needs an explicit distinction between government EMIS and commercial admin software | Worked-example word counts are not evidence of example quality; core task observation still reveals no explicit market-product boundary in the high-level router. |
| Applied proof | 36 | 56/59 skill examples under 60 words; 0/59 routing-complete fixture coverage; Tier-3 work remains zero-spend | Instructions and fixtures do not yet demonstrate full claim-level research products or broad task performance. |
| Standards currency | 52 | `docs/source-registers/research-standards-register.md` overdue since 2026-10-08; six source-register records overdue; TOP statement remains in academic reporting skill | Key current standards need dated source records and verified scope; ICD 206 and RFC 9309 are absent from register. |
| Output readiness | 53 | Prior audit assessed eleven output types, with market evidence pack 45 and benchmark/competitive study 40 | Observed market task cannot support commercial market size, vendor share, Uganda adoption, or current pricing. |
| Accessibility and inclusion | 45 | Prior audit: East African English and Uganda/Kenya academic routes present; limited language and document accessibility checks | No fresh accessibility or language-output assessment was part of the three observation tasks. |
| Production and handoff | 58 | `validate_engine.py` passes 37 tests; prior audit found no real-output rendering evidence | Native tools pass, but live research handoff still lacks archive snapshots and full source-register records. |
| Hygiene | 42 | Prior audit: duplicate sections, cross-engine imports; current checkout has 4 files with machine-specific paths (3 skill files plus `AGENTS.md`) | Old CI cross-engine links were fixed in commit `9ab4eb0`, but machine-specific paths remain and two legacy markdown links were flagged by a naive scan. |
| Safety and integrity | 64 | Evidence discipline; read-only source-evaluation contract; source-ingestion guardrail 0 findings; no-book check passes | Source-verification requires an archive snapshot for every URL; the observation did not establish snapshot availability. Model/account status and manual source-semantic review remain distinct from local validators. |

Simple mean: **52.1/100**. Published cap: `min(52.1, 65) = 52.1/100`.
This is the ten-dimension arithmetic mean, not the prior audit's weighted
overall result of 51.6/100. Any safety, legal, privacy, or release blocker
remains independent of the numerical score.

## Measured inputs

| Measure | Baseline result | Evidence / limitation |
|---|---|---|
| Skill contract | 59 active skills; 59 fully compliant; exit 0 | `python -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json`; automated contract result only. |
| Routing | 29/29 top-3; 25/29 rank-1 = 86.2%; lexical proxy | `python -X utf8 scripts/routing_smoke_test.py`; top-3 threshold 1.000. Not live agent routing. |
| Owned negatives | 9 rows: 7 pass, 0 fail, 2 not assessed; 5 distinct skills have negatives | Same routing run; two not-assessed rows are not passes. |
| Fixture coverage | 0/59 skills have ≥3 positives and ≥2 owned negatives | Recomputed directly from `tests/skill-engine/routing-fixtures.json`. Current distribution: 28 skills with positive rows; five with owned negatives. |
| Worked-example length | 56/59 below 60 words, 0/59 missing a Worked example heading | Read-only heuristic counts words from example heading to next heading; length is only a proxy, not quality. |
| Machine-specific paths | 3 skill files plus `AGENTS.md` contain `C:\wamp64` references | `skills/skill-writing/SKILL.md`, `skills/skill-taxonomy-and-routing/SKILL.md`, `skills/skill-safety-audit/SKILL.md`, `AGENTS.md`. |
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

The branch and all checkout writes remain held until the accounting cycle
finishes. No source register `Last verified` date has been advanced based only
on this preparation record.


## Installation and runtime evidence available at baseline

- The engine's Claude-compatible marketplace install succeeded offline in a
  disposable environment. The loader reports the `research@chwezi-research`
  plugin installed and enumerates all 59 skill directories. Its output says one
  user configuration option is unset (`hooks_enabled`); hook execution is
  therefore **NOT_ASSESSED**. Evidence: `/tmp/chwezi-portfolio-kaizen/chwezi-research-engine-claude-install.log`.
- Codex local-marketplace installation succeeded in an offline disposable
  environment. The plugin inventory reports `installed: true`, `enabled: true`,
  source `/engine`, and `authPolicy: ON_INSTALL`. This records install state,
  not active-session identity or public-directory acceptance. Evidence:
  `/tmp/chwezi-portfolio-kaizen/chwezi-research-engine-codex-install.log`.
- The prior direct plugin validation at baseline passed with warnings: plugin
  description/author absent from the plugin manifest, root `CLAUDE.md` not
  loaded as project context, and icon missing. Marketplace metadata does contain
  attribution and a description. No manifest rebuild is selected based only on
  these warnings. Evidence: `/tmp/chwezi-portfolio-kaizen/digital-research-engine-plugin-baseline.log`.
- Checkout file count at baseline: 1,041 regular files including `.git`, 1,007
  after excluding `.git`; both are far below the 5,000-file ceiling. Counting
  method: `find . -type f | wc -l` and
  `find . -type f -not -path './.git/*' -not -path './.venv/*' -not -path './__pycache__/*' | wc -l`.
