# Reviewer attribution and source-register path checks

Date: 2026-11-07. Kaizen action: R1.1; related source-gate regression repair.

The source verifier called every recorded support review a human review,
although its input did not identify reviewer kind. It now records `human`,
`ai`, or `unknown`. Omitted legacy kinds become `unknown`; malformed explicit
kinds fail validation. A declared human kind is attribution supplied by the
caller, not identity verification or release approval. All support states
remain non-certifying, with the same release block as before.

The manifest template and tools documentation explain this boundary.
Historical verification reports remain historical; they have not been
rewritten to invent reviewer identities.

The new regression tests failed against the preceding implementation and pass
after the repair. They cover all support states across human, AI, unknown and
omitted kinds, report serialisation, malformed kinds and release readiness.

The wider unit suite exposed an existing Windows failure: `/tmp/new.json`
was not rejected as an invalid relative successor path. The currency gate now
rejects rooted paths, drive-qualified paths, alternate data stream syntax and
parent traversal independently of the host path flavour, and checks resolved
containment. The existing unsafe-path test also covers Windows spellings.

Validation after the initial repair on Windows: all 96 engine unit tests pass; all 59 active skills pass
the skill contract gate. The aggregate validator stops at the existing file
count gate (6,255 full-checkout entries versus a 5,000 ceiling; its separate
package-oriented count is 3,054). No ceiling was relaxed. Aggregate acceptance
is therefore not established by the passing focused checks.

Recovery: revert the changed verifier, currency checker, tests, template and
skill together to the preceding revision. That restores the documented
attribution and path-validation defects. No source content, credentials,
model configuration or publication state was changed.

## Archive profiles and guidance boundary

R1.2 adds an explicit `audit-only` default and a `release` profile to the tool.
Audit-only cannot grant readiness. Release cannot omit archive lookup and
requires all structural results to pass. Supplied archive URLs are candidates;
lookup must confirm a parseable capture date and the original URL. The helper
still does not compare archived content with the claim or grant publication
authority. Unavailable lookups and unsupported semantic claims stay blocked.

The expanded engine unit suite passed 99 tests. Independent review then found
that a non-empty malformed capture timestamp could pass; the repair now parses
compact timestamps or ISO dates. All 14 focused source-verifier tests pass
after that correction, including malformed and impossible-date cases.

The research skill-text candidate was restored to its preceding version and
kept outside runtime guidance: the research replay gate has no historical
research-product replay for this candidate. These deterministic tool repairs
follow the engineering execution path; they are not evidence of a general
research-guidance improvement or a passed research replay gate.
