---
name: validation-contract
description: Use when compiling a research publication's evidence inventory, recording applicability of validation categories and assembling reviewer handoffs. For software deployment evidence use the engineering engine; for factual support use source-verification.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Validation Contract

This is the research-context adapter. The portfolio ownership register assigns
the shared validation standard to `chwezi-dev-engine/validation-contract`;
resolve that engine through the active routing table for software release work.
The local evidence templates remain available for research inventories without
requiring an external checkout. They do not certify source truth: run this
engine's `source-verification` checks and retain its unresolved gaps.

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Research deliverable scope, acceptance criteria, and applicable categories | Research owner and specialist skills | Record the missing scope or criteria; do not claim acceptance. |
| Concrete research evidence | Source registers, verification results, research artifacts, and reviewers | Mark the category missing or not applicable with reason; never fabricate evidence. |

## Capability Contract

Inventory review defaults to read-only. Run validators and edit records only within the authorised task. This adapter grants no publication or software release authority.

## Degraded Mode

If a tool, environment, artifact, or reviewer is unavailable, mark that category unassessed and block any claim that depends on it. Produce the partial bundle and recovery action.

## Decision Rules

| Finding | Action | Failure/risk avoided |
|---|---|---|
| Required category has no artifact | Mark research acceptance unresolved | Evidence-free readiness claim |
| Category truly does not apply | Record N/A with same-line reason | Empty compliance theatre |
| Artifact contradicts acceptance criteria | Fail and remediate | Selective reporting |

## Preliminary Evidence Corrections

- Treating a checklist tick as evidence. Fix: link the artifact.
- Filling every category just for symmetry. Fix: map actual risks.
- Using unexplained N/A. Fix: state the reason.
- Writing the inventory after acceptance. Fix: give the reviewer the evidence first.
- Editing evidence during review. Fix: preserve provenance.

## Worked Example

For a research report, link the claim register and source-verification results in the inventory. If a required source is unavailable, preserve that gap and withhold the dependent acceptance claim. Justify categories that do not apply; the inventory does not itself verify a fact.
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Preparing research deliverables for independent acceptance.
- Mapping the seven validation categories to applicable artefacts and reviewers.
- Assembling the local evidence bundle with unresolved gaps and justified exclusions.

## Do Not Use When

- Software deployment, application PR review or SaaS feature release evidence
  belongs to `chwezi-dev-engine/validation-contract`.

- The work is purely local, experimental, or explicitly throwaway with no path to production.
- The skill being authored is a baseline, process, or pure index skill. Those do not declare evidence.
- The task is unrelated to validation planning or shipping readiness.

## Validation Source Requirements

- The research deliverable's scope, acceptance criteria and named reviewer.
- Source-verification and source-evaluation results, including their limitations.
- The retained local references below for category labels and inventory format.

## Validation Method Summary

Map applicable categories to existing research artifacts and their reviewers.
Record missing or contradictory evidence explicitly. Refer software validation
and changes to the shared standard to the canonical engineering owner.

## Quality Standards

Every applicable inventory row links concrete evidence and states its status.
An N/A needs a reason. Separate structural checks from source correctness and
reviewer acceptance; never use completion of a template as proof of either.

## Legacy Validation Warnings

Do not copy the template's software release examples into a research acceptance
claim. Local references are retained formats, not a second canonical standard.

## Initial Validation Deliverables

A research evidence inventory with source-result links, named reviewers,
applicability reasons and unresolved gaps ready for the research owner.

## References

- [references/evidence-categories.md](references/evidence-categories.md): per-category definition, indicative contributing skills, and common artifact shapes.
- [references/declaration-form.md](references/declaration-form.md): the `## Evidence Produced` table form, rules, and worked examples.
- [references/release-evidence-bundle-template.md](references/release-evidence-bundle-template.md): the retained local bundle template for inventory use.
- [references/integration-rollout.md](references/integration-rollout.md): audit trail of edits made to other skills during this skill's rollout.
<!-- dual-compat-end -->

## Shared-standard ownership

The shared category definitions, declaration rules and software risk-tier
requirements are owned by `chwezi-dev-engine/validation-contract`. Do not amend
that shared taxonomy in this adapter. Resolve the canonical owner when changing
the standard or reviewing a software release; if unavailable, mark that
engineering assessment `NOT_ASSESSED` rather than certifying it here.

For a research inventory, use the retained local category reference,
declaration form and bundle template. Record applicability and unresolved
items; the template alone cannot establish source correctness or release
approval. Use `source-verification` for factual support and `source-evaluation`
for source quality, preserving their gaps in the handoff.

## Workflow

1. Confirm research scope, acceptance criteria and reviewer; record unknowns.
2. Map each category to a concrete artifact and named consumer.
3. Review artifact provenance and acceptance evidence without altering it.
4. Block missing or contradictory required evidence.
5. Recover from missing or contradictory evidence through authorised research remediation; refresh the inventory and request review again before claiming acceptance.

## Outputs

| Artifact | Consumer | Acceptance condition |
|---|---|---|
| Research evidence inventory | Research release owner and reviewer | Every applicable category links evidence with its actual review status, or carries justified N/A; source-verification gaps remain visible. |

## Evidence Produced

| Artefact | Format | Acceptance condition |
|---|---|---|
| Research inventory and review handoff | Completed local bundle template with source-verification result links | Scope, reviewer, applicable categories, unresolved source/claim gaps and reviewer decision are traceable; a template tick never substitutes for evidence. |

## Anti-Patterns

- Checklist ticks as evidence. Fix: link artifacts.
- Every category by default. Fix: map risk.
- Unexplained N/A. Fix: give reason.
- Inventory after acceptance. Fix: provide evidence before review.
- Editing evidence during review. Fix: preserve provenance.
