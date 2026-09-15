---
slug: historic-preservation-grant-volunteer-match-documentation
status: sandbox
cell_id: naics-712120
created: 2026-09-15
owner_agent: sweep-2
job: Grant-funded historic site staff manually fill out Excel or paper volunteer timesheets
  and hand-calculate in-kind match dollar values (hours worked times a fixed wage
  rate) to submit alongside each payment request, because federal and state Historic
  Preservation Fund grant portals provide only a static timesheet template with no
  integrated hour-tracking or match-value calculation tied to the payment-request
  workflow.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 2
---

# Historic Preservation Grant Volunteer Match Documentation

## Problem statement

Historic sites and historical societies that receive Historic Preservation Fund (HPF)
matching grants — administered by the National Park Service through state SHPOs —
must document non-cash match, including volunteer and in-kind labor, to justify each
payment request. The required workflow is a static Excel or paper timesheet: staff or
volunteers log dates and hours by hand, apply a fixed hourly rate (federal minimum
wage, or a capped professional rate for skilled work) themselves, get a supervisor
signature, and attach the completed sheet to the payment request. Nothing in the
published process ties hour-logging to automatic dollar-value calculation or to the
grant payment system itself.

## Evidence

- [type: regulatory] (page last updated 2021-05-21, program active) National Park
  Service Historic Preservation Fund "Sample Documents for Recipients & Contractors"
  page specifies that donated labor must be valued at "the Federal minimum wage
  unless the person donating time is professionally skilled," caps skilled-labor
  rates at "120% of a General Schedule (GS) Federal employee at Grade 15, Step 10,"
  and requires recorded fields of contributor name, work type, dates, hours,
  hourly rate, and a supervisor verification signature — all on a downloadable
  template rather than a connected system.
  https://home.nps.gov/subjects/historicpreservationfund/sample-documents-for-recipients-contractors.htm
- [type: regulatory] (current program page, no explicit date) Florida Division of
  Historical Resources Small Matching Grants program requires that "Completed time
  sheets should be submitted with any payment request which cites these services,"
  instructs grantees to "use the federal minimum wage of $7.25 an hour" to value
  volunteer time, states "All match must be accounted for during the grant period,"
  and distributes a downloadable Excel "Volunteer Timesheet" template as the
  documentation mechanism.
  https://dos.fl.gov/historical/grants/small-matching-grants/

## Automation hypothesis

SPECULATIVE. A small web or mobile tool for grant-funded historic sites to log
volunteer/in-kind hours as they occur, auto-apply the correct wage-rate rule (federal
minimum vs. capped professional rate), and generate the signed timesheet PDF required
at each payment request could remove the manual hand-calculation step. This is a
paperwork layer around a compliance requirement rather than a connection to a single
software system, so the integration surface is generating the correct output document
for each state SHPO's payment-request process, not an API — it would need per-state
verification since HPF is federally funded but administered separately by each SHPO.
