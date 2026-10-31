# Digital Research Engine: kaizen pass 2, scope and observation record

Date: 2026-10-31 (Africa/Kampala)
Cycle: `2026-10-engine-kaizen-pass-2`, a continuation of the 29 October 2026 cycle
(`docs/kaizen/2026-10-engine-kaizen/`).
Mode: observation and baseline only. Nothing in this file was written after a
change to engine content; the baseline in `01-baseline-scorecard.md` is frozen
from the measurements recorded here.

## Step 0: preconditions

| Item | Result |
|---|---|
| Starting branch | `main` |
| Starting HEAD | `d350ce2` (`docs(research): normalise final audit whitespace`, 2026-10-29) |
| `git status --porcelain` at start | empty (0 lines); no foreign uncommitted files to preserve |
| Working branch | `kaizen/2026-10-pass2`, created from that HEAD with `git switch -c` |
| Tracked files | 984; regular files on disk 1,080 excluding `.git`, 1,268 including it |
| Toolchain | Python 3.14.8, Node 22.23.1; no `pwsh`, no `pytest` on the system interpreter |
| Push, tag, pull request | none made, none planned |

Read before observing: `AGENTS.md`, `CLAUDE.md`, the Portfolio Kaizen Standard,
the currentness gate, the 29 October evidence folder (all seven files), the
29 September re-audit (executive summary and roadmap), `kaizen-research-loop.md`,
and the skills used in the three tasks: `source-evaluation`, `source-verification`,
`research-orchestration`, `evidence-claim-graph`, `critical-reasoning-and-argument`
and `online-legal-research`. The two protected documents
(`docs/continuous-improvement/portfolio-kaizen-standard-2026-08.md`,
`docs/continuous-improvement/kaizen-currentness-gate.md`) were read and are not
edited in this cycle; proposed changes go to `06-next-cycle.md`.

### Inputs carried over from 29 October

The 29 October report left these items open. Each was re-checked against HEAD
`d350ce2` before being used here.

| Carried item | Confirmed state on 2026-10-31 |
|---|---|
| Archive snapshots for live-source verification | Still open; needs Peter's decision on an archive workflow. Not changed this cycle. |
| Independent human review of the standards register | Still open; no second reviewer available to this run. |
| Cross-engine machine-error handoff | Still open; the validator still cannot run on this host (see defect D-01). |
| School-administration software market size | Still a gap; this cycle's search again found no product-matched figure (Task 2). |
| Fixture coverage beyond one route | Open: 1 of 59 skills has three positives and two owned negatives. |
| Tier 3 behaviour, remote CI, marketplace | `NOT_ASSESSED`; no paid model calls, no remote state read. |
| Prompt-listed open findings from September: two CI links into a sibling checkout | Closed at `9ab4eb0`; no cross-repository link remains in `skills/` (scan below). |
| September finding: 14 imported engineering skills, three near-duplicates | Open, structural, moved to `06-next-cycle.md`. |
| September finding: worked examples under 60 words | Open: 55 of 59 (was 56). |
| September finding: oracle `055-route-release-evidence-mirror` fails at rank 4 | Not testable from this checkout. The case lives in the portfolio package (`chwezi-engine-agents/evals/cases/055-route-release-evidence-mirror.yaml`) and is evaluated in union mode there. This repository's routing run reports 0 failures and holds no row with that id. Status `NOT_ASSESSED` here; passed to the portfolio cycle. |

## Step 0.5: validators run once, before any change

All commands run from the repository root. Exit codes and counts are as printed.

| Command | Exit | Result |
|---|---:|---|
| `python3 -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json` | 0 | 59 active, 59 compliant, no failure counts |
| `python3 -X utf8 scripts/routing_smoke_test.py` | 0 | 34/34 top-3; precision@1 30/34 (88.2%); precision@3 100%; owned negatives 11 (9 pass, 0 fail, 2 `NOT_ASSESSED`) |
| `python3 -X utf8 scripts/validate_engine.py` | 0 | contract and routing pass; no-book check OK; engine doctor OK; 50 unit tests OK |
| `python3 -X utf8 scripts/check_portable_references.py` | 0 | 376 files, 0 findings |
| `python3 -X utf8 scripts/check_file_count_cap.py` | 0 | full checkout 1268/5000; package-oriented 987/5000 |
| `python3 -X utf8 scripts/source_ingestion_guardrail.py` | 0 | 0 findings |
| `python3 -X utf8 scripts/validate_source_currency.py docs/source-registers/kaizen-currentness-2026-10.json --as-of 2026-10-31` | 0 | 0 findings; metadata and dates only |
| `python3 -X utf8 scripts/validate_source_currency.py tests/fixtures/source-currency.json --as-of 2026-10-31` | 0 | 0 findings; fixture only |
| `python3 -X utf8 scripts/validate_source_currency.py docs/source-registers/skills-kaizen-wave2-2026-09.json --as-of 2026-10-31` | 1 | 6 findings: every record overdue (`review_after` 2026-10-03) |
| `python3 -X utf8 scripts/validate_source_currency.py docs/source-registers/skills-kaizen-wave2-2026-09-verification.json --as-of 2026-10-31` | 1 | `sources must be a nonempty list`. This file is a verification log, not a register, so the failure is a wrong input rather than a defect. It is recorded so nobody repeats it. |
| `python3 -X utf8 scripts/validate_machine_error_gate.py` | 1 | 12 of 12 targets missing: every path in the fixture begins `C:/wamp64/www/` |
| `python3 -m pytest` | NOT_ASSESSED | no `pytest` module on the system interpreter; not installed, per the brief |

The prompt also lists `python -X utf8 ...`; on this host the interpreter is
`python3`, so every command above uses `python3`.

## Step 1: observation

Router path used for all three tasks: `AGENTS.md` standard workflow, then
`source-evaluation` with `evidence-discipline`, then `source-verification`.
`research-orchestration` was read and rejected for Tasks 1 and 3 because its own
"Do Not Use When" excludes a single known fact lookup (line 21). The lexical
routing proxy (`scripts/routing_smoke_test.py`, imported read-only) was also run
on each prompt to see what a description-matching agent would load first.

| Prompt | Top five by lexical proxy | Verdict |
|---|---|---|
| "What is the current Uganda NSSF employer contribution rate?" | `uganda-academic-research` 22.0, `systems-thinking-and-mental-models` 8.8, `capability-matrix` 8.0, `doctrine-spine` 8.0, `systems-process-requirements` 7.4 | Wrong. No evidence skill and no legal skill appears. The country token carries the whole score. |
| "Assess the school management software market in Uganda and Kenya." | `kenya-academic-research` 35.2, `uganda-academic-research` 22.0, `calibration-and-forecasting` 9.9, `quantitative-modelling` 9.9, `source-evaluation` 8.8 | Partly right. The intended route is fourth; two academic-research skills outrank it. |
| "Why does Kenya's NSSF still cap employee contributions at a flat KES 200 a month in 2026?" | `kenya-academic-research` 35.2, `data-quality-pipeline` 4.4, then zero scores | Wrong. One irrelevant skill, then nothing. |

The proxy is not live routing. A live agent also reads `AGENTS.md`, which does
list `source-evaluation` and `source-verification` first. The finding is that the
two country skills carry descriptions heavy enough in country names to win any
description-based choice for a country-specific question that is not academic.

### Task 1: current-state question with a checkable answer

**Request:** "What is the current Uganda NSSF employer contribution rate?"

**Answer produced.** The employer contribution is 10% of the employee's gross
monthly wage, and the employee contribution is 5%, for 15% in total. Contributions
are due by the 15th day of the following month. Two current official statements
agree, and the statute text agrees on the total and on the employee share.

**Evidence record.**

| Item | Source | Tier | Observed on 2026-10-31 |
|---|---|---|---|
| Employer 10%, employee 5%, total 15%, due by the 15th of the following month | NSSF Uganda, membership page (`nssfug.org/about-us/membership/`) | 1, first party | Page states the rates and deadline in those words. **The page carries no publication or revision date.** The only date is a footer, "2019-2021 NSSF Uganda. All Rights Reserved". Currency of this page is therefore unproven on its own terms. |
| Same rates and deadline; statutory basis named as the National Social Security Fund Act (Cap. 230) and the 2022 Amendment Act | Ministry of Finance business portal (`doingbusiness.finance.go.ug/licensing/nssf-employer-registration`) | 2, official secondary | Page states "Last reviewed: 15 June 2026" and the same figures. This is the only dated current statement found. |
| Section 11(1): "a standard contribution of 15 percent calculated on the total wages"; section 12(1): employee's share "of 5 percent" | National Social Security Fund Act, Uganda Legal Information Institute consolidation | 1, primary legal text | The consolidation header reads "Chapter 222, Legislation as at 31 December 2000" and warns "There are outstanding amendments that have not yet been applied: Act 1 of 2022, Act 1 of 2022, General Notice 2917 of 2024." I extracted the section text from the saved PDF with `pdftotext`. |
| No source reports a 2026 change to the split | Search of current reporting | 3 and 5 | No change found. Not used as support, only as absence of contrary evidence. |

**Verification and support state.**

- Employer 10% and employee 5%: `supported` by two current official statements and by the 2000-dated statute text. The statute frames the employer as liable for the full 15% with a right to deduct the employee's 5% (sections 11 and 12), so the "10% employer" figure is the scheme's presentation of the remainder, an **(inference)** from the two sections.
- Whether Act 1 of 2022 or General Notice 2917 of 2024 altered section 11 or 12 percentages: `NOT_ASSESSED`. The consolidation does not apply them. The 2021 Bill PDF has a scanned operative text layer that could not be read, so its clauses were not checked.
- Chapter number: the consolidation says Cap. 222 and the Ministry page says Cap. 230. Both may be right for different editions of the laws; this was not checked and is `NOT_ASSESSED`.
- Archive snapshot: not captured (no authorised archive write). Archive verification is `NOT_ASSESSED`.

**Judgement against the Mission standard.** The headline answer is correct and
dated. Three things a careful analyst would want were left to the agent's own
diligence rather than the engine's guidance: the undated first-party page, the
stale statute consolidation with a visible outstanding-amendments banner, and the
absence of any lightweight record shape for a single claim (see D-04 and D-05).

### Task 2: broad brief

**Request:** "Assess the school management software market in Uganda and Kenya."

**Method.** A bounded web search and four page or document reads. This is a
sample, not a market scan. Fetched content was treated as data.

**Evidence.**

| ID | Claim | Source and locator | Tier | Support state and limit |
|---|---|---|---|---|
| E1 | Uganda had 45,164 primary schools on its education information system in 2025: 12,544 government and 32,620 private. 7,466 secondary: 1,507 government and 5,959 private. 24,923 pre-primary, all private. | Uganda Education Statistical Abstract 2025, executive summary (Ministry of Education and Sports; file dated 23 December 2025; extracted with `pdftotext`) | 2 | Supported for registered schools. |
| E2 | Of those primary schools, 26,597 responded to the system: 12,511 government (47%) and 14,086 private (53%). | Same abstract | 2 | Supported. Registered and responding counts differ by 18,567. Which one is a denominator for a software market is a modelling choice, not a fact. |
| E3 | Kenya had 130,659 institutions offering basic education in 2025: 48,190 pre-primary, 39,339 primary, 32,079 junior and 11,051 secondary. | KNBS Economic Survey 2026, as reported by Radio Generation, 1 May 2026 | 3 (secondary report of a tier 2 release) | Supported at secondary remove. The primary release was not opened. Junior schools were folded into basic education, so earlier counts are not comparable. |
| E4 | A vendor planning document gives East Africa as "30,200 schools (Kenya: 12,000, Tanzania: 7,500, Uganda: 6,000, Rwanda: 1,200)" and a global serviceable market of USD 10 billion. | YeboLearn internal business page, "Last Updated: November 23, 2025" | 5, vendor self-assertion | Rejected as a denominator. The four country figures sum to 26,700, not 30,200. Its Uganda figure is 6,000 against 45,164 in E1. It cites no link for its country counts and is internally inconsistent on its own serviceable-market figures (USD 10 billion and 10.3 billion). |
| E5 | Kenya: 23% of surveyed respondents used a school management system. | Acumen East Africa education research, Kenya (carried forward from 29 October; not re-opened) | 3 | Supported within that survey only. Not a national rate. |
| E6 | No source found that sizes a paid school-administration software market for Uganda, Kenya or both. | Search of market-research vendors and aggregators | n/a | **Gap.** Results were report tables of contents, vendor blogs and a general Statista "administrative software" outlook for Eastern Africa that is not school-specific. |

**Conflicts handled.**

- Uganda school count: 45,164 (E1) against 6,000 (E4). Resolution: E1 is an official statistical release for a defined year and a defined register; E4 is an unsourced vendor figure. E4 is quarantined and not averaged with E1.
- Kenya school count: 12,000 (E4) against 39,339 primary plus 11,051 secondary (E3). Same resolution. Even the sum of E3's primary and secondary counts (50,390) is four times E4.
- Denominator definition inside one source: registered (45,164) against responding (26,597) in E1/E2. Both are reported; neither is chosen for the reader.
- Kenya count basis changed between years: E3 counts junior schools as basic education from 2024 onward, so 2023 and 2025 counts differ by definition as well as by growth.

**Evidence-claim graph (compact).**

| Node | Type | Edges |
|---|---|---|
| E1, E2 | evidence | support C1: Uganda has a large private-school base |
| E3 | evidence | supports C2: Kenya has a larger institution count than Uganda at every level |
| E4 | evidence (rejected) | contradicts C1 and C2 on counts; excluded as tier 5 with arithmetic error |
| E5 | evidence | supports C3: some Kenyan respondents use school management systems; scope limited to that survey |
| C1, C2 | claims | together bound a school-count denominator; they do not size a market |
| C4 | inference | "private schools are a plausible buyer segment"; **(inference)**, no source shows willingness to pay |
| G1 | gap | price per school, paid adoption rate, vendor revenue: no source found |
| G2 | gap | primary KNBS release not opened for E3 |

**Synthesis.** The evidence fixes the number of schools in each country well
enough to name the buyer population and shows that vendor-supplied counts cannot
be used. It does not support a market size: no source gives price, paid adoption
or vendor revenue for school administration software in either country. The
brief should say so and stop there. **(synthesis)**

**Limitations statement.** Bounded sample of about eight sources. Kenya counts
rest on a news report of a statistical release. No vendor pricing, customer
interview or procurement data was found. Uganda's registered count includes
schools that did not respond to the system and may include inactive schools; this
was not tested. The Uganda and Kenya counts are for different years and
definitions. This is an absence of evidence in the sample, not evidence that the
market is small.

**Judgement.** The market-boundary rule added on 29 October held: no adjacent
figure was relabelled as a market size. Two gaps: the engine has no worked rule
for conflicting denominators (registered against responding, definition changes)
and no instruction to check a vendor figure's internal arithmetic. Both were done
by hand here (see D-07).

### Task 3: question built on a false premise

**Request:** "Why does Kenya's NSSF still cap employee contributions at a flat
KES 200 a month in 2026?" This replaces the 29 October premise (the Uganda EMIS)
so the cycle tests a new case.

**Answer produced.** The premise is false and the question cannot be answered as
asked. Kenya's NSSF Year 4 notice (effective February 2026) sets contributions at
6% of pensionable earnings for employee and employer alike, in two tiers: a lower
earnings limit of KES 9,000 (maximum KES 540 each) and an upper earnings limit of
KES 108,000 (Tier 2 maximum KES 5,940 each). The maximum employee contribution is
therefore KES 6,480 a month, and the maximum for employee and employer together is
KES 12,960. Employers remit by the 9th day of the following month. A better
question is how the phased increase under the Third Schedule works, or why the
flat figure is still quoted.

**Evidence record.**

| Item | Source | Tier | Observed |
|---|---|---|---|
| Year 3 rates ended on 31 January 2026; Year 4 rates apply from February 2026; limits and maxima as above; remittance by the 9th | NSSF Kenya, "Notice to Employers, Year 4 (2026) NSSF Contribution Rates", Managing Trustee and CEO, citing the Third Schedule of the NSSF Act (Cap. 258) | 1, first party | Text extracted with `pdftotext`. The notice is hosted on a government site other than `nssf.or.ke`, carries no printed issue date (it refers to a 6 February 2026 annual general meeting, so it post-dates that), and its embedded file metadata shows April 2025 creation, which I treat as template reuse and not as the notice date. |
| Same limits and maxima | Several payroll and law-firm summaries of the Year 4 rates | 3 and 5 | Consistent with the notice; used only as corroboration. |
| `nssf.or.ke` home page | NSSF Kenya | 1 | States no rates; shows a 4 June 2026 "Clarification on the Status of NSSF Contributions" headline whose text was not read. **That clarification is unread and could bear on the answer: `NOT_ASSESSED`.** |

**What was not established.** The history of the KES 200 figure, and when it was
replaced, was not checked against a primary source in this run; it is not asserted
here. The unread 4 June 2026 clarification is open. No archive snapshot.

**Judgement.** The premise was detected and stated before answering, but only
because the agent chose to check the premise. No skill, rule or router line asks
for it: a search of `skills/`, `rules/` and `AGENTS.md` for "false premise",
"presuppos", "premise check" and "loaded question" returns zero hits. The
critical-reasoning method (lines 43 and 44) asks to "flag ambiguous or loaded
language" but not to test the factual presuppositions inside the question. That
skill also excludes narrow factual questions in its own "Do Not Use When"
(line 26). See D-03.

## Defects and guidance gaps

Severity follows the brief: critical (safety, legal, financial, privacy or release
failure), major (a gate cannot run, a guidance gap changed an output), minor.

| ID | Severity | File and line | Finding |
|---|---|---|---|
| D-01 | Major | `scripts/validate_machine_error_gate.py:40`; `tests/fixtures/machine-error-gate-baseline.json:8-26` | The validator reads each target with `Path(target["path"])` and the fixture holds 17 hard-coded `C:/wamp64/www/...` paths. On any other host all 12 targets fail as missing, so the cross-engine handoff check cannot run. Every target except one exists under a renamed or relocated checkout on this machine. |
| D-02 | Major | `scripts/validate_source_currency.py:93-94`; `docs/source-registers/skills-kaizen-wave2-2026-09.json`; `.github/workflows/skill-engine-quality.yml` (last step) | The validator has no concept of a superseded register, so six records that the 29 October cycle dispositioned still fail with exit 1. Separately, CI runs the validator only on `tests/fixtures/source-currency.json` with a fixed date of 2026-08-06; no real register is checked by CI, so an expired record cannot block release. `AGENTS.md` says overdue records block release. |
| D-03 | Major | `skills/critical-reasoning-and-argument/SKILL.md:22-26, 43-44`; `skills/research-orchestration/SKILL.md:19-21` | No rule anywhere asks the agent to extract and test factual presuppositions in a question. Grep for "false premise", "presuppos", "premise check", "loaded question": 0 hits in `skills/`, `rules/`, `AGENTS.md`. |
| D-04 | Major | `skills/research-orchestration/SKILL.md:19-21`; `skills/evidence-claim-graph/SKILL.md:23`; `skills/critical-reasoning-and-argument/SKILL.md:26` | Three skills each exclude a single-claim lookup and none says where it goes. A current-state question (Tasks 1 and 3) has no owner, no record shape and no stop rule. |
| D-05 | Major | `skills/source-evaluation/references/freshness-and-uncertainty.md:12-14, 28-35`; `skills/online-legal-research/references/east-african-overlay.md:106` | Nothing covers a first-party page with no date and a stale footer year (Task 1), or a statute consolidation whose own header lists outstanding amendments (Task 1). The overlay's "statute currency" step says to locate the consolidated version and check the gazette amendment index but not to read the repository's own currency notice. Grep for "undated" in `source-evaluation` and `source-verification`: 0 hits. |
| D-06 | Major | `skills/uganda-academic-research/SKILL.md` and `skills/kenya-academic-research/SKILL.md` descriptions | Country-name density lets these two skills outrank every evidence skill for non-academic country questions under description matching (table above). |
| D-07 | Minor | `skills/quantitative-modelling/SKILL.md` (market-boundary section) | The 29 October boundary rule covers product and buyer. It has no rule for conflicting denominators (registered against responding; definition changes) or for checking a vendor figure's own arithmetic. |
| D-08 | Major | `scripts/check_portable_references.py:10-11, 15-17`; `CONTRIBUTING.md:7, 17`; `docs/skill-authoring-standard.md:3, 7` | Two scanner false negatives. (a) The sibling-link pattern matches only names beginning `chwezi-`, so `../../../skills-web-dev/...` passes. (b) The default scope is `AGENTS.md`, `README.md` and `skills/**/*.md`, so host-absolute paths in `CONTRIBUTING.md` and the authoring standard, which new skills are told to follow, are never scanned. The scanner also checks no relative link for existence. |
| D-09 | Minor | `skills/doc-standards.md:446` | Link to `docs/markdown-portability-reference.md`, a file that never existed in this repository (`git log --all` returns nothing for it). |
| D-10 | Minor | `docs/continuous-improvement/ai-slop-responsibility-assessment-2026-09-11.md:7`; `kaizen-wave-1-2026-08-11.md:14,20,36`; `kaizen-wave-2-2026-08-11.md:30,31,58` | Seven relative links climb out of the repository (to `skills-web-dev` and to two workspace-level report files). They resolve only where a sibling or parent file exists. |
| D-11 | Minor | `skills/*/SKILL.md` (19 skills) | Duplicate H2 headings in 19 skills (13 repeat "Companion Skills", the rest "See also", "Sources for this skill", "Reference index", "Core outcome", "Orchestrator outputs"; `capability-matrix` has three). The contract validator checks duplicates only for its 13 required section titles, so these pass. Nine more skills carry generated "Evidence Notes 1" and "Evidence Notes 2" headings. |
| D-12 | Minor | `skills/data-quality-pipeline`, `skills/dataset-discovery-and-analysis`, others: 7 mentions | Companion lists name `data-quality-assessment` (4 mentions) which is no active skill. `world-class-engineering` (2) and `data-visualization` (1) are skills in other engines and are named without saying so. |
| D-13 | Major (owner decision) | `docs/continuous-improvement/english-collocations-and-lexical-precision-2026-09-02.md:146-147` | Two "Local source" lines give a personal Windows path and filenames that carry the markers of unofficial book-sharing sites. No book content is stored, so the no-extraction rule is not breached, but the provenance line is a machine-specific path with personal data and signals unlawful copies. Not edited: it is a user-authored provenance record. Escalated to Peter. |
| D-14 | Minor (protected file) | `docs/continuous-improvement/portfolio-kaizen-standard-2026-08.md:76`; `docs/continuous-improvement/kaizen-currentness-gate.md:52` | Both name `C:\wamp64\www\digital-research-engine`, a path that exists on no other host and that differs from the local checkout name here. Not edited, by instruction. Proposed text in `06-next-cycle.md`. |
| D-15 | Minor (protected file) | `docs/continuous-improvement/kaizen-currentness-gate.md:49`; `scripts/validate_source_currency.py:12` | The gate lists evidence fields (`source_id`, access date, verification date, review date) that the validator names differently (`id`, `accessed`, `verified_at`, `review_after`). The mapping is written nowhere, and sibling registers use a third naming (below). |

No critical defect was found: no output contained a fabricated claim, no secret
or personal credential is in the repository, and no safety, legal, financial or
privacy failure reached an output. D-13 is the closest to a legal or privacy flag
and is escalated for an owner decision, not hidden behind the score.

## Measured inputs, fresh

| Measure | Value | Command or method |
|---|---|---|
| Active skills | 59 | contract validator |
| Routing precision@1 / top-3 | 30/34 (88.2%) / 34/34 (100%) | `routing_smoke_test.py` |
| Owned negatives | 11 rows, 9 pass, 0 fail, 2 `NOT_ASSESSED` | same run |
| Skills with at least one positive fixture | 29 of 59 | recount from `tests/skill-engine/routing-fixtures.json` |
| Skills with at least one owned negative | 6 of 59 | same recount |
| Skills with three positives and two owned negatives | 1 of 59 (`quantitative-modelling`) | same recount |
| Worked examples under 60 words | 55 of 59 (median 26 words); four at 60 words or more | word count from the "Worked example" heading to the next heading |
| Broken relative links, active scope (`AGENTS.md`, `README.md`, `skills/**/*.md`, 376 files) | 1 (D-09) | read-only link scan, fenced code skipped |
| Relative links leaving the repository, active scope | 0 | same scan |
| Relative links leaving the repository, `docs/continuous-improvement` | 7 (D-10) | same scan over the five non-historical `docs/` folders (40 files) |
| Machine-specific paths, tracked text | 28 files outside `projects/` and 3 inside it. Three outside `docs/` history are in scope for repair: `CONTRIBUTING.md`, `docs/skill-authoring-standard.md` and the machine-error fixture. `engine/tests/test_portable_references.py` holds deliberate negative test strings. The rest are dated plans, audits and reports (immutable history) plus the two protected documents. | `git grep -lIE` for drive-letter, `/home/`, `/Users/` forms |
| Duplicate H2 headings | 19 skills, 19 heading pairs; 9 skills with generated "Evidence Notes N" | scripted count |
| Companion names that are neither active skills nor declared external | 3 distinct names, 7 mentions | scripted count over "Companion Skills" sections |
| Dangling cross-engine references | 3 names (above); 6 sibling routers hard-code the research engine path (below) | grep over sibling checkouts |
| Expired source records | 6 (all in `skills-kaizen-wave2-2026-09.json`) | `validate_source_currency.py` |
| Source records due within 30 days | 4 (the OpenAI platform records, `review_after` 2026-11-29) | register read |
| Checkout file count | 1268/5000 full; 987/5000 package-oriented | `check_file_count_cap.py` |

## Cross-engine boundary check (read-only)

The brief forbids editing any sibling; this section records only.

| Engine file | Line | Observation |
|---|---:|---|
| `chwezi-accounting-doctrine/AGENTS.md` | 56 | Names `C:\wamp64\www\digital-research-engine`. |
| `design-system-skills/AGENTS.md` | 66 | Same. |
| `srs-skills/AGENTS.md` | 47 | Same. |
| `social-media-skills/AGENTS.md` | 47, 232 | Same; line 232 says to locate the repository locally if the path differs. |
| `website-skills/AGENTS.md` | 61, 371 | Same; line 371 says to resolve through the engine-routing table, then repeats the Windows path. |
| `skills-web-dev/AGENTS.md` (dev engine) | 40 | Same. |
| `linux-skills/AGENTS.md` | 46, 175 | Correct: "resolve through the device catalogue". |
| `windows-admin-engine-skills/AGENTS.md` | 58, 166 | Correct: resolves through the device catalogue. |
| `proposal-skills/AGENTS.md` | 47 | Correct: resolves through the catalogue binding. |
| `chwezi-engine-agents/catalog/engines.yaml` | 80-82 | Catalogue path is `digital-research-engine`; the local directory here is `chwezi-research-engine`. |

Register convention: this engine's validator requires `id`, `accessed`,
`verified_at`, `review_after` and `freshness_class`. Run read-only against
sibling registers with `--as-of 2026-10-31`, the validator returns 308 findings
for `windows-admin-engine-skills/engine/source-register.yaml` (it uses `status`
and `accessed` only), 20, 22 and 41 for three `website-skills` registers, and one
finding each for the social-media, business-plan and proposal registers. The
sibling registers do not share this engine's schema, so a handed-off claim cannot
be machine-checked on arrival. Recorded for the portfolio cycle.

Machine-error gate targets: every target except `political-essay-skills` exists
under its current local name (checked with `test -f`). `political-essay-skills`
has no checkout in `skill-engines/` on this machine.
