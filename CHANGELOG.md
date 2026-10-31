# Changelog

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
