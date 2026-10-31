# Single-claim lookup

Use this when the answer is one claim, or a handful: a rate, a date, a version, a
status, a count. `research-orchestration`, `evidence-claim-graph` and
`critical-reasoning-and-argument` each exclude this kind of question, so it is
handled here. If the question needs several jurisdictions, a time series or a
judgement, hand it to `research-orchestration`.

## 1. Check the premise before searching

A question carries claims of its own. Write them down before any search.

1. List every factual presupposition: words such as "still", "no longer", "why has",
   "since", "after", and any figure, date or name the asker supplies.
2. Pick the load-bearing ones: the presuppositions that make the question pointless
   if they are false.
3. Test each against a current source before shaping an answer.
4. If one is false, say so in the first sentence, name the source, and give the
   closest question that can be answered. Do not answer the question as asked and
   mention the problem afterwards.
5. If one cannot be tested, answer only with that premise labelled `unverified`.

Correcting a premise from memory is not a check. A false premise stated with
confidence and no source is the same failure as a fabricated statistic.

## 2. Classify the claim and choose the sources

Classify the claim with `freshness-and-uncertainty.md`. A time-sensitive claim
needs a current authoritative source. For a rule, rate or status, take the scheme
or regulator's own statement (tier 1) and one independent dated official source
(tier 2 or better), and read the primary text where it exists. A vendor, news or
blog statement can locate a source but cannot be the support.

## 3. Record the claim

One row is enough. Keep access date, publication date and review date apart.

| Field | Content |
|---|---|
| Claim | The answer in one sentence, with its scope (place, period, who it applies to) |
| Sources | Each with tier and locator (page, section, table) |
| Dates | Publication or revision date of each source, or `undated`; access date; review date |
| Verification | What was compared with what, and what agreed |
| Support state | `supported`, `partial`, `unverified` or `NOT_ASSESSED`, per sub-claim |
| Open limits | What was not read, not checked or not available |

Label an inference as `(inference)`, for example a figure worked out from two
sections rather than stated in one.

## 4. Stop rules

- Answer when two independent current sources agree and the primary text, where read, does not contradict them.
- Return a gap, not an answer, when the only support is one source, an unreadable document or a stale text. Say what would close it.
- An archive snapshot, where the verification gate requires one, is recorded as captured or `NOT_ASSESSED`. Absence is never silently dropped.

## Worked example: a question built on a false premise

Question put to the engine on 2026-10-31: "Why does Kenya's NSSF still cap employee
contributions at a flat KES 200 a month in 2026?"

Presuppositions: (a) the cap is flat, (b) it is KES 200, (c) it still applies in
2026. All three are load-bearing, so the check comes first.

| Field | Content |
|---|---|
| Claim | The premise is false. The scheme's Year 4 notice, effective February 2026, sets employee and employer contributions at 6% of pensionable earnings in two tiers. Tier 1 is on a lower earnings limit of KES 9,000 (maximum KES 540 each). Tier 2 is on earnings up to an upper limit of KES 108,000 (maximum KES 5,940 each). The maximum employee contribution is KES 6,480 a month; employee and employer together, KES 12,960. Employers remit by the 9th of the following month. |
| Sources | NSSF Kenya, "Notice to Employers, Year 4 (2026) NSSF Contribution Rates", signed by the Managing Trustee and CEO and citing the Third Schedule of the NSSF Act (tier 1, table of rates). Payroll and law-firm summaries agree on every limit (tier 3 and 5, corroboration only). |
| Dates | Notice undated on its face; it refers to a 6 February 2026 annual general meeting, so it post-dates that. Embedded file metadata shows April 2025 and is treated as template reuse. Accessed 2026-10-31. |
| Verification | Limits, rates and maxima in the notice were compared line by line with three independent summaries; no disagreement. The notice does not mention a flat KES 200 figure. |
| Support state | `supported` for the February 2026 rates. The origin of the KES 200 figure was not checked and is not asserted. |
| Open limits | The scheme's home page carries a 4 June 2026 headline, "Clarification on the Status of NSSF Contributions", that was not read. Until it is read, the answer stands for the February 2026 notice only. No archive snapshot: `NOT_ASSESSED`. |

Answer given: the premise is wrong, here is the current structure, and a better
question is how the phased increase under the Third Schedule works or where the
flat figure is still quoted.
