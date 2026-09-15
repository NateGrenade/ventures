---
slug: cable-copyright-statement-of-account-compilation
status: sandbox
cell_id: naics-517112
created: 2026-09-15
owner_agent: sweep-3
job: cable system regulatory/compliance staff manually compile subscriber counts,
  gross receipts by service tier, and distant-signal carriage logs from billing and
  headend systems into semiannual Section 111 Statement of Account (SA3) filings for
  the U.S. Copyright Office, because neither the billing platform nor the headend/traffic
  system exports data in the form the Office's SA3/SA3E schema requires, and the Distant
  Signal Equivalent calculation has no off-the-shelf tool.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 4
---

# Cable Copyright Statement of Account (SA3) Compilation

## Problem statement

Every cable system that retransmits distant broadcast signals under the
Section 111 compulsory license must file a semiannual Statement of Account
(Form SA3, or its electronic counterpart SA3E) with the U.S. Copyright
Office. The filing requires the system to report, per community/system:
gross receipts broken out by every service tier that includes a broadcast
signal, subscriber counts and rates per tier, MDU (multi-dwelling-unit)
account detail, and a signal-carriage log used to compute a Distant Signal
Equivalent (DSE) for every distant station carried, which sets the royalty
rate tier. None of this is a native export of a billing system (which knows
tiers and subscriber counts but not FCC/Copyright Office signal
classifications) or a headend/traffic system (which knows carriage logs but
not billing categories). Compliance or regulatory-affairs staff at the cable
system assemble the filing by hand from both systems every six months, and
the industry's own trade association has been on record for two decades
describing the underlying process as "administratively complex" and
"burdensome."

## Evidence

- [type: regulatory] (2024-12, in effect from 2025-07-01) U.S. Copyright
  Office rule made electronic filing of Statements of Account mandatory for
  cable systems, formalizing SA3E as the standard filing route and replacing
  the prior paper-or-electronic choice; the electronic form only changes the
  transmission channel, not the underlying compilation of tier, subscriber,
  and carriage data from internal systems. https://www.copyright.gov/rulemaking/digsig/
- [type: regulatory] 37 CFR 201.17 itself specifies exactly what a cable
  system must compile each accounting period to complete an SA3: a log of
  the dates/hours of carriage for each part-time distant signal, subscriber
  counts and rates broken out by service-tier category, gross receipts for
  the basic secondary-transmission service, and station call sign/community/
  channel/network-status detail for every primary transmitter carried — the
  raw inputs to the DSE and royalty-tier calculation.
  https://www.law.cornell.edu/cfr/text/37/201.17
- [type: regulatory] (2006-09-22) American Cable Association comments to
  the Copyright Office (Docket No. RM-2005-6) quote the Office's own 1997
  report to Congress: "the administrative complexity of the current cable
  rates is burdensome... many hours are spent by cable systems just to
  understand how much they owe and how to fill out the forms (which often
  requires legal advice)." The same filing states ACA's roughly 1,100
  small/medium member systems collectively "file tens of thousands of
  statements of accounts each year," and that a rejected industry proposal
  to add per-MDU-account detail to the SOA would have added "hundreds, if
  not thousands, of additional hours" of compilation work per filing cycle
  industry-wide. https://www.copyright.gov/rulemaking/section111/aca.pdf
- [type: regulatory] Copyright Office SA3 long-form royalty schedule
  confirms the multi-tier calculation a filer must perform by hand from
  compiled DSE and gross-receipts figures: systems with semiannual gross
  receipts at or above $527,600 must pay the greater of a 1.064% minimum fee
  or a base-rate-plus-3.75%-per-DSE calculation, with a separate 0.5%
  minimum tier for systems under $80,000 — a tiered calculation performed
  against operator-compiled inputs, not returned by any single system of
  record. https://www.copyright.gov/forms/sa3.pdf

## Automation hypothesis

SPECULATIVE. A connector that pulls subscriber/tier/rate data from common
cable billing platforms (CSG, Wide Open West-style billing suites, or
smaller operators' QuickBooks-adjacent billing tools) and carriage-log data
from headend/traffic logging systems, maps both into the Copyright Office's
SA3E schema, and auto-computes DSE and royalty tier, could collapse a
twice-yearly multi-day compilation task into a review-and-file step. This is
most tractable for the ~1,000+ small and mid-size systems represented by
ACA Connects, which lack in-house software teams to build custom exports and
currently rely on spreadsheets and, per the association's own comments,
outside legal advice to interpret the forms. Integration surface and
willingness to pay by a fragmented population of small operators are both
unverified and would need direct validation before this is worth building.
