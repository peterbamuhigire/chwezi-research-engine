# Experiment log

Cycle: `2026-10-engine-kaizen`
Baseline frozen in `01-baseline-scorecard.md` before these experiments.
No Tier-3 model calls, external archive writes, plugin submissions, or public
publication were performed.

## PDSA-1 — currentness record refresh (R-KZ-01)

- **Plan:** Recheck the standards named by the prompt and TOP against current
  primary sources, then replace only the obsolete TOP statement and add a
  dated, claim-linked source register. Keep old source snapshots immutable.
- **Do:** Added the dated claim register; directly refreshed PRISMA, GRADE,
  Cochrane, ICD 203, ICD 206, RFC 9309 and TOP from official publisher sources;
  corrected the TOP count and provenance wording in the academic-reporting
  skill. Six due source records are dispositioned in the new register while
  the old register remains unchanged.
- **Study:** `validate_source_currency.py
  docs/source-registers/kaizen-currentness-2026-10.json --as-of 2026-10-29`
  exits 0 with zero metadata findings. Contract validator: 59/59 compliant;
  routing remains 29/29 top-3, 25/29 rank-1, with 7 negative passes, 0
  failures, 2 NOT_ASSESSED; `validate_engine.py` exits 0 with 37 tests; the
  source-ingestion guard exits 0 with zero findings. Source limitations are
  recorded per row in the JSON register.
- **Act:** Kept. The new register validates and the skill now separates EQUATOR
  guidance from independently governed GRADE, Cochrane and TOP sources. The
  metadata pass does not certify semantic support; archive snapshots remain
  unassessed.
- **Stop/rollback:** If a source cannot be opened or its scope is ambiguous,
  keep that claim `NOT_ASSESSED`; historical source records remain immutable.

## PDSA-2 — portable-path recurrence check (R-KZ-02)

- **Plan:** Remove only confirmed machine-specific paths from active routers
  and skills; add a small scanner with synthetic positive and negative cases.
- **Do:** Added `scripts/check_portable_references.py`, integrated it into
  `validate_engine.py` and the router, and replaced machine-specific paths in
  active router/skill Markdown with local references or repository names
  resolved through the engine-routing table. The first whole-scope scan also
  exposed Windows `Downloads` paths in source-reference notes, outside the
  initially listed router and three skills; these were changed to retain the
  source titles and access dates without workstation paths. The frozen tree
  was then rescanned retrospectively with the new checker: 376 files, 52
  host-absolute findings. This retrospective diagnostic is not a change to
  the frozen baseline.
- **Commit:** `d02f841 fix(research-kaizen): reject nonportable skill references`.
- **Follow-up commit:** `aa8ba37 fix(research-kaizen): cover host root path variants`;
  broadened the Unix-root pattern after review so it catches `/opt`-style
  host paths while continuing to allow URL routes and generic relative links.
- **Study:** Clean-tree CLI: exit 0, 376 files and 0 findings. Unit tests: 7
  passed, including Windows/Unix absolute paths, forward/backslash sibling
  links, and allowed public/local relative links. A synthetic file containing
  a machine-specific Windows path returned exit 1 with one finding. `validate_engine.py`
  exits 0 with 43 tests and its included portable check; contract remains
  59/59, routing remains 29/29 top-3 and 25/29 rank-1, owned negatives 7
  pass/0 fail/2 NOT_ASSESSED. CI workflow invokes `validate_engine.py`.
  The separate `validate_machine_error_gate.py` was run and exits 1 because
  its twelve configured targets are unavailable to this validator on this
  Linux host. This is recorded as a failed command and the semantic
  cross-engine check remains NOT_ASSESSED; no foreign engine was edited.
- **Act:** Keep the deterministic scan and repairs. It closes the locally
  measurable recurrence gap with zero current findings. The baseline scan
  uncovered additional reference-note occurrences, so the original three-file
  four-file targeted defect description is retained as the initial observation, not the total
  scope.
- **Stop/rollback:** Revert pattern or integration if it flags public URLs,
  historical evidence, or allowed relative paths.

## PDSA-3 — market boundary and routing proof (R-KZ-03)

- **Plan:** Add the smallest quantitative-modelling rule/example that separates
  government MIS, adjacent EdTech spending and commercial school-administration
  software; add three positive and two owned-negative fixtures for that route.
- **Do:** Added a market-boundary check and sourced worked example to
  `skills/quantitative-modelling/SKILL.md`. The example states buyer, product,
  geography, period, and revenue basis; keeps government EMIS/NEMIS evidence
  and adjacent learning-product evidence out of a commercial software TAM;
  and returns product-matched inputs as gaps. Added three positive fixtures
  and two owned negatives for `quantitative-modelling`.
- **Commit:** `68d9747 fix(research-kaizen): bound school software market sizing`.
- **Study:** Re-ran the market brief through the revised workflow against the
  same bounded evidence set recorded in `00-scope-and-evidence.md`: no
  defensible Uganda/Kenya commercial TAM was produced, and government-system
  coverage and the Kenya survey were not substituted for paid customer or
  revenue inputs. The three new positive prompts rank the expected route first.
  `python -X utf8 scripts/routing_smoke_test.py --min-rank1 84 --lint-fixtures`
  reports 34/34 top-3, 30/34 rank-1 (88.2%), 100% p@3, zero fixture-lint
  findings, and 11 owned negatives (9 pass, 0 fail, 2 NOT_ASSESSED). Frozen
  baseline values in `01-baseline-scorecard.md` were 29/29 top-3, 25/29 rank-1
  (86.2%), 100% p@3, 0/59 skills with complete fixture coverage, and 9 owned
  negatives (7 pass, 0 fail, 2 NOT_ASSESSED). Direct recount of
  `tests/skill-engine/routing-fixtures.json` confirms the changed skill now has
  3 positive and 2 owned-negative fixtures, or 1/59 skills meeting that
  coverage rule. The added prompts are lexical tests, not live-agent routing
  evidence.
- **Act:** Keep. All five new fixtures pass and the aggregate rank-1 rate is
  above the frozen baseline. The observed task remains evidence-limited and
  its TAM conclusion remains a gap, which is the intended safe outcome.
- **Stop/rollback:** Remove any fixture that uses its target skill name,
  copies the skill description, or fails ranking rather than weakening the
  smoke-test threshold.

## PDSA-4 — checkout and package capacity gate (R-KZ-05)

- **Plan:** The portfolio task sets a hard 5,000-file ceiling on the full
  checkout and package-oriented inventory. The official OpenAI plugin ZIP
  error reference separately states a 5,000 archive-entry maximum. Add a
  routine guard for both inventories, with exact-limit and one-over checks.
- **Do:** Added `scripts/check_file_count_cap.py`, integrated it into
  `validate_engine.py`, and added a boundary fixture and unit tests. The full
  checkout count includes `.git`; package-oriented count excludes only the
  explicitly listed VCS/cache/virtual-environment directories and retains
  tests and `.pytest_cache`. Neither is represented as a built archive count.
- **Commit:** `72bc019 feat(research-kaizen): enforce checkout package file cap`.
- **Study:** The official [OpenAI ZIP error reference](https://developers.openai.com/plugins/deploy/submission-errors),
  accessed 2026-10-29, states that an archive must not contain more than
  5,000 entries. The portfolio's full-checkout/package-oriented ceiling is an
  explicit task constraint; the latter remains a preflight inventory rather
  than a built ZIP count. `python -X utf8 engine/tests/test_file_count_cap.py`
  passes 6 tests: equality at the configured limit passes, one-over fails for
  both the full and package-oriented count, caller-supplied limits above 5,000
  or below zero are rejected, package exclusions work, and a symlinked
  directory is counted without traversal. The integrated
  `python -X utf8 scripts/validate_engine.py` exits 0 with 50 tests on the
  acceptance-review rerun. Current
  tree report: `python -X utf8 scripts/check_file_count_cap.py` exits 0; final
  committed-tree counts are recorded in `04-validation-record.md`.
- **Act:** Keep. Both inventories are measured by the registered validator;
  exact-limit and over-limit failure paths are covered by the fixture and
  tests. Built-ZIP entry count remains an archive-level release check.
- **Stop/rollback:** If filesystem counting diverges from actual archive
  entries or excludes runtime files, retain the full-checkout guard and revise
  the package-oriented inventory rule before release; archive-level validation
  remains required before submission.
