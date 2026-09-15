---
slug: language-placement-score-transfer-into-banner
status: sandbox
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
