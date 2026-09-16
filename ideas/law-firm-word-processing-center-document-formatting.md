---
slug: law-firm-word-processing-center-document-formatting
status: demoted
cell_id: onet-43-9022.00
created: 2026-09-15
owner_agent: sweep-12b
job: Law firm word processing/document specialist staff manually rebuild attorney
  redlines and dictated drafts into firm-templated Word documents with correct Tables
  of Contents, Tables of Authorities, and cross-references, working night shifts because
  the firm's document management system (iManage) and citation tools (Best Authority)
  do not auto-generate court-compliant formatting from markup.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 3
---

# Law Firm Word Processing Center Document Formatting

## Problem statement

Large law firms staff dedicated "word processing" or "legal document specialist"
roles, often on night or overnight shifts, whose job is to take partner-marked-up
redlines, dictation, and rough drafts and turn them into final, court-ready Word
documents: correct Tables of Contents and Tables of Authorities, working
cross-references, consistent numbering schemes across merged sections, and
firm-branded templates. This is distinct from generic scan-to-Word retyping —
the buyer is a law firm's document production department (or an outsourced
vendor filling that seat), the inputs are attorney redlines/dictation rather
than plain scans, and the output must satisfy court filing formatting rules
(TOA citation format, TOC pagination) that general word processing software
does not generate automatically from a marked-up draft.

## Evidence

- [type: job-posting] (2026-07) Akerman LLP posted a fully remote "Legal
  Document Specialist (Word Processing)" role, Monday-Friday 4:00pm-12:00am
  Eastern with mandatory rotating weekend on-call, requiring 5+ years of legal
  document production experience. Duties explicitly listed: "Create and update
  Tables of Contents (TOCs), Tables of Authorities (TOAs), pleadings, briefs,
  and other legal filings," plus document conversion and formatting
  troubleshooting across platforms. Required tools: MS Word 2016/365, Adobe
  Acrobat, Best Case, Best Authority, and iManage. Posted salary range
  $92,612-$240,040. https://www.legal.io/jobs/5840041/Full-time/Legal-Document-Specialist-Word-Processing/Remote
- [type: job-posting] (2026-09) A live LinkedIn jobs search for "legal word
  processor" shows concurrent open postings at multiple large firms and legal
  vendors, confirming this is an active, recurring hiring category rather than
  a one-off: "Word Processor" at Bodman PLC (Detroit, MI); "Word Processing
  Operator" at Davis Polk & Wardwell LLP (New York, NY) and at Simpson Thacher
  & Bartlett LLP (New York Metro); "Legal Word Processor" at Pettit Kohn
  Ingrassia Lutz & Dolin PC (San Diego, CA) and at Kelley Drye & Warren LLP
  (New York, NY); "Global Document Specialist" at Vinson & Elkins (NY, DC,
  Dallas, Houston, Austin); and "Legal Document Specialist" (multiple shifts)
  at document-production vendor RRD (Phoenix, AZ).
  https://www.linkedin.com/jobs/legal-word-processor-jobs
- [type: job-posting] (2026-05) ZipRecruiter aggregation reports over 1,000
  active "Night Shift Legal Word Processor" listings around Los Angeles, CA
  alone, with hourly pay commonly $22-$37/hr, indicating the night-shift
  document-formatting role is a standing staffing need rather than a rare
  posting. https://www.ziprecruiter.com/Jobs/Night-Shift-Legal-Word-Processor/-in-Los-Angeles,CA

## Automation hypothesis

SPECULATIVE. A tool that ingests an attorney's redlined/dictated draft plus the
firm's style template and produces a compliant TOC/TOA, consistent numbering,
and resolved cross-references — flagging only ambiguous citations or
non-standard formatting for human review — could absorb the bulk of this
role. Feasibility depends on integrating with firm document-management systems
(iManage) and citation tools (Best Authority) that currently require manual
operation, and on handling the wide variety of court-specific and firm-specific
formatting rules reliably enough that a human reviewer is checking rather than
rebuilding the document.

## Evaluation & Scrutiny Log

Triage kill: legal document production is already a mature software category with three-plus established products covering this exact job—Litera Draft automates numbering, styling, cross-references, TOCs, and jurisdiction-specific TOAs (https://www.litera.com/capabilities/draft), BigHand automates firm styles, numbering, and TOCs (https://www.bighand.com/en-gb/our-solutions/document-formatting-styling/), and Thomson Reuters Drafting Assistant supplies TOA building and court-rule format validation inside Word (https://www.thomsonreuters.com/content/dam/helpandsupp/en-us/Topics/drafting-assistant/files/user-guide-for-drafting-assistant.pdf); ILTA's technology survey also records adoption of Litera, BigHand, BEC LegalBar, Infoware Word LX, and other established alternatives (https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedFiles/pdZZ3jT6TSaA3uqL2USt_TechSurvey2021.pdf).
