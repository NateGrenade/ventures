---
slug: grain-warehouse-monthly-regulatory-report-compilation
status: sandbox
cell_id: naics-493130
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-sweep-03
job: licensed grain warehouse office staff manually compile stock, receipt, liability,
  and capacity totals between internal position records and government reporting forms,
  because state portals and federal questionnaires require operator-submitted figures.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 4
---

# Grain Warehouse Monthly Regulatory Report Compilation

## Problem statement

Licensed grain warehouses maintain daily position records and submit recurring stock and
receipt totals to regulators. Kansas requires monthly company totals across all functional
units, while Iowa provides a separate portal in which operators enter the prior month's
W-11 report
([Kansas regulation](https://regulations.justia.com/states/kansas/agency-4/article-25/section-4-25-5/),
[Iowa portal](https://data.iowaagriculture.gov/grainreport/)). USDA's current off-farm
grain-stocks questionnaire separately asks multi-facility firms to assemble state-level
capacity and commodity totals
([USDA/NASS](https://www.nass.usda.gov/Publications/Methodology_and_Data_Quality/Grain_Stocks/02_2026/IL_Off_Farm_GrainStocks_Questionnaire_Dec2025.pdf)).

## Evidence

- [type: regulatory] (current through 2025-06-26) Kansas Administrative Regulation
  4-25-5 requires public warehousemen to maintain daily summarized position reports, send
  copies of executed warehouse receipts each month, and submit monthly grain-stock totals
  across all functional units by the fifth day of the month.
  https://regulations.justia.com/states/kansas/agency-4/article-25/section-4-25-5/
- [type: regulatory] (2026 statutes, current page accessed 2026-09-15) Kansas Statute
  34-249a requires a monthly statement of stocks for each licensed warehouse location and
  requires receipt, grain-liability, unencumbered-grain, and total-stock information on
  demand.
  https://kslegislature.gov/b2025_26/laws/034_000_0000_chapter/034_002_0000_article/034_002_0049a_section/034_002_0049a_k/
- [type: regulatory] (current portal accessed 2026-09-15) The Iowa Department of
  Agriculture Grain Warehouse Bureau instructs warehouse operators to enter the previous
  month's W-11 report in its reporting portal and separately enter the quarterly
  per-bushel assessment.
  https://data.iowaagriculture.gov/grainreport/
- [type: regulatory] (2025-12 reference period; form current in 2026) USDA/NASS's Illinois
  off-farm grain-stocks questionnaire asks an operation to report aggregate capacity and
  stock by commodity, prepare separate state reports, and combine multiple facilities when
  individual plants do not report. USDA estimates 15 minutes per response for reviewing
  instructions, searching data sources, gathering and maintaining data, and completing and
  reviewing the form.
  https://www.nass.usda.gov/Publications/Methodology_and_Data_Quality/Grain_Stocks/02_2026/IL_Off_Farm_GrainStocks_Questionnaire_Dec2025.pdf

## Automation hypothesis

SPECULATIVE. A reporting connector could map daily-position and warehouse-receipt exports
to state and federal report fields, aggregate across locations, and retain a reviewable
submission package. The sources prove repeated operator reporting and data aggregation;
they do not prove that any specific regulator offers an API or that a warehouse's existing
grain software lacks built-in exports for these forms.
