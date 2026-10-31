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
    - Change: ICD 203 moved from `verified` to `partial`, because a second technical amendment exists and its date cannot be read reliably. ICD 206 moved from `partial` to `NOT_ASSESSED`, because the PDF has no text layer and no OCR tool is installed here. RFC 9309 moved from `verified` to `partial`, because the errata are unread.
    - Result: PRISMA 2020, GRADE, Cochrane 6.5 and TOP 2025 were unchanged, and the redirected ODNI links in `analytic-tradecraft` were updated. No independent reviewer has signed any row.

### Documentation and portability

The 31 October documentation wave. No skill body was edited.

16. **Install and validation guidance in the README** (`390a80c`, `ebed632`)
    - Problem: the README told readers to clone `digital-research-skills`, run `./install.sh` and use a `pack --out <file>.zip` example. `install.sh` is tracked as mode 100644, so `./install.sh` fails on Linux with "Permission denied". The example did not say that an absolute path outside the project writes the archive and then exits 1.
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

- Scores are reviewer judgement from the [29 October baseline](docs/kaizen/2026-10-engine-kaizen/01-baseline-scorecard.md) and [final report](docs/kaizen/2026-10-engine-kaizen/05-final-report.md), and the pass 2 [baseline](docs/kaizen/2026-10-engine-kaizen-pass-2/01-baseline-scorecard.md) and [final report](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md). They are copied, not re-measured.
- The pass 2 baseline (56.3) is lower than the 29 October final (58.2). Fresh observation found defects that the earlier scoring had missed. The code did not change.
- The rises in routing precision come from added fixtures that pass, except the NSSF probe in item 13.
- The unit-test counts come from `python3 -m unittest discover -s engine/tests`. The 29 October final report says 48 in one table row, and its validation record says 50. The run gives 50.
- Three targets stay unresolved on a default run. One of them, `political`, has no public checkout.
- The portable-reference scan was re-measured at `d350ce2` and now. The 5 findings that the new rules give on the old tree come from the evidence file.

## References

The sources below are those cited in this repository: skill source sections and source registers, [`RESEARCH_CRAFT_INTEGRATION.md`](RESEARCH_CRAFT_INTEGRATION.md), the July 2026 book-to-engine map, Kaizen records, the 2026-Q4 ecosystem scan and code attribution comments. Where the repository omits an author, year or publisher, so does this list. Citations only; no book content is reproduced.

### Books

- Aaker, Kumar, Leone and Day (2022) *Marketing Research*, 13th ed., Wiley.
- Abbott (2014) *Digital Paper*.
- Bailey (2018) *Academic Writing: A Handbook for International Students*, 5th ed., Routledge.
- Bazerman (1988) *Shaping Written Knowledge: The Genre and Activity of the Experimental Article in Science*, University of Wisconsin Press.
- Bazzell *Open Source Intelligence Techniques*, 11th ed.
- Bean (2011) *No More Secrets: Open Source Information and the Reshaping of U.S. Intelligence*, Praeger Security International / ABC-CLIO.
- Behrens and Hawranek (1991) *Manual for the Preparation of Industrial Feasibility Studies*, rev. ed., UNIDO.
- Belcher (2019) *Writing Your Journal Article in Twelve Weeks*, 2nd ed., University of Chicago Press.
- Bell (2015) *Librarian's Guide to Online Searching*, 4th ed.
- Berg (2004) *Qualitative Research Methods for the Social Sciences*, Pearson.
- Bergeron (2003) *Essentials of Knowledge Management*.
- Boardman and Sauser *Systemic Thinking: Building Maps for Worlds of Systems*.
- Booth, Colomb, Williams, Bizup and FitzGerald (2016) *The Craft of Research*, 4th ed., University of Chicago Press.
- Booth, Sutton and Papaioannou (2021) *Systematic Approaches to a Successful Literature Review*, 3rd ed., SAGE.
- Botwright (2024) *Advanced OSINT Strategies: Online Investigations and Intelligence Gathering*.
- Boynton *The New New Journalism*.
- Brause (1999) *Writing Your Doctoral Dissertation: Invisible Rules for Success*, Falmer Press / RoutledgeFalmer.
- BRB Publications *The Sourcebook to Public Record Information*.
- Brockman (ed.) *Thinking: The New Science of Decision-Making, Problem-Solving, and Prediction*.
- Brody (2017) *The Ultimate Guide to Web Scraping*.
- Brown (2017) *Harnessing the Power of Google*.
- Bui (2019) *How to Write a Master's Thesis*, 3rd ed., SAGE.
- Burke (1945) *A Grammar of Motives*.
- Burtonshaw-Gunn *Essential Tools for Management Consulting*.
- Buzan *Mind Map Mastery*; Buzan *Buzan Study Skills Handbook*.
- Caples and Hahn (1998) *Tested Advertising Methods*, 5th ed., Prentice Hall.
- Clark (2019) *Intelligence Analysis: A Target-Centric Approach*, 6th ed., CQ Press.
- Clippinger (2019) *Business Report Guides: Research Reports and Business Plans*.
- Cottrell (2023) *Critical Thinking Skills*, 4th ed., Bloomsbury.
- Day and Gastel (2017) *How to Write and Publish a Scientific Paper*, 8th ed., Cambridge University Press.
- Deason *Internet Research with Google*.
- Denscombe (2019) *Research Proposals: A Practical Guide*, 2nd ed., Open University Press.
- Duarte (2014) *Slidedocs: Spread Ideas with Effective Visual Documents*, Duarte Inc.
- Dunleavy (2003) *Authoring a PhD*, Palgrave Macmillan.
- Eco (2015) *How to Write a Thesis* (English translation).
- Edwards (2019) *Legal Writing and Analysis*, 5th ed., Wolters Kluwer.
- Ellet (2007) *The Case Study Handbook*, Harvard Business Review Press.
- Forsyth (2016) *How to Write Reports and Proposals*.
- Garner (2013) *HBR Guide to Better Business Writing*, Harvard Business Review Press.
- Garner (2013) *Legal Writing in Plain English*, 2nd ed., University of Chicago Press.
- Geffner *Business English*.
- George *Excel 2019 Advanced Topics*.
- George and Bruce (eds.) (2008) *Analyzing Intelligence: Origins, Obstacles, and Innovations*, Georgetown University Press.
- Glaser and Strauss (1967) *The Discovery of Grounded Theory*.
- Glatthorn and Joyner (2017) *Writing the Winning Thesis or Dissertation*, 4th ed., Corwin.
- Gottschall (2013) *The Storytelling Animal: How Stories Make Us Human*, Mariner Books.
- Graham (2013) *White Papers For Dummies*, Wiley.
- Grant (2021) *Contemporary Strategy Analysis*, 11th ed., Wiley.
- Hackos *The Complete Guide to Knowledge Management*.
- Hague, Hague and Morgan (2022) *Market Research in Practice*, 4th ed., Kogan Page.
- Hancock and Algozzine (2006) *Doing Case Study Research: A Practical Guide for Beginning Researchers*, Teachers College Press.
- Hanington and Martin *The Pocket Universal Methods of Design*.
- Hart (2018) *Doing a Literature Review*, 2nd ed., SAGE.
- Hart *Storycraft*.
- Hartley (2008) *Communicating Ideas: The Politics of Scholarly Publishing*, Routledge.
- Hattori *The McKinsey Edge*.
- Heath and Heath (2013) *Decisive: How to Make Better Choices in Life and Work*, Random House.
- Henwood (2020) *Business Writing for Innovators and Change-Makers*, Business Expert Press.
- Hetherington (2015) *The Guide to Online Due Diligence Investigations*, 2nd ed., Facts on Demand Press.
- Heuer (1999) *Psychology of Intelligence Analysis*, CIA Center for the Study of Intelligence.
- Heuer and Pherson *Structured Analytic Techniques for Intelligence Analysis*, CQ Press / SAGE (1st ed. 2010; 3rd ed. cited as 2020 and 2021).
- Hewings and Hewings *Grammar and Context*, Routledge.
- Hood *Words at Work*.
- Hyland (1998) *Hedging in Scientific Research Articles*.
- Hyland (2004) *Disciplinary Discourses: Social Interactions in Academic Writing*, 2nd ed., University of Michigan Press.
- Jordan *ICDL Word*.
- Kamler and Thomson (2014) *Helping Doctoral Students Write*, 2nd ed., Routledge.
- Kantor (2009) *Crafting White Paper 2.0*, Lulu.
- Kelley *The Art of Reasoning: An Introduction to Logic and Critical Thinking*.
- Koelsch *Requirements Writing for System Engineering*.
- Kotler and Keller (2022) *Marketing Management*, 16th ed., Pearson.
- Kramer and Call *Telling True Stories*.
- Krone *Navigating the Dissertation Writing Process*.
- Kunz, Schmedemann, Erlinder, Downs and Bateson (2020) *The Process of Legal Research: Practices and Resources*, 9th ed., Wolters Kluwer.
- Lawson (2015) *Web Scraping with Python*, Packt.
- Lindsell-Roberts (2024) *Business Writing with AI for Dummies*, Wiley.
- Locke, Spirduso and Silverman (2013) *Proposals That Work*, 6th ed., SAGE.
- Lockridge and Van Ittersum *Writing Workflows*.
- Long *Legal Research Using the Internet*.
- MacLeod (2012) *How to Find Out Anything*.
- Magaziner and Patinkin (1989) *The Silent War*, Random House.
- Maslen (2019) *Persuasive Copywriting*, 2nd ed., Kogan Page.
- Maxwell (2020) *7 Steps to Better Writing*.
- McCandless (2014) *Knowledge is Beautiful*, William Collins.
- McInerny *Being Logical: A Guide to Good Thinking*.
- McMahon (2001) *Practical Handbook for Professional Investigators*.
- Medina (2014) *Brain Rules*, 2nd ed., Pear Press.
- Merriam (2001) *Qualitative Research and Case Study Applications in Education*, Jossey-Bass.
- Minto (1985; revised 1996, 2002, 2009) *The Minto Pyramid Principle: Logic in Writing, Thinking and Problem Solving*, Minto Books International.
- Morley (2017) *Academic Phrasebank*, 4th ed.
- Murray (2017) *How to Write a Thesis*, 4th ed., Open University Press.
- National Research Council (2011) *Intelligence Analysis for Tomorrow: Advances from the Behavioral and Social Sciences*, National Academies Press.
- Norman (2004) *Emotional Design: Why We Love (or Hate) Everyday Things*, Basic Books.
- O'Dell and McCarthy (2017) *English Collocations in Use Advanced*, 2nd ed., Cambridge University Press.
- Ogilvy (1985) *Ogilvy on Advertising*, Vintage.
- Oxylabs (2024) *Python Web Scraping for Developers*.
- Patton (2015) *Qualitative Research & Evaluation Methods: Integrating Theory and Practice*, 4th ed., SAGE.
- Phillips and Pugh (2015) *How to Get a PhD*, 6th ed., Open University Press.
- Porter (1980) *Competitive Strategy*, Free Press; Porter (1985) *Competitive Advantage*.
- Poynter (2010) *The Handbook of Online and Social Media Research*.
- Punch (2016) *Developing Effective Research Proposals*, 3rd ed., SAGE.
- Putman and Albright (2018) *Legal Research, Analysis and Writing*, Cengage.
- Ramsey (2017) *Business Writing Scenarios*, Bedford/St Martin's.
- Rasiel (1999) *The McKinsey Way*, McGraw-Hill.
- Rasiel and Friga (2001) *The McKinsey Mind*, McGraw-Hill.
- Raymond (2003) *Pamphlets and Pamphleteering in Early Modern Britain*, Cambridge University Press.
- Ridley (2012) *The Literature Review: A Step-by-Step Guide for Students*, 2nd ed., SAGE.
- Roman and Raphaelson (2000) *Writing That Works*, 3rd ed.
- Rowland (2000) *The Creative Guide to Research*.
- Rubie and Provost *How to Tell a Story*.
- Rumelt (2011) *Good Strategy, Bad Strategy*, Crown Business.
- Russell (2019) *The Joy of Search*.
- Seely *The Oxford Guide to Effective Writing and Speaking*.
- Shiach *How to Write Essays*.
- Shikhman and Mueller (2021) *Mathematical Foundations of Big Data Analytics*.
- Silverman (ed.) (2015) *Verification Handbook for Investigative Reporting*.
- Smith and Albaum (2005) *Fundamentals of Marketing Research*, SAGE.
- Stake (1995) *The Art of Case Study Research*, SAGE.
- Starkman, Hamilton, Chittum and Salmon (eds.) (2014) *The Best Business Writing 2014*, Columbia University Press / Columbia Journalism Review Books.
- Stelzner (2007) *Writing White Papers*, WhitePaperSource Publishing.
- Stoner and Perkins (2015) *Making Sense of Messages*, 2nd ed., Routledge.
- Strunk and White *The Elements of Style*, 4th ed.
- Sugarman (2007) *The Adweek Copywriting Handbook*, Wiley.
- Swales (1990) *Genre Analysis*.
- Swales and Feak (2012) *Academic Writing for Graduate Students*, 3rd ed., University of Michigan Press.
- Thompson (2014) *Feasibility Studies: Tools and Techniques*, Routledge.
- Treverton (2003) *Reshaping National Intelligence for an Age of Information*, Cambridge University Press.
- Trzeciak and Mackay (1994) *Study Skills for Academic Writing*.
- Tufte (2001) *The Visual Display of Quantitative Information*, 2nd ed.
- Urban *Advanced Excel for Productivity*.
- Van Der Post *Python in Excel Advanced*.
- Vic *Microsoft Word 2022 for Beginners & Pros*.
- Walkenbach and Alexander *Microsoft Excel 365 Bible*.
- Walker *Python Data Cleaning Cookbook*.
- Wallwork (2016) *English for Writing Research Papers*, 2nd ed., Springer.
- Watkins *The Six Disciplines of Strategic Thinking*.
- Wempen *Advanced Microsoft Word 2016*.
- Wengler (2026) *Automate Excel with Python*.
- Wiegers *More About Software Requirements*.
- Wiegers and Hokanson *Software Requirements Essentials*.
- Williams and Newton (2007) *Visual Communication: Integrating Media, Art, and Science*, Routledge.
- Wohlstetter (1962) *Pearl Harbor: Warning and Decision*, Stanford University Press.
- Yayici *Business Analysis Methodology Book*.
- Yin (2014) *Case Study Research: Design and Methods*, 5th ed., SAGE; Yin (2018) *Case Study Research and Applications: Design and Methods*, 6th ed., SAGE.
- Young and Quinn (2002) *Writing Effective Public Policy Papers*, Open Society Institute.
- Zelazny (2001) *Say It With Charts: The Executive's Guide to Visual Communication*, 4th ed., McGraw-Hill.
- Titles cited without an author: *AI-Based Data Analytics: Applications for Business Management*; *Applying the Kaizen in Africa* (2018); *Better Data Visualizations*; *Business Requirements Gathering and Data Architecture Modeling*; *Clear Written Communication* (50Minutes); *Critical Thinking, Logic & Problem Solving*; *Critical Thinking Skills: Developing Effective Analysis and Argument*; *Critical Thinking Skills for Education Students*; *Dare to Disrupt*; *Data Analytics using Python*; *Data Journalism Heist*; *Design Systems Handbook*; *Design Thinking*; *Designing for AI* (early release); *Developments in Information and Knowledge Management Systems for Business Applications*; *Doing Internet Research*; *Doing Your Research Project*; *Excel 2025 All-in-One*; *Facility Move Playbook*; *Finish Your Thesis or Dissertation! Tips & Hacks for Success*; *Growth Engineering*; *Hands-On Website Scraping with Python*; *How to Write a Literature Review: A Workbook in Six Steps*; *How to Write a Master's Thesis Fast*; *Inside the Minds: Leading Consultants*; *Introduction to Data Analytics*; *Knowledge Management and Business Strategies*; *LEAN Ultimate Collection* (2018); *Legal Research* (anonymous compendium); *Make Phenomenal Profits*; *Mental Models 2*; *Microsoft Excel Bible 2026*; *MSC Software Magazine* (2019); *Oxford Guide to Effective Argument and Critical Thinking*; *Platform Enterprise* (early release); *Project Scope Management: A Practical Guide to Requirements*; *Remarkable Business Growth*; *Rewired: The McKinsey Guide to Outcompeting in the Age of Digital and AI*; *Smart Thinking: Skills for Critical Understanding and Writing*, 2nd ed.; *The Art of Asking Essential Questions*; *The Data Analytics Advantage*; *The Great Mental Models, Volume 1*; *Think Deeper*; *Thinking in Systems and Mental Models*; *True or False*; *Ultimate Excel Formula & Function Reference Guide*; *Writing a Postgraduate Thesis or Dissertation: Tools for Success*.

### Repositories

- affaan-m/ECC — https://github.com/affaan-m/ECC — MIT — `santa-method` dual-reviewer convergence and stratified batch sampling (`peer-review-loop`); `scientific-thinking-literature-review` rigour levels (`academic-reporting-standards`); the MSYS2 path fix and installer scope choice (`install.sh`, `scripts/install-engine.js`).
- obra/superpowers — https://github.com/obra/superpowers — MIT, commit `8ca22db` — the description-narration lint in `skills/skill-writing/scripts/quick_validate.py` (my-10-kaizen SP-14).
- addyosmani/agent-skills — https://github.com/addyosmani/agent-skills — MIT, commit `2686b62` — four Tier-1 lint rules from `scripts/lib/skill-lint.js` (`quick_validate.py`) and the owner-outranks-self routing rule from `scripts/run-evals.js` (`scripts/routing_smoke_test.py`) (my-10-kaizen M10-03).
- JuliusBrussee/caveman — https://github.com/JuliusBrussee/caveman — MIT (skill side only), commit `2fd153c` — the evidence-rung vocabulary for improvement claims in `ai-evaluation-and-data-flywheel/references/eval-flywheel.md` (my-10-kaizen CV-07).
- DietrichGebert/ponytail — https://github.com/DietrichGebert/ponytail — MIT, commit `e3ba2aa` — the thin `CLAUDE.md` bridge to `AGENTS.md` and a real semantic version, 1.1.0 (my-10-kaizen PT-01, PT-04).
- pbakaus/impeccable — https://github.com/pbakaus/impeccable — Apache-2.0, commit `114ea1d` — anti-slop source record, the design trigger block, the detector rule-source pin for the K5 re-audit and the `PROJECT.md` context read in `AGENTS.md` (my-10-kaizen IM-11); ideas paraphrased, no code copied.
- ComposioHQ/awesome-claude-skills — https://github.com/ComposioHQ/awesome-claude-skills — NOASSERTION, commit `be2a406` — scan source for the first quarterly ecosystem scan (my-10-kaizen AC-04); nothing installed.
- Egonex-AI/Understand-Anything — https://github.com/Egonex-AI/Understand-Anything — MIT, commit `b05cc3b` — `/understand-knowledge` sandbox pilot recorded as `NOT_ASSESSED` under the zero-spend rule; not installed or adopted.
- WebBreacher/obsidian-osint-templates — https://github.com/WebBreacher/obsidian-osint-templates — practitioner OSINT note structure (`osint-investigation/references/osint-case-vaults.md`).
- donvito/codex-astra-luna-orchestrator — https://github.com/donvito/codex-astra-luna-orchestrator — commit `21f4561` — concept reference for the Codex model-policy helper in `.codex/`; independently implemented.
- peterbamuhigire/chwezi-dev-engine — https://github.com/peterbamuhigire/chwezi-dev-engine — canonical skill-writing standard and ecosystem-scan intake procedure.
- Reviewed in the 2026-Q4 ecosystem scan with no borrowing (licences and verdicts in [`docs/continuous-improvement/ecosystem-scan-2026-Q4.md`](docs/continuous-improvement/ecosystem-scan-2026-Q4.md)): agentskills/agentskills, alibaba/open-code-review, alirezarezvani/claude-skills, anthropics/skills, asgeirtj/system_prompts_leaks, blader/humanizer, career-ops-hq/career-ops, cathrynlavery/diagram-design, CherryHQ/cherry-studio, diegosouzapw/OmniRoute, farion1231/cc-switch, github/awesome-copilot, googleworkspace/cli, Graphify-Labs/graphify, headroomlabs-ai/headroom, hesreallyhim/awesome-claude-code, Imbad0202/academic-research-skills, jeecgboot/JeecgBoot, JimLiu/baoyu-skills, K-Dense-AI/scientific-agent-skills, KKKKhazix/khazix-skills, Leonxlnx/taste-skill, mvanhorn/last30days-skill, nextlevelbuilder/ui-ux-pro-max-skill, nexu-io/open-design, NousResearch/hermes-agent, NVIDIA/SkillSpector, OthmanAdi/planning-with-files, Panniantong/Agent-Reach, pascalorg/editor, phuryn/pm-skills, reactive-resume/reactive-resume, router-for-me/CLIProxyAPI, rtk-ai/rtk, ruvnet/ruflo, shanraisshan/claude-code-best-practice, shareAI-lab/learn-claude-code, sickn33/agentic-awesome-skills, snyk-labs/toxicskills-goof, stablyai/orca, thedotmack/claude-mem, titanwings/distilly, topoteretes/cognee, tt-a1i/archify, virgiliojr94/book-to-skill, VoltAgent/awesome-agent-skills, VoltAgent/awesome-openclaw-skills, zhayujie/CowAgent.

### Standards and official sources

- PRISMA 2020 statement and checklist — https://www.prisma-statement.org/prisma-2020; Page et al., *BMJ* 2021;372:n71.
- EQUATOR Network reporting guidelines — https://www.equator-network.org/ — including CONSORT 2025 (https://www.consort-spirit.org/), STROBE (https://www.strobe-statement.org/) and MOOSE (Stroup et al., *JAMA* 2000;283:2008-2012).
- GRADE Working Group — https://www.gradeworkinggroup.org/; GRADEpro handbook — https://gradepro.org/handbook/.
- Cochrane Handbook for Systematic Reviews — https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current.
- Center for Open Science TOP Guidelines — https://www.cos.io/initiatives/top-guidelines.
- ICMJE Recommendations — https://www.icmje.org/recommendations/.
- ODNI Intelligence Community Directive 203, *Analytic Standards* (2015) — https://www.dni.gov/files/documents/ICD/ICD-203.pdf; ICD 206, *Sourcing Requirements for Disseminated Analytic Products*.
- Kent (1964) "Words of Estimative Probability", *Studies in Intelligence* — https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf.
- NATO Admiralty Code, STANAG 2511 / AJP-2.1.
- UK Professional Head of Intelligence Assessment, *Probability Yardstick*.
- Silberman-Robb WMD Commission Report (2005).
- Berkeley Protocol on Digital Open Source Investigations — https://humanrights.berkeley.edu/wp-content/uploads/2024/02/Berkeley-Protocol.pdf.
- FIRST CTI SIG, "Source Evaluation" — https://www.first.org/global/sigs/cti/curriculum/source-evaluation.
- IETF RFC 9309, *Robots Exclusion Protocol* (September 2022).
- NIST AI Risk Management Framework — https://www.nist.gov/itl/ai-risk-management-framework; NIST, "Four Principles of Explainable Artificial Intelligence" — https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence.
- IEEE Computer Society, SWEBOK Guide V4.0 — https://www.computer.org/education/bodies-of-knowledge/software-engineering.
- Schema.org `ClaimReview` — https://schema.org/ClaimReview; Google Fact Check structured data — https://developers.google.com/search/docs/appearance/structured-data/factcheck; Google Search Central documentation.
- Citation standards: APA 7; *OSCOLA*, 4th ed. (2012); *The Bluebook: A Uniform System of Citation*, 21st ed. (2020).
- IFRS Conceptual Framework (qualitative characteristics of useful financial information).
- Plain Language Action and Information Network, *Federal Plain Language Guidelines*.
- World Bank Project Appraisal Document templates and *Reference Guide to Cost-Benefit Analysis*; ESOMAR *Global Market Research* and methodology guidelines.
- Institutional doctoral regulations (accessed 2026-04-26): University of Cambridge, University of Oxford, London School of Economics, Harvard Griffin GSAS and SEAS, Yale GSAS and Registrar, and Princeton Graduate School and Library. Links are in `skills/academic-reporting-standards/references/oxbridge-ivy-examination-conventions.md`.
- Ugandan handbooks: Busitema University research dissemination handbook; Makerere University Directorate of Research and Graduate Training guidelines (2011); Uganda Christian University Research Manual (revised April 2018).
- Kenyan handbooks: Adventist University of Africa Research Handbook; Regional Centre on Groundwater Resources research guide (2019); Kenyatta University School of Hospitality research guide.
- W3C WCAG 2.2; Apple Human Interface Guidelines (Onboarding); GOV.UK Service Manual (user research and prototypes), from the design and product learning record.
- Anthropic, Claude Code plugin manifest reference — https://code.claude.com/docs/en/plugins-reference; OpenAI API models and pricing pages — https://developers.openai.com/api/docs/models (currentness register `docs/source-registers/skills-kaizen-wave2-2026-09.json`).

### Websites and articles

- Bellingcat, *Online Open Source Investigation Toolkit* and the Information Laundromat — https://bellingcat.gitbook.io/toolkit/more/all-tools/the-information-laundromat.
- Dutch OSINT Guy, "OSINT Is A State Of Mind" (2018) — https://medium.com/@Dutchosintguy/osint-as-a-mindset-7d42ad72113d.
- AaronCTI, "My OSINT Blueprint — Methodology and Tools", parts one and two (2024) — https://aaroncti.com/my-osint-blueprint-methodology-and-tools-part-one/ and https://aaroncti.com/my-osint-blueprint-methodology-and-tools-part-two/.
- CQCore, "OSINT Methodology" (2024) — https://www.cqcore.uk/osint-methodology/.
- Sector035, "Week in OSINT #2023-06" — https://sector035.nl/articles/2023-06.
- Neon Maxima, "How I Turned Obsidian Into a Black-Ops Intelligence Hub" (Medium, 2025); Obsidian — https://obsidian.md/.
- NATO StratCom COE, report on information laundering in the Nordic-Baltic region — https://stratcomcoe.org/news/a-new-report-focuses-on-information-laundering-in-the-nordic-baltic-region/133.
- FEVER dataset — https://fever.ai/dataset/fever.html; AVeriTeC dataset — https://fever.ai/dataset/averitec.html.
- "Automated Fact-Checking" survey, *TACL* (2022) — https://aclanthology.org/2022.tacl-1.11.pdf; CREDULE / EVVER — https://arxiv.org/abs/2404.18971; Guo et al., "On Calibration of Modern Neural Networks" — https://arxiv.org/abs/1706.04599.
- Barbara Minto — https://www.barbaraminto.com/; McKinsey Alumni interview, "Barbara Minto: MECE" — https://www.mckinsey.com/alumni/news-and-events/global-news/alumni-news/barbara-minto-mece-i-invented-it-so-i-get-to-say-how-to-pronounce-it.
- University of Manchester, *Academic Phrasebank* (online).
- Cleveland and McGill (1984) "Graphical perception", *Journal of the American Statistical Association* 79(387).
- Cowan (2000) "The Magical Number 4 in Short-term Memory", *Behavioral and Brain Sciences* 24.
- Davis and Morley (2015) "Phrasal intertextuality", *Journal of Second Language Writing* 28.
- DeMarco and Tufts (2014) "The Mechanics of Writing a Policy Brief", *Nursing Outlook* 62(3).
- Dow et al. (2010), parallel prototyping study, *ACM TOCHI* 17(4).
- Flowers (1979) "Madman, Architect, Carpenter, Judge".
- MacEachin (1994) "Tradecraft of Analysis: Challenge and Change in the CIA".
- Wineburg and McGrew (2019) "Lateral reading and the nature of expertise", *Teachers College Record* 121(11).
- Open policy and communication guides: IDRC, *How to Write a Policy Brief*; ODI, *Writing Policy Papers*; Tsai, *Communicating Research for Policy Change*; Anthony, *Communicating Research to Non-Specialist Audiences* (Wellcome Trust); The Op-Ed Project, *How to Write an Op-Ed*; Content Marketing Institute, *Case Study Roadmap*.
- Eleken design and product guides (design-system checklist, onboarding, product-idea validation, dashboards, SaaS launch, AI design workflow, design consistency, UX ideas), from `docs/continuous-improvement/eleken-design-product-learning-2026-08.md`.

## Contributing, author and licence

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and the [skill authoring standard](docs/skill-authoring-standard.md) before you change a skill, and run the checks in [Validation](#validation). The [documentation index](docs/README.md) lists the standards, gates and records.

Author: Peter Bamuhigire, for Chwezi Core Systems. Licence: GNU General Public License, version 3 only (`GPL-3.0-only`); see [`LICENSE`](LICENSE).
