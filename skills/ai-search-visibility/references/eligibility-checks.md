# Eligibility Checks

## 1. Google's conditions

Google says a page must be indexed and eligible to be shown in Google Search with a snippet, fulfilling the Search technical requirements, and that the site must be included in Search generative AI features in Search Console [G-001, G-022]. Google's AI features page says there are no additional technical requirements [G-010]. Indexing and serving aren't guaranteed, even when a page meets them [G-001, G-010].

The four conditions:

1. Indexed.
2. Eligible to be shown with a snippet.
3. Meets the Search technical requirements.
4. Included through the Search generative AI control for the property that covers it.

## 2. Evidence for each check

The rest of this section is operating method: the evidence that settles each check and the common ways it goes wrong.

| Check | Evidence that settles it | Watch for |
| --- | --- | --- |
| Response | A normal GET of the canonical URL: the final status code and the redirect chain | Soft 404s, a challenge page or 403 from bot protection, CDN or location differences |
| Crawl access | robots.txt for the host, read for the Googlebot group that applies, plus access to required resources | Rules for `Google-Extended` or `GoogleOther` don't block Search crawling [G-005, G-023]. A Googlebot disallow stops Google reading the page's own robots rules [G-009] |
| Indexed | URL Inspection's indexed result with its date, or the Page indexing report | Indexable isn't indexed. A `site:` search isn't proof |
| Canonical | The declared canonical and the Google-selected canonical | The Generative AI report assigns most data to the canonical URL [G-002] |
| Snippet eligibility | The rendered robots meta tags, the `X-Robots-Tag` response header and any `data-nosnippet` regions, with the source of each rule | `nosnippet` and `max-snippet:0` remove the snippet and stop direct input to AI Overviews and AI Mode, and other `max-snippet` values limit both [G-009]. A rule sent only in a header doesn't show in the HTML |
| Technical requirements | The page returns successfully, Googlebot isn't blocked, and the page has indexable content | Main content that appears only after interaction or a failed script |
| Search generative AI control | Settings, then Search generative AI, for the property covering the URL and each parent above it [G-004] | Reading only the parent. A URL-prefix child property can override it [G-004] |

Record each check as one of:

- **Verified pass**: checked, with the evidence, method and date.
- **Verified issue**: checked, and it fails or limits the condition.
- **Unknown**: not checked, or not checkable with the access available. Name the next check and who can make it.
- **Not applicable**: the check doesn't apply, with the reason.

Describe a page as **eligible** only when all four conditions are verified passes. Otherwise write `Eligibility not verified:` and list the open checks, or `Not eligible:` and the verified issue. A `max-snippet` value above zero still allows a snippet, so record the snippet check as a verified pass and report the limit under controls.

## 3. Finding the effective Search Console setting

The default for all properties is to include links and content, and a property with a parent defaults to inheriting. It inherits from its closest parent that has stopped inheriting, or from the top-level Domain property if none has. A child property's owner can override the inherited setting at any time, and owners of the top-level Domain property see a notification when a child property overrides it [G-004].

So, for each priority URL:

1. List every property that covers it, from the Domain property down to the most specific URL-prefix property.
2. Record each property's setting and whether it inherits.
3. Take the effective setting from the most specific property that has its own setting, or from the Domain property if none does.
4. Record the source property, the setting, the evidence and the date. If any covering property wasn't seen, the effective setting is unknown.

## 4. Checks that are ordinary SEO, not AI requirements

Internal links, mobile layout, page speed, semantic HTML, accessibility and structured data can help readers and ordinary search work. Google doesn't list them as extra conditions for AI features [G-010]. Report problems with them as ordinary SEO findings and hand technical defects to technical SEO work, rather than labelling them AI requirements.

## 5. New pages

A new page that is indexable but not yet indexed isn't eligible yet. Check that relevant pages link to it and that it isn't a near-duplicate of an existing page. Requesting indexing again doesn't change eligibility. Hand a page that stays unindexed to technical SEO or site architecture work.
