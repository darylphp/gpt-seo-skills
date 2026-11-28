# Findings and Corrections

Everything in this file is operating method, not Google guidance. The severities and the correction record follow the Content Evidence, Briefing and Publishing QA playbook.

## 1. One record per finding

| Field | Content |
| --- | --- |
| ID | `QA-01`, `QA-02` and so on, kept across rechecks |
| Pass | 1, 2 or 3 |
| Revision and location | The revision ID, the section ID or field, and the exact current wording |
| Finding | The observed problem, not a guessed cause |
| Evidence | The brief section, the claim ID and source location, the policy ID, or the inspected output |
| Severity and effect | One severity, and what it does to the reader or the release |
| Return to | One owner from the table below |
| Required action and acceptance | The bounded fix, and what the recheck will look for to call it resolved |
| Reapproval | Whether the fix changes approved meaning or scope, and who reapproves |

Report findings first, most severe first. A finding without a location and evidence is a question, not a finding.

## 2. Severity

| Severity | Examples | Treatment |
| --- | --- | --- |
| Publication blocker | An unsupported, contradicted or overstated material claim; a usable claim missing its condition; invented experience, people, credentials, reviews or approval; a misleading identity, offer, price or location; an unresolved rights, consent or privacy issue; a material policy concern; a broken essential customer path | Correct, remove or defer the affected material before release |
| Material improvement | The page misses part of its task, fails a completion test, lacks its promised contribution, or is unclear where a reader has to decide | Correct before release, unless a narrower approved scope resolves it |
| Minor correction | A typo, spacing, a small wording or presentation issue that changes no meaning | Fix proportionately. Check only the fix |
| Research note | An interesting but unproven idea | Keep apart from the findings. Never production copy |

## 3. Return routes

| Return to | When |
| --- | --- |
| Site architecture | The page's task, role or boundary is wrong, or it overlaps another page or a page set |
| Evidence owner | A needed claim has no record, a record is stale, or a conflict needs a primary source or the owner |
| Brief owner | The brief's plan, completion test or contribution does not fit the evidence or the task |
| Writer | A section is missing, needs restructuring, or needs rewriting from the brief and dossier |
| Editor | Wording, a heading, voice or a release field needs a bounded fix |
| Specialist reviewer | A regulated or high-consequence claim needs a qualified review |
| Business owner | A commercial fact, permission or consent needs confirmation |
| Publishing | A rendered, link, structured data or production check that can only be done on the built page |

## 4. Bounded recheck

After corrections, recheck the failed passages, the changed passages and every field that repeats or depends on them. Expand only when a change or an unresolved issue gives a reason. Record each earlier finding as Resolved, Partly resolved, Not resolved or Superseded, with the new wording. A new problem found in a changed passage gets a new ID.

Do not rerun a full audit after a punctuation fix. Do not cycle through rounds of "make it more human" or chase a tool score. If the same finding comes back twice, name the owner who has to decide and stop.

## 5. Research notes

An unproven idea, a figure that might be worth sourcing later, or a competitor angle worth testing goes in a research note in section 6, apart from the findings. A research note never becomes a finding or production copy without its own evidence.
