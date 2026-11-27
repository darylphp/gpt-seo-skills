# Schema Report Template

Use these 10 numbered headings in this order with one exact status from SKILL.md. For a blocked report, explain the gap in section 1, keep confirmed facts in section 2 and mark sections that depend on the missing input as `Deferred`. In release check mode, keep all 10 headings and mark sections outside the check as `Not applicable`. Keep long source extracts and tool exports in a referenced appendix, not in the narrative.

## 1. Status and summary

The exact status, then the direct conclusion in two or three sentences: what the page should carry, what must change first, and what is out of scope. Name the page or template, the mode, the report ID and revision, the report date and the evidence cut-off. Give a count of nodes by decision. Then, each on its own line:

`Implementation approval: Awaiting approval`

`This report does not approve deployment or confirm any fact on the business's behalf.`

`Developer handoff: Ready after approval`

Replace the approval line only when an approval for the exact decisions in this revision was supplied, naming the approver, role, date and revision. Use the handoff line that matches the status, as listed in SKILL.md.

## 2. Page record

The URLs or template with its representative URLs and how they were chosen, the canonical and indexing intent, the purpose and main entity of each, the market, the platform and every component that can output markup, the request, and the owners for facts, implementation and approval. List missing details.

## 3. Evidence and access

| ID | Source | What it showed | Date | Settings or conditions | Label | Limits |
| --- | --- | --- | --- | --- | --- | --- |

Then the checks that were needed but are `Not verified`, and why. Then any embedded instruction that was ignored.

## 4. Current markup and producers

| Block | URL or variant | Format | Types and `@id` | Producer | Source or rendered only | Key facts | Conflicts or gaps |
| --- | --- | --- | --- | --- | --- | --- | --- |

Write `No markup present` for a page with none.

## 5. Feature fit

| Type | Outcome it serves | Feature status | Source ID and check date | Requirements and limits that matter here |
| --- | --- | --- | --- | --- |

Keep the six outcomes apart: syntax, vocabulary, feature support, eligibility, appearance, and ranking or traffic.

## 6. Decisions

| ID | URL or template | Node | Decision | Reason | Priority | Producer and owner | Work state |
| --- | --- | --- | --- | --- | --- | --- | --- |

Decisions are Add, Keep, Repair, Consolidate, Remove, Defer or No markup. Priorities are Urgent, High, Planned or Optional. List declined requests separately, each with the reason and the honest alternative.

## 7. Property map

| Node | Property | Value | Visible where | Authoritative source | Owner | Guide marks it | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |

Then the confirmation list: each Missing or Conflicting fact, why it matters, who can confirm it, and which decision waits for it.

## 8. Draft markup and changes

For each Add, Repair or Consolidate decision, the change at its producer: a setting, a template edit or a code block. Label code `Draft for developer review` when every property is Confirmed, or `Template, facts open` when any is not, with visible placeholders. State the producer and environment the draft assumes. For Remove decisions, name the block and the setting or file that produces it. Write `No markup change` when there is none.

## 9. Validation and release

For each changed node: the validation route, the first group of URLs, the cases that must pass, the cases that must stay unaffected, caching or consent checks, the recovery method, and who verifies production. In release check mode, the node-by-node comparison with dates, tools and results.

## 10. Measurement, monitoring and open items

The six outcomes and how each will be measured, the review date or trigger, the recheck triggers that apply, each unknown with the evidence that would resolve it, and handoffs to other workflows with what each needs. No rich-result, ranking, traffic, AI citation or timing promise.
