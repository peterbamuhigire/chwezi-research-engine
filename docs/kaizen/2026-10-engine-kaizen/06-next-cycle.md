# Next cycle — open research-engine findings

Review date: 2026-11-30

Owner: Peter Bamuhigire

## Open findings

| Finding | Status | Required evidence / boundary |
|---|---|---|
| Archive snapshots for live-source verification | NOT_ASSESSED | Decide an authorised archive workflow or document a safe unavailable-source branch without weakening the universal release gate; test a representative manifest. |
| Independent semantic review of the new standards register | NOT_ASSESSED | Have a second reviewer check claim scope, source support, dates, and each disposition; the metadata validator alone cannot do this. |
| Cross-engine machine-error handoff | NOT_ASSESSED | Run the research handoff against actual current sibling checkouts and compare the exact invocation, source-register fields, and handoff expectations; the local check currently cannot read the configured target files below. |
| Market size for paid school-administration software in Uganda and Kenya | Gap | Obtain product-matched customer, price, paid-adoption, and geography evidence; do not reuse government EMIS coverage or supplemental-learning TAM as a proxy. |
| Fixture coverage beyond the quantitative-modelling route | Open | Expand only when a task observation shows a route defect; current cycle makes no claim that 1/59 is broad coverage. |
| Tier-3 behaviour, live model comparison, and user outcomes | NOT_ASSESSED | Requires authorised paid evaluation and a defined independent protocol; no model policy change is proposed here. |
| Remote CI and public marketplace readiness | NOT_ASSESSED | Confirm in the portfolio release cycle; local validators and offline plugin loading do not substitute for remote CI or marketplace review. |

The failed local `validate_machine_error_gate.py` check reads the shared
editorial gate at
[`docs/continuous-improvement/machine-errors-editorial-gate-2026-09-03.md`](../../continuous-improvement/machine-errors-editorial-gate-2026-09-03.md)
and checks the following configured counterparts from
[`tests/fixtures/machine-error-gate-baseline.json`](../../../tests/fixtures/machine-error-gate-baseline.json).
The exact source-side research instructions are in
[`skills/anti-ai-slop/SKILL.md`](../../../skills/anti-ai-slop/SKILL.md) and
[`skills/ai-slop-audit/SKILL.md`](../../../skills/ai-slop-audit/SKILL.md).
The gate reported the target files missing from this host, so their content
and handoff agreement are **NOT_ASSESSED**; the table records configured
targets, not verified cross-engine mismatches.

| Engine target | Configured counterpart file | Status |
|---|---|---|
| SRS | `chwezi-sdlc-documentation/09-governance-compliance/28-anti-ai-slop/SKILL.md` | NOT_ASSESSED; target unavailable |
| Business plan | `business-plan-skills/skills/meta-utility/anti-ai-slop/SKILL.md` | NOT_ASSESSED; target unavailable |
| Website copy | `website-skills/skills/content-copy/premium-commercial-writing/references/genuine-writing-and-ai-slop-gate.md` | NOT_ASSESSED; target unavailable |
| Social media | `social-media-skills/skills/ai-marketing/anti-ai-slop/SKILL.md` | NOT_ASSESSED; target unavailable |
| Linux | `linux-skills/AGENTS.md` | NOT_ASSESSED; target unavailable |
| Proposal | `proposal-skills/skills/meta/anti-ai-slop/SKILL.md` | NOT_ASSESSED; target unavailable |
| Engineering | `chwezi-dev-engine/skills/sdlc-meta/anti-ai-slop/SKILL.md` | NOT_ASSESSED; target unavailable |
| Accounting | `chwezi-accounting-doctrine/governance/anti-slop-finance-output.md` | NOT_ASSESSED; target unavailable |
| Design | `chwezi-design-engine/doctrine/references/ai-slop-taxonomy.md` | NOT_ASSESSED; target unavailable |
| Digital research | `digital-research-engine/skills/anti-ai-slop/SKILL.md` | NOT_ASSESSED; target unavailable to this validator invocation |
| Windows | `windows-admin-engine-skills/AGENTS.md` | NOT_ASSESSED; target unavailable |
| Political essay | `political-essay-skills/skills/political-essay-doctrine/SKILL.md` | NOT_ASSESSED; target unavailable |

## Small next experiment

Run one authorised source-verification exercise using a read-only public
standard page and an approved archive method. Record the live locator, archive
locator, access/review dates, support state, and failure handling in a single
fixture. Keep the universal archive requirement unchanged unless its owner
approves a doctrine update based on that evidence.

Re-audit on **2026-11-30**. The raw score remains below the Standard target of
95/100; the capped report score is not a substitute for the open evidence
items above.
