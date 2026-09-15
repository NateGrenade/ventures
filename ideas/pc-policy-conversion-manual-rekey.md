---
slug: pc-policy-conversion-manual-rekey
status: sandbox
cell_id: naics-524121
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-sweep-11
job: Carrier policy-conversion representatives manually rekey property and casualty
  policy records between legacy and target administration systems during acquisitions,
  because the acquisition workflow assigns record transfer and scenario resolution to
  manual conversion staff.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 2
---

# P&C Policy Conversion Manual Rekey

## Problem statement

Property and casualty carriers hire temporary conversion teams during acquisitions to transfer policies from one administration system to another. A current posting describes a year-long role focused on manual data entry, data verification, discrepancy identification, and judgment-based resolution of policy conversion scenarios.

## Evidence

- [type: job-posting] (2026-02-24) A leading Canadian P&C insurer undergoing an acquisition advertised policy-conversion representatives for up to 12 months at CAD 25.64 per hour to perform manual entry and processing from one policy system to another, verify accuracy, identify discrepancies, and resolve scenario-based issues. https://www.crawljobs.com/o/policy-conversion-representative-property-casualty-insurance/7f7ad2cfed13eca
- [type: job-posting] (2026-09-11) National General, part of Allstate, advertised a book-transfer specialist to execute carrier conversions, support data migration and policy issuance, coordinate conversion documentation, and track conversion outcomes. https://www.greatinsurancejobs.com/job/transfer-acquisition-specialist-agency-carrier-book-roll-national-general-603605

## Automation hypothesis

SPECULATIVE. A conversion workbench could map legacy records into the target policy schema, prefill conversion screens, compare source and target values, and route only ambiguous scenarios for human judgment. The product would need carrier-specific mappings, auditable validation, and safe handling of policy exceptions that cannot be inferred from structured fields.
