---
slug: taxi-voucher-scrip-program-reconciliation
status: sandbox
cell_id: onet-53-3054.00
created: 2026-09-15
owner_agent: sweep-17
job: Taxi company back-office staff collect paper senior/disability transportation
  vouchers from drivers, manually count and match them to trips, and submit the paper
  batch each month to a county or transit agency for reimbursement, because the agency's
  voucher program has no digital submission or trip-verification system bridging the
  taxi company's records and the agency's payment process.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 4
---

# Taxi Voucher / Scrip Program Reconciliation

## Problem statement

Hundreds of counties and small transit agencies run subsidized taxi voucher
("scrip") programs for seniors and people with disabilities: riders buy
discounted paper coupon booklets, hand a coupon to the driver instead of cash,
and the taxi company collects the paper coupons and submits them once a month
to the sponsoring agency for reimbursement at a fixed per-trip or per-coupon
rate. Because the coupon is the transaction record, taxi company staff must
manually count, batch, and reconcile paper vouchers against driver trip
records before mailing or hand-delivering a monthly claim, and the agency
must manually verify and pay each claim. This is a recurring, low-tech
paperwork cycle sitting on top of physical taxi driving, run by a party (the
taxi operator's office staff) distinct from the driver.

## Evidence

- [type: procurement] (2016-05-18) Monterey-Salinas Transit District RFQ #16-05
  for its Taxi Voucher Program specifies: "The taxi operator will submit all
  collected taxi vouchers following the end of each month of service and
  submit them to Monterey-Salinas Transit District. MST will reimburse the
  total value of the vouchers within 30 calendar days of receipt of each
  claim." Reimbursement is per verified paper voucher, at a fixed rate per
  one-way trip. https://mst.org/wp-content/media/MST-DRAFT-FINAL-TAXI-VOUCHER.pdf
- [type: regulatory] (2025, program notice, viewed 2026-09) Napa Valley's Vine
  Transit "Taxi Scrip" program page states: "Starting September 2025, Taxi
  Scrip will begin using PEX Payment Cards," describing "The Lifeline Taxi
  Program" moving off its paper-coupon system to a payment-card model.
  https://vinetransit.com/taxi-scrip/
- [type: trade-press] (2025-04-08) Berkeleyside reports the City of Berkeley
  is cutting back its "Rides for Seniors and the Disabled" program; the city
  manager's memo notes participants "lose hundreds of dollars each year in
  taxi scrip and other ride benefits," confirming a paper-scrip taxi
  subsidy program still operating city-wide as of 2025.
  https://www.berkeleyside.org/2025/04/08/berkeley-rides-for-seniors-and-the-disabled-program-cuts
- [type: procurement] (2016-05-18, same document) MST RFQ requires drivers to
  be certified in an ADA training program before "any contract execution or
  voucher reimbursement," and ties reimbursement eligibility to a paper
  compliance record checked against the same voucher claims.
  https://mst.org/wp-content/media/MST-DRAFT-FINAL-TAXI-VOUCHER.pdf

Additional programs of the same structure were identified but not
individually verified with dated primary sources in this sweep: Anne Arundel
County MD (ETA Taxi Voucher Program), Clark County NV (Taxi Assistance
Program coupon booklets), and other county aging/disability offices — these
are candidate leads for a follow-up sweep or Phase 2 deepening, not evidence
used to support this file's tier.

## Automation hypothesis

SPECULATIVE. A lightweight claims portal or scanning/OCR workflow could let
taxi operators submit voucher images or trip-matched digital claims directly
to the sponsoring agency, and let the agency auto-verify against driver
certification status and program budget caps, replacing the physical
mail-in batch cycle. The Vine Transit and MST cases suggest the integration
surface is narrow (one program administrator, one or a handful of contracted
taxi operators per county) but fragmented across thousands of counties/transit
districts nationally, each running its own bespoke paper process — a real
constraint on total addressable market per deal, favoring a multi-tenant SaaS
sold to transit agencies rather than to individual taxi companies.
