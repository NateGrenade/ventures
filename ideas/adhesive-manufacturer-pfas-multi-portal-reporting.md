---
slug: adhesive-manufacturer-pfas-multi-portal-reporting
status: demoted
cell_id: naics-325520
created: 2026-09-15
owner_agent: sweep-23
job: Product-stewardship and regulatory-affairs staff at adhesive manufacturers manually
  search historical formulation, bill-of-materials, and raw-material purchase records
  for PFAS substances used since 2011, then re-enter the same per-product PFAS data
  separately into EPA's TSCA Section 8(a)(7) CDX portal and into state portals such
  as Minnesota's PRISM, because formulation/BOM records live in PLM/ERP/SDS systems
  with no integration to any of these disconnected government reporting systems.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 4
---

# Adhesive Manufacturer PFAS Multi-Portal Regulatory Reporting

## Problem statement

Adhesive and sealant manufacturers are now required to report per-substance, per-product
PFAS data to both a federal system (EPA TSCA Section 8(a)(7), via the Central Data
Exchange) and a growing set of state systems (Minnesota's PRISM now, New Mexico and
others soon), each with its own data fields, formats, and deadlines. The federal rule
requires searching back through any year since 2011 for PFAS use across raw materials,
processing aids, and "hidden" additives — data that was never tagged as PFAS-relevant
when originally recorded. Trade press describes this as a "massive data collection
effort" distinct from and in addition to the state-level filings. Staff must pull
formulation and purchasing records and manually assemble/re-enter overlapping but
differently-structured submissions for each portal.

## Evidence

- [type: regulatory] (2026, current) EPA TSCA Section 8(a)(7) requires any entity that
  manufactured or imported PFAS or PFAS-containing articles in any year since January 1,
  2011 to report chemical identity, uses, production volumes, byproducts, and worker
  exposure per substance, filed electronically through EPA's Central Data Exchange (CDX);
  standard deadline October 13, 2026, with 1,462 PFAS substances covered.
  https://www.epa.gov/assessing-and-managing-chemicals-under-tsca/tsca-section-8a7-reporting-and-recordkeeping
- [type: regulatory] (2026, current) Minnesota's Amara's Law requires manufacturers to
  report intentionally-added PFAS per product/component into the state's PRISM system,
  with initial reports due and annual updates each February 1; PRISM supports a
  downloadable Excel template for batch upload (capacity raised from 250 to 10,000 rows
  as of PRISM 1.3, July 2026), implying manufacturers were hitting that row ceiling while
  compiling per-product entries. https://www.pca.state.mn.us/air-water-land-climate/reporting-pfas-in-products
  and https://www.pca.state.mn.us/air-water-land-climate/prism-support
- [type: trade-press] (2026-04-22) Adhesives & Sealants Industry magazine describes 2026
  as a year of "dual challenge" for the sector, noting manufacturers must identify PFAS
  "not only in raw materials but also in processing aids and 'hidden' additives," under a
  federal reporting window that opened April 13, 2026 and closes October 13, 2026, while
  separately meeting Minnesota's Amara's Law obligations — calling the combined effort a
  "massive data collection effort." https://www.adhesivesmag.com/articles/102349-pfas-update-2026-continued-refinement-of-us-and-global-strategies-and-greater-focus-on-adhesives-and-sealants
- [type: trade-press] (2025-07-22) The same publication's earlier PFAS column details
  that New Mexico (effective 2027) and Minnesota (effective 2026) each require
  per-product PFAS amount reporting identified by CAS Registry Number, in state-specific
  formats, and states the regulatory landscape is fragmented enough that "it is simply
  impossible to give a state-by-state update on what categories and/or specific items are
  prohibited." https://www.adhesivesmag.com/articles/101901-the-pfas-discussion-update-2025

## Automation hypothesis

SPECULATIVE. A tool that ingests a manufacturer's formulation/BOM data (raw material CAS
numbers and concentrations, however currently stored — spreadsheet, PLM, or SDS PDFs),
cross-references it against the federal and state PFAS substance lists, and generates the
correctly-formatted submission for each target portal (CDX for federal TSCA, PRISM's
Excel template for Minnesota, and future state formats) could collapse redundant manual
compilation into one maintained source of truth. This depends on formulation data being
recoverable in some machine-readable form (historical records since 2011 may not be),
on each state's format staying scriptable rather than requiring a live web form, and on
manufacturers trusting an automated tool with data that carries regulatory liability if
wrong.

## Scrutiny decision

Demoted at triage: multi-jurisdiction PFAS data compilation and reporting is already a
mature software category with more than three established direct players, each naming
TSCA Section 8(a)(7) and US state PFAS reporting explicitly —
[Assent](https://www.assent.com/resources/pfas-compliance/pfas-reporting/) ("maintains
records of substances present in parts and products in alignment with reporting
requirements under TSCA Section 8(a)(7), as well as state-level PFAS regulations within
the U.S.", and its materials reference Minnesota's PRISM),
[Source Intelligence](https://www.sourceintelligence.com/solution/tsca) (TSCA solution
that "ensures accurate submissions, including PFAS reporting under TSCA Section 8(a)(7)"),
[3E PFAS Risk Management](https://www.3eco.com/3e-solutions/sustainability/pfas-risk-management/),
and [Certivo](https://www.certivo.com/blog-details/pfas-compliance-software-2026-tsca-reach-state-reporting-guide),
which markets BOM-level substance mapping with jurisdiction-specific reporting outputs and
publishes a dedicated [Minnesota PRISM filing guide](https://www.certivo.com/blog-details/minnesota-pfas-reporting-the-complete-prism-filing-guide-for-2026).
The remaining gap — pressing the submit button inside CDX or PRISM rather than producing
the formatted data — is thin, and is the part that a regulatory signatory is least likely
to delegate.

Two secondary problems, recorded but not load-bearing for the kill:

1. Buyer pool. The cell is NAICS 325520, where Census counts roughly 382 firms across 546
   establishments ([SICCODE, citing US Census](https://siccode.com/naics-code/325520/adhesive-manufacturing));
   after cutting to firms large enough to staff a product-stewardship function the
   addressable count is on the order of a hundred, and serving the broader chemical
   manufacturing base means competing head-on with the vendors above.
2. Deadline-shaped demand. The federal obligation is a one-time historical look-back whose
   submission window has now slipped repeatedly (November 2024 to July 2025 to the current
   October 13, 2026 date, with a November 2025 proposed rule adding exemptions still
   pending, per [EPA](https://www.epa.gov/assessing-and-managing-chemicals-under-tsca/tsca-section-8a7-reporting-and-recordkeeping)),
   and Minnesota's PRISM deadline was extended to September 15, 2026
   ([B&D](https://www.bdlaw.com/publications/minnesota-extends-pfas-in-products-reporting-deadline-to-september-15-2026/)).
   Recurring revenue would rest on the annual state updates, not the federal event.
