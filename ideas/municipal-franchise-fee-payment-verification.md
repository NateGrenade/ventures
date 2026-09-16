---
slug: municipal-franchise-fee-payment-verification
status: demoted
cell_id: naics-517112
created: 2026-09-15
owner_agent: sweep-3
job: municipal finance/franchise administration staff manually cross-reference state
  public-utility-commission access-line and cable/video franchise authority reports
  against the franchise fee payments actually received from each cable, video, and
  telecommunications provider, because the city's accounts-receivable ledger has no
  link to the state regulator's provider filings and no standard procedure exists
  for reconciling the two.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 3
---

# Municipal Franchise Fee Payment Verification Against State Provider Filings

## Problem statement

Cable, video, and telecommunications providers operating in a municipality's
rights-of-way owe the city a franchise fee, typically a percentage of gross
revenue, under either a negotiated local franchise agreement or (for cable/
video specifically, since the 2005 Texas-style state-franchising wave) a
state-issued certificate that bypasses local negotiation entirely.
State-authorized providers self-report to the state regulator (e.g., a state
Public Utility Commission) but the municipality is still owed a percentage of
their local revenue. Municipal finance staff must independently verify that
every provider certified to operate in the city is actually paying, and
paying the correct amount, by manually pulling and cross-referencing the
state regulator's provider/access-line reports against the city's own
accounts-receivable records — a reconciliation with no dedicated tool, no
standard procedure in most cities, and revenue leakage large enough that a
single mid-size city found six-figure annual gaps.

## Evidence

- [type: regulatory] (2024-04) City of Denton, TX Office of the City
  Auditor, "Audit of Franchise Fee Collections" (Audit Project #038): found
  the city had "not created written documentation to guide staff when
  tracking or verifying the accuracy of franchise fee payments from
  certified telecommunications providers," and that a review of state
  Public Utility Commission access-line reports against the city's own
  receipts found 8 of 33 certified telecommunications providers submitting
  no payment at all (an estimated $344,000 net loss, ~92% attributable to
  one provider) and 12 more submitting inaccurate amounts (~$7,900 net
  loss). Separately, 2 of 5 state-certified cable/video providers had
  submitted no franchise fee payments during the two-year audit window, and
  only one of the five submitted documentation adequate to verify its 5%
  rate was applied correctly.
  https://www.cityofdenton.com/DocumentCenter/View/9087/Audit-of-Franchise-Fee-Collections-PDF
- [type: regulatory] Same audit: recommends the city "create a standard
  operating procedure to guide staff in tracking and verifying the accuracy
  of all investor-owned franchise fee payments... including obtaining the
  certified telecommunications provider access line report from the Public
  Utilities Commission of Texas," confirming this cross-referencing step is
  currently ad hoc rather than systematized. Finance Department response
  (2024-04) concurred and committed to building the SOP manually.
  https://www.cityofdenton.com/DocumentCenter/View/9087/Audit-of-Franchise-Fee-Collections-PDF
- [type: study] Federal Cable Act, Section 622, caps franchise fees at 5% of
  a cable operator's gross revenue from cable service in the jurisdiction,
  the statutory basis municipalities use to check provider self-reported
  payments; New York State Department of Public Service's "Issues in Cable
  Franchising: The Franchise Fee" brief (2023-12) describes the same
  gross-revenue definition disputes that drive reconciliation work.
  https://dps.ny.gov/system/files/documents/2023/12/issues-in-cable-franchising-the-franchise-fee.pdf

## Automation hypothesis

SPECULATIVE. A tool that ingests a state regulator's published provider/
access-line or certificate-holder reports (many state PUCs publish these
periodically as public data) and a city's own AR ledger of received
franchise fee payments, then flags providers certified to operate in the
city with no matching payment or an amount inconsistent with the expected
rate, could replace the manual lookup-and-compare process the Denton audit
found the city was not doing at all. This is most viable sold to municipal
finance/revenue departments (the buyer is the city, not the cable operator)
and would need to be repeated per state regulator's data format, so the
integration surface is state-specific and would need validation against at
least a second state's PUC/franchising-authority reporting format before
assuming it generalizes beyond Texas.

## Evaluation & Scrutiny Log

Triage kill: franchise-fee verification and recovery is already a mature service
category with three-plus established providers. Azavar combines technology and
experts to reconcile expected and actual payments, Local Government Services has
offered franchise-fee audits and billing-database reconciliation since 2002, and
Cohen Law Group reports more than 20 years and 300 franchise-fee audits; GMA also
offers a pooled compliance-audit service used by nearly 200 cities.
https://www.azavar.com/compliance-audits
https://www.localgovservices.com/
https://www.cohenlawgroup.org/practice-areas/franchise-fee-audits-and-cable-compliance-reviews/
https://www.gacities.com/services/telecommunications-and-right-of-way-management
