# Escalation Output

Expected output when the request is: "Search Console says we have a manual action for structured data. Can you check our service pages?" Supplied: a Manual Actions screenshot (27 Nov 2026) naming a structured data issue on some pages; the saved source of `https://brightwater-plumbing.example/services/blocked-drains/`, which carries a `Service` node and an `AggregateRating` of 4.9 from 312 reviews added by a "trust badges" plugin on every service page; and the visible page, which shows no reviews or rating. The owner, Ari Mendes, says: "The plugin lets you type in a rating. We never collected reviews on the site." Synthetic example.

## 1. Status and summary

**Escalate first: Misleading markup or manual action**

The service pages state a 4.9 rating from 312 reviews that the business never collected and that no visitor can see, and Search Console shows a structured data manual action. Remove the rating from markup on every service page first, at the plugin that adds it. Until that's done, the rest of the markup review waits.

Page set: the service page template, sampled with the blocked drains page. Mode: Audit. Report SM-2026-11-03, revision 1, dated 28 Nov 2026. Evidence cut-off 27 Nov 2026. Decisions: 1 Remove, 1 Keep.

`Implementation approval: Awaiting approval`

`This report does not approve deployment or confirm any fact on the business's behalf.`

`Developer handoff: Correction first`

## 2. Page record

Service page template at `https://brightwater-plumbing.example/services/`, sampled with the blocked drains page. Purpose: describe one plumbing service. Main entity: the service. Owner and approver: Ari Mendes. Implementer: not named. Market and full plugin list: not supplied.

## 3. Evidence and access

| ID | Source | What it showed | Date | Settings or conditions | Label | Limits |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | Manual Actions screenshot | A structured data issue affecting some pages | 27 Nov 2026 | Search Console | Supplied | Pages not listed in the screenshot |
| E02 | Saved source, blocked drains page | `Service` node; `AggregateRating` 4.9 from 312 from the trust badges plugin | 27 Nov 2026 | Saved by the owner | Supplied | One page |
| E03 | Owner's statement | The rating was typed in; no reviews were collected on the site | 27 Nov 2026 | | Supplied | |

Not verified: the other service pages, the rendered output, and whether any other plugin adds markup.

## 4. Current markup and producers

| Block | URL or variant | Format | Types and `@id` | Producer | Source or rendered only | Key facts | Conflicts or gaps |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | Blocked drains page | JSON-LD | `Service` | Not identified | Source | Service name and description | Producer not identified |
| B2 | Every service page (per plugin settings) | JSON-LD | `AggregateRating` attached to the service | Trust badges plugin | Source | 4.9 from 312 | Invented and not visible |

## 5. Feature fit

| Type | Outcome it serves | Feature status | Source ID and check date | Requirements and limits that matter here |
| --- | --- | --- | --- | --- |
| `AggregateRating` | Review stars | Restricted | M07, 28 Nov 2026 | Ratings must be genuine and visible on the page; no fake reviews |
| `Service` | Accurate description | Descriptive only | M03, M16, 28 Nov 2026 | No dedicated Google feature |

## 6. Decisions

| ID | URL or template | Node | Decision | Reason | Priority | Producer and owner | Work state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D01 | Service template | `AggregateRating` | Remove | Invented rating that no visitor can see [M07]; matches the manual action [M01] | Urgent | Trust badges plugin; Ari | Proposed |
| D02 | Service template | `Service` | Keep | Describes the visible service. Review its facts once D01 is done | Planned | Producer not identified | Not applicable |

## 7. Property map

| Node | Property | Value | Visible where | Authoritative source | Owner | Guide marks it | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Service` | `aggregateRating` | Remove | Nowhere | None | Ari | Review guidelines [M07] | Conflicting |

## 8. Draft markup and changes

Turn off the rating output in the trust badges plugin, or remove the plugin if the rating is its only output. Don't replace it with another rating. No other code change in this revision.

## 9. Validation and release

Check the source of the blocked drains page and two more service pages: no `AggregateRating` remains. Purge any page cache, then check again. URL Inspection live test on the blocked drains page. **Google guidance [M01]:** the manual action removes rich result eligibility; it doesn't affect how the pages rank in web search. Ari checks the Manual Actions report for its state and next steps. No timing for a review or reprocessing is promised.

## 10. Measurement, monitoring and open items

Monitor the Manual Actions report and the service pages' source after every plugin update. Open: the producer of the `Service` node, the rendered output, and a review of the other service pages. If Ari later collects genuine reviews, rating markup on these pages still needs to meet the review guidelines [M07]. No rich result, ranking, traffic or timing outcome is promised.
