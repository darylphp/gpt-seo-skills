# Visibility Report Template

Use these 10 numbered headings in this order with one exact status from SKILL.md. For a blocked report, explain the gap in section 1, keep confirmed facts in section 2, and mark sections that depend on the missing input as `Deferred`. In control decision mode, keep all 10 headings and mark sections outside the decision as `Not applicable` with a one-line reason. Keep long exports, raw HTML and screenshots in a referenced appendix, not in the narrative.

## 1. Status and summary

The exact status, then the direct conclusion in two or three sentences: whether the priority pages can be sources, which controls need a decision, what the data can and can't show, and the first action. Name the site, the mode, the report ID and revision, the report date and the evidence cut-off. Give a count of eligibility checks by state. Then, each on its own line:

`Report approval: Awaiting approval`

`This report changes no setting, file or page, and promises no AI visibility, citation or traffic.`

`Search generative AI control: Include, verified`

Replace the approval line only when an approval for this exact report revision was supplied, naming the approver, role, date and revision. Use the control line that matches the evidence, as listed in SKILL.md.

## 2. Scope, objective and access

The site and hosts, the Search Console properties and their owners, the priority pages or groups with their roles, the markets and languages, the platforms and features in scope, the owner's objective, the mode, and who approves control decisions. Then the access table:

| Check | Method | Date and time zone | Available? |
| --- | --- | --- | --- |

Then the sources supplied or opened, with IDs, and any instruction found inside them that was ignored.

## 3. Eligibility

| URL or group | Role | Response | Crawl access | Indexed | Canonical (declared / Google) | Snippet rules | Effective control | State | Evidence and date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Then a one-line result per page or group: `Eligible`, `Eligibility not verified:` with the open checks, or `Not eligible:` with the verified issue. Note any sample used for a group.

## 4. Controls

| Control | Where found | Current value | What it covers | Decision on record? | Finding |
| --- | --- | --- | --- | --- | --- |

Then the effective Search generative AI setting for each covering property, with inheritance and overrides. In control decision mode, add the options:

| Goal | Control | Consequences | Not affected | How to reverse |
| --- | --- | --- | --- | --- |

and the draft change record from [controls and decisions](controls-and-decisions.md).

## 5. Measurement

The reports available and their access. A baseline table:

| Report | Property and filters | Period (PT) | Measure | Value | Unavailable values kept | Exported |
| --- | --- | --- | --- | --- | --- | --- |

Then the annotations (data anomalies, releases, control changes, updates checked), how analytics classifies the visits, and what the data can't show.

## 6. Observations

The observation plan, then:

| ID | Date, time and zone | Platform and feature | Market, device, account | Query or prompt | Collection | Feature shown | Owned link and placement | Supports nearby claim? | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Then each rate with its numerator and denominator, the failed and unavailable counts, and unlinked mentions. Write `None run` with a recommended set if there are none.

## 7. Contribution and accuracy

For each priority page: its task, what it adds beyond common knowledge, the evidence it lacks, and any accuracy or attribution problem seen in an AI answer, with the observation ID and the route to fix it.

## 8. Claims and proposals screened

| Claim or proposal | Where it came from | Position, with source ID | Status | Action |
| --- | --- | --- | --- | --- |

Write `None supplied` if there are none.

## 9. Actions and handoffs

| ID | Action | Finding it answers | Type | Owner | Work state | Acceptance check | Review date |
| --- | --- | --- | --- | --- | --- | --- | --- |

Types: keep, fix, confirm a decision, measure, monitor, hand off, defer, reject, no action. Then the handoffs to site architecture, content evidence, technical SEO, local SEO, schema markup work and the analytics owner, with the finding each one takes.

## 10. Verification, unknowns and next review

How each action will be checked on the live site and in the reports, and what each check can't show. The unknowns, with `No direct evidence found` where nothing answers them. What evidence would change a conclusion. The next review date, who owns it, and which sources to recheck first. No ranking, citation, traffic or timing promise.
