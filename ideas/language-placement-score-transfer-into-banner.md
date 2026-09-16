---
slug: language-placement-score-transfer-into-banner
status: demoted
cell_id: onet-25-1124.00
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-resume-04
job: Language-program advising staff manually copy language placement results from
  WebCAPE into Banner SOATEST because the documented workflow requires staff recording
  before student records can use the assessment outcome.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 4
---

# Language Placement Score Transfer into Banner

## Problem statement

University of Montana advising staff manually enter introductory language placement scores in Banner within two to three business days; the source assessment is WebCAPE. Proctoring status changes whether higher-level results are entered, making the handoff more than copying a score. This is administrative information work supporting language instruction; academic placement judgment remains with the institution. [type: institutional] (2025–2026 academic year, pp. 28–29) https://www.umt.edu/office-student-success/for-faculty-staff/um-advising-manual-25-26.pdf

## Evidence

- [type: institutional] (2025–2026 academic year; accessed 2026-09-15) Montana's advising manual explicitly identifies manual SOATEST recording by H&S Advising. It also distinguishes proctored higher-level assessments from unproctored results. This establishes a specific manual interface, without establishing its transaction volume or technical cause. https://www.umt.edu/office-student-success/for-faculty-staff/um-advising-manual-25-26.pdf
- [type: institutional] (updated 2026-03-05; accessed 2026-09-15) UC Davis describes an immediate testing-system email followed one to five days later by confirmation that a result has entered the Language Center Results Database. Proficiency results subsequently reach MyDegree through the registrar. This corroborates a separate results-recording handoff, but does not explicitly establish manual entry or use of Banner. https://ucdlc.ucdavis.edu/exam-results-information
- [type: institutional] (undated; accessed 2026-09-15) Counterevidence: East Carolina University's French, German and Spanish placement survey sends placement automatically to Banner, with registration possible within two business days. Existing automation therefore addresses this interface at some institutions. https://foreign.ecu.edu/resources/placement-exams/

## Automation hypothesis

SPECULATIVE. A language-program operations tool could import approved assessment results and proctoring flags, validate institution-specific score mappings and student identifiers, and prepare auditable SOATEST updates for staff approval. It would preserve academic decisions and route exceptions to staff. Viability depends on permitted assessment exports and Banner write access; neither has been verified. The buyer hypothesis is the language-program or advising operations owner. ECU's existing integration makes implementation differences and remaining staff workload essential questions before further investment.

## Evaluation & Scrutiny Log

### Triage (`critic-scrutiny-20260915T204319Z-9`, 2026-09-15)

**Demoted at triage — the manual workflow is already a mature software category with
three-plus established players, and one of them is the source assessment vendor itself.**
Moving approved language placement results into the SIS test-score record is a shipped
capability, not an unserved job:

- **Emmersion (the WebCAPE vendor named in this idea's own job statement)** — the WebCAPE
  product page states: "Seamlessly connect with your current workflow through our Enterprise
  API and integrations, such as Banner." Verified by reading the page.
  https://emmersion.ai/products/webcape/
- **Avant Assessment (STAMP)** — sells a custom API for pushing testing data into systems
  that support integration, with an onboarding process aimed at institutions whose SIS
  supports Open API/JSON, plus third-party paths such as Ellevation.
  https://www.avantassessment.com/integrations/api and https://www.avantassessment.com/en/integrations
- **Ellucian Banner itself** — ships native bulk test-score loading via the Electronic
  Prospect Load (SRTLOAD) with SSRSRIN matching and SRRPREL migration, documented as the
  supported path for AP and other test-score tapes into student records.
  https://fhdafiles.fhda.edu/downloads/eisDocs/STTapeLoadProcessing80WB.pdf

Queries run: "WebCAPE placement test score automatic upload Banner SOATEST integration";
"Banner SRTLOAD electronic test score load process placement scores automated"; "Avant STAMP
placement test results API integration student information system university".

The file's own counterevidence points the same way: East Carolina University already sends
French/German/Spanish placement results to Banner automatically
(https://foreign.ecu.edu/resources/placement-exams/). Montana's manual SOATEST entry is
therefore best read as one institution's configuration choice within a solved category
rather than a market. Secondary problems, not reached because the category kill is decisive:
the buyer named ("language-program or advising operations owner") is a departmental role
without SIS-integration budget, which sits with the registrar or IT, and the ceiling is a
per-department micro-purchase at institutions that mostly already own the integration
through their assessment contract. No full critique written.
