# Documentation index

This folder holds the engine's standards, gates, registers and improvement records. The router is [`../SKILL.md`](../SKILL.md); the operating rules for agents are in [`../AGENTS.md`](../AGENTS.md); the front door is [`../README.md`](../README.md): what the engine is, a task-to-skill table, a summary of the skill groups, how to install and validate it, and what the October 2026 kaizen cycles improved.

## Working documents

| Document | What it covers |
|---|---|
| [`skill-authoring-standard.md`](skill-authoring-standard.md) | How to add or change a skill, and the mechanical gates a change must pass |
| [`pathing-model.md`](pathing-model.md), [`pathing-model-engine-vs-projects.md`](pathing-model-engine-vs-projects.md) | Where engine files, examples and active project workspaces live |
| [`output-manifests.md`](output-manifests.md), [`release-pack-spec.md`](release-pack-spec.md) | Assembly of a deliverable and the evidence pack that `python3 -m engine pack` builds |
| [`migration-notes.md`](migration-notes.md) | Bringing a pre-kernel project workspace under the project kernel |
| [`osint-tool-index.md`](osint-tool-index.md) | Ingesting public OSINT toolkit pages into a project registry |
| [`agent-runtime-safety.md`](agent-runtime-safety.md), [`approval-enforcement.md`](approval-enforcement.md), [`approval-adapter.json`](approval-adapter.json) | Runner-neutral safety contract and the approval adapter |
| [`control-plane-adoption.md`](control-plane-adoption.md) | How the engine exposes itself to the shared control plane |
| [`ai-prompting/`](ai-prompting/) | The domain prompt contract for ready-to-paste research prompts |
| [`world-class-exemplars/`](world-class-exemplars/) | The shared running example used across skills |
| [`skill-catalogue.md`](skill-catalogue.md) | All 59 skills in 11 workflow groups, one line and one link each; the README summarises the groups |
| [`references.md`](references.md) | The books, standards, repositories and articles cited across the engine; the README links here |

## Gates and registers

| Folder | What it holds |
|---|---|
| [`quality-gates/`](quality-gates/) | Release-blocking gates and the anti-slop governance text |
| [`source-registers/`](source-registers/) | The research standards register and the dated, machine-checked currentness registers (`validate_source_currency.py --registers-dir docs/source-registers`) |
| [`continuous-improvement/`](continuous-improvement/) | The Portfolio Kaizen Standard, the currentness gate, model-policy reviews and earlier kaizen waves. The standard and the currentness gate are protected doctrine and change only on the maintainer's decision; the proposed wording is recorded in the pass 2 `06-next-cycle.md` |

## Improvement records

Each record under [`kaizen/`](kaizen/) holds the same seven files: `00-scope-and-evidence.md`, `01-baseline-scorecard.md`, `02-improvement-backlog.md`, `03-experiment-log.md`, `04-validation-record.md`, `05-final-report.md` and `06-next-cycle.md`. The README record is the one exception: a single file, because it was a scoped micro-cycle.

| Record | Date | Notes |
|---|---|---|
| [`kaizen/2026-09-23-research-scraping/`](kaizen/2026-09-23-research-scraping/) | 23 September 2026 | The `ResearchScraper` and its command line |
| [`kaizen/2026-10-engine-kaizen/`](kaizen/2026-10-engine-kaizen/) | 29 October 2026 | First October cycle; final raw score 58.2 |
| [`kaizen/2026-10-engine-kaizen-pass-2/`](kaizen/2026-10-engine-kaizen-pass-2/) | 31 October 2026 | Second October cycle; raw 59.5, capped 59.5; next re-audit 2026-11-27 |
| [`kaizen/2026-10-readme-kaizen/`](kaizen/2026-10-readme-kaizen/readme-kaizen-record.md) | 31 October 2026 | README reading-quality micro-cycle; no score published |

Older audits and plans, kept as history:

- [`audits/`](audits/): the September 2026 kaizen reviews and the `2026-09-29-m10-reaudit/` set.
- [`engine-upgrade-july-2026/`](engine-upgrade-july-2026/): the July 2026 upgrade audit and completion reports.
- [`analysis/initial-evaluation/`](analysis/initial-evaluation/): the April 2026 self-evaluation.
- [`plans/`](plans/) and [`superpowers/`](superpowers/): design and implementation plans and specifications.
