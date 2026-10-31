# Digital Research Engine

The Digital Research Engine is Chwezi Core Systems' engine for finding, evaluating, verifying and synthesising evidence. It holds 59 skills that plan research in waves, admit and score sources, verify URLs, quotations, statistics and claim links, and build evidence-to-claim graphs.

Every material claim must trace to a source, be independently verified, carry a currentness date and stay separate from inference.

It is for researchers, analysts, consultants, investigators, due-diligence teams, postgraduate students and their supervisors, and decision-makers who need evidence they can defend. Use it when a task depends on current or uncertain facts. The other Chwezi engines consult it for the same reason.

**At a glance**

- **Skills:** 59 in 11 groups, stored as `skills/<skill-name>/SKILL.md`. All 59 pass the skill contract validator.
- **Runs in:** Claude Code (plugin `research`), Codex (through `AGENTS.md`) and any other agent that can read files.
- **Routing check:** 40 of 40 routing fixtures reach the right skill in the top three, and 36 of 40 at rank 1. This is a lexical proxy, not live routing.
- **Tests:** `validate_engine.py` passes and runs 94 unit tests. The full pytest run on this host gives 220 passed, 3 failed and 2 modules that cannot load, because optional packages are missing ([details](#test-status-measured)).
- **Quality score:** 59.5/100 in the latest published audit, under a reporting cap of 65. The target is 95.
- **Date gate:** the source registers pass on 2026-10-31 and fail from 2026-11-30 unless the sources are re-read ([dates](#date-triggered-gates)).

## Start here

1. **Load it.** In Claude Code, add the marketplace and install the plugin. [Install](#install) covers the clone, Codex and manual routes.

   ```text
   /plugin marketplace add https://github.com/peterbamuhigire/chwezi-research-engine
   /plugin install research@chwezi-research
   ```

2. **Check it.** From a clone, run the engine validator. It needs Python 3.11 or newer and `PyYAML`, and it exits 0 on a clean checkout until the [date gate](#date-triggered-gates).

   ```bash
   python3 -X utf8 scripts/validate_engine.py
   ```

3. **Use it.** Give the agent a task from [Find the right skill](#find-the-right-skill), or scaffold a research workspace:

   ```bash
   python3 -m engine new-project "<name>" --type <research-type> --audience <audience>
   ```

## Contents

- [Find the right skill](#find-the-right-skill)
- [How it works](#how-it-works)
- [Skill catalogue](#skill-catalogue)
- [Install](#install)
- [Scaffold a research workspace](#scaffold-a-research-workspace)
- [Operating rules and quality gates](#operating-rules-and-quality-gates)
- [Validation](#validation)
- [Quality and improvement](#quality-and-improvement)
- [What the October 2026 kaizen improved](#what-the-october-2026-kaizen-improved)
- [What the October 2026 kaizen changed in skills, standards and documents](#what-the-october-2026-kaizen-changed-in-skills-standards-and-documents)
- [October 2026 measures, before and after](#october-2026-measures-before-and-after)
- [References](#references)
- [Contributing, author and licence](#contributing-author-and-licence)

## Find the right skill

Describe the task in plain words and the router [`SKILL.md`](SKILL.md) selects the skills. To load one yourself, use this table. The full list of 59 is in the [Skill catalogue](#skill-catalogue).

| You need to | Skill |
|---|---|
| Judge whether sources are credible and assign evidence tiers | [`source-evaluation`](skills/source-evaluation/) |
| Check one current rate, date, status or count | [`source-evaluation`](skills/source-evaluation/), then its `single-claim-lookup.md` reference |
| Verify every URL, quotation and statistic in a finished manifest | [`source-verification`](skills/source-verification/) |
| Plan research waves, parallel cohorts and agent briefs | [`research-orchestration`](skills/research-orchestration/) |
| Choose questions, sampling and method for a new study | [`research-design`](skills/research-design/) |
| Run due diligence on a company | [`due-diligence`](skills/due-diligence/) |
| Investigate lawfully from public records | [`osint-investigation`](skills/osint-investigation/) |
| Research statutes and cases, or confirm a law is still in force | [`online-legal-research`](skills/online-legal-research/) |
| Size a market or model scenarios | [`quantitative-modelling`](skills/quantitative-modelling/) |
| Test a forward-looking judgement with structured analytic techniques | [`analytic-tradecraft`](skills/analytic-tradecraft/) |
| Turn verified findings into a board brief | [`executive-communication`](skills/executive-communication/) |
| Grade a finished document for AI slop | [`ai-slop-audit`](skills/ai-slop-audit/) |

## How it works

- A task enters through the router [`SKILL.md`](SKILL.md). The router sends it to one or more skills, and you load only those.
- [`rules/common/core.md`](rules/common/core.md) travels with every routed skill.
- Each skill is a folder, `skills/<skill-name>/`, with a `SKILL.md` and, where the skill needs one, a `references/` folder.

### Standards it follows

- PRISMA 2020 and the EQUATOR Network reporting guidelines (CONSORT, STROBE, MOOSE), for reporting reviews and studies.
- GRADE and the Cochrane Handbook, for evidence synthesis.
- ODNI ICD 203 and ICD 206, for analytic and sourcing standards.
- The NATO Admiralty Code (STANAG 2511), for source reliability.
- The Berkeley Protocol, for digital open-source investigation.
- IETF RFC 9309, for crawler conduct.

The [standards register](docs/source-registers/research-standards-register.md) records how far each was checked against primary pages. ICD 203 and RFC 9309 are `partial`, and ICD 206 is `NOT_ASSESSED`.

### What it produces

- Research plans and wave roadmaps.
- Source registers and verification manifests.
- Evidence-claim graphs and audit-ready evidence packs.
- Intelligence briefs and estimative memos.
- Due-diligence reports, OSINT chronologies and legal research memoranda.
- Systematic and scoping literature reviews, and theses and dissertations checked against named Ugandan and Kenyan university handbooks.
- Policy briefs, market analyses, decision memos and white papers.
- Professional Microsoft Word, Excel and PDF documents with render evidence.

## Skill catalogue

The table groups the 59 active skills into 11 workflow groups. It was generated from the skill front matter. The inventory is the filesystem below `skills/`, not this table. `skills/doc-standards.md` and `skills/encoding-patterns-into-skills.md` are shared notes, not skills.

| Category | Skill | What it does |
|---|---|---|
| Research operating system (6) | [`00-meta-initialization`](skills/00-meta-initialization/) | Initialises a research workspace with profile, method, audience-output matrix, wave roadmap and dispatch gate |
| | [`doctrine-spine`](skills/doctrine-spine/) | Defines and audits the mandatory research sequence from evidence discipline to export |
| | [`research-orchestration`](skills/research-orchestration/) | Chooses research type, discipline strategy and reading mode, then plans waves, gap filling and synthesis |
| | [`research-design`](skills/research-design/) | Sets formal questions, method, case logic, historical or trend design and MROC design |
| | [`research-techniques`](skills/research-techniques/) | Supplies named techniques: mini-analysis, crosswalk matrix, gap analysis, reference interview, search-operator grammar |
| | [`agentic-research-operations`](skills/agentic-research-operations/) | Designs and audits multi-agent research: briefs, roles, tool limits, verification loops and recovery |
| Source discipline and verification (5) | [`source-evaluation`](skills/source-evaluation/) | Admits sources after testing provenance, authority, independence, timeliness, bias and fit to the claim |
| | [`source-verification`](skills/source-verification/) | Verifies URLs, quotations, statistics, claim-source links, archive snapshots and release readiness |
| | [`evidence-claim-graph`](skills/evidence-claim-graph/) | Builds a traceable graph of sources, evidence, claims, warrants, gaps and contradictions |
| | [`validation-contract`](skills/validation-contract/) | Defines the seven evidence categories and the Release Evidence Bundle for specialist skills and releases |
| | [`peer-review-loop`](skills/peer-review-loop/) | Runs adversarial, red-team, source and method review with dissent handling before release |
| Reasoning, analysis and forecasting (6) | [`critical-reasoning-and-argument`](skills/critical-reasoning-and-argument/) | Tests claims for warrants, assumptions, countercases and implications |
| | [`analytic-tradecraft`](skills/analytic-tradecraft/) | Applies structured analytic techniques, bias checks and calibrated estimative language |
| | [`calibration-and-forecasting`](skills/calibration-and-forecasting/) | Calibrates, scores and updates forecasts, probability judgements and confidence claims |
| | [`decision-support-analysis`](skills/decision-support-analysis/) | Frames decisions with alternatives, values, uncertainty, trade-offs and pre-mortems |
| | [`systems-thinking-and-mental-models`](skills/systems-thinking-and-mental-models/) | Analyses feedback loops, root causes and leverage points with systemigrams and mental models |
| | [`mind-mapping-and-synthesis`](skills/mind-mapping-and-synthesis/) | Compresses a verified corpus into a navigable mind map for synthesis and decomposition |
| Data and quantitative work (3) | [`dataset-discovery-and-analysis`](skills/dataset-discovery-and-analysis/) | Finds public datasets, retrieves them with integrity checks and profiles their quality |
| | [`data-quality-pipeline`](skills/data-quality-pipeline/) | Profiles, cleans, merges and validates tabular data through lineage and quality gates |
| | [`quantitative-modelling`](skills/quantitative-modelling/) | Builds market-sizing, scenario and forecast models with assumption registers and model audits |
| Investigation and collection (7) | [`osint-investigation`](skills/osint-investigation/) | Runs lawful public-source investigation: reconnaissance, adverse media, chronology and case vaults |
| | [`due-diligence`](skills/due-diligence/) | Conducts corporate, sanctions, ownership and background due diligence with an auditable finding trail |
| | [`pi-investigation`](skills/pi-investigation/) | Supports authorised licensed-investigator work with chain of custody and evidentiary reports |
| | [`online-legal-research`](skills/online-legal-research/) | Researches statutes, cases and treaties by jurisdiction and refuses unverified law |
| | [`primary-research`](skills/primary-research/) | Designs interviews, observation, focus groups and coding for first-hand qualitative evidence |
| | [`web-scraping-foundations`](skills/web-scraping-foundations/) | Chooses the least invasive web acquisition path, with politeness and error handling |
| | [`scraping-engineering-python`](skills/scraping-engineering-python/) | Scales Python scrapers with caching, concurrency, browser automation and form handling |
| Academic research (5) | [`academic-writing`](skills/academic-writing/) | Drafts academic prose with source-away composition, citation, synthesis and register controls |
| | [`academic-reporting-standards`](skills/academic-reporting-standards/) | Applies named reporting and examination standards to papers, theses and systematic reviews |
| | [`dissertation-writing-process`](skills/dissertation-writing-process/) | Plans and drafts a dissertation from research question to defence-ready manuscript |
| | [`uganda-academic-research`](skills/uganda-academic-research/) | Checks academic work against named Ugandan university handbooks |
| | [`kenya-academic-research`](skills/kenya-academic-research/) | Checks academic work against named Kenya-based institutional handbooks |
| Writing and communication (9) | [`research-output-formats`](skills/research-output-formats/) | Selects the document form and academic or non-academic variant for a deliverable |
| | [`analytical-report-shapes`](skills/analytical-report-shapes/) | Shapes decision-grade artefacts: intelligence briefs, estimative and decision memos, evaluation reports |
| | [`report-and-proposal-craft`](skills/report-and-proposal-craft/) | Drafts long-form reports, proposals, business plans, bid responses and white papers |
| | [`business-writing`](skills/business-writing/) | Drafts emails, memos, letters, articles, web copy and speeches |
| | [`executive-communication`](skills/executive-communication/) | Turns verified research into answer-first memos, reports, decks and one-pagers |
| | [`consulting-delivery`](skills/consulting-delivery/) | Structures consulting work with issue trees, hypothesis-led workplans and implementation logic |
| | [`east-african-english`](skills/east-african-english/) | Adjusts English to natural, professional East African usage |
| | [`anti-ai-slop`](skills/anti-ai-slop/) | Prevents generic, unsupported or mechanical prose while an artefact is produced |
| | [`ai-slop-audit`](skills/ai-slop-audit/) | Grades a finished artefact for AI slop with evidenced findings, fixes and a verdict |
| Document production (5) | [`professional-word-output`](skills/professional-word-output/) | Produces and checks Word documents with controlled styles, pagination, tables and render evidence |
| | [`excel-spreadsheets`](skills/excel-spreadsheets/) | Builds and repairs Excel workbooks with formulas, tables, charts and formatting |
| | [`python-document-generation`](skills/python-document-generation/) | Generates branded Excel, Word and PDF exports from Python |
| | [`manual-guide`](skills/manual-guide/) | Writes end-user manuals and reference guides for ERP or SaaS features |
| | [`markdown-lint-cleanup`](skills/markdown-lint-cleanup/) | Repairs Markdown lint issues without changing meaning |
| Knowledge products (2) | [`knowledge-mining`](skills/knowledge-mining/) | Turns a corpus into claim libraries, evidence maps, dossiers and ontology seeds |
| | [`knowledge-productization`](skills/knowledge-productization/) | Converts research into reusable knowledge assets and audience-specific offerings |
| Requirements and project documentation (5) | [`project-requirements`](skills/project-requirements/) | Runs a discovery interview that yields requirements, business rules, user types and workflows |
| | [`systems-process-requirements`](skills/systems-process-requirements/) | Describes systems, processes, interfaces, states and data in testable, traceable form |
| | [`spec-architect`](skills/spec-architect/) | Produces coding-ready specifications with scope, acceptance criteria and risks |
| | [`doc-architect`](skills/doc-architect/) | Generates a project's layered `AGENTS.md` documentation from observed workspace evidence |
| | [`update-claude-documentation`](skills/update-claude-documentation/) | Reconciles project documentation with code after an authorised change |
| Engine and skill practice (6) | [`skill-writing`](skills/skill-writing/) | Creates or upgrades a skill under the canonical chwezi-dev-engine standard |
| | [`skill-composition-standards`](skills/skill-composition-standards/) | Sets house style, artefact contracts and evidence declarations for composed skills |
| | [`skill-taxonomy-and-routing`](skills/skill-taxonomy-and-routing/) | Normalises skill names, resolves skill-or-reference decisions and updates routers |
| | [`skill-safety-audit`](skills/skill-safety-audit/) | Reviews a new or changed skill for credential harvesting, unsafe installers and hidden mutation |
| | [`capability-matrix`](skills/capability-matrix/) | Maps a technology domain to its foundation, implementation, validation and companion skills |
| | [`ai-evaluation-and-data-flywheel`](skills/ai-evaluation-and-data-flywheel/) | Designs evaluations, failure analysis, regression sets and feedback loops for AI-assisted research |

**Total: 59 skills** (6 + 5 + 6 + 3 + 7 + 5 + 9 + 5 + 2 + 5 + 6).

## Install

### Prerequisites

- Claude Code, for the plugin route.
- Node.js 18 or newer, for the clone installers. `install.sh` and `install.ps1` both delegate to `scripts/install-engine.js`.
- Python 3.11 or newer, for the research workspace CLI (`python3 -m engine`), the validators and the Codex model-policy helper.
- `PyYAML` for the validators and `pytest` for the test suite. CI runs Python 3.12 with both.
- Optional packages for the document tools, the data and scraping tools and three test modules are listed under [Validation](#validation). The repository ships no requirements file.
- Commands in this README use `python3`. On Windows, read it as `python`.

### Claude Code plugin

This is step 1 of [Start here](#start-here). The marketplace is `chwezi-research` and the plugin is `research` (`.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`).

### Clone and install

```text
git clone https://github.com/peterbamuhigire/chwezi-research-engine
cd chwezi-research-engine
bash install.sh --scope project --dry-run   # macOS, Linux, Git Bash: print the plan, write nothing
bash install.sh --scope project
.\install.ps1 --scope project               # Windows PowerShell
node scripts/install-engine.js doctor --scope project
```

- `--scope user` (the default) copies the engine into `~/.claude`. `--scope project` copies it into `.claude` under the current directory.
- The installer also accepts `--dry-run`, `--json` and `--force`.
- `doctor` reports each installed engine as OK, DAMAGED or LOCALLY MODIFIED.
- `install.sh` is tracked without the executable bit, so run it through `bash`. `./install.sh` fails with "Permission denied" on Linux.
- The installer records the name of the checkout directory as the engine name. That matches the repository name when you clone as shown.
- The GitHub repository is `chwezi-research-engine`. The older name `digital-research-skills` redirects to it. The portfolio catalogue and the Kaizen prompts still use that older name as this engine's id.
- To update, pull the checkout and run the installer again. A repeat install copies files over the old ones and does not delete files that were removed upstream. For a clean copy, uninstall first.
- The same script runs `uninstall --engine <name>` (use the name that `list-installed` prints) and `list-installed`.

### Codex

Point Codex at the clone. It reads `AGENTS.md`, which routes to `SKILL.md` and `rules/common/core.md`. The Codex-only model-policy check lives in `.codex/`:

```text
python3 <engine-root>/.codex/ensure_model_policy.py --runtime codex --check
```

The check exits non-zero when the Codex configuration is missing or has drifted. With `--runtime claude` it prints `NOT_APPLICABLE` and exits 0.

### Manual use in any agent

Clone the repository and read `CLAUDE.md` (Claude Code) or `AGENTS.md` (other runners). Then open the router `SKILL.md` and load only the routed `skills/<skill-name>/SKILL.md` files. To scaffold and check a research workspace, see the next section.

## Scaffold a research workspace

```text
python3 -m engine doctor
python3 -m engine new-project "<name>" --type <research-type> --audience <audience>
python3 -m engine validate <project>
python3 -m engine pack <project> --out export/<name>.zip
```

- `--type` is free text.
- A relative `--out` path is resolved inside the project folder. An absolute path outside it writes the archive and then exits 1, because the release ledger cannot record it.
- On a freshly created workspace, `validate` exits 1 (gates 01, 03 and 05 report blockers) until `_context/` and the registries are filled. Run the `00-meta-initialization` skill first.

## Operating rules and quality gates

- Load [`rules/common/core.md`](rules/common/core.md) with any routed skill. Current, legal, regulatory and platform claims need an authoritative source and a dated currentness check. Unexecuted checks are reported as `NOT_ASSESSED`.
- Release gates live in [`docs/quality-gates/`](docs/quality-gates/). The standards register is [`docs/source-registers/research-standards-register.md`](docs/source-registers/research-standards-register.md).
- Kaizen guidance is under [`docs/continuous-improvement/`](docs/continuous-improvement/). The improvement records are indexed in [`docs/README.md`](docs/README.md) and summarised under [Quality and improvement](#quality-and-improvement).
- Checks: [Validation](#validation) lists each command, what it needs and what it returned on 2026-10-31.
- The 5,000-entry cap gate follows the [OpenAI ZIP entry limit](https://developers.openai.com/plugins/deploy/submission-errors) for the package-oriented tree. It follows the portfolio's full-checkout ceiling for the whole checkout. The two are measured separately.
- Book-derived knowledge enters only as paraphrased, task-oriented references. `scripts/check_no_book_extractions.py` blocks book extractions from the repository.

## Validation

Run every command from the repository root. They were run on 2026-10-31 on Linux with Python 3.14, Node 22 and pytest 9.0.3. A check that cannot run on a host is `NOT_ASSESSED`, never a pass.

| Command | What it checks | Needs | Result on 2026-10-31 |
|---|---|---|---|
| `python3 -X utf8 scripts/validate_engine.py` | Eight checks in order, stopping at the first failure | `PyYAML` | exit 0; 94 unit tests |
| `python3 -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json` | Zero-debt skill contract over the filesystem catalogue | `PyYAML` | exit 0; 59 active skills, 1 template, 59 compliant |
| `python3 -X utf8 scripts/routing_smoke_test.py --min-rank1 84 --lint-fixtures` | Lexical proxy for routing, with a rank-1 floor and a lint of the fixtures | `PyYAML` | exit 0; 40 of 40 fixtures in the top three, rank 1 for 36 of 40 (90.0%), 15 owned negatives pass, 2 `NOT_ASSESSED` |
| `python3 -X utf8 scripts/validate_source_currency.py --registers-dir docs/source-registers` | Dates and review metadata of every source register, as of today. Claim support is not checked | Python only | exit 0; 3 registers, 0 findings |
| `python3 -X utf8 scripts/validate_source_currency.py tests/fixtures/source-currency.json --as-of 2026-08-06` | The same validator against its fixed fixture | Python only | exit 0 |
| `python3 -X utf8 scripts/check_portable_references.py` | Host paths, repository-escaping links and dead relative links in active documents | Python only | exit 0; 389 files, 0 findings |
| `python3 -X utf8 scripts/check_file_count_cap.py` | Entry count of the full checkout and of the package-oriented tree, against 5,000 | Python only | exit 0; package-oriented tree 1002 of 5,000 |
| `python3 -X utf8 scripts/check_no_book_extractions.py` | No book-extraction folders, and no text file that links into one | Python; uses `git` when present | exit 0 |
| `python3 -X utf8 scripts/source_ingestion_guardrail.py` | No raw books or reconstructive text | Python only | exit 0; 0 findings |
| `validate_machine_error_gate.py` (command below the table) | The ME1 to ME7 and AS1 to AS7 identifiers exist in 11 bound engines. Wording quality is not checked | Sibling engine checkouts | exit 0; 11 engines |
| `python3 -m pytest -q -p no:cacheprovider tests engine/tests --continue-on-collection-errors` | The pytest suite ([Test status](#test-status-measured)) | `pytest` and the [packages](#packages) below | exit 1; 220 passed, 3 failed, 2 skipped, 16 subtests passed, 2 collection errors |
| `node scripts/generate-plugin-manifest.js --engine . --check` | `.claude-plugin/plugin.json` lists every skill directory | Node | exit 0; current, 59 skills |
| `node hooks/test-destructive-bash-gate.js` | The shipped destructive-command hook | Node | exit 0; 61 of 61 |
| `node hooks/test-plugin-hook-config.js` | The hook enable switch | Node | exit 0; 7 of 7 |
| `python3 -X utf8 <chwezi-dev-engine>/skills/sdlc-meta/skill-writing/scripts/quick_validate.py skills/<skill-name>` | The canonical single-skill validator, run on each changed skill | `PyYAML` and a checkout of `chwezi-dev-engine` | exit 0 on `skills/source-evaluation` |

### Notes on the table

- `validate_engine.py` runs these checks in order: portable references, file-count cap, register gate, skill contract, routing smoke test, no book extractions, `engine doctor`, and the unit tests in `engine/tests`.
- The full-checkout figure of the file-count cap counts `.git` objects, so it grows with every commit. It was 1,561 when measured.
- The machine-error gate finds the other engines under portfolio roots. A root is a folder that holds engine checkouts. Separate roots with `:` on Linux and macOS and `;` on Windows.
- Without `--engine` the gate exits 1, even with both roots named. The fixture's `political` target (`political-essay-skills`) has no checkout.

The gate command, with the workstation's two roots:

```bash
CHWEZI_ENGINES_ROOT=<root>[:<root>] python3 -X utf8 scripts/validate_machine_error_gate.py --engine srs --engine business-plan --engine website-copy --engine social-media --engine linux --engine proposal --engine engineering --engine accounting --engine design --engine windows --engine digital-research
```

### CI

- `.github/workflows/skill-engine-quality.yml` installs `PyYAML` and `pytest`. It then runs the contract validator, the routing smoke test, `tests/test_routing_ratchet.py` only, `validate_engine.py` and both currency commands.
- `.github/workflows/source-ingestion-guardrail.yml` runs the ingestion guardrail.
- CI does not run the machine-error gate or the rest of the pytest suite. Remote CI was not checked in this pass.

### Test status, measured

- Without `--continue-on-collection-errors`, pytest stops at collection (exit 2), because two modules cannot be imported here.
- The three failures are the `tests/test_research_scraper.py` tests. The scraper records `ModuleNotFoundError: No module named 'bs4'` for every page, so each test fails an assertion on its page counts.
- The same three fail identically at `d350ce2`, the commit before the second October pass (3 failed, 176 passed there).
- The two collection errors are `tests/test_enriched_docx_structure.py` (no `docx`) and `tests/test_merge_population_conservation.py` (no `pandas`).
- Whether these two modules and the three scraper tests pass with their packages installed is `NOT_ASSESSED`. Nothing was installed on this host, so none was rerun with `pandas`, `python-docx`, `beautifulsoup4` and `lxml` available.
- The two skips are opt-in tests: an installed portfolio, and all installed visual adapters.

### Packages

The repository ships no requirements file. Install only what the command you are running needs, and record a check that cannot run as `NOT_ASSESSED`.

| Package | Used by |
|---|---|
| `PyYAML` | the contract validator, routing smoke test, workspace registry checks and `quick_validate.py` |
| `pytest` | the pytest suite |
| `pandas` (with `numpy`) | `tools/data/` and `tests/test_merge_population_conservation.py` |
| `python-docx` and `xlsxwriter` | the document generators in `scripts/`, `tools/dd/report_builder.py` and `tests/test_enriched_docx_structure.py` |
| `beautifulsoup4` and `lxml` | the extractors in `tools/scraping/` and the three scraper tests |
| `httpx`, `requests`, `playwright`, `rapidfuzz`, `feedparser` and others | optional tools; the full baseline is in [`tools/README.md`](tools/README.md) |

No repository validator needs Pandoc, Mermaid, a browser, LibreOffice or a container. The Word and Excel render checks that the document skills describe run per deliverable, not here. `install.ps1` needs Windows PowerShell or `pwsh`. Neither exists on this host, so it is `NOT_ASSESSED`.

## Quality and improvement

Improvement records live under `docs/kaizen/`. Each holds seven files: scope and evidence, baseline scorecard, backlog, experiment log, validation record, final report and next cycle. The pass 2 folder adds `07-docs-followups.md`.

[`docs/README.md`](docs/README.md) indexes all of it, and earlier audits are under [`docs/audits/`](docs/audits/).

- [`2026-09-23-research-scraping/`](docs/kaizen/2026-09-23-research-scraping/)
- [`2026-10-engine-kaizen/`](docs/kaizen/2026-10-engine-kaizen/) (29 October 2026)
- [`2026-10-engine-kaizen-pass-2/`](docs/kaizen/2026-10-engine-kaizen-pass-2/) (31 October 2026)

The two October cycles are summarised under [What the October 2026 kaizen improved](#what-the-october-2026-kaizen-improved).

The cycle method is the [Portfolio Kaizen Standard](docs/continuous-improvement/portfolio-kaizen-standard-2026-08.md) and the [currentness gate](docs/continuous-improvement/kaizen-currentness-gate.md). Both are protected doctrine and change only on the maintainer's decision.

### Latest published score

Pass 2 ([final report](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md)): raw 59.5/100, published under the Portfolio Standard as `min(59.5, 65) = 59.5/100`.

- The frozen baseline for that pass was 56.3, and the 29 October final was 58.2.
- The target is 95/100. The cap is a reporting ceiling, not a rating.
- The pass kept ten backlog items, reverted none and found no critical defect.

### Open findings that matter to a user

The full list is in [`06-next-cycle.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/06-next-cycle.md).

- Archive snapshots for live-web verification are `NOT_ASSESSED`. A live-web answer carries that status until a workflow is approved.
- ICD 206 content, the latest ICD 203 amendment date and the RFC 9309 errata are `NOT_ASSESSED`. The register records ICD 203 as partial.
- Two worked records in `skills/source-evaluation/references/single-claim-lookup.md` name sources still unread: a Kenya NSSF clarification of 4 June 2026, and Uganda sections 11 and 12 after Act 1 of 2022. The pass 2 report counts 55 of 59 skill worked examples under 60 words.
- Market size for paid school-administration software in Uganda and Kenya is still a gap. The denominator rule exists, but product-matched numerator evidence does not.
- Routing evidence is lexical. Live-agent routing, paid behavioural runs, remote CI, marketplace readiness and installed-plugin discovery are `NOT_ASSESSED`.
- Four decisions wait for the maintainer:
  - two provenance lines in `docs/continuous-improvement/english-collocations-and-lexical-precision-2026-09-02.md` (lines 146 and 147);
  - binding or dropping the `political` target in the machine-error gate fixture;
  - retiring or redirecting about 14 imported engineering and documentation skills, which would change the 59-skill rule;
  - replacement wording for two protected documents in `docs/continuous-improvement/` that still name a workstation path.

### Date-triggered gates

`validate_engine.py` and CI check the source registers as of the day they run. They fail on the dates below unless the sources are re-read and the registers updated first. The counts assume nothing is re-verified in between.

Measure a date with `python3 -X utf8 scripts/validate_source_currency.py --registers-dir docs/source-registers --as-of <date>`.

| As of | Exit | Findings | What lapses |
|---|---:|---:|---|
| 2026-11-29 | 0 | 0 | Nothing; the last passing day |
| 2026-11-30 | 1 | 11 | Four OpenAI platform records dated 29 October, which also removes the accepted supersession of the six September records |
| 2026-12-01 | 1 | 13 | Two OpenAI platform records dated 31 October |
| 2027-01-30 | 1 | 21 | Eight standards records dated 29 October (PRISMA, PRISMA-C, GRADE, Cochrane Handbook, ICD 203, ICD 206, RFC 9309, TOP) |
| 2027-02-01 | 1 | 29 | The same eight standards records dated 31 October |

The next re-audit is on 2026-11-27, a Friday. Re-read the six OpenAI platform records first, rerun every validator in this README and re-measure the ten dimensions.

A full model-policy comparison is also due by 2026-12-28 under [`docs/continuous-improvement/model-policy-review-gpt6-luna-2026-09-28.md`](docs/continuous-improvement/model-policy-review-gpt6-luna-2026-09-28.md). No validator enforces that date.

## What the October 2026 kaizen improved

Two cycles ran in October 2026. Their evidence is linked below.

- 29 October: [final report](docs/kaizen/2026-10-engine-kaizen/05-final-report.md) and [experiment log](docs/kaizen/2026-10-engine-kaizen/03-experiment-log.md).
- 31 October: [final report](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md), [backlog](docs/kaizen/2026-10-engine-kaizen-pass-2/02-improvement-backlog.md),
  [experiment log](docs/kaizen/2026-10-engine-kaizen-pass-2/03-experiment-log.md) and [validation record](docs/kaizen/2026-10-engine-kaizen-pass-2/04-validation-record.md).

All 18 items were kept and are on `main`. Neither cycle reverted an experiment. Each short hash was checked against `git log` and `git show --stat`.

Figures marked "re-measured" were rerun on 2026-10-31 from the commit named, in a scratch extraction outside this checkout. The others are copied from the linked evidence file.

Every check is a unit, repository or lexical check. No live-agent run, paid model call, remote CI run or installed-plugin check backs any item.

Items 1 to 8 are here. Items 9 to 18 are under [What the October 2026 kaizen changed in skills, standards and documents](#what-the-october-2026-kaizen-changed-in-skills-standards-and-documents).

### Gates and checks that were broken or blind

Ordered by severity. The pass 2 baseline rated the first, second and fourth items Major. The 29 October backlog rated the path defect P0.

1. **The machine-error gate ran on one host only** (`00bdc44`)
    - Problem: all 12 targets failed as missing, because the fixture held 17 absolute checkout paths.
    - Change: targets now resolve under `--engines-root`, `CHWEZI_ENGINES_ROOT` or the checkout's parent, with an alias table for renamed checkouts. An unresolvable target still fails.
    - Result: fixture host paths fell from 17 to 0, and unresolved targets on a default run from 12 to 3 (re-measured). With the workstation's two engine roots named, the 11 bound engines pass on identifier presence only, which says nothing about semantic agreement. 12 new tests.
2. **Source registers could not be marked superseded** (`d581e01`)
    - Problem: `validate_source_currency.py` could not read that a register was superseded, so six records that the 29 October cycle had already dispositioned still failed. CI checked only a fixture at a fixed date, so no real register could block a release.
    - Change: the validator accepts a `superseded_by` key, only when the successor validates and dispositions every old record. A new `--registers-dir` gate runs in `validate_engine.py` and CI, as of the day.
    - Result: the older register moves from exit 1 to exit 0 on 2026-10-31 (re-measured). The gate fails by date; the table under [Date-triggered gates](#date-triggered-gates) lists when. 13 new tests.
3. **Host paths had no guard** (`d02f841`, `aa8ba37`)
    - Problem: host-specific absolute paths sat in the router and in skill references. A scan of the frozen tree found 52 in 376 Markdown files (a retrospective scan, not a pre-change run).
    - Change: `scripts/check_portable_references.py` now runs inside `validate_engine.py`, and the paths are replaced.
    - Result: a clean tree reports 0 findings, and a synthetic Windows path exits 1. 7 tests.
4. **The path scanner missed whole classes of link** (`f610ce7`)
    - Problem: the scanner missed `../../../skills-web-dev/...` style links, because its pattern matched only `chwezi-` names. It never read `CONTRIBUTING.md` or the authoring standard, and it checked no link target. A dead link at `skills/doc-standards.md:446`, to a file that never existed, passed.
    - Change: two rules (`link-escapes-repository`, `broken-relative-link`) and a wider default scope. They found 5 findings on the unrepaired tree (evidence file), and those were repaired.
    - Result: the scan covers 389 files with 0 findings (re-measured), and its test file holds 14 tests, up from 7.
5. **A test failed on stale hashes** (`4c27f39`)
    - Problem: `tests/test_research_evaluator_contract.py` failed on stale guidance hashes in the frozen tree as well as the current one.
    - Change: its fixture now pins hashes in memory only. The production hash check is unchanged.
    - Result: the module runs 5 tests with `python3 -m unittest tests.test_research_evaluator_contract` (re-measured). The pytest total recorded for that cycle (184 passed) came from a portfolio environment with packages this host lacks, and it was not reproduced.

### New checks and tests

6. **Nothing guarded the file-count limit** (`72bc019`, `4c27f39`)
    - Problem: the 5,000-entry limit is the portfolio ceiling and matches the OpenAI archive limit, and no check enforced it.
    - Change: `scripts/check_file_count_cap.py` counts the full checkout and a package-oriented tree, runs inside `validate_engine.py` and refuses a limit outside 0 to 5,000.
    - Result: 6 tests, including exact-limit and one-over. When this account was written it counted 1,548 and 1,002 (re-measured; the full count includes `.git`). It is a preflight proxy, not a count of a built archive.
7. **Skills repeated headings** (`b9648f6`)
    - Problem: 19 skills repeated an H2 heading, because the contract validator checked duplicates only for its 13 required titles.
    - Change: a `duplicate_heading` code now rejects any repeat. 18 empty stub headings were removed in 17 skills and two repeated headings were renamed, with the set of non-blank lines checked as unchanged.
    - Result: the new check reports 19 on the tree before the fix. The catalogue now has 0 and is 59 of 59 compliant (re-measured). 5 tests.
8. **Companion lists named a retired skill** (`d094054`)
    - Problem: companion lists named `data-quality-assessment`, merged into `data-quality-pipeline` in April 2026, 15 times in 12 files.
    - Change: an `unresolved_companion_name` code now requires every backticked name in a Companion Skills section to be an active skill, or an entry in `tests/skill-engine/external-skills.json` with its engine and a check date.
    - Result: none of the 15 mentions remains (re-measured). 7 tests.

## What the October 2026 kaizen changed in skills, standards and documents

These are items 9 to 18 of the same account. The method, evidence labels and limits are stated under [What the October 2026 kaizen improved](#what-the-october-2026-kaizen-improved).

### Skill content added where a task exposed a gap

9. **Premise check and single-claim lookups** (`4f73c9c`, `81970a4`)
    - Problem: nothing asked an agent to test the premise of a question, and three skills excluded single-claim lookups without naming where they go.
    - Change: `skills/source-evaluation/references/single-claim-lookup.md` now holds a premise check, a one-claim record and stop rules. It is reachable from `AGENTS.md`, `source-evaluation` and the three skills that excluded such lookups.
    - Result: lines matching the four premise phrases in `skills/`, `rules/` and `AGENTS.md` went from 0 to 11 (re-measured).
    - Caveat: one held-out false premise (a claimed 2025 rise in Uganda's NSSF employer rate to 12 percent) was handled by following the procedure. That is one recorded run, not a measure of agent behaviour.
10. **Undated pages and unapplied amendments** (`b81c727`)
    - Problem: an undated first-party page and a statute consolidation that lists unapplied amendments had no rule.
    - Change: the same reference now covers both, with a worked record on the Uganda NSSF rate checked against the Act text. `online-legal-research` points to it.
    - Result: lines mentioning "undated" in `skills/` went from 0 to 7 (re-measured). Whether Act 1 of 2022 changed the rate sections is still unread.
11. **A market-size boundary** (`68d9747`)
    - Problem: the 29 October market brief could not support a commercial school-administration software market size. `quantitative-modelling` had no rule separating government school-system coverage and adjacent learning-product spend from it.
    - Change: a boundary rule (product, buyer, geography, period, revenue basis) and a sourced worked example.
    - Result: the re-run still ends at a gap rather than a figure, which is the intended result.
12. **Conflicting denominators** (`9621cc6`)
    - Problem: the same skill had no rule for conflicting denominators or for checking a vendor figure's own arithmetic.
    - Change: a denominator check and a 336-word example. The example uses the recorded figures: 45,164 registered against 26,597 responding Ugandan primary schools, and a vendor subtotal of 30,200 against components that sum to 26,700.
    - Result: verified by redoing the arithmetic, not by a behavioural run.

### Routing and discoverability

13. **Current-state prompts did not reach the right skill** (`fb4dfee`)
    - Problem: a plain "current NSSF employer rate" prompt ranked `source-evaluation` 55th, because no skill text mentioned a current rate, date or status.
    - Change: one "Use When" bullet and four fixtures.
    - Result: the prompt moves to 1st (re-measured with `routing_smoke_test.rank`). With "Uganda" in the prompt it moves from 56th to 2nd, still behind `uganda-academic-research`.
    - Limit: a Kenya false-premise prompt still does not reach it, because in this proxy a proper noun in a skill name outweighs general vocabulary.
    - Dropped: a planned rewrite of the two country skills' descriptions, after the diagnosis showed the descriptions were not the cause.

### Standards currency

14. **The standards register was overdue and incomplete** (`bd5a693`)
    - Problem: the register omitted GRADE, Cochrane 6.5, ICD 206 and RFC 9309.
    - Problem: `academic-reporting-standards` described GRADE, Cochrane and TOP as hosted by EQUATOR, and TOP as eight modular standards. The publisher's current page describes TOP 2025 as seven Research Practices and two Verification Practices.
    - Change: a dated, claim-linked register (12 records). The six overdue records were dispositioned, and the skill now separates EQUATOR guidance from GRADE, Cochrane and TOP, each with its own source.
    - Result: the validator checks dates and metadata only, not whether a source supports a claim.
15. **The register overstated three standards** (`aeceb5a`)
    - Problem: the 29 October register overstated three standards. Two days later the named standards were re-read from primary pages (10 sources, 11 claims).
    - Change: ICD 203 moved from `verified` to `partial`, because a second technical amendment exists and its date cannot be read reliably.
    - Change: ICD 206 moved from `partial` to `NOT_ASSESSED`, because the PDF has no text layer and no OCR tool is installed here.
    - Change: RFC 9309 moved from `verified` to `partial`, because the errata are unread.
    - Result: PRISMA 2020, GRADE, Cochrane 6.5 and TOP 2025 were unchanged, and the redirected ODNI links in `analytic-tradecraft` were updated. No independent reviewer has signed any row.

### Documentation and portability

The 31 October documentation wave. No skill body was edited.

16. **Install and validation guidance in the README** (`390a80c`, `ebed632`)
    - Problem: the README told readers to clone `digital-research-skills`, run `./install.sh` and use a `pack --out <file>.zip` example.
    - Problem: `install.sh` is tracked as mode 100644, so `./install.sh` fails on Linux with "Permission denied". The example did not say that an absolute path outside the project writes the archive and then exits 1.
    - Change: the README names `chwezi-research-engine`, uses `bash install.sh` and a project-relative `--out`, and carries the [Validation](#validation) table.
    - Result: each command in that table was run on 2026-10-31, and each package-dependent test is marked `NOT_ASSESSED` where its package was absent.
17. **Counts and shell blocks in the guidance files** (`a77d75d`, `1542d6f`)
    - Problem: `AGENTS.md` said every skill ships `AGENTS.md`, `README.md`, `CLAUDE.md` and `references/`. The counts are 27, 27, 27 and 48 of 59 (re-measured). `CONTRIBUTING.md`, the authoring standard and the evidence pack template used PowerShell blocks and backslash paths.
    - Change: `AGENTS.md` now states the counts, adds the `python3` note and documents the portfolio-root options of the machine-error gate (`a77d75d`). The other three files now use bash, `python3` and forward slashes (`1542d6f`).
18. **There was no documentation index** (`15b1a47`, `d912001`)
    - Problem: two April 2026 briefs also read as current.
    - Change: `docs/README.md` now indexes the folder and the improvement records, and the two briefs carry a status note.
    - Result: the findings the wave left unchanged are recorded in [`07-docs-followups.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/07-docs-followups.md).

Considered and left out: the nine "Evidence Notes 1 and 2" headings (one holds a table the contract reads as its evidence section), and the description rewrite noted under item 13. Both are recorded in the [pass 2 experiment log](docs/kaizen/2026-10-engine-kaizen-pass-2/03-experiment-log.md).

## October 2026 measures, before and after

| Measure | Before | After | Basis |
|---|---|---|---|
| Raw score, then `min(raw, 65)` | 52.1 then 52.1 (29 October baseline); 56.3 then 56.3 (pass 2 baseline) | 58.2 then 58.2 (29 October final); 59.5 then 59.5 (pass 2 final) | Reviewer judgement; copied |
| Routing, top-3 and rank-1 (lexical proxy) | 29/29 and 25/29 (86.2%) at `444b7ce`; 34/34 and 30/34 (88.2%) at `d350ce2` | 40/40 and 36/40 (90.0%) | Re-measured at each commit |
| Owned negatives: pass, fail, `NOT_ASSESSED` | 9 (7, 0, 2) then 11 (9, 0, 2) | 17 (15, 0, 2) | Re-measured |
| Skills with 3 positive and 2 owned-negative fixtures | 0 of 59 then 1 of 59 | 3 of 59 (`online-legal-research`, `quantitative-modelling`, `source-evaluation`) | Re-counted from the fixtures file |
| Unit tests run by `validate_engine.py` | 37 at `444b7ce`; 50 at `d350ce2` | 94 | Re-measured |
| Skills with a repeated heading | 19 | 0 | Re-measured |
| Machine-error gate targets unresolved on a default run | 12 of 12 | 3 of 12 | Re-measured |
| Overdue records in the older register on 2026-10-31 | 6 (exit 1) | 0 (exit 0, `SUPERSEDED` note) | Re-measured |
| Portable-reference scan | 376 files, 0 findings, narrow rules | 389 files, 0 findings, link rules added | Re-measured |
| Skills contract | 59 of 59 | 59 of 59, now with two more codes | Re-measured |
| Worked examples under 60 words | 55 of 59 | 55 of 59 | Evidence file; still open |

Notes on the table:

- Scores are reviewer judgement. They are copied, not re-measured.
  - 29 October: [baseline](docs/kaizen/2026-10-engine-kaizen/01-baseline-scorecard.md) and [final report](docs/kaizen/2026-10-engine-kaizen/05-final-report.md).
  - Pass 2: [baseline](docs/kaizen/2026-10-engine-kaizen-pass-2/01-baseline-scorecard.md) and [final report](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md).
- The pass 2 baseline (56.3) is lower than the 29 October final (58.2). Fresh observation found defects that the earlier scoring had missed. The code did not change.
- The rises in routing precision come from added fixtures that pass, except the NSSF probe in item 13.
- The unit-test counts come from `python3 -m unittest discover -s engine/tests`. The 29 October final report says 48 in one table row, and its validation record says 50. The run gives 50.
- Three targets stay unresolved on a default run. One of them, `political`, has no public checkout.
- The portable-reference scan was re-measured at `d350ce2` and now. The 5 findings that the new rules give on the old tree come from the evidence file.

## References

The engine cites books, standards and official sources, open-source repositories, and websites and articles. The full list, grouped in that way, is in [`docs/references.md`](docs/references.md). It gives citations only; no book content is reproduced.

Two records explain how sources entered the engine: [`RESEARCH_CRAFT_INTEGRATION.md`](RESEARCH_CRAFT_INTEGRATION.md) and the [2026-Q4 ecosystem scan](docs/continuous-improvement/ecosystem-scan-2026-Q4.md). The scan gives the licence and verdict for each repository reviewed without borrowing.

## Contributing, author and licence

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and the [skill authoring standard](docs/skill-authoring-standard.md) before you change a skill, and run the checks in [Validation](#validation). The [documentation index](docs/README.md) lists the standards, gates and records.

Author: Peter Bamuhigire, for Chwezi Core Systems. Licence: GNU General Public License, version 3 only (`GPL-3.0-only`); see [`LICENSE`](LICENSE).
