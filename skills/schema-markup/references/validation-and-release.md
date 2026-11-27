# Validation and Release

IDs in brackets refer to the [source register](source-register.md). Text marked **Google guidance** paraphrases that source. Everything else is operating method.

## 1. Validation route by case

| Case | Route | How to read the result |
| --- | --- | --- |
| A Google feature the Rich Results Test supports | Rich Results Test on the code and the deployed URL, plus a check of the facts against the page [M04] | Fix critical errors. Assess recommended-property warnings against the facts that exist. A pass is not eligibility or appearance |
| Descriptive-only markup, such as `Service` | Schema Markup Validator for syntax and vocabulary, plus the property map and the deployed output [M04] | No Rich Results Test detection is expected and is not a failure |
| Site name | Schema Markup Validator, then URL Inspection on the home page [M06] | The Rich Results Test does not support site names |
| Any markup | URL Inspection live test on representative URLs | Confirms Google can fetch and render the page now. Not a promise of indexing or a feature |
| After rollout | The matching Search Console rich result report, where one exists, and the Manual Actions report [M01, M02] | Watch for new invalid items after template, plugin or theme changes |

**Google guidance [M01, M02]:** test with the Rich Results Test and URL Inspection, validate during development, deploy to a few pages first, then monitor the rich result reports, because templating or serving problems can break markup after release.

**Google guidance [M18]:** the Rich Results Test accepts JSON-LD, Microdata and RDFa, defaults to a smartphone user agent, and ignores comments inside JSON-LD even though the JSON-LD standard does not allow them.

## 2. Before release

Record for each Add, Repair, Consolidate or Remove decision:

- the producer to change and the setting, template or file, with the environment the draft assumes
- the URLs or template variants it affects, and a small first group to deploy to before the rest
- the cases that must pass (for example, one business node with the confirmed phone on every sampled page) and the cases that must stay unaffected (for example, every `Event` node on class pages)
- how to recover: the previous setting, template or file, and who can restore it
- caching, script optimisation and consent tools that could change the output, and whether a cache purge is needed
- who verifies production and how

## 3. Release check mode

1. Take the approved decisions and property map as the specification. Name its revision and approver.
2. Fetch or obtain the production source HTML and rendered output for each representative URL. Record the date, device and tool.
3. Compare node by node: the types, `@id` values and references, every property value against the page and the confirmed fact, and the producers. Note any block that should have gone and is still there.
4. Run the validation route for each feature from section 1. Record each result with its date and settings.
5. Give each decision one work state: implemented, technically verified, or not verified with the reason. A Rich Results Test pass on a code snippet does not show the change is live.
6. Repairs found in the check go back into the decisions as new Repair items, with the evidence.

## 4. A rich result that is missing or was lost

**Google guidance [M05]:** check in this order.

1. Does the page appear in Google Search at all? If not, a rich result will never show.
2. Can Google index the page with its markup? Markup on a duplicate rather than the canonical page is not used.
3. Test on desktop and mobile. Some rich results appear on one device type only, such as breadcrumbs on desktop [M11].
4. Common causes: the page hasn't been crawled since the change, Google can't access it, the markup is incorrect, there is a policy issue or manual action, or the feature isn't available in that place.
5. Google doesn't guarantee a rich result for any page, and may decide another result type serves the query better.

Then read the specific feature guide's troubleshooting section. Record which checks were possible and which stay `Not verified`.

## 5. Work states

Keep five states separate for every decision: **proposed**, **approved**, **implemented**, **technically verified** and **outcome reviewed**. Proposed is the default. Approval, a CMS save or a passing test does not move a decision past its own state.

## 6. Measuring the result

Report each outcome separately:

1. Technical validity: valid items, warnings and errors.
2. Detection: whether URL Inspection and the Search Console reports see the markup.
3. Eligibility: whether the page meets the current feature requirements.
4. Appearance: impressions and clicks for the relevant search appearance, where Search Console reports it.
5. Organic performance: clicks, impressions, position and conversions for the affected pages and queries.
6. Confidence: whether a change is causal, correlated or unresolved.

**Google guidance [M02]:** test on a few pages first, comparing before and after, using pages with several months of Search Console data that seasonality or timeliness won't skew, and compare performance over a few months.

A missing report is not evidence of zero exposure. Account for seasonality, page changes, results-page changes, indexing, algorithm updates and other releases before claiming any effect. Never report markup as a ranking or AI visibility gain.

## 7. Recheck triggers

Revalidate the affected templates after: a Google structured data documentation change, a plugin, theme, page builder or ecommerce update, a redesign or migration, canonical or URL changes, changes to the business name, address, phone or hours, price, stock, variant, shipping or return changes, author or date changes, review system changes, and any new error in a Search Console report or a manual action.
