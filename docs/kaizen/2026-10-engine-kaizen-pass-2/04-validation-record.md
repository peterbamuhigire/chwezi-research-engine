# Validation record, kaizen pass 2

As of 2026-10-31 (Africa/Kampala). Repository: Digital Research Engine, branch
`kaizen/2026-10-pass2`, tip `81970a4` before the evidence commit. All commands run
from the repository root with `python3` (Python 3.14.8). Every command below was
run after the last change to engine content. These are lexical, unit and
repository checks; they do not establish live agent behaviour or independent
source review.

## Registered validators and gates

| Command | Exit | Result |
|---|---:|---|
| `python3 -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json` | 0 | 59 active, 59 fully compliant, no failure counts. The run now includes the new `duplicate_heading` and `unresolved_companion_name` codes. |
| `python3 -X utf8 scripts/routing_smoke_test.py --min-rank1 84 --lint-fixtures` | 0 | 40/40 top-3; precision@1 36/40 (90.0%); precision@3 100%; 17 owned negatives: 15 pass, 0 fail, 2 `NOT_ASSESSED`; 0 fixture-lint findings. (Baseline: 34/34, 30/34 = 88.2%, 11 negatives.) |
| `python3 -X utf8 scripts/validate_engine.py` | 0 | Portability scan, file cap, register gate, contract, routing, no-book check, engine doctor and 94 unit tests all pass. (Baseline: 50 tests.) |
| `python3 -X utf8 scripts/check_portable_references.py` | 0 | 389 files scanned (wider scope than the baseline's 376), 0 findings. |
| `python3 -X utf8 scripts/check_file_count_cap.py` | 0 | full checkout 1471/5000; package-oriented 996/5000. The full count includes `.git` and has grown with this branch's objects; the package-oriented count is the preflight proxy for an archive and is not a built-ZIP measurement. |
| `python3 -X utf8 scripts/source_ingestion_guardrail.py` | 0 | 0 findings. |
| `python3 -X utf8 scripts/validate_source_currency.py docs/source-registers/skills-kaizen-wave2-2026-09.json --as-of 2026-10-31` | 0 | 0 findings; printed note `SUPERSEDED: 6 overdue record finding(s) accepted as history`. (Baseline: exit 1, 6 findings.) |
| `python3 -X utf8 scripts/validate_source_currency.py docs/source-registers/kaizen-currentness-2026-10.json --as-of 2026-10-31` | 0 | 0 findings. |
| `python3 -X utf8 scripts/validate_source_currency.py docs/source-registers/kaizen-currentness-2026-10-31.json --as-of 2026-10-31` | 0 | 0 findings. |
| `python3 -X utf8 scripts/validate_source_currency.py tests/fixtures/source-currency.json --as-of 2026-10-31` | 0 | 0 findings; fixture only. |
| `python3 -X utf8 scripts/validate_source_currency.py --registers-dir docs/source-registers --as-of 2026-10-31` | 0 | 3 registers checked, 1 verifier-output file skipped by name, 0 findings. New gate; runs inside `validate_engine.py` and CI as of today. |
| `python3 -X utf8 scripts/validate_machine_error_gate.py` (defaults) | 1 | 3 targets not found: `linux` and `engineering` are not siblings of this checkout on this host (they live under `.claude/skills`), and `political` has no checkout. 9 of 12 resolve. (Baseline: 12 of 12 missing.) |
| `python3 -X utf8 scripts/validate_machine_error_gate.py --engines-root <skill-engines> --engines-root <claude-skills>` | 1 | Only `political` missing. Roots here are this host's checkout directories, not recorded in engine content. |
| The same with `--engine` for the 11 bound engines | 0 | PASS: `accounting, business-plan, design, digital-research, engineering, linux, proposal, social-media, srs, website-copy, windows`, each resolved file printed. Identifier presence only; semantic and visual agreement `NOT_ASSESSED`. |
| `SKILL_ENGINE_LIVE_TESTS=1` with `CHWEZI_ENGINES_ROOT` set and `SKILL_ENGINE_TARGETS` listing the 11 engines: `python3 -X utf8 -m unittest tests.test_machine_error_gate` | 0 | 5 tests pass, none skipped, including the all-visual hard-ban integration test. |
| `python3 -m pytest -q` | NOT_ASSESSED | `No module named pytest` on the system interpreter. Not installed, per the brief. The pytest-based files in `tests/` were not run; the unittest-compatible suites above were. The 29 October record's 184-test run used a portfolio environment that this run did not have. |

Counts cross-checked against an independent source: the 94 unit tests equal the
94 `def test_` definitions found by `grep` in `engine/tests/` (subtests are not
counted separately); the full-checkout file count equals `find . -type f | wc -l`
(1473 after the evidence files were added; the 1471 in the table was read before
two evidence files existed); the package-oriented count follows the script's
documented exclusions and has no independent `find` equivalent. The finding counts
for the two new validator codes (19 and 4) were reproduced on a `git archive`
extraction of the pre-fix tree, not read from the validator's claim about the
repaired tree.

## Failure-path evidence for each new check

| Check | Failing reproduction | Result on repaired tree |
|---|---|---|
| Machine-error fixture holds no host path | The 29 October fixture: 17 entries match a host-path pattern. | 0 entries; test passes. |
| Register supersession and registers gate | Shipped registers on 2026-10-31 before `superseded_by` was added: 6 overdue findings (the test failed). The rejection-path tests (missing successor, overdue successor, undispositioned record, five unsafe `superseded_by` values, another finding in a superseded register, a cycle) fail as intended. | 0 findings; `SUPERSEDED` note printed. |
| Scanner link rules and wider scope | New scanner on the unrepaired tree: 5 findings in 389 files (`CONTRIBUTING.md:7, 17`; `docs/skill-authoring-standard.md:3, 7`; `skills/doc-standards.md:446`). By path over three historical records: link to `skills-web-dev` and workspace-level files, which the old scanner passed. | 0 findings. |
| `duplicate_heading` | Contract validator on a `git archive` extraction of the commit before the fix: `duplicate_heading: 19`, 40 of 59 compliant. | 0; 59 of 59. |
| `unresolved_companion_name` | Same method: 4 findings, all `data-quality-assessment` (the registry file copied in so that only the real defect shows). | 0. |

## Step 1 re-run

**Task 1, Uganda NSSF employer rate.** Re-applied with `single-claim-lookup.md`
(no new page was needed; the reads of 2026-10-31 stand). The headline answer is
unchanged: 10% employer, 5% employee, 15% total, due by the 15th of the following
month. It now carries what the baseline answer left to the agent's diligence: the
membership page is undated (footer "2019-2021"), the Ministry page is the only
dated statement (15 June 2026), the statute consolidation is "as at 31 December
2000" with Act 1 of 2022 and General Notice 2917 of 2024 unapplied, and whether
those amendments changed sections 11 or 12 is `NOT_ASSESSED`. The record is Worked
example 2 in the reference. Routing probe: `source-evaluation` is rank 2, from
outside the top five.

**Task 2, school management software market.** Re-applied with the revised
`quantitative-modelling`. The brief records each denominator with its definition
(45,164 registered against 26,597 responding Ugandan primary schools), quarantines
the vendor figures (6,000 for Uganda, an East Africa total that fails its own
sum), flags the Kenyan count break, and still stops at a gap for market size. No
price, paid adoption or vendor revenue was found. Probe: `quantitative-modelling`
is rank 4 and the two country-named academic skills still outrank it.

**Task 3, held-out false premise.** Question: "Why did Uganda's NSSF raise the
employer contribution to 12 percent in 2025?" Following the reference. Premise
list: (a) the employer rate was raised, (b) to 12 percent, (c) in 2025. Test: two
current official statements give 10% employer (one reviewed 15 June 2026, one
undated), the statute text as consolidated gives 15% total with a 5% employee
share, and a search for a 2025 increase found no report of one; the only
12 percent figures found were a fund interest or return figure and Kenya's 6% plus
6% split. **Answer first:** the premise is contradicted by the current statements
(10% employer) and no source supports an increase; the better question is where a
12 percent figure came from. The suggestion that the figure was confused with an
interest or Kenyan figure is an **(inference)** from search results and is not
verified. Limits: one of the two statements is undated, the consolidation
predates the 2022 amendment, no archive snapshot, and absence of a report is not
proof of absence of a change. This is a second premise handled by the same
procedure, not a measurement of agent behaviour.

Lexical routing probe, before and after (scores from `routing_smoke_test.rank`):

| Prompt | Baseline top | After |
|---|---|---|
| Current Uganda NSSF employer rate | `uganda-academic-research` 22.0; `source-evaluation` not in top five | `uganda-academic-research` 22.0; `source-evaluation` rank 2 at 15.0 |
| Current NSSF employer rate (no country word) | `systems-thinking-and-mental-models` 8.8; `source-evaluation` rank 55 | `source-evaluation` rank 1 at 15.0 |
| Kenya flat KES 200 false premise | `kenya-academic-research` 35.2, then zeros | unchanged; limit of the proxy |

## Step 5: currency and the gate

| Item | Observation on 2026-10-31 | Record |
|---|---|---|
| PRISMA | Official page presents PRISMA 2020 as the current statement; no successor; page undated (copyright 2024-2026). PRISMA-C 2026 extension: children and adolescents aged 0-19, BMJ 2026;393:e088561. | `SRC-PRISMA-CORE-2026-10-31`, `SRC-PRISMA-C-2026-10-31`: verified |
| GRADE | Living Map footer "Version: 13 June 2026". Separates current, superseded and archived sources and says related papers are not valid GRADE guidance. Does not mention the old Handbook. | verified, scoped |
| Cochrane Handbook | Version 6.5, "Last updated: 22 August, 2024"; no newer version announced. | verified |
| ICD 203 | `archive.dni.gov` PDF, 8 pages: base directive signed 2 January 2015; two technical amendment pages (annual training; and a page printing 21 January 2022 while citing a memorandum signed 22 August 2022). Text layer looks OCR-derived. | partial; latest amendment `NOT_ASSESSED` |
| ICD 206 | PDF is image-only; no text; no OCR tool on this host. | `NOT_ASSESSED`; the 29 October amendment date is unconfirmed |
| RFC 9309 | Proposed Standard, Internet Standards Track, copyright 2022, no obsoletes or updates statement in the text returned. Errata not listed in what was returned. | partial; errata `NOT_ASSESSED` |
| TOP | TOP 2025: seven Research Practices, two Verification Practices, four Verification Study types, three levels for Research Practices; "Updated in 2025", 2026 citation. | verified |
| ODNI locators | `www.dni.gov` ICD 203 URL 301 to `www.odni.gov`; `www.odni.gov` ICD 203 and 206 URLs 301 to `archive.dni.gov`. | verified as observed behaviour; links in `analytic-tradecraft` updated |
| Model currentness | OpenAI changelog: GPT-6.1 Terra 26 October; GPT-6 Rosalind 30 October (trusted access, life-sciences research). Catalogue flagship list unchanged: Astra, Sol 6.1, Terra, Luna. | Luna/high Codex pin retained. Release noted; a release alone does not justify a change and the entry names no replacement. Full comparison last 28 September; due by 28 December. Claude's own model selection is outside that policy and unchanged. Task fit, cost, latency, quality: `NOT_ASSESSED`. |
| Gate paths | Every path the currentness gate and the Standard name exists in this checkout (`.codex/model-policy.md`, `docs/source-registers/`, the model review file) except the Windows path `<drive>:\<web-root>\digital-research-engine`, named once in each, which exists on no other host. | Documents not edited; proposed text in `06-next-cycle.md` |
| `skills-kaizen-wave2-2026-09` register | Six records dispositioned on 29 October and now machine-checkably superseded. | closed |

## NOT_ASSESSED and outstanding

- Archive snapshots: none captured for any record or task; the universal archive gate is unchanged and needs Peter's decision.
- Live-agent routing, Tier 3 behaviour, comparative model quality, cost and latency: not run; no paid calls.
- ICD 206 content and the latest ICD 203 amendment: unreadable here.
- RFC 9309 errata: not read.
- The Kenya NSSF "Clarification on the Status of NSSF Contributions" (4 June 2026 headline) was not read; the Task 3 answer stands for the February 2026 notice only.
- Whether Act 1 of 2022 or General Notice 2917 of 2024 changed Uganda's section 11 or 12: unread.
- System pytest; remote CI state; marketplace readiness; installed-plugin discovery this pass (the 29 October operator evidence was not repeated).
- Independent human review of any support state: none available.
- Sibling engines: identifier presence only; no semantic review. `political-essay-skills`: no checkout, so its target is unchecked.
- Oracle `055-route-release-evidence-mirror` lives in `chwezi-engine-agents/evals/cases/`; not run here.
- No package was installed. No `npm ci` was needed or run.
