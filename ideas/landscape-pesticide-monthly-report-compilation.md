---
slug: landscape-pesticide-monthly-report-compilation
status: demoted
cell_id: naics-561730
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-resume-07
job: Landscape contractor report preparers manually total application records into
  monthly county pesticide-use forms because the documented form route requires product-level
  totals and county-specific reports separate from individual applications.
split_from: null
evidence_tier: 1
scores:
  deal_economics: 0
human_verdict: null
cost_usd: null
source_count: 5
revenue_ceiling_usd: null
composite: 0
gate_pass: false
scored_profile: balanced
---

# Landscape Pesticide Monthly Report Compilation

## Problem statement

California's form-based reporting route requires landscape maintenance businesses to enter product identifiers, amounts and application totals in a monthly county report. Lindsay's landscape-maintenance contract also requires monthly records to reach both the county and city. These artifacts establish required compilation and delivery; they do not measure staff time or establish how many contractors still prepare forms manually. [type: regulatory] (form revised 2024-12) https://www.cdpr.ca.gov/wp-content/uploads/2024/12/dpr-pml-060.pdf [type: procurement] (revision 2024-07-16) https://www.lindsay.ca.us/sites/default/files/fileattachments/city_services/page/8510/addendum_no._1.pdf

## Evidence

- [type: regulatory] (revised 2024-12; accessed 2026-09-15) California DPR form PML-060 includes landscape-maintenance pest-control businesses. Instructions require separate reports by county, monthly product totals, registration numbers from labels and application counts, with special counting instructions for tank mixes. It specifies copies for the commissioner and preparer. This is direct evidence of the form-completion task, not evidence that electronic alternatives are absent. https://www.cdpr.ca.gov/wp-content/uploads/2024/12/dpr-pml-060.pdf
- [type: procurement] (revision 2024-07-16; accessed 2026-09-15) City of Lindsay's Olive Bowl/Kaku Park procurement, section 02449 Landscape Maintenance, requires contractors to maintain application records and submit chemical-use records monthly to the County Agricultural Commissioner and City. This confirms a landscape customer also requires the information. https://www.lindsay.ca.us/sites/default/files/fileattachments/city_services/page/8510/addendum_no._1.pdf
- [type: institutional] (undated page with 2026 reporting data; accessed 2026-09-15) Contra Costa County accepts pesticide-use reports through CalAgPermits, mail, fax or in person. This establishes an existing electronic submission path and limits the candidate to any remaining preparation or client-reporting work, rather than assuming paper-only filing. https://www.contracosta.ca.gov/6242/Pesticide-Use-Reporting-and-Data

## Automation hypothesis

SPECULATIVE. A tool for a landscape contractor's reporting administrator could aggregate approved application records by county, month and product; validate units and identifiers; and prepare county and client copies for review. Access to existing field records and permitted submission interfaces would determine whether it removes work. The prevalence of manual preparation, available CalAgPermits imports and existing landscape-software exports are unverified. It would document completed applications, with pesticide selection and application decisions remaining outside scope.

## Scrutiny triage

Demoted: compiling field application records into California monthly pesticide-use reports
is a mature software category with more than three established direct players, including
landscape-specific ones. JanMar
[Field Service Cloud](https://www.janmarsystems.com/fieldservicecloud/features/pesticide-reporting)
sells pesticide reporting to landscape maintenance companies and states "California MS-PUR /
CalAgPermits Submission: For companies in California, Field Service Cloud supports Monthly
Summary Pesticide Use Report submission through CalAgPermits where applicable" — that is the
candidate's entire job description. Adkad's GroundsKeeper Pro
[chemical application tracking](https://www.adkad.com/chemical-application-tracking-reporting/)
records "herbicide, pesticide, fertilizer and any other type of lawn and landscape chemical
applications" and prints or emails application reports per customer or across all customers
for a date range, covering the client-copy half. WorkWave
[PestPac](https://www.pestpac.com/features/pest-control-reporting-software) ships built-in
California Material and Cal-Ag reports with EPA registration numbers auto-populated from the
mobile app. [GorillaDesk](https://gorilladesk.com/features/chemical-tracking-software/),
FieldRoutes and [Jobber](https://www.getjobber.com/features/chemical-tracking/) all sell
chemical tracking to lawn care and pest control.

The remaining gap after those products is submission, and the idea's own third source closes
it: [Contra Costa County](https://www.contracosta.ca.gov/6242/Pesticide-Use-Reporting-and-Data)
accepts reports through CalAgPermits electronically. Evidence establishes that the form
exists (PML-060) and that a city contract requires monthly copies, but not that any
meaningful population of landscape contractors still compiles it by hand rather than from a
field-service system they already run. Persistence here would land on `regulatory-moat` or
`incumbent-distribution`, neither of which is promotion-eligible. No full critique written;
killed at triage.
