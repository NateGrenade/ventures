---
slug: radiation-therapy-charge-review-before-ehr-export
status: demoted
cell_id: onet-29-1124.00
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-resume-08
job: Radiation therapists manually review and correct treatment charge records between
  ARIA or MOSAIQ and the hospital EHR export queue, because automated charge interfaces
  retain a human accuracy check before billing release.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 3
---

# Radiation Therapy Charge Review Before EHR Export

## Problem statement

Radiation therapists review treatment charges before releasing them into the hospital billing record. UT Southwestern's October 2023 audit describes a peer therapist checking charges in MOSAIQ before its nightly Epic export. This establishes recurring administrative review despite an existing interface, but does not measure labor hours or establish which checks could be automated. Source: https://utsystem.edu/sites/default/files/documents/ut-system-reports/2023/utsw-radiation-oncology-charge-capture-and-reconciliation-report/utsw-radiation-oncology-charge-capture-and-reconciliation-report.pdf

## Evidence

- [type: job-posting] (2021-07) UW Health's Radiation Therapist – Clinical Documentation Specialist position description assigns daily review of treatment charges and necessary edits before export to HealthLink. The document also names ARIA among departmental systems. This is an older role description, not proof of a currently open vacancy. Search-indexed employer text was readable on 2026-09-15; direct web PDF open returned an internal error. https://www.uwhealth.org/files-directory/position-descriptions/technologists-technicians/radiation.therapist.clin.doc.spec.500037.pdf [UNREACHABLE]
- [type: institutional] (2023-10-19; audit period 2022-07 through 2023-06) UT Southwestern's public internal audit describes therapist entry into ARIA or MOSAIQ, an hourly ARIA-to-MOSAIQ interface, peer therapist review/correction, and release for nightly Epic export. The report describes strong existing reconciliation processes overall and corrective-action plans; persistence of the same workflow in 2026 is unverified. The candidate is the therapist's pre-export review, not the financial analyst's separate end-of-treatment review. https://utsystem.edu/sites/default/files/documents/ut-system-reports/2023/utsw-radiation-oncology-charge-capture-and-reconciliation-report/utsw-radiation-oncology-charge-capture-and-reconciliation-report.pdf
- [type: practitioner] (2024-08-06 through 2024-08-08) Respondents in a radiation-therapy practitioner thread describe checking their own billed charges weekly and daily billing review among extra duties. This corroborates recurring checks but does not identify systems, quantify time, or independently verify respondents' employment. Search-indexed discussion was readable on 2026-09-15; direct web open returned an internal error. https://www.reddit.com/r/RadiationTherapy/comments/1ekr1w6/

## Automation hypothesis

SPECULATIVE. A pre-export exception worklist could compare recorded services with draft charges, identify missing identifiers, duplicate entries, unreviewed records, and mismatches in export status, then present supporting records to the therapist. The buyer hypothesis is radiation oncology departmental administration. Existing interfaces already move charges; the untested question is whether a useful share of the retained review consists of repeatable data checks. Clinical interpretation, coding judgment, and charge approval remain with qualified staff. Current workflow validation, access to vendor interfaces, and measured review time are prerequisites to pursuing this candidate.

## Evaluation & Scrutiny Log

Triage kill (`critic-scrutiny-20260915T204319Z-11`, 2026-09-15): pre-export charge
validation for radiation oncology is already a mature software category with well over
three established players, and the automation hypothesis above describes a product that is
already sold into this exact workflow.

Direct competitors, verified by opening the pages:

- **[Radformation QuickCode](https://blog.radformation.com/quickcodes-epic-integration-closes-system-gaps-to-improve-revenue-optimization-and-compliance)** — sold explicitly to "automate charge validation directly within the Epic workflow" and "instantly identify missed or duplicate charges," integrating Epic alongside ARIA and MOSAIQ to catch inconsistencies before claims submission. This is the candidate's exception worklist, shipping. Radformation's own marketing names the candidate's buyer and workflow outright: [it advertises reducing "a lead therapist's review workload" from "a full day to just 15 minutes"](https://blog.radformation.com/managing-radiation-oncology-billing-chaos) and verifying 65 patients in the time previously taken to check two. The pre-export therapist review this idea proposes to automate is the incumbent's headline case study.
- **[Iridium Suite](https://iridiumsuite.com/iridium-suite-radiation-oncology-billing-software/)** — rad-onc billing software built to "import captured codes from record and verify systems like Aria and Mosaiq," with a scrubber carrying "the entire NCCI edit file that will prompt users of any conflicts before claims are filed," plus automated weekly-treatment-code (77427) threshold prompting.
- **[medaptus Charge Pro](https://seekingalpha.com/pr/20169509-peterson-health-chooses-medaptus-charge-pro-to-capture-missing-charges-and-increase-revenue)** — EHR-integrated charge capture and reconciliation sold on capturing missing charges.

Adjacent and substitute coverage is likewise crowded, which removes the fallback position
that the incumbents miss the specific job. Horizontal revenue-integrity vendors already
run rules-based missing-charge detection over the itemized bill —
[FinThrive](https://finthrive.com/solutions/revenue-integrity) markets a 100% review of
patient-itemized bills against 12,000+ rules to find missing charges and coding errors,
and [Craneware](https://www.techtarget.com/revcyclemanagement/feature/leading-hospital-chargemaster-software-products)
integrates with 30+ patient accounting systems including Epic. The services substitute is
also established: [RCCS](https://www.rccsinc.com/oncology-consulting.html) sells "daily
remote charge capture and documentation review" with "oncology EMR configuration support
for ARIA and MOSAIQ-based systems." The category is mature enough to have drawn a
published comparative vendor analysis in the radiation oncology literature
([Enhancing Charge Capture Accuracy in Radiation Oncology: A Comprehensive Software
Analysis](https://www.sciencedirect.com/science/article/pii/S036030162402162X), IJROBP;
abstract page returned HTTP 403 to direct fetch, so this is cited as corroboration of
category maturity only, not as a load-bearing claim).

Two secondary triage failures, recorded but not load-bearing given the above:

1. **No named buyer.** The file's buyer hypothesis is "radiation oncology departmental administration" — a department, not a role that holds budget. Neither Radformation page names a purchasing title either, so the budget holder was not established from any source.
2. **Source reachability.** Two of the three cited sources carry the sweeper's own notes that direct fetch failed (the UW Health position description is tagged `[UNREACHABLE]`; the Reddit thread returned an internal error), leaving the UT Southwestern audit as the only directly readable source. That audit additionally describes the department's reconciliation controls as working, not as a gap.

Searches run: `radiation oncology charge capture software vendor ARIA MOSAIQ charge
reconciliation`; `"radiation oncology" charge capture automation software "missing charges"
review before billing 2025 vendors`; `charge integrity software hospital missing charge
review vendor Craneware FinThrive`.

No full critique written, no rubric values emitted, and no persistence tag chosen, per the
triage rules in `niche-scrutiny` Step 1.
