# Changelog

## 2026-11-07 - Explicit reviewer attribution

- Source verification distinguishes recorded human, AI and unknown reviewer kinds without certifying semantic support. Legacy records retain unknown attribution. A Windows source-register path validation failure found by the unit suite is also repaired. [Evidence and limitations](docs/continuous-improvement/2026-11-07-reviewer-attribution.md).

## 2026-10-31 - Documentation wave after pass 2

- README: a measured validation table (commands, packages, results), the test status with its package list, a quality and improvement section with the latest score and the date-triggered gate calendar, `bash install.sh`, a project-relative `pack --out` path, `python3` throughout and the repository name `chwezi-research-engine` (`390a80c`).
- AGENTS.md: corrected the claim that every skill ships `AGENTS.md`, `README.md`, `CLAUDE.md` and `references/` (27 and 48 of 59 do), and added the `python3` note and the machine-error gate root rules (`a77d75d`).
- CONTRIBUTING, the skill authoring standard and the evidence pack template: bash blocks, `python3` and forward-slash paths instead of PowerShell, `python` and backslashes (`1542d6f`).
- Added `docs/README.md` as the documentation index; marked `PROJECT_BRIEF.md` and `RESEARCH_CRAFT_INTEGRATION.md` as April 2026 records (`15b1a47`).
- Recorded the findings this wave did not change in `docs/kaizen/2026-10-engine-kaizen-pass-2/07-docs-followups.md` (`d912001`).
- README: added "What the October 2026 kaizen improved" under Quality and improvement, an account of the 18 changes kept in the 29 and 31 October cycles with their commits, verification and before and after figures; it points to the evidence files and does not replace them.
- README restructured for reading (`c75a92f`, `ea7d370`, `7a98d48`, `165d906`): a front door with an at-a-glance list and a three-step Start here, a contents list, a 12-row task-to-skill table, shorter sections and sentences, and the 18-item October account as numbered Problem, Change and Result lists. The 220-line reference list moved to `docs/references.md` and the 59-row skill table to `docs/skill-catalogue.md`; the README keeps an 11-row group summary. Corrected the scraper test note: the three failures are assertion failures caused by the scraper recording `ModuleNotFoundError: No module named 'bs4'` for each page. Measures, validators and the preservation check are in `docs/kaizen/2026-10-readme-kaizen/readme-kaizen-record.md`.

Commit index for the pass 2 entry below, by theme:

- Premise check, single-claim owner, undated-page and statute-consolidation rules, worked example: `4f73c9c`, `b81c727`, `81970a4`.
- Denominator check and conflicting-count example: `9621cc6`.
- Machine-error gate target resolution: `00bdc44`.
- Register supersession and the register gate: `d581e01`.
- Portable-reference scanner: `f610ce7`.
- Contract checks and repeated headings: `b9648f6`, `d094054`.
- Primary-page re-verification of named standards: `aeceb5a`.
- Routing vocabulary and fixtures for current-state questions: `fb4dfee`.
- Evidence records (baseline, backlog, experiments, validation, report, next cycle): `436dd70`, `a822fc6`, `6463f56`, `cfd910c`.

## 2026-10-31 - October 2026 Kaizen, pass 2

- Added a premise check and a named owner for single-claim questions (`skills/source-evaluation/references/single-claim-lookup.md`), with rules for an undated official page and for a statute consolidation that lists unapplied amendments, and two checked worked records.
- Added a denominator check and a checked conflicting-count example to `quantitative-modelling`.
- Made the machine-error gate runnable on any host: targets resolve under `--engines-root`, `CHWEZI_ENGINES_ROOT` or the parent of the checkout, with no host path in the fixture.
- Added machine-checkable register supersession (`superseded_by`) and a gate over every register in `docs/source-registers/`, run by `validate_engine.py` and CI.
- Extended the portable-reference scanner to repository-escaping and dead relative links and to the author-facing guides; repaired the findings.
- Added `duplicate_heading` and `unresolved_companion_name` contract checks; merged repeated headings in 19 skills and replaced a retired skill name in 12 files.
- Re-verified PRISMA, GRADE, Cochrane Handbook, ICD 203 and 206, RFC 9309 and TOP from primary pages; corrected ICD 203 to partial and ICD 206 to `NOT_ASSESSED`.
- Added routing vocabulary and fixtures for current-state questions; three skills now hold three positive and two owned-negative fixtures.
- Recorded the baseline, experiments, validation evidence, residual gaps and next review under `docs/kaizen/2026-10-engine-kaizen-pass-2/`.

## 2026-10-29 - October 2026 Kaizen

- Added a claim-linked source-currentness register for reviewed research standards and dispositioned overdue historical records.
- Added a portable-reference scan to the engine validator and replaced workstation-specific paths in active router and skill Markdown.
- Added an automated entry-count gate for both the complete checkout and package-oriented tree, with an exact-limit boundary fixture.
- Added product-boundary guidance and sourced evidence for commercial school-administration software sizing, with positive and owned-negative routing fixtures.
- Recorded the cycle baseline, experiments, validation evidence, residual gaps, and next review under `docs/kaizen/2026-10-engine-kaizen/`.

## 2026-07-08 - Engine Upgrade July 2026

- Added root `SKILL.md` router for digital-research-engine routing and release sequence.
- Added target architecture directories for source registers, quality gates, exemplars, shared templates, test fixtures, and report tools.
- Added engine/project pathing model to separate reusable doctrine, examples, active workspaces, and generated artefacts.
- Added engine-wide running example for Chwezi Core Systems research deliverables.
- Added research standards register and release-blocking quality gates.
- Added unified source verifier and source-verification manifest template.
- Added citation-density dashboard and manual dashboard template.
- Added analytic-tradecraft scored fixtures for ACH, KAC, pre-mortem, and estimative language.
- Added complete schema A-S exemplar folders under `examples/research-types/`.
- Added book-to-engine knowledge map for all attached references.
- Added anti-slop governance for research language quality.
- Repaired example workspace registry fixtures for `example-market-landscape`, `example-due-diligence-dossier`, and `example-academic-paper` so repo validation reaches pass status.
- Expanded legacy example-project analysis fixtures and output manifests so `scripts\validate_engine.py` passes with no warnings.
