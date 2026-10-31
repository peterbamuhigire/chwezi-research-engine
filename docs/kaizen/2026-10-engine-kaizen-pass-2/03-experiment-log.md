# Experiment log, kaizen pass 2

Cycle: `2026-10-engine-kaizen-pass-2`, branch `kaizen/2026-10-pass2`.
The baseline in `01-baseline-scorecard.md` was committed (`436dd70`) before the
first change. Each entry below is a plan, do, study, act record for one backlog
item. One change at a time; every kept change has its own commit. No paid model
call, archive write, push, tag or pull request was made.

Where an entry says "failing reproduction", the new check was run against the
committed tree from before the fix (extracted with `git archive` to a scratch
directory outside the repository) and failed there, then passed on the repaired
tree. That is the evidence the check can fail, not only pass.

## R2-01: machine-error gate resolves targets by portfolio root

- **Plan.** Hypothesis: if targets are named by engine directory plus a root-relative path, the gate runs on any host and reports a real result per engine.
- **Do.** `scripts/validate_machine_error_gate.py` resolves each target under `--engines-root` (repeatable), `CHWEZI_ENGINES_ROOT`, or the parent of the checkout, with an alias table for renamed checkouts (`engine_aliases` in the fixture). The fixture holds no host path. The `digital-research` target uses `self`, so it works under any clone name. An unresolvable target is an error. `AGENTS.md` documents the options.
- **Study.** 12 new unit tests pass (`engine/tests/test_machine_error_gate_roots.py`), including: alias resolution, canonical name wins over alias, second root searched, unresolvable target fails closed, relative path without `engine_dir` fails closed, an unbound target skipped only when the engine is not selected, and a check that the shipped fixture holds no host path. Failing reproduction for that last check: the 29 October fixture has 17 host-path entries. Live run on this host with roots `skill-engines` and `.claude/skills` and the 11 bound engines selected: PASS, 11 engines, each resolved file printed. All 12 targets: FAIL on one target only, `political` (no checkout). The opt-in live tests (`SKILL_ENGINE_LIVE_TESTS=1`) pass, including all five visual adapters. `validate_engine.py` exit 0.
- **Act.** Kept. Commit `00bdc44`.
- **Unplanned finding.** The social-media target, recorded on 29 October as missing the ME2 to ME6 and AS2 to AS6 identifiers, passes today. That engine has since had its own commits (read-only observation; not mine). The 29 October mismatch no longer reproduces; semantic agreement stays `NOT_ASSESSED`.

## R2-02: machine-checkable register supersession and a release gate for real registers

- **Plan.** Hypothesis: if a historical register can name a validated successor, and every real register is checked as of today, overdue records block release as `AGENTS.md` says and a register that is only history stops failing.
- **Do.** `validate_source_currency.py` gains an optional top-level `superseded_by`, accepted only when the successor exists, validates with 0 findings on the same date, and lists a disposition for every old source ID; the file name must be relative and without `..`; cycles are rejected. New `--registers-dir` mode checks every JSON file with a `sources` key and skips others by name. Wired into `validate_engine.py` and the CI workflow. `superseded_by` added to the older register (one top-level key; no record changed).
- **Study.** 13 new tests pass (`engine/tests/test_source_currency_supersession.py`): accepted pairing; missing successor, overdue successor, undispositioned old ID, unsafe `superseded_by` values (five subcases) and a two-register cycle each still fail; another finding in a superseded register still fails; directory mode skips verifier output, reports file names, fails closed on an empty directory and on unreadable JSON. Failing reproduction: before the key was added, the test that checks the shipped registers failed with the six overdue records; after, it passes. Command on the older register: exit 1 with 6 findings before, exit 0 with a printed `SUPERSEDED` note after. `registers-dir` mode today: 3 registers checked, 0 findings. `validate_engine.py` exit 0. The CI fixture check with `--as-of 2026-08-06` still passes.
- **Act.** Kept. Commit `d581e01`.
- **Consequence to plan for.** From 2026-11-30 the four OpenAI platform records in the 29 October register (`review_after` 2026-11-29) fail the gate, and from 2026-12-01 the two in the 31 October register. That is the stated policy, but it will turn `validate_engine.py` and CI red on those dates until the records are re-read. Recorded in `06-next-cycle.md` with an earlier re-audit date.

## R2-03: premise check and an owner for single-claim questions

- **Plan.** Hypothesis: if one named reference owns single-claim questions and begins with a premise check, a fresh agent states a false premise first and does not improvise a record.
- **Do.** New `skills/source-evaluation/references/single-claim-lookup.md`: premise check, source choice, one-claim record, stop rules, and a worked example on the false Kenya NSSF premise. Pointers added in `AGENTS.md` workflow step 1, `source-evaluation`, and the "Do Not Use When" lines of `research-orchestration`, `evidence-claim-graph` and `critical-reasoning-and-argument` (plus step 1 of its method). Fixtures for `source-evaluation`: two positives and two owned negatives, so it has three and two.
- **Study.** Grep for the four phrases from D-03 ("false premise", "presuppos", "premise check", "loaded question"): 0 hits before, hits in the new reference and the pointers after. Routing: 36/36 top-3, 32/36 rank-1 (88.9%) after this change alone, 0 lint findings. Contract validator 59/59. The reference's first example is the Task 3 record, checked against the primary notice; it was re-run in `04-validation-record.md` on a held-out premise.
- **Act.** Kept. Commit `4f73c9c`; follow-up `81970a4` points the skill's own worked example at the two checked records.

## R2-04: undated first-party page and stale statute consolidation

- **Plan.** Hypothesis: with both rules written down, a Task 1 style answer carries the limits without relying on the agent's diligence.
- **Do.** Section 3 of the reference (two page-level traps) and a second worked example on the Uganda NSSF rate, with every figure and section number taken from `00-scope-and-evidence.md`. A statute-currency pointer in `online-legal-research/references/east-african-overlay.md` and in step 3 of the legal workflow. Fixtures for `online-legal-research`: two positives and two owned negatives, so it has three and two.
- **Study.** Grep for "undated" in `source-evaluation` and `source-verification`: 0 before, present after. Routing after the change: 38/38 top-3, 34/38 rank-1 (89.5%), 13 owned negatives passing, 0 lint findings. A fourth candidate negative (`olr-n1b`, a pre-investment vetting prompt) ranked `online-legal-research` first, so it was rejected and a different prompt used; the overlap between legal research and due diligence on words such as "litigation" is a real lexical collision, noted for the next cycle.
- **Act.** Kept. Commit `b81c727`.

## R2-05: routing vocabulary for current-state questions

- **Plan.** Hypothesis (from the baseline, D-06): the country-named academic skills outrank the evidence skills because their descriptions repeat country names; rewriting the two descriptions will fix it.
- **Do first (diagnosis).** Scored the probe prompt with and without the country word. Without "Uganda", the top result for "What is the current NSSF employer contribution rate?" is `systems-thinking-and-mental-models` at 8.8, and `source-evaluation` is rank 55. With it, `uganda-academic-research` scores 22.0, all of it from the one token "uganda" in the skill name and title (weight 5). The descriptions are already academic-scoped. **The hypothesis was wrong.** No skill text mentions a current rate, fee, deadline, version or status, so nothing competes. The planned description rewrite was not made, and the backlog row is superseded by this entry. The baseline file stays as frozen.
- **Do (revised change).** One new bullet in the "Use When" section of `source-evaluation` naming the current-question and false-premise case. Four fixtures: two positives for `source-evaluation`, and an owned negative for each of `uganda-academic-research` and `kenya-academic-research`, with prompts that avoid the exact word in the skill name.
- **Study.** In six probes, `source-evaluation` now ranks first in five, none of which contains the exact word "uganda" (it was rank 55 for the plain NSSF prompt, now 1). The sixth, the original probe with "Uganda" in it, moves `source-evaluation` from outside the top five to rank 2; the country skill still wins at 22.0 against 15.0. The Kenya false-premise probe still does not reach `source-evaluation`. This is a limit of a lexical proxy: a proper noun in a skill name beats any general vocabulary, and the fix is not to pad descriptions. Full run: 40/40 top-3, 36/40 rank-1 (90.0%, from 88.2% at baseline), 15 owned negatives passing, 2 `NOT_ASSESSED`, 0 lint findings.
- **Act.** Kept (revised change only). Commit `fb4dfee`. Live-agent routing remains `NOT_ASSESSED`.

## R2-06: scanner false negatives and the files it never read

- **Plan.** Hypothesis: if the scanner tests the class of defect (non-portable or unresolvable reference) and covers the author-facing guides, these defects cannot return unseen.
- **Do.** `check_portable_references.py` gains `link-escapes-repository` and `broken-relative-link` rules (fenced and inline code skipped; a link counts as resolved if it exists beside the file or from the root) and a wider default scope: top-level guides, the authoring standard, `skills/`, `rules/`, `templates/`, `docs/quality-gates/`, `docs/ai-prompting/`. Repaired the five findings it then reported: `CONTRIBUTING.md:7, 17`, `docs/skill-authoring-standard.md:3, 7`, `skills/doc-standards.md:446` (a link to a file that never existed; replaced with a pointer to the Pandoc section that does exist, `skills/professional-word-output/references/word-features.md`, confirmed present).
- **Study.** Failing reproduction: the new scanner on the unrepaired tree reported exactly those five findings (389 files). Run by path over the three historical records, it reports the old-name sibling link `../../../skills-web-dev/...` that the 29 October scanner passed. After repair: 389 files, 0 findings. 7 new unit tests (14 in the file); `validate_engine.py` exit 0.
- **Act.** Kept. Commit `f610ce7`. The seven escaping links in `docs/continuous-improvement` history are not repaired (dated records) and are listed in `06-next-cycle.md`.

## R2-07: repeated headings

- **Plan.** Hypothesis: a validator code for any repeated heading stops the accretion, and merging the 19 skills makes them read as one contract.
- **Do.** New `duplicate_heading` code in `skill_contract_validator.py`. Of 19 skills with a repeated heading, 17 had an empty stub heading in front of the real section; the stubs were removed with a check that the set of non-blank lines was identical except for the removed heading line (18 lines in total, no insertions: `git diff --stat` shows 18 deletions). Two repeats carried content and were renamed, not merged: `osint-investigation` "Reference Index" (a link list repeating the table) became "Reference links", and `research-orchestration` first "Orchestrator outputs" (the per-cohort file list) became "Cohort output files".
- **Study.** Failing reproduction: the new check on the committed tree from before the fix reports `duplicate_heading: 19`, 40 of 59 fully compliant; after, `failure counts: {}`, 59 of 59. 5 new tests. `validate_engine.py` exit 0; routing unchanged at the time (36/40).
- **Scope narrowed.** The backlog also named the nine skills with generated "Evidence Notes 1 and 2" headings. In the one skill inspected (`quantitative-modelling`) the second heading holds a table that serves as the contract's evidence section, so renaming it blindly could create a new duplicate. Not done; recorded as residual, 9 skills.
- **Act.** Kept. Commit `b9648f6`.

## R2-08: denominator check

- **Plan.** Hypothesis: a rule plus a checked example makes a market brief record each denominator with its definition and quarantine a vendor count that fails arithmetic.
- **Do.** A "Denominator check" paragraph in the market-boundary section of `quantitative-modelling` and a second worked example built from the Task 2 figures (45,164 registered and 26,597 responding Ugandan primary schools; a vendor 6,000 against 45,164; vendor components summing to 26,700 against a stated 30,200; Kenya's changed basic-education count).
- **Study.** Arithmetic re-done: 12,000 + 7,500 + 6,000 + 1,200 = 26,700; 6,000 / 45,164 = 13.3%. Worked example is 336 words. Routing unchanged (36/40; the three `quantitative-modelling` positives and two negatives still pass). Contract 59/59; portability scan 0 findings.
- **Act.** Kept. Commit `9621cc6`.

## R2-09: companion names that resolve nowhere

- **Plan.** Hypothesis: if a backticked name in a Companion Skills list must be an active skill or a declared external skill, the stale-name accretion cannot return.
- **Do.** New `unresolved_companion_name` code and `tests/skill-engine/external-skills.json` (engine and check date per entry; `world-class-engineering` and `data-visualization` declared). `data-quality-assessment`, merged into `data-quality-pipeline` in April 2026 (commit `85b9364`, confirmed from its message), was still named 15 times in 12 files; each now names the successor, or its `dataset-quality-four-axes.md` reference where the sentence sits inside that skill's own references.
- **Study.** Failing reproduction: on the committed tree from before the fix the check reports 4 findings, all `data-quality-assessment`. After: 0. 7 new tests (12 in the file). `validate_engine.py` exit 0.
- **Act.** Kept. Commit `d094054`.

## R2-10: currency re-verification

- **Plan.** Re-read the primary page for each named standard on 2026-10-31 and record only what the page says.
- **Do.** New register `docs/source-registers/kaizen-currentness-2026-10-31.json` (10 sources, 11 claims), with a `changes_from_previous` list; the markdown register rows updated only where re-read; ICD 203 links in `analytic-tradecraft` moved to the host that now serves the PDF.
- **Study.** Unchanged since 29 October: PRISMA 2020 (and PRISMA-C 2026, BMJ 2026;393:e088561), GRADE Living Map (version 13 June 2026), Cochrane Handbook 6.5 (22 August 2024), TOP 2025 structure. Corrected: ICD 203 is partial (a second technical amendment adds annual analyst training; the January 2022 amendment prints a signature date that conflicts with the August 2022 memorandum it cites; the text layer looks like OCR output, so a digit may be misread). ICD 206 is `NOT_ASSESSED`: the PDF is image-only and no OCR tool is installed, so the 29 October amendment date is not confirmed. RFC 9309 is partial: status and 2022 date supported, errata not read. ODNI PDF URLs now redirect (301): `www.dni.gov` to `www.odni.gov` to `archive.dni.gov`. OpenAI: GPT-6 Rosalind released 30 October (trusted access, life sciences); flagship catalogue unchanged; the Luna/high Codex pin is retained and its full comparison is not due until three months after 28 September. `validate_source_currency.py` on the new register: exit 0, 0 findings.
- **Act.** Kept. Commit `aeceb5a`.

## Reverted

None. One planned change (the country-skill description rewrite in R2-05) was not made after the diagnosis refuted it, and one scope item (generated "Evidence Notes" headings in R2-07) was left out; both are recorded above.
