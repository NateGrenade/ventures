---
slug: neurodiagnostic-device-to-emr-billing-rekey
status: sandbox
cell_id: onet-29-2099.01
created: 2026-09-15
owner_agent: sweep-4
job: neurodiagnostic technologists manually re-key patient test results and study
  billing charges from the diagnostic acquisition software (Cadwell, Natus, Nihon
  Kohden) into the hospital EMR (Cerner, Epic) and the practice-management/billing
  system (e.g. AthenaHealth), because neurodiagnostic acquisition devices have no
  native interface to hospital EMR or billing platforms.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 2
---

# Neurodiagnostic Device-to-EMR/Billing Rekey

## Problem statement

Neurodiagnostic technologists (EEG, EMG/nerve-conduction, and polysomnography
technologists — O*NET 29-2099.01 and its close relatives) run studies on
dedicated acquisition workstations from vendors like Cadwell, Natus, and
Nihon Kohden. Those workstations are purpose-built for waveform capture and
scoring but are not integrated with the hospital's EMR or billing/scheduling
systems. Job postings for these roles routinely list fluency in three or
more separate systems as a requirement and assign the technologist the task
of manually transcribing study results into the EMR and manually entering
the resulting charge into the billing system after every study — a rekeying
step performed once per patient encounter, effectively daily in any
active department.

## Evidence

- [type: job-posting] (accessed 2026-09-15, posting live) Ascension Sacred
  Heart EMG/NCV Technician posting instructs technologists to "Utilize
  AthenaHealth, Cerner and Cadwell Systems to review and record patient
  data," naming three distinct, non-integrated systems (practice
  management, hospital EMR, and neurodiagnostic acquisition software) the
  technologist must move data across by hand.
  https://www.aaet.info/job-postings/emg-ncv-technician/41
- [type: job-posting] (accessed 2026-09-15, posting live) Eisenhower Health
  "Polysomnographic Technologist-Sleep Lab" posting lists as separate,
  named duties: "Documents accurate and pertinent information on technical
  notes at the time [of] study; documents and processes procedures on a
  daily basis in the department records" and "Processes billing charges or
  credits as assigned" — i.e., the technologist, not a biller, is the one
  entering the charge after each study.
  https://careers.eisenhowerhealth.org/jobs/polysomnographic-technologist-sleep-lab/

## Automation hypothesis

SPECULATIVE. This looks like a candidate for a narrow HL7/interface-engine
style adapter purpose-built for the handful of dominant neurodiagnostic
acquisition platforms (Cadwell Cascade/Arc, Natus NeuroWorks/Xltek, Nihon
Kohden Neurofax), pushing completed-study metadata (patient ID, study type,
CPT-mappable procedure code, completion timestamp) directly into the
hospital's EMR results queue and the practice-management system's charge
queue. The integration surface is well-defined (a handful of device
vendors, a handful of EMR/PM vendors) but the buyer is diffuse — individual
hospital neurodiagnostics departments and outpatient neurology practices
rather than a single enterprise IT purchaser — so go-to-market would likely
need to piggyback on existing interface-engine vendors (Mirth/NextGen
Connect, Corepoint) or department-level champions rather than a top-down
hospital IT sale. Whether the acquisition vendors expose any accessible
export format (HL7, CSV, DICOM SR) versus a closed proprietary database is
the key unresolved feasibility question.
