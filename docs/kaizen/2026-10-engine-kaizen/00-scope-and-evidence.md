# Digital Research Engine — observation notes

Date: 2026-10-29 (Africa/Kampala)
Checkout: `digital-research-engine`, HEAD `444b7ce`
Mode: read-only preflight and observation; no repository files changed.

## Router and skills read

Read `AGENTS.md`, `rules/common/core.md`, `skills/source-evaluation/SKILL.md`,
`skills/source-evaluation/references/evidence-discipline.md`,
`skills/source-verification/SKILL.md`, and
`skills/research-orchestration/SKILL.md`. The router names source evaluation
and verification as universal routes, with specialist skills layered by task.

| Task | Routes selected for this observation | Assessment |
|---|---|---|
| Current Uganda NSSF employer rate | `source-evaluation`; `source-verification`; currentness gate. `online-legal-research` is a reasonable additional route because this is a statutory compliance claim. | Correct core routes; legal route is not explicit for current-rate questions in the high-level sequence. The page supports the ordinary rate and remit timing, with category/exemption caveats. |
| Broad Uganda/Kenya school management software market brief | `research-orchestration`; `quantitative-modelling`; `source-evaluation`; `source-verification`; `evidence-claim-graph`; `analytic-tradecraft`. | Appropriate routes. Preserve the boundary between government education MIS and privately purchased school administration software; the available evidence does not establish the latter's market size. |
| False-premise question about Uganda EMIS | `source-evaluation`; `source-verification`; `critical-reasoning-and-argument`. | The premise is refuted by a current official statistical abstract, which distinguishes the legacy system from the redeveloped EMIS. |

## Observation 1 — current-state answer

**Request:** “What is the current Uganda NSSF employer contribution rate?”

**Observed answer:** The employer contribution is 10% of an eligible employee's
gross monthly wage; the employee share is 5%, for a 15% total contribution.
The employer remits monthly by the 15th of the following month. The official
NSSF membership page states the split and timing ([NSSF Membership](https://www.nssfug.org/about-us/membership/), accessed 2026-10-29); Uganda's Ministry of Finance business portal independently states the same rates and provides the statutory basis ([NSSF Employer Registration](https://doingbusiness.finance.go.ug/licensing/nssf-employer-registration), reviewed there 2026-06-15 and accessed 2026-10-29).

**Evidence record:** NSSF is a first-party scheme source (tier 1 under the
engine's ladder); the Ministry portal is an official authoritative secondary
source (tier 2). Both pages were opened and checked on 2026-10-29. Rate, base,
payment interval, and deadline match. The Ministry portal names the National
Social Security Fund Act, Cap. 230 and the 2022 amendment. No archive snapshot
was captured, although source-verification's universal ship gate calls for
one; archival verification is therefore **NOT_ASSESSED**. This is a sourced
observation, not an independent legal opinion.

## Observation 2 — broad market brief (evidence-limited)

**Request:** “Assess the school management software market in Uganda and
Kenya.”

**Scope warning:** Government EMIS/NEMIS platforms collect and manage sector or
school/learner information; that evidence does not by itself measure the
commercial market for school-purchased administration software.

**Evidence points:**

- Uganda's 2025 Ministry of Education statistical abstract says the legacy
  EMIS was discontinued and describes a redeveloped, web-based system rolled
  out from November 2022 ([Uganda Education Statistical Abstract 2025, pp.
  3–4](https://www.education.go.ug/wp-content/uploads/2026/01/UGANDAS-EDUCATION-STATISTICAL-ABSTRACT_2025.pdf),
  accessed 2026-10-29). It also reports school response data, but this is
  government-system coverage, not paid software adoption.
- Kenya's Ministry describes NEMIS as a government system for collecting
  institution data and tracking learner and teacher information ([Kenya
  Ministry of Education: NEMIS](https://education.go.ke/nemis), accessed
  2026-10-29). A May 2025 ministry press release announced a team to develop
  KEMIS and a planned pilot; the current KEMIS rollout state is **NOT_ASSESSED**
  ([Ministry press release](https://www.education.go.ke/sites/default/files/2025-06/Students%20Master%20Register%20team%20unveiled%20.pdf),
  accessed 2026-10-29).
- Acumen's Kenya education research reports that 23% of surveyed respondents
  used a school management system; its study describes an online/SMS survey of
  more than 1,500 school owners, teachers and parents and 22 stakeholder
  interviews ([Kenya Education Market Research Summary, pp. 2–7](https://acumen.org/wp-content/uploads/2024/03/Acumen-East-Africa-Education-Research-Kenya.pdf),
  accessed 2026-10-29). This is useful market-oriented secondary evidence, but
  it is Kenya-only and its accessible methods excerpt does not establish a
  representative national sample. Its addressable-market tables concern
  supplemental learning products/services, not school administration SaaS;
  those totals must not be relabelled as this software market.
- A 2025 Uganda news report citing ministry and HISP Uganda sources describes
  private-school gaps in submitting data to the national EMIS ([The Observer,
  26 March 2025](https://observer.ug/education/two-years-later-private-schools-lag-in-information-system-compliance/),
  accessed 2026-10-29). This is evidence about reporting/compliance, not proof
  of willingness to buy a commercial platform.

**Evidence-claim graph (compact):**

| Claim | Source(s) | Support state / limit |
|---|---|---|
| Uganda operates a redeveloped official EMIS | Uganda Ministry statistical abstract | Supported for government system; does not establish private SaaS use. |
| Kenya operates NEMIS and announced KEMIS development | Kenya Ministry NEMIS page and May 2025 release | Supported for NEMIS description and the historical announcement; current KEMIS operational status is **NOT_ASSESSED**. |
| Some Kenyan school owners/respondents report use of school management systems | Acumen report | Supported within that survey; sampling representativeness and current prevalence are not established here. |
| Commercial school-administration software has a specific Uganda/Kenya TAM/SAM | no source found in this bounded search | **Gap**; no defensible size estimate. |
| Government MIS rollout implies commercial software demand | none | Unsupported; do not infer. |

**Synthesis:** the bounded source set establishes government MIS activity in
both countries and one Kenya survey reporting school-management-system use.
It does not support a combined market size, comparable adoption rates, vendor
share, current price range, or Uganda commercial penetration. Those remain
gaps. An investment-grade brief would need fresh country-separated school
counts, paid-vendor/customer evidence, pricing, and a transparent sizing
method. **(synthesis)**

**Limitations:** this is a bounded web-search sample, not a comprehensive
market scan. The Acumen survey is older than the access date; its publication
date and sampling frame were not verified from the opened extract. One indexed
Kenyan academic item returned HTTP 404 and was not used. Archive snapshots,
vendor pricing, customer interviews, public/private segmentation, and an
independent Uganda commercial-use estimate were not assessed. There is no
contradictory like-for-like market-size estimate in this evidence set; that is
an evidence gap, not evidence of no market.

## Observation 3 — false premise

**Request:** “Uganda's education EMIS launched in 1999 and is still the old
unsupported system in 2026. Why has the government not replaced it?”

**Observed answer:** The premise combines a true historical start date with a
false current-state assumption. The Ministry's 2025 statistical abstract says
the old EMIS/Annual School Census approach was discontinued in 2017 and
describes a redeveloped EMIS, rolled out from November 2022. Therefore the
question should be reframed to ask about the current system's coverage,
performance, or remaining data-quality gaps rather than why it has not been
replaced ([Uganda Education Statistical Abstract 2025, pp. 3–4](https://www.education.go.ug/wp-content/uploads/2026/01/UGANDAS-EDUCATION-STATISTICAL-ABSTRACT_2025.pdf),
accessed 2026-10-29). **(inference)** The redeveloped system's quality and
completeness require separate evidence; the existence of the system does not
prove complete operation.

## Defects and guidance gaps observed

| Severity | Evidence | Finding |
|---|---|---|
| Major | `skills/source-verification/SKILL.md`, universal ship gate | Requires archive snapshots for every URL. The live observation used accessible official sources but did not capture archive snapshots; the skill leaves no explicit low-risk/current-access exception or “archive unavailable” accepted status. Keep archive status **NOT_ASSESSED** rather than imply verification is complete. |
| Major | `docs/source-registers/research-standards-register.md:3–5` | Register says last verified 2026-07-08 and next review 2026-10-08; as-of 2026-10-29 it is overdue. |
| Major | `docs/source-registers/research-standards-register.md:11–13`; `skills/academic-reporting-standards/SKILL.md:90` | Register omits GRADE, Cochrane edition, ICD 206 and RFC 9309. `academic-reporting-standards/SKILL.md:90` still says TOP has “8 modular standards × 3 implementation levels”; current COS claim requires direct refresh before retaining it. |
| Minor | `skills/academic-reporting-standards/SKILL.md:142–148` | Several “Tier 1” references are canonical homepages, not a claim-level source record with publication/version date, access date, review date, scope, and support state. |
| Minor | `skills/quantitative-modelling/SKILL.md:43–53` at pre-change HEAD `444b7ce` | Baseline market task exposed a need for a clear guard against treating national education MIS coverage, school counts, or adjacent EdTech TAM as paid administrative-software market size. The baseline file required explicit units, time periods, and populations and warned about mixing populations or periods, but had no product/buyer boundary example. |

## Repository preconditions

- At observation start, `git status --short` was clean and `git log --oneline
  -20` showed pre-change HEAD `444b7ce`.
- Repository edits began after the root agent released the accounting-cycle
  hold; implementation commits and experiment evidence are in
  `03-experiment-log.md`.
- The full outputs for all three task observations are retained above in this
  in-repository evidence record.
