# README kaizen record, 31 October 2026

This is a scoped micro-cycle on `README.md`. It follows the Portfolio Kaizen steps: Observe, Baseline, Select, Experiment, Check, Standardise, Teach, Re-measure. It publishes no score. The audit score stays at the pass 2 figure in [`../2026-10-engine-kaizen-pass-2/05-final-report.md`](../2026-10-engine-kaizen-pass-2/05-final-report.md).

The method is the [Portfolio Kaizen Standard](../../continuous-improvement/portfolio-kaizen-standard-2026-08.md) and the [currentness gate](../../continuous-improvement/kaizen-currentness-gate.md). Both are protected doctrine and were not edited.

Start state: branch `main` at `ee46525`, working tree clean. Work branch: `kaizen/2026-10-readme-kaizen`. Host: Linux, Python 3.14.8, Node 22, pytest 9.0.3 from an existing scratch virtual environment. No package was installed. The engine's own installer ran only into a scratch directory, to check its update behaviour.

## Observe

The README was 8,202 words under 6 H2 sections. Findings from reading it and measuring it:

- The `## References` section held 2,949 words (221 lines of citations) and the Quality section held 2,589 words, mostly the October account as one block.
- Paragraphs ran to 144 words and table cells to 40 words. 44 lines were over 300 characters, and the longest was 1,983.
- There was no contents list, no task-to-skill table and no statement of what to do first. The first fenced command was at line 17, after two paragraphs of 1,046 and 865 characters.
- One statement was wrong. The README said each of the three scraper test failures is `ModuleNotFoundError: No module named 'bs4'`. A direct probe and the pytest output show the scraper catches that error per page and records it, so each test fails an assertion on its page counts (`0 != 1`, `0 != 2`, `2 != 1`). The cause is still the missing `bs4`.
- Two tracked files link `README.md#validation` (`AGENTS.md` and `CONTRIBUTING.md`). That anchor is an interface and was kept.
- Only `scripts/check_portable_references.py` reads `README.md` as data (it scans it for host paths and dead links). `engine doctor` requires the file to exist. No script, test, manifest or router reads any section by heading.

### Baseline metrics

Measured with `readme-metrics.py` on `README.md` at `ee46525`.

| Metric | Baseline |
|---|---:|
| `words` | 8202 |
| `h2` | 6 |
| `toc` | 0 |
| `first_cmd` | 17 |
| `longest_sec` | 2940 |
| `long_lines` | 44 |
| `max_line` | 1983 |
| `sent_len` | 16.7 |
| `fre` | 43 |

Supplementary hand measures: longest paragraph 144 words, longest table cell 40 words, mean sentence length over paragraphs and bullets 14.8.

### Baseline validators

Run on `main` before any edit with `PYTHONDONTWRITEBYTECODE=1`. The exit codes are in the Check table below.

## Select

| Item | Decision | Reason |
|---|---|---|
| R1 Front door | Applied | An opening, an At a glance list of six measured facts and a three-step Start here end at line 37. The first fence is at line 22. At a glance is a bold label, not an H2, so that the contents list falls before the third H2, which is where the `toc` metric looks. |
| R2 Contents | Applied | 13 links. The preservation check resolves all 17 in-page anchors. |
| R3 Structure | Applied | 15 H2 sections. The longest is 977 words by the metric script. The October account and its measures table are three H2 sections, and Validation and Quality have H3 sections. |
| R4 Find the right skill | Applied | 12 rows. Each skill is a directory under `skills/`, checked by a script. Tasks follow the routing fixtures in `tests/skill-engine/routing-fixtures.json`. |
| R5 No walls of text | Applied | Longest paragraph 45 words, longest table cell 25 words, no line over 300 characters. |
| R6 Plain English | Applied | Sentences were shortened, long paragraphs became bullets, terms are defined where first used. British English. No marketing wording. |
| R7 Say it once | Applied | The standards and outputs lists, which were packed into the opening, each appear once. The `python3` note and the repository alias each appear once. The October account stays, in the new style. The scoring narrative stays only where it states current status. |
| R8 Relocate bulk | Applied twice | The reference list moved to `docs/references.md` and the 59-row skill table to `docs/skill-catalogue.md`. The conditions hold for both (see Experiment). |

The skill table was first kept in the README, because with the checker then in use its 59 links, rebased from `skills/<name>/` to `../skills/<name>/`, would have been reported as lost, not moved. The preservation checker was then changed to resolve each relative link against the location of the file that holds it. With that change the table moves cleanly, and the README keeps an 11-row group summary and the task-to-skill table at the top. The table was 945 words, inside the 1,200-word limit, so the move is for reading speed, not to meet a limit.

Not in scope: skill bodies, scripts, tests and the protected doctrine files.

## Experiment

Each commit is one theme, with explicit paths staged.

| Commit | Theme | What changed |
|---|---|---|
| `c75a92f` | Structure and front door | New opening, At a glance, Start here, Contents and task-to-skill table. How it works, Install by route (with update behaviour), Scaffold a research workspace, Contributing, author and licence. Validation, Quality and the October account split into H3 or H2 sections. Prose unchanged in the old sections. |
| `ea7d370` | Plain English | Validation table rewritten to one command per row with short cells. The machine-error gate command moved to a code block. Long bullets split. The 18 October items became numbered Problem, Change and Result lists with the same figures and hashes. Scraper wording corrected. |
| `7a98d48` | Relocation | `## References` (Books, Repositories, Standards and official sources, Websites and articles) moved to `docs/references.md`. The README keeps a short section with links to the page, to `RESEARCH_CRAFT_INTEGRATION.md` and to the 2026-Q4 ecosystem scan. |
| `165d906` | Relocation | The 59-row table moved to `docs/skill-catalogue.md` with links rebased to `../skills/`. README keeps a summary table of the 11 groups with counts, and a link. The package-oriented file count in the Validation table became 1005 and the full-checkout figure became "about 1,600". |
| The commit that adds this file | Record | This record, the 2026-10-31 `CHANGELOG.md` bullet and the `docs/README.md` index lines. |

The R8 conditions, for both moved sections:

- No script, test, manifest or router reads either section. `grep` for the heading texts (`References`, `Books`, `Skill catalogue`, `Research operating system`, `Total: 59`) and for `README.md#references` over `scripts`, `tests`, `engine`, `hooks`, `.github`, `.skills-engine`, `.claude-plugin`, the router, the guidance files and `rules/` found nothing except an unrelated `## References` heading in `templates/skill-template/SKILL.md`.
- A short summary and a link stay in the README.
- The preservation check reports 94 link targets as moved (46 from References, 48 from the catalogue, which the task table does not repeat), with none lost.
- The validators give the same exit codes as before.

## Check

### Validators

Same commands as the README Validation table, run from the repository root. The checks on the right ran after the last README edit (`165d906`), with the changelog, index and record files in the working tree.

| Command | Before | After | After: result |
|---|---:|---:|---|
| `python3 -X utf8 scripts/validate_engine.py` | 0 | 0 | eight checks pass |
| `python3 -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json` | 0 | 0 | 59 of 59 compliant |
| `python3 -X utf8 scripts/routing_smoke_test.py --min-rank1 84 --lint-fixtures` | 0 | 0 | 40/40 top three, 36/40 rank 1 |
| `python3 -X utf8 scripts/validate_source_currency.py --registers-dir docs/source-registers` | 0 | 0 | 3 registers, 0 findings |
| `python3 -X utf8 scripts/validate_source_currency.py tests/fixtures/source-currency.json --as-of 2026-08-06` | 0 | 0 | 0 findings |
| `python3 -X utf8 scripts/check_portable_references.py` | 0 | 0 | 389 files, 0 findings |
| `python3 -X utf8 scripts/check_file_count_cap.py` | 0 | 0 | package-oriented tree 1005 of 5,000 with this record |
| `python3 -X utf8 scripts/check_no_book_extractions.py` | 0 | 0 | OK |
| `python3 -X utf8 scripts/source_ingestion_guardrail.py` | 0 | 0 | 0 findings |
| `validate_machine_error_gate.py` with 11 `--engine` flags and both engine roots | 0 | 0 | 11 engines, identifier presence only |
| `python3 -m pytest -q -p no:cacheprovider tests engine/tests --continue-on-collection-errors` | 1 | 1 | 220 passed, 3 failed, 2 skipped, 2 collection errors, 16 subtests passed, both runs |
| `node scripts/generate-plugin-manifest.js --engine . --check` | 0 | 0 | current, 59 skills |
| `node hooks/test-destructive-bash-gate.js` | 0 | 0 | 61 of 61 |
| `node hooks/test-plugin-hook-config.js` | 0 | 0 | 7 of 7 |
| `python3 -X utf8 <chwezi-dev-engine>/skills/sdlc-meta/skill-writing/scripts/quick_validate.py skills/source-evaluation` | 0 | 0 | valid |

All 15 exit codes are identical before and after. Pytest was run twice more to re-measure the test statement: without `--continue-on-collection-errors` it exits 2 with the two collection errors (`docx`, `pandas`). With the flag the three scraper tests fail, with `bs4` missing as the cause (checked by the probe above). The pytest environment is an existing scratch virtual environment with system site packages. It adds no `bs4`, `pandas` or `python-docx`.

### Preservation check

`python3 -I readme-preserve-check.py <repo> main kaizen/2026-10-readme-kaizen`, run on the branch tip:

The anchors line is shortened in the block below. Quoted verbatim, it contains the pattern the checker searches for and the checker flags it as a broken link to itself.

```text
links: old README 131 targets; new README 44; moved to docs 94; LOST 0
commands: old README 33; kept in README 33; moved to docs 0; LOST 0
anchors: 1 distinct anchor (validation) linked from tracked files; BROKEN 0
in-page links: 17 anchors used; BROKEN 0
RESULT: OK
```

The checker, both as first supplied and as updated to resolve relative links by file location, stops with `UnicodeDecodeError: 'utf-8' codec can't decode byte 0x97` because one tracked file is not valid UTF-8: `projects/healthcare-app-clinical-data/drug-interactions/research/wave1-data.md`. I ran a copy of the updated checker that decodes with `errors="replace"` (the only change). No README line or link was flagged as a deliberate replacement.

### Metrics

| Metric | Baseline | After | Target | Met |
|---|---:|---:|---|---|
| `words` | 8202 | 5483 | baseline plus 5 percent at most; aim minus 10 percent | Yes (minus 33.2 percent) |
| `h2` | 6 | 15 | none | n/a |
| `toc` | 0 | 1 | 1 | Yes |
| `first_cmd` | 17 | 22 | 40 or less | Yes, but later than the baseline: the opening and At a glance now come first |
| `longest_sec` | 2940 | 977 | 1,500 or less; 1,200 preferred | Yes |
| `long_lines` | 44 | 0 | cut by half | Yes |
| `max_line` | 1983 | 300 | 700 or less | Yes |
| `sent_len` | 16.7 | 10.2 | 16.5 or less | Yes, with a caveat below |
| `fre` | 43 | 57 | no lower than baseline; aim plus 5 | Yes (plus 14) |

Caveat on `sent_len` and `fre`: the script samples only paragraph lines, not bullets or tables. Many sentences moved from paragraphs into bullets, so the paragraph sample is smaller and shorter. Over paragraphs and bullets together, mean sentence length went from 14.8 to 11.6. Both figures are in the target.

No target was missed. Hand measures after: longest paragraph 45 words, longest table cell 25 words.

### Facts re-measured or corrected

- Re-measured on 2026-10-31 and unchanged in the README: 59 skills; the routing, unit-test, pytest, contract, portable-reference and hook figures in the table above; the five date-gate rows (2026-11-29, 11-30, 12-01, 2027-01-30, 02-01, each with its exit code and finding count); 2026-11-27 is a Friday.
- Corrected: the scraper test failure wording (see Observe).
- Corrected: the full-checkout file count. The README said "about 1,500". It measured 1,561 at the start and 1,580 at the end, and it grows with every commit, so the README now says about 1,600.
- Corrected: the package-oriented tree count in the Validation table, 1002 to 1005, because `docs/references.md`, `docs/skill-catalogue.md` and this record are new files.
- Corrected: "Each holds seven files" now notes that the pass 2 folder adds `07-docs-followups.md`.
- New facts, each checked: a repeat install of the same engine overwrites files and does not delete files removed upstream (code in `scripts/install-engine.js`, and a scratch install run twice, both exit 0); `doctor` reports OK, DAMAGED or LOCALLY MODIFIED (code, and a scratch run that printed `OK (393 files, 0 missing, 0 locally modified)`); the licence is `GPL-3.0-only` (`LICENSE` and `.claude-plugin/marketplace.json`); the register marks ICD 203 and RFC 9309 `partial` and ICD 206 `NOT_ASSESSED` (`docs/source-registers/kaizen-currentness-2026-10-31.json`).

### Not verified

- The README was not rendered on GitHub or in a Markdown viewer. Anchors were checked with the preservation script's slug rules, which follow the GitHub algorithm for these headings but are not GitHub itself.
- `python3 -m engine new-project`, `validate` and `pack` were not rerun. They write under `projects/` in this checkout. Their text is unchanged from the 31 October documentation wave.
- The Claude Code `/plugin` commands, `install.ps1` and remote CI were not run. `install.ps1` is `NOT_ASSESSED` on this host, which has no PowerShell.
- The three scraper tests and the two import-error modules were not run with their packages, because nothing was installed.

## Standardise

README conventions for a maintainer of this engine:

1. Skeleton: title and purpose; an At a glance list; Start here (three numbered steps with exact commands); Contents; Find the right skill; How it works; Skill catalogue; Install; engine-specific usage; Operating rules; Validation; Quality and improvement; the October account; References; Contributing, author and licence.
2. Limits: first fenced command by line 40; contents list before the third H2; no H2 over 1,200 words; no paragraph over 90 words; no table cell over 35 words; no line over 300 characters outside code fences; mean sentence length 16 words or fewer.
3. Task table: 6 to 12 rows. Every skill name is a real directory under `skills/`. Prefer tasks that the routing fixtures already use.
4. Anchors: `#validation` is linked from `AGENTS.md` and `CONTRIBUTING.md`. Keep the heading, or change those links in the same commit.
5. Numbers: every figure in the README comes from a command in the Validation table, with the date. Re-run the command when you edit the figure.
6. Bulk: lists over about 50 rows or 1,000 words go to `docs/`, with a summary and link in the README, but only when no script reads the section and the preservation check reports the links as moved. The skill table and the reference list already live in `docs/skill-catalogue.md` and `docs/references.md`; edit them there.
7. Protected files: link the Portfolio Kaizen Standard and the currentness gate. Do not edit them.
8. After any README edit, run `python3 -X utf8 scripts/check_portable_references.py`. It scans the README for host paths and dead links.

## Teach

- Open with what the engine is, who it is for, six measured facts and three commands. Put the contents list next. Detail goes below that.
- Move any list you scroll past, such as sources or catalogues, to `docs/` and keep a link. Check what reads the section first.
- Measure before and after with the same script, and keep every number tied to a command and a date.

## Re-measure and next cycle

Re-measure the nine metrics after the next README edit. The next full re-audit is on 2026-11-27, and the source registers lapse on 2026-11-30 (see the README, Date-triggered gates).

Findings for the maintainer, not changed here:

- `.claude-plugin/marketplace.json` lines 12 and 13 still give `https://github.com/peterbamuhigire/digital-research-skills` as the plugin homepage and repository. The README says that name redirects. Replacing it changes plugin metadata, so it needs a decision.
- `projects/healthcare-app-clinical-data/drug-interactions/research/wave1-data.md` is not valid UTF-8 (byte 0x97, a Windows-1252 dash). It breaks any tool that reads tracked text files as UTF-8, including the README preservation checker.
- The supplied `readme-preserve-check.py` should decode with `errors="replace"`, or skip files it cannot decode.
- A README length and line-width check in `scripts/` would stop the next drift. It would be a new validator, so it was not added in a scoped README cycle.
