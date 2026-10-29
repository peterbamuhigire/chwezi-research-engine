# Validation record — October 2026

As of 2026-10-29 (Africa/Kampala). Repository: Digital Research Engine,
branch `kaizen/2026-10`. The checks below are lexical/unit/repository checks;
they do not establish live model quality or independent source-review quality.

## Native validators and measures

| Command | Result | Notes |
|---|---|---|
| `python -X utf8 scripts/check_portable_references.py` | PASS; exit 0 | 376 active router, README, and skill Markdown files scanned; 0 findings. |
| `python -X utf8 scripts/check_file_count_cap.py` | PASS; exit 0 | Independent acceptance-review rerun: full checkout 1,240/5,000, package-oriented inventory 987/5,000. Counts include symlink entries without following directory symlinks; the full count includes repository metadata, while package-oriented exclusions are documented in `scripts/check_file_count_cap.py`. |
| `python -X utf8 engine/tests/test_portable_references.py` | PASS; exit 0 | 7 unit tests cover Windows and Unix absolute paths, forward/backslash sibling links, and allowed public/local relative links. |
| `python -X utf8 engine/tests/test_file_count_cap.py` | PASS; exit 0 | 6 tests cover the exact limit, one-over failure for each tree, rejection of caller-supplied limits above 5,000 and below zero, cache exclusion in package-oriented count, symlink no-follow behaviour, and fail-closed handling of a walk error. |
| `python -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json` | PASS; exit 0 | 59 active skills, 59 compliant; zero failures. |
| `python -X utf8 scripts/routing_smoke_test.py --min-rank1 84 --lint-fixtures` | PASS; exit 0 | 34/34 top-3, 30/34 rank-1 (88.2%), p@3 100%, 0 fixture-lint findings; 11 owned negatives: 9 pass, 0 fail, 2 NOT_ASSESSED. |
| `python -X utf8 scripts/validate_engine.py` | PASS; exit 0 | Acceptance-review rerun: includes portable-reference and file-count cap checks, contract/routing checks, no-book guard, engine doctor, and 50 tests. |
| `python -X utf8 scripts/validate_source_currency.py docs/source-registers/kaizen-currentness-2026-10.json --as-of 2026-10-29` | PASS; exit 0 | Zero metadata/date findings. Validator explicitly does not assess semantic source support. |
| `python -X utf8 scripts/validate_source_currency.py tests/fixtures/source-currency.json --as-of 2026-10-29` | PASS; exit 0 | Zero metadata/date findings; fixture only. |
| `python -X utf8 scripts/source_ingestion_guardrail.py` | PASS; exit 0 | Zero findings. |
| System Python: `python -m pytest -q tests engine/tests` | NOT_ASSESSED; exit 1 | The system interpreter has no `pytest` module. A portfolio-managed test environment was used for the checks below; no dependency was installed into this repository. |
| Portfolio test environment: `python -m pytest -q engine/tests` | PASS; exit 0 | 50 passed, 11 subtests passed after the two hard-ceiling regressions were added. |
| Dependency-complete portfolio test environment: `python -m pytest -q tests engine/tests` | PASS; exit 0 | 184 passed, 2 skipped, 11 subtests passed. The temporary environment includes the core `beautifulsoup4` parser dependency and the previously missing spreadsheet/document test dependencies; none were installed into the repository. |
| `python -X utf8 scripts/validate_machine_error_gate.py` | FAIL; exit 1 | Default Windows checkout paths do not resolve on this Linux host. A read-only replay remapped fixture paths to workspace aliases in a disposable fixture and found the social-media identifier mismatch in `06-next-cycle.md`; one configured target outside the public engine catalogue has no workspace binding and remains NOT_ASSESSED. This checks text identifiers only, not semantic/editorial quality. No other engine was edited. |

## Failure-path and before/after evidence

The portable-reference CLI was invoked on a temporary Markdown file containing
a synthetic machine-specific Windows path. It reported `1 files, 1 findings`
and exited 1. The same checker over the active tree exited 0 with no findings.
The unit suite also rejects a sibling checkout expressed with Windows
backslashes.

The first full-suite attempt after installing spreadsheet/document test
dependencies exposed three scraper-test errors because the temporary
environment still lacked the documented core `beautifulsoup4` dependency.
After installing that dependency outside the repository, the remaining
evaluator readiness test still failed
on stale guidance hashes in the frozen baseline as well as the current tree.
The test now refreshes hashes in its in-memory fixture only, so it tests the
structural-ready contract without bypassing production hash validation. The
frozen `444b7ce` archive reproduced that same single assertion failure; after
the fixture correction and dependency installation, the complete current
pytest suite passes as shown above. Production evaluator logic and its
hash-mismatch blockers were not weakened.

The retrospective scan against frozen pre-change HEAD `444b7ce`, using the
new scanner without modifying that tree, found 52 host-absolute occurrences
across the same 376 Markdown files. This diagnostic was made after the change
and is not represented as a pre-change validator run. The initial baseline
count had only enumerated the four router/skill files then under review; the
additional reference-note paths explain the wider retrospective count.

Routing baseline in `01-baseline-scorecard.md`: 29/29 top-3, 25/29 rank-1
(86.2%), p@3 100%, 0/59 skills with three positives and two owned negatives;
9 owned negatives (7 pass, 0 fail, 2 NOT_ASSESSED). Post-change routing adds
three positive and two owned-negative fixtures for `quantitative-modelling`;
that skill is now the sole skill with complete fixture coverage (1/59).
Aggregate rank-1 and top-3 results are no worse than baseline.

## Native package/runtime evidence

The portfolio operator reports successful offline local-plugin installation
for both Codex and Claude. A native offline debug `prompt-input` inspection
after alias expansion found 59 manifest skill paths and 59 runtime skill paths,
with no missing paths, no network access, and zero model calls. This is
operator-run evidence, separate from this agent's local repository validators.
It proves discovery/loading for the tested runtime invocation; it does not
prove model behaviour, authentication success for external services, or
marketplace publication readiness.

## Model-policy and package-limit currentness

As of 2026-10-29, the official OpenAI changelog records GPT-6.1 Terra released
on 2026-10-26; the model catalogue lists GPT-6 Astra, GPT-6.1 Sol, GPT-6.1
Terra, and GPT-6 Luna ([changelog](https://developers.openai.com/api/docs/changelog),
[catalogue](https://developers.openai.com/api/docs/models), accessed
2026-10-29). The authorised Luna/high pin is retained; a release date alone
does not establish task fit or justify switching. The Luna model page is the
primary provider source for that model ID ([GPT-6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna),
accessed 2026-10-29). These records are in
[`kaizen-currentness-2026-10.json`](../../source-registers/kaizen-currentness-2026-10.json).
Comparative quality, latency, observed task cost, and account/session
availability remain **NOT_ASSESSED**; no paid model calls were made.

The portfolio task's ceiling is checked separately for the full checkout and
the package-oriented inventory. OpenAI's submission reference independently
states that an uploaded archive must not contain more than 5,000 entries
([ZIP structure and limit errors](https://developers.openai.com/plugins/deploy/submission-errors),
accessed 2026-10-29). The checkout/package inventory is a preflight proxy, not
a built-ZIP measurement.

## NOT_ASSESSED / outstanding

- Semantic source support is not certified by the currentness metadata
  validator; each source was reviewed directly for the scoped currentness
  register, but no independent human reviewer signed off.
- Archive snapshots were not captured for the three practitioner tasks;
  source-verification release status remains NOT_ASSESSED.
- Cross-engine semantic handoffs remain NOT_ASSESSED. The workspace-resolved
  identifier check found a social-media target mismatch and one unbound target
  outside the public engine catalogue, recorded in `06-next-cycle.md`.
- Tier-3 behavioural evaluation, comparative model quality/cost/latency,
  and live-agent routing were not run. No paid model calls were made.
- Remote CI state and public marketplace submission were not checked or
  performed in this engine task.
