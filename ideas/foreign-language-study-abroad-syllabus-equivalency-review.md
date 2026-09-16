---
slug: foreign-language-study-abroad-syllabus-equivalency-review
status: demoted
cell_id: onet-25-1124.00
created: 2026-09-15
owner_agent: sweep-24
job: Language-department reviewers manually collect syllabi and record language-course
  approvals on transfer forms linking student submissions to registrar credit records,
  because course documents, departmental approvals, and official transcripts arrive
  through separate submissions.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 2
---
# Foreign-Language Study-Abroad Approval Packet Handoff

## Problem statement

Language departments receive syllabi or course descriptions together with transfer or study-abroad approval forms. Butler asks students to bring those documents to the appropriate language faculty reviewer and leave the equivalent-course fields blank. UVA requires language-department approvals and supporting syllabi for designated courses, with both pre- and post-approval for some languages. Changed courses must also be listed on final approval forms.

The information-work candidate is collecting the right course version, recording an already-decided approval, and matching final course records to that approval. Academic equivalency judgment remains the faculty's responsibility. UVA already routes signatures and completed approvals through DocuSign; the evidence does not establish a universal lack of integration or manual rekeying into every registrar system.

## Evidence

- [type: institutional] (undated; accessed 2026-09-15) Butler's language-credit procedure requires students to provide a syllabus or description for each course and the applicable transfer or study-abroad form to the designated language faculty reviewer. Students leave the Butler-equivalency fields blank and obtain translation when a syllabus uses a language Butler does not offer. This establishes document intake and completion around faculty review. https://www.butler.edu/arts-sciences/modern-languages-literatures-cultures/transfer-credits/
- [type: institutional] (current instructions accessed 2026-09-15; DocuSign process introduced Fall 2025) UVA requires departmental approvals and syllabi or course descriptions for World Language credit. Some language departments require pre- and post-approval. Changed courses require a final approval form, while the host institution separately sends the official transcript. Counterevidence: DocuSign automatically routes signatures and approved forms to the next office, so that handoff already has software support. https://college.as.virginia.edu/study-abroad-transfer-credit-form-instructions

## Automation hypothesis

SPECULATIVE. A packet-preparation tool could check that each course has the required syllabus version, approval fields and signatures, track changes between pre-approval and final enrollment, and match an arriving transcript to approved course records. It would preserve faculty decisions and use existing signature-routing tools. Remaining workload, integration access and department willingness to adopt another tool are unverified.

## Additional Evidence

The resumed sweep matched its packet-routing finding to this existing slug at 0.48. The coordinator narrowed the job from academic document comparison to information handling and replaced the blanket integration claim with the documented DocuSign limitation. The original slug is retained; earlier evidence and wording remain in Git history and resume notes. Current local source vocabulary recognizes institutional operating procedures.

## Evaluation & Scrutiny Log

### Triage (`critic-scrutiny-20260915T204319Z-9`, 2026-09-15)

**Demoted at triage — the manual workflow is already a mature software category with
three-plus established players.** The job as written (collect the course syllabus/description,
attach it to a transfer or study-abroad approval form, route it to the designated
departmental faculty reviewer, record the approval, and track courses that changed between
pre-approval and final enrollment) is the advertised feature set of the study-abroad and
transfer-credit software category, not an unserved gap:

- **Terra Dotta Course Approvals** — applicants select foreign courses, indicate home course
  equivalents, select an approver, and submit an electronic course approval form; approvers
  get an emailed link to view, amend, and set approve/deny status per request, which triggers
  applicant notification. https://support.terradotta.com/hc/en-us/articles/360041350013-Study-Abroad-Course-Approvals
  (Zendesk returned 403 to the fetch tool; content confirmed via the indexed article and the
  product page https://www.terradotta.com/outgoing/)
- **Via TRM (Via Global)** — reviewer/approver routing workflows, batch approvals, and
  form/reminder automation for outgoing study abroad. https://www.viatrm.com/via-global
- **CollegeSource TES** — Evaluation Tracker is a paperless workflow for recording transfer
  credit evaluation decisions; TES/Transferology integration explicitly "eases the routing of
  courses and proposed equivalencies to faculty for comment, revision, and approval."
  https://collegesource.com/transfer-tools/tes/ and https://collegesource.com/tes-and-transferology/

Queries run: "transfer credit course equivalency evaluation software higher education
CollegeSource TES Transferology"; "study abroad management software Terra Dotta Via TRM
course approval syllabus workflow".

The idea file already carries its own counterevidence: UVA routes signatures and approved
forms automatically through DocuSign as of Fall 2025, so even the un-platformed institution
cited here has software on the handoff. What remains is the faculty's academic equivalency
judgment, which the file itself excludes from scope. No full critique written; the kill is
not close.
