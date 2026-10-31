# Next cycle: open findings, proposed edits, handoff

Re-audit date: **2026-11-27** (a Friday), earlier than the 2026-11-30 used in the
29 October plan. Reason: the register gate now fails `validate_engine.py` and CI
from 2026-11-30 unless the four OpenAI platform records dated 29 October (review
2026-11-29) are re-read first, and from 2026-12-01 for the two dated 31 October.
Owner: Peter Bamuhigire. Raw score now 59.5, capped 59.5; the plan still targets 95.

## Decisions needed from Peter

| Decision | Why it is yours | Default if unanswered |
|---|---|---|
| Redact or keep the two provenance lines at `docs/continuous-improvement/english-collocations-and-lexical-precision-2026-09-02.md:146-147` (a personal Windows path and filenames carrying unofficial book-sharing markers) | User-authored record; possible legal and privacy exposure; no book content is stored | Left as found; flagged in every cycle |
| Archive workflow for live-source verification: authorise one, or approve an "archive unavailable" branch | The universal archive gate is doctrine | Gate unchanged; every live-web answer carries archive `NOT_ASSESSED` |
| Bind or drop the `political` target in `tests/fixtures/machine-error-gate-baseline.json:31` (`political-essay-skills`; no checkout under the engines directory) | Names an engine outside the public catalogue | Full gate run fails on that one target; a run with `--engine` for the 11 bound engines passes |
| Apply the proposed text for the two protected documents below | Protected this cycle | Both keep a Windows path that exists on no other host |
| Retire or redirect about 14 imported engineering and documentation skills (three near-duplicates of other engines) | Changes the 59-skill count rule in `AGENTS.md` | Open since September |

## Proposed text for the protected documents (not applied)

**`docs/continuous-improvement/portfolio-kaizen-standard-2026-08.md`, line 76.** Replace
"All engines may reach `<drive>:\<web-root>\digital-research-engine`." with:
"All engines reach the Digital Research Engine through the active engine-routing table, or through the `digital-research-skills` entry in `chwezi-engine-agents/catalog/engines.yaml`."

**`docs/continuous-improvement/kaizen-currentness-gate.md`, lines 51-52.** Replace
"For this engine, the canonical checkout is `<drive>:\<web-root>\digital-research-engine`;" with:
"This engine is resolved through the active engine-routing table;" and keep the rest of the sentence.

**Same file, line 49 (evidence record).** Add after the field list:
"In the engine's machine-checked registers the fields are `sources[].id` (source_id), `accessed` (access date), `verified_at` (verification date), `review_after` (review date), `freshness_class`, `scope`, one of `publication_date`, `revision_date` or `as_of`, and, per claim, `claims[].id`, `source_ids`, `requires_currentness`. Support status, limitation and owner are recorded by convention and are not validated. `scripts/validate_source_currency.py --registers-dir docs/source-registers` checks every register; a historical register may name a validated successor in `superseded_by`."

**Same file, new line under "Release gates".** "Run the register gate as of today before release; an overdue record in any non-superseded register blocks release."

## Open findings

| Finding | Status | Evidence needed |
|---|---|---|
| Archive snapshots for live-source verification | `NOT_ASSESSED` | The decision above, then one representative manifest tested end to end. |
| ICD 206 content; latest ICD 203 amendment date; RFC 9309 errata | `NOT_ASSESSED` | A text version of the two directives or an approved OCR tool; the RFC Editor errata page read directly. |
| Kenya NSSF "Clarification on the Status of NSSF Contributions" (4 June 2026 headline) unread; Uganda sections 11 and 12 after Act 1 of 2022 and General Notice 2917 of 2024 unread | Open | Read both; the worked examples in `skills/source-evaluation/references/single-claim-lookup.md` name them as open limits and should be updated if either changes an answer. |
| Market size for paid school-administration software in Uganda and Kenya | Gap | Product-matched customer, price and paid-adoption evidence; the denominator rule is in place, the numerator is not. |
| Nine skills with generated "Evidence Notes 1 and 2" headings | Open | Fold each into the contract section it duplicates, one skill at a time, checking the contract validator after each. `quantitative-modelling` holds a table there that the contract reads as its evidence section. |
| 55 of 59 skill worked examples under 60 words; 56 of 59 skills without three positives and two owned negatives | Open | One real, checked artefact per skill per cycle; fixtures only where a task shows a route defect. |
| Seven relative links that leave the repository, in `docs/continuous-improvement/ai-slop-responsibility-assessment-2026-09-11.md:7`, `kaizen-wave-1-2026-08-11.md:14,20,36` and `kaizen-wave-2-2026-08-11.md:30,31,58` | Open (dated records) | Decide whether to edit history. The scanner reports them when pointed at those files by path. |
| Lexical collision between `online-legal-research` and `due-diligence` on words such as "litigation" | Noted | One candidate fixture ranked the legal skill first; a description edit or an owned negative, whichever evidence supports. |
| Live-agent routing, Tier 3 behaviour, model comparison | `NOT_ASSESSED` | Authorised paid evaluation and an independent protocol. |
| Remote CI, marketplace readiness, installed-plugin discovery this pass | `NOT_ASSESSED` | Portfolio release cycle. |
| Independent human review of the registers | `NOT_ASSESSED` | A second reviewer for claim scope, support and dates. |

## Cross-engine mismatches (for each engine's cycle or the portfolio cycle)

None of these files was edited.

| Mismatch | Engine-side file and line | This engine's side |
|---|---|---|
| Router hard-codes `<drive>:\<web-root>\digital-research-engine` instead of resolving through the catalogue | `chwezi-accounting-doctrine/AGENTS.md:56`; `design-system-skills/AGENTS.md:66`; `srs-skills/AGENTS.md:47`; `social-media-skills/AGENTS.md:47, 232`; `website-skills/AGENTS.md:61, 371`; the dev engine's `AGENTS.md:40` (`skills-web-dev` on this machine) | Correct in `linux-skills/AGENTS.md:46, 175`, `windows-admin-engine-skills/AGENTS.md:58, 166`, `proposal-skills/AGENTS.md:47`. This checkout's directory is `chwezi-research-engine` while the catalogue path is `digital-research-engine`. |
| Source-register schema differs; this engine's validator cannot check a handed-off register | `windows-admin-engine-skills/engine/source-register.yaml` (308 findings: `status` and `accessed` only); `website-skills/docs/source-registers/performance-currentness-2026-09-23.json` (20), `performance-currentness-2026-09-25.json` (22), `search-ai-currentness-2026-09-05.json` (41); one finding each in `social-media-skills/docs/source-registers/source-register.json`, `business-plan-skills/docs/source-registers/country-market-data.json`, `proposal-skills/docs/source-registers/2026-10-currentness.json` | `scripts/validate_source_currency.py:21` (`REQUIRED`) and `docs/continuous-improvement/kaizen-currentness-gate.md:49` name the fields differently; the mapping is in the proposed text above. Read-only runs with `--as-of 2026-10-31`. |
| Catalogue validators and released commit for this engine are stale | `chwezi-engine-agents/catalog/engines.yaml:80-90`: `released_commit: "d4a613d"` (an ancestor of `main`, not its tip); validators omit `validate_source_currency.py --registers-dir docs/source-registers` and `validate_machine_error_gate.py` | `AGENTS.md` and `scripts/validate_engine.py` now run the register gate; the machine-error gate needs `--engines-root` or `CHWEZI_ENGINES_ROOT`. |
| Oracle that this repository cannot test | `chwezi-engine-agents/evals/cases/055-route-release-evidence-mirror.yaml` (expects the dev engine's `validation-contract` first) | The September audit measured `skills/validation-contract` as a cosine-1.0 near-duplicate of the dev skill; the retire-or-redirect decision above settles it. |
| Windows register points at a repository name, not a path | `windows-admin-engine-skills/engine/source-register.yaml` (`portfolio_gate`: `digital-research-skills/docs/continuous-improvement/kaizen-currentness-gate.md`) | The gate lives at that path inside this repository; the prefix is the GitHub name, not a checkout directory. |
| Social-media identifier mismatch from 29 October | `social-media-skills/skills/ai-marketing/anti-ai-slop/SKILL.md` | No longer reproduces: the identifier check passes at that engine's current HEAD. Semantic agreement `NOT_ASSESSED`. |

## One small experiment for next time

Put the two worked records in `single-claim-lookup.md` into machine-readable form
as rows in a scratch register and run `scripts/validate_source_currency.py` on
them. If the reference's record table maps onto the validator's fields without
loss, add the fields to the reference; if it does not, the gap is the field-name
mismatch recorded above and the fix belongs in the gate text, not in the skill. No
paid call, no new dependency, one fixture file.

## Re-audit

Re-audit on **2026-11-27**: re-read the six platform records first, rerun every
registered validator, and re-measure the ten dimensions against this report. The
raw score is 59.5 against a target of 95; the capped figure is not a substitute
for the open evidence above.
