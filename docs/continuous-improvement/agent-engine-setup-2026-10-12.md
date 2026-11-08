# Agent skill-engine setup audit

**Date:** 2026-10-12  
**Scope:** Twelve local skill-engine repositories and their Codex and Claude Code routing  
**Owner:** Local agent-engine maintainer  
**Decision rights:** User owns model, plugin, and global agent configuration

## Aim and baseline

Make all twelve local engines reachable through lightweight Codex skills and the Claude router, keep Claude's native engine plugins enabled, and update local engine checkouts without discarding local work.

At baseline, the Codex central `skill-engines` router covered the twelve engines, but only six engine-specific routers were present. The Claude `skill-engines` router contained an obsolete engineering path. Claude's plugin inventory showed all twelve engine plugins installed and enabled. All twelve engine repositories and the `skills-engine-agents` coordination checkout had an upstream remote.

## Change and measure

Added six Codex router skills for accounting, design, digital research, general engineering, Windows administration, and political writing. Replaced the stale Claude router with a pointer to the maintained global Claude routing table. Repaired the managed Codex policy block with the Digital Research helper; its subsequent check passed.

Fetched and ran `git pull --ff-only` on all twelve engines plus `skills-engine-agents`. All reported `Already up to date`. Existing local Claude plugin manifest edits and the political engine's untracked `.claude-plugin` directory were preserved.

| Measure | Result |
|---|---|
| Engine-specific Codex routers | 12 of 12 |
| Claude engine plugins installed and enabled | 12 of 12 |
| Claude plugin manifests validated | 12 of 12 |
| Repository checkouts at upstream head | 13 of 13, including coordination package |
| Codex managed policy check | PASS |
| Local changes discarded | 0 |

## Model-currentness review

**Review date:** 2026-10-12. The OpenAI runtime catalogue on this device lists `gpt-6.1-sol`, `gpt-6-luna`, and `gpt-6-astra`; all three list high reasoning support. The current official model catalogue and release notes list GPT-6.1 Sol and describe its rollout to ChatGPT Work and Codex. Sources: [OpenAI model catalogue](https://developers.openai.com/api/docs/models), [OpenAI model-selection guide](https://developers.openai.com/api/docs/guides/model-selection), [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes), and local `codex debug models` output.

The new model is a review trigger, not evidence to replace the user's policy. Provider task-fit descriptions are not a controlled comparison on this workload. Comparative quality, latency, Codex account cost, and the running root session's model identity are **NOT_ASSESSED**. Published API rates do not establish Codex subscription cost. **Decision:** retain the configured Luna/high default and Astra's user-selected exception; do not promote GPT-6.1 Sol without representative evidence and user authority. Reassess promptly with task-fit evidence; do not mark model currentness passed.

## PDSA and recovery

- **Plan:** Fill the missing engine-specific Codex routes and correct Claude's stale pointer while preserving the central routers and plugin setup.
- **Do:** Add six small Codex routing skills and update the Claude router.
- **Study:** Confirmed twelve engine-specific Codex routes, twelve enabled Claude plugins, thirteen up-to-date checkouts, and a passing Codex policy check.
- **Act:** Keep repositories as source of truth and use their live routers and skills. On a failed route or plugin check, restore the relevant router from the source table and re-run the checks; do not remove plugin or repository data as a repair step.

**Adoption evidence:** filesystem inventory under `C:\Users\BIRDC\.agents\skills`, Claude `plugin list`, repository `git status`/pull results, and the policy helper's PASS output, all checked 2026-10-12.  
**Re-audit:** after the next engine update or router change, and by 2027-01-12 at the latest. The model comparison is due sooner because GPT-6.1 Sol is a relevant release.
