---
slug: cable-copyright-statement-of-account-compilation
status: demoted
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
buyer_role: VP/Director of Regulatory Affairs
buyer_count: null
annual_price_usd: null
persistence: regulatory-moat
scores:
  pain_evidence: 1
  buyer_clarity: 1
  incumbent_gap: 3
  reachability: 2
  tractability: 1
  replicability: 1
  persistence_quality: 1
  deal_economics: 0
human_verdict: null
cost_usd: null
source_count: 4
revenue_ceiling_usd: null
composite: 38
gate_pass: false
scored_profile: balanced
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

## Evaluation & Scrutiny Log

### Competition

Queries run: `"SA3" cable copyright filing services`, `"Distant Signal
Equivalent" software cable`, `Section 111 Statement of Account preparation
service`, and `cable copyright royalty SA3 filing consultant`. No direct or
adjacent product for compiling operator data into SA3E was found. The concrete
substitutes are the Copyright Office's native Excel form and internal staff or
outside legal advice: the Office requires the native SA3E workbook to be emailed
one filing at a time, while ACA says understanding the amount due and completing
the forms often requires legal advice. No public price for that outside support
was found. Sources:
https://www.copyright.gov/licensing/sec_111.html and
https://www.copyright.gov/docs/soaaudit/comments/06102013/American-Cable-Association.pdf

### Buyer

The plausible operational owner is a VP or Director of Regulatory Affairs. A
New Jersey BPU cable-industry contact list identifies Charter's VP of State
Regulatory Affairs and Comcast's Senior Director of Regulatory Affairs, but it
does not establish that either role controls a software budget for federal
copyright filings. Buyer clarity is therefore 1 rather than 2.
https://www.nj.gov/bpu/bpu/pdf/boardorders/2020/20200520/5-20-20-LSA.pdf

### Deal economics

`buyer_count` is undetermined. The FCC reports about 420 U.S. cable companies and
4,139 cable systems, and ACA Connects aggregates approximately 500 independent
operators and municipalities, but neither source identifies how many separate
buying organizations file the revenue-thresholded SA3 rather than SA1-2. Applying
an SA3 share would be an unsupported size cut. Confidence in any usable count is
low. Sources: https://docs.fcc.gov/public/attachments/FCC-24-2A1.pdf and
https://acaconnects.org/about/

`annual_price_usd` is also undetermined. The current $725 SA3 filing fee is a
government charge, not evidence of what operators pay for compilation software,
and the burden sources do not quantify per-filing labor or outside-counsel spend.
https://www.copyright.gov/licensing/fees.html

### Replicability and technical barrier

The Copyright Office's mandatory native Excel SA3E form supplies a common output
format and shared calculation logic. No reviewed source supports the candidate's
claim that billing and headend systems lack suitable exports, identifies a common
input format, or names a billing/headend vendor with meaningful market share.
Customer-specific mappings therefore remain likely, so replicability is 1.
Because access to the raw billing and carriage data is unestablished,
tractability is also 1 despite the standard output workbook.
https://www.copyright.gov/licensing/sec_111.html

### Evidence verification

The Copyright Office page confirms semiannual Section 111 filing, the SA3 revenue
threshold, and mandatory native-Excel submission. ACA's 2013 comments confirm
that the royalty structure is burdensome and can require many hours and legal
advice. Neither source confirms the proposed cross-system connector gap, so that
claim was excluded from scoring. The two sources are independent as publisher
and practitioner association, though the ACA document is hosted by the Office.

### Persistence hypothesis

**regulatory-moat.** The evidence attributes persistence to a complex royalty
structure and the need for legal interpretation. The 2025 native-Excel mandate
standardizes submission, but it does not show that extraction from operator
systems has recently become feasible, so `recently-unlocked` is unsupported.
