# Contributing

Changes to this engine must preserve evidence discipline and pass the zero-debt skill contract.

## Skill changes

Start from [the local authoring standard](docs/skill-authoring-standard.md) and [skill template](templates/skill-template/SKILL.md). Read the target skill and its directly linked references before editing. Compare the nearest neighbours so the positive and negative triggers remain distinct. Proposal-engine changes belong in the standalone `proposal-skills` repository, resolved through the engine-routing table.

Add or update routing fixtures for trigger changes. Fixtures must cover the positive route, a negative or neighbouring route, limited capabilities, and a failure or stop path where applicable.

## Required checks

```bash
python3 -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json
python3 -X utf8 scripts/routing_smoke_test.py --min-rank1 84 --lint-fixtures
python3 -X utf8 scripts/validate_engine.py
python3 -X utf8 <engineering-engine-root>/skills/sdlc-meta/skill-writing/scripts/quick_validate.py <skill-directory>
git diff --check
```

`<engineering-engine-root>` is the checkout of `chwezi-dev-engine` (the engineering engine, formerly `skills-web-dev`), resolved through the engine-routing table. If it is unavailable, record `quick_validate.py` as not assessed.

Run relevant syntax, link, unit, render, or domain checks as well: `python3 -m pytest -q -p no:cacheprovider tests engine/tests` for the test suite, and `python3 -X utf8 scripts/validate_machine_error_gate.py` after any anti-slop or cross-engine gate change. The [README](README.md#validation) lists every command, the packages it needs, and what it returned on 2026-10-31, including the two pytest modules and three scraper tests that cannot run without `pandas`, `python-docx` and `beautifulsoup4`. A check that cannot run is `not assessed`, not passed.

## Release procedure

1. Fetch the remote and confirm the branch is not behind `origin/main`.
2. Run all required checks and inspect the complete diff.
3. Remove generated caches and stage only intended files.
4. Review the staged statistics and representative skill, validator, fixture, and documentation diffs.
5. Commit once and push without force. Verify the local and remote commit identifiers match.
