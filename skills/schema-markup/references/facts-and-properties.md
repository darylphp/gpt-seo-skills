# Facts and Properties

IDs in brackets refer to the [source register](source-register.md). Text marked **Google guidance** paraphrases that source. Everything else is operating method.

## 1. Evidence labels

Give every source and every finding one label.

| Label | Meaning |
| --- | --- |
| Observed | Opened, fetched, rendered or tested in this work. Record the URL or file, the date, the tool and its settings, and what it showed. |
| Supplied | Provided by the user and not independently checked: page source, a testing-tool export, a plugin settings screenshot, a Search Console screenshot or a note. Record who supplied it and when. |
| Inference | A conclusion drawn from labelled premises. Name the premises and keep the uncertainty. |
| Not verified | The check was needed but no evidence was available. Never report it as passed. |

Give confidence as High (direct evidence and a clear applicable rule), Medium (good evidence with a gap) or Low (indirect evidence, one sample or an untested assumption).

## 2. What each source can and cannot show

| Source | Can show | Cannot show |
| --- | --- | --- |
| Source HTML | The markup the server sends before scripts run, and which block it sits in | Markup added later by scripts, tag managers or widgets |
| Rendered output | The markup after scripts run, for that request, device and consent state | What Google's own rendering received, or other template variants |
| Rich Results Test | Which Google rich results it can detect in a URL or snippet, with errors and warnings, and a preview for some features [M04, M18] | Facts, policy compliance, appearance in results, or features it does not support, such as site names [M06] |
| Schema Markup Validator | Schema.org vocabulary and syntax across all types, without Google feature warnings [M04] | Google support, eligibility or whether the facts are true |
| URL Inspection, indexed result | What Google recorded at its last crawl, including detected structured data | Whether today's deployment works |
| URL Inspection, live test | Whether Google can fetch and render the page now, and what markup it detects | That the page will be indexed or a feature shown |
| Search Console rich result reports | Valid and invalid items for supported features across crawled pages | Pages not yet crawled, or the cause of a missing appearance |
| Plugin or CMS settings | Which component is set to output which node | What actually reaches the page after caching and other plugins |
| Business records | The approved fact and its owner | Whether the page shows it |

Comments inside JSON-LD are ignored by the Rich Results Test but are not supported by the JSON-LD standard, so remove them before publishing [M18].

## 3. Inventory every producer

List every structured data block on each sampled URL.

| Block | Format | Types and `@id` | Producer | In source or rendered only | Key facts stated | Conflicts or gaps |
| --- | --- | --- | --- | --- | --- | --- |

Look for every component that can output markup: the theme, the SEO plugin, ecommerce, events, booking or review plugins, the page builder, a review widget, custom code in the theme or a snippets plugin, and the tag manager. Several blocks or formats on one page are not an error in themselves. Problems are conflicting facts about the same entity, two identities for one real entity, broken references, and nodes the page doesn't support.

Before turning off a component's output, check what else it produces. An events plugin that also outputs every `Event` node cannot simply be switched off. Prefer changing the setting that owns a node, so one producer owns each major node or template.

## 4. The page truth record

Record, for each sampled URL:

- the canonical URL and whether it is meant to be indexed
- the page's purpose and its main entity
- each visible fact markup could carry: where it appears, its authoritative source, its owner and how often it changes
- facts that are visible but unconfirmed, and facts that are confirmed but not visible

**Google guidance [M01, M02]:** don't mark up content that is not visible to readers, even if it is accurate, and don't create blank or empty pages just to hold structured data. Markup goes on the page it describes, and duplicate pages should carry the same markup.

If a fact is wrong or unconfirmed on the page, the fix starts on the page. Send claims that need proof to the SEO Content Evidence Skill, and Business Profile facts to the Local SEO Audit Skill.

## 5. The property map

Build it before any code.

| Node | Property | Value | Visible where | Authoritative source | Owner | Guide marks it | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |

`Guide marks it` is Required, Recommended, Optional or `Not checked`, from the feature guide opened for this work. `Status` is Confirmed, Missing or Conflicting.

Rules:

- **Google guidance [M01]:** include every required property for the feature, or the markup is not eligible for it. Use the most specific applicable type and properties.
- **Google guidance [M02]:** it is more important to supply fewer, complete and accurate recommended properties than many incomplete, badly formed or inaccurate ones.
- A Missing or Conflicting property stays out of any draft. If it is required, the decision that needs it waits, and the report status is **Facts needed: Confirmation list open**.
- Never fill a property because a plugin exposes the field or a tool warns that an optional property is missing. Assess recommended-property warnings against the facts that actually exist.
- Never invent or approximate reviews, ratings, review counts, prices, sale dates, availability, GTINs or other identifiers, dates, authors, addresses, phone numbers, opening hours or credentials.
- Dynamic values from the CMS must be escaped and valid JSON, and they must change when the visible value changes.

## 6. One entity graph

- Give each real reusable entity (the website, the business, a person, a product) one node with a stable absolute `@id`, such as `https://example.com/#organization`.
- Reference that node by `@id` from other nodes and pages instead of copying it with different details. Where a reference sits in a block on a page that does not include the full node, also give the referenced entity's name and URL, so the reference is meaningful on its own.
- Keep names, URLs, logos, phone numbers and profile links consistent across every producer.
- Use canonical absolute URLs.
- **Google guidance [M01]:** a page can contain several items, nested under a main item or marked up separately, and items that belong together can be linked with `@id`. Include the main type that reflects the page's focus.

Stable identifiers and linked nodes make markup easier to maintain and less likely to conflict. No evidence shows they improve rankings or AI inclusion, so never present them that way.

## 7. Scripts, caching and server output

**Google guidance [M02]:** Google can read JSON-LD that scripts or embedded CMS widgets insert into the page. **Merchant Center guidance [M09]:** structured data used by Merchant Center must be in the HTML returned by the server, not generated by scripts after the page loads, and must match the values shown to users.

Operating rule: prefer markup the server or CMS template outputs, because it is easier to inspect and maintain. Wherever it comes from, verify the rendered output on production. Caching, script optimisation and consent tools can change or remove markup after release, so test the live URL as well as staging.
