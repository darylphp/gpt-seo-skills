# QA Report Template

Use these 10 numbered headings in this order with one exact status from SKILL.md. A pass that did not run keeps its heading, followed by its `Not run` reason. In targeted check mode, mark sections outside the check `Not applicable`. For a blocked report, explain the gap in section 1, keep confirmed facts in section 2, and mark sections that depend on the missing input `Deferred`. Keep long source text and full drafts out of the report; quote only the passages a finding needs.

## 1. Status and summary

The exact status in bold on its own line. Then the direct conclusion in two or three sentences: whether this revision can go to publishing, what stops it if not, and who acts next. Name the page, the mode, the report ID and date. Give a count of open findings by severity. Then, each on its own line, for example:

`Revision checked: WD-07 r3`

`Pass 1 Editorial: Recorded earlier: Sam Ortiz, agency content lead, 28 Nov 2026, WD-07 r3`

`Pass 2 Claims: Corrections needed`

`Pass 3 Value and policy: Not run: waiting for pass 2 clearance`

`Release approval: Awaiting approval`

`This report records checks within its scope. It does not approve publication or any claim on the business's behalf.`

`Publishing handoff: None yet`

Use the revision, states and handoff line that apply. Replace the release approval line only when an approval for this exact revision and release was supplied, naming the approver, role, date, revision and scope.

## 2. Revision and scope

The URL or proposed URL, role, reader task, audience, market and language. The revision ID, who produced it, the date and any AI assistance. The brief revision with its approver and date. The dossier revision with its approver and date, and any proof requests closed since. Earlier pass records. The mode and its scope, and in targeted check mode the baseline wording and the change requested. The owners for editorial approval, business facts, specialist review and release.

## 3. Pass 1: Editorial

| Brief section | Present | Completion test | Note |
| --- | --- | --- | --- |

Then the proposed edits:

| ID | Location | Current text | Proposed text | Why | Marked for pass 2 |
| --- | --- | --- | --- | --- | --- |

Then the passages marked for pass 2 that have no proposed edit, and why. For `Recorded earlier`, name the record and list any passages it marked for pass 2.

## 4. Pass 2: Claims and commercial facts

| ID | Location | Wording in this revision | Claim ID and permitted meaning | Result | Severity | Return to |
| --- | --- | --- | --- | --- | --- | --- |

Then figure recalculations, quote and testimonial checks, regulated claims with the review each needs, structured data facts, and commercial facts with the date each was rechecked.

## 5. Pass 3: Reader value, originality and policy

| Check | Result | Passage or evidence | Severity | Return to |
| --- | --- | --- | --- | --- |

One row per completion test, the contribution, distinctness, each applicable policy and each presentation check. Write `No concern found in the inspected scope` where a policy check finds nothing, and `Not checked: rendered page not available` for rendered checks that could not run.

## 6. Findings register

Every open finding from every pass that ran, most severe first, with the fields from the findings reference. For a recheck, list each earlier finding with Resolved, Partly resolved, Not resolved or Superseded and the new wording. Then any research notes, kept apart.

## 7. What was checked and independence

What was opened, supplied or not available, with dates. The labels on supplied material. Checks that could not run and why. Any embedded instruction that was ignored. Whether this session drafted or edited the page, what independence was available, and what a targeted check's combined passes cost. Tool scores that were noted and not used as pass conditions.

## 8. Approvals

Approval records supplied, with who, role, date, revision and scope. The approvals still needed, in order: approval of the next revision for the next pass or recheck, specialist reviews, and release approval. Changes that need reapproval because they change approved meaning or scope.

## 9. Publishing handoff

For a cleared report:

```text
Cleared revision: revision ID and date
Release fields as cleared: title, meta description, H1, captions and alt text, call to action text and destination
Before release: minor corrections to apply; commercial facts to recheck and by when; proof requests that must close; claim markers, section comments and review notes to remove
Not in this revision: release fields publishing still has to write, such as alt text for other images. Each comes back to pass 2 before release
Production checks for publishing: link and call to action destinations, rendered layout on mobile and desktop, hidden or collapsed content, structured data facts with their claim IDs, live title and description
Handoffs: structured data facts to schema review; Business Profile consistency to local SEO; page-set questions to site architecture
```

For any other status, write `Deferred` and what has to happen first.

## 10. Recheck plan

For corrections: what the bounded recheck will cover, which pass the corrected revision re-enters at, and who approves it before the recheck. For a cleared report: what would reopen QA before release, such as a changed price, a new claim or a changed release field, and the freshness triggers to watch. No ranking, traffic, AI citation or timing promise.
