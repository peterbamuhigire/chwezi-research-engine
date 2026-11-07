# `tools/` - runtime utilities for the engine

These Python modules implement the operations described by the skills. The
layout below is filesystem-backed; planned modules are not advertised here.

## Layout

```
tools/
|-- academic/             academic prose and citation helpers
|-- data/                 data-quality and tidy-data helpers
|-- datasets/             dataset search, registry, retrieval, and analysis
|-- dd/                   due-diligence helpers
|-- google/               search and stakeholder-recon helpers
|-- pi/                   licensed private-investigation records
|-- reports/              citation-density reporting
|-- sanctions/            sanctions-list screening helpers
|-- scraping/             HTTP, robots, throttling, retry, caching, and extraction
|   `-- extractors/       feed, JSON-LD, OpenGraph, and HTML extraction
|-- verification/         archive, provenance, EXIF, and source verification
`-- osint_tool_index.py   candidate OSINT-tool index support
```

### Implemented module groups

- `scraping/`: `http_client.py`, `throttle.py`, `robots.py`, `retry.py`,
  `cache.py`, `pagination.py`, `cleaning.py`, `headless.py`, and the
  `extractors/` modules.
- `verification/`: `archive.py`, `exif.py`, `provenance.py`, and
  `source_verifier.py`.
  The verifier defaults to `--profile audit-only` and never declares release
  readiness in that profile. `--profile release` requires archive checks and
  all structural results to pass; it cannot certify semantic support or approve
  publication. An unconfirmed supplied archive URL remains a gap.
  New manifests record `support_review.reviewer_kind` as `human`, `ai` or
  `unknown`; omitted legacy kinds remain unknown, and explicit malformed kinds
  fail. Attribution is caller-supplied, not verified human identity. The CLI
  returns 2 for non-ready reports, including audit-only results. The aggregate
  repository validator runs tests, not a project's evidence manifest; downstream
  release workflows must invoke the explicit profile and retain its result.
- `google/`: `search_api.py`, `stakeholder.py`, and `tld_atlas.py`.
- `dd/`, `datasets/`, `data/`, `academic/`, `pi/`, `sanctions/`, and
  `reports/`: use the files present in each directory as the module index.

## Dependency baseline

Optional dependencies are not proof that a runtime or provider is available.
Install only through the repository's approved environment and record an
unavailable check as `not assessed`.

```text
Core: httpx, requests, beautifulsoup4, lxml, selectolax, tenacity,
      python-dateutil, charset-normalizer, ftfy
Optional browser/crawler: playwright, curl-cffi, aiohttp, scrapy,
                          scrapy-playwright
Optional extraction/storage: extruct, feedparser, pyarrow, pydantic,
                              boto3, psycopg
Optional verification: exifread, piexif, ephem, python-whois, waybackpy
```

Optional dependencies are imported inside functions where practical. Importing
a package does not prove that its optional runtime is installed or that a
network, archive, browser, or third-party provider is available.

## Engineering principles

1. Use lazy imports for optional dependencies.
2. Type public functions and classify operational errors.
3. Respect robots.txt and host rate limits by default.
4. Do not silently retry client errors or bypass CAPTCHA controls.
5. Keep source provenance, verification status, and unresolved gaps visible.
6. Treat personal-data handling as a lawful, scope-limited operation.
7. Test modules at the smallest layer that proves the named risk.

## Anti-patterns

- Advertise a module that is not present. Fix: derive this index from the tree
  or update it in the same change as the module.
- Treat URL liveness as semantic claim support. Fix: use the source verifier's
  explicit reviewer attribution and non-certifying support-review boundary.
- Store personal data without a lawful basis or retention boundary. Fix: stop
  and obtain the required authority before collection.
- Bypass robots, CAPTCHA, access controls, or provider terms. Fix: record the
  unavailable source as a gap and use an authorised alternative.
- Claim a browser, archive, or provider check passed when it was unavailable.
  Fix: mark that check `not assessed`.

See the relevant skill and module docstring for inputs, permissions, failure
handling, and evidence requirements.
