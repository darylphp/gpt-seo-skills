# Feature Support

IDs in brackets refer to the [source register](source-register.md). Text marked **Google guidance** paraphrases that source. Everything else is operating method.

## 1. Six outcomes that must stay apart

| Outcome | What it means | What it does not show |
| --- | --- | --- |
| Valid syntax | The JSON-LD, Microdata or RDFa parses | That the vocabulary is right or the facts are true |
| Valid Schema.org vocabulary | The types and properties fit the Schema.org data model | That Google supports a feature for them |
| Google feature support | Google currently documents a feature for this type and use case | That this page meets the feature's requirements |
| Eligibility | The page meets the feature's required properties, guidelines and policies | That Google will show the feature |
| Appearance | Google showed the feature for a particular search, device and place | That it will show again, or that it changed rankings |
| Ranking or traffic change | An observed change in position, clicks or conversions | That the markup caused it, without a suitable comparison |

**Google guidance [M01, M05]:** correct markup does not guarantee a rich result. Google's algorithm decides what fits each search and may show an ordinary result instead.

## 2. Feature status labels

Give each candidate type one status, with its source ID and the date the source was checked.

| Status | Meaning | Default treatment |
| --- | --- | --- |
| Google feature | Google's current documentation describes a search feature for this type and use case | Follow the feature's own guide for required properties, guidelines and availability |
| Descriptive only | Valid Schema.org vocabulary with no Google feature for this use, such as `Service` | Use only when it accurately describes the page for a stated consumer. No rich-result promise |
| Retired | Google stopped showing the feature or removed its documentation | Remove any Google visibility promise. Keep the markup only for a named non-Google consumer |
| Restricted | Google documents the feature, but this page, site type, region, language or device falls outside it | Record the restriction. Do not promise the feature |
| Needs verification | The current guide was not opened, or the guide and other sources disagree | Open the guide before deciding. Do not treat as eligible |

## 3. Google features in the gallery

**Google guidance [M03]:** Google's gallery of supported structured data, last updated 16 Oct 2026 and checked on 28 Nov 2026, lists Article, Breadcrumb, Carousel, Course list, Dataset, Discussion forum, Education Q&A, Employer aggregate rating, Event, Image metadata, Job posting, Local business, Math solver, Movie, Organization, Product, Profile page, Q&A, Recipe, Review snippet, Software app, Speakable, Subscription and paywalled content, Vacation rental and Video. It notes that actual appearance in results may differ. Site names use `WebSite` markup and have their own guide [M06].

Each feature has its own guide with required and recommended properties, content guidelines, and often limits on region, language or device. The gallery listing alone does not establish that a page is eligible. Open the feature guide before relying on any requirement, and record the date.

**Retired or removed [M15]:** Google removed the FAQ rich result documentation on 15 June 2026 after the feature stopped appearing in Search, and removed the practice problem documentation on 6 January 2026. FAQ, how-to, sitelinks search box and practice problem features were not in the gallery checked on 28 Nov 2026. **Google guidance [M15]:** Dataset markup is used by Dataset Search, not Google Search.

## 4. Starting points by page type

A starting point, not a recommendation to add every type. Always check the current feature guide.

| Page or purpose | Starting types | Google position | Main guardrail |
| --- | --- | --- | --- |
| Domain or subdomain home page | `WebSite` with the site name, plus one node for the business: `Organization` or the most accurate `LocalBusiness` subtype | Site names [M06]; Organization and Local business are in the gallery [M03] | One business identity with real details. Site names work at domain or subdomain level only |
| About or contact page | `AboutPage` or `ContactPage` referencing the business node by `@id` | Mainly descriptive | Do not create a second business node with different facts |
| A real location customers visit | The most accurate `LocalBusiness` subtype | Local business [M20] | Only the real location shown on the page. Suburb or service-area pages are not locations |
| Service page | `WebPage` with `mainEntity` set to `Service`, linked to the provider | Descriptive only: no dedicated feature in the gallery [M03, M16] | Accurate description, no rich-result promise |
| Product people can buy on the page | `Product` with `Offer`; `ProductGroup` for genuine variants | Merchant listings [M08] | Price, availability and identifiers must match the visible offer |
| Product page where people can't buy | `Product` | Product snippets [M08] | Reviews must meet the review guidelines [M07] |
| Category or collection | `CollectionPage`; `ItemList` only where it truthfully matches the visible list | No general category rich result. Carousels combine `ItemList` only with Recipe, Course list, Restaurant or Movie [M03] | Do not mark a category as one `Product` |
| Article or blog post | `Article`, `BlogPosting` or `NewsArticle` | Article is in the gallery [M03] | Real author, real dates, `dateModified` only for a meaningful update |
| Author or profile page | `ProfilePage` with a `Person` or `Organization` main entity | Profile page is in the gallery [M03] | The page must mainly be about that person or organisation |
| Breadcrumb trail | `BreadcrumbList` | Desktop only [M11] | Match a typical user path, not the URL structure. Keep visible breadcrumbs for mobile users |
| One question users can answer | `QAPage` | Q&A [M12] | Users must be able to submit answers. Not for FAQ pages or site-written answers |
| FAQ section | `FAQPage` only for a named non-Google consumer | Retired in Google Search [M15] | No Google FAQ visibility promise. Keep the visible questions if they help readers |
| Reviews or ratings | `Review` or `AggregateRating` nested in an eligible type | Review snippet, eligible types only [M07] | No self-serving business stars, no ratings from other sites |
| Video watch page | `VideoObject` | Video is in the gallery [M03] | The video must be the page's focus and accurately described |
| One event session | `Event` | Event [M10] | One event per page, real dates and place, price including fees |
| Anything else | Follow the exact current feature guide | Check | Do not copy a generic template without the feature's content guidelines |

## 5. Feature checks verified for this skill

**Site names [M06]:** add `WebSite` markup with `name` and `url` to the home page of the domain or subdomain. Subdirectory home pages are not supported. `alternateName` can list genuine alternatives. If the home page already has a `WebSite` node, add the site name properties to it rather than a second block. Duplicate home pages (http and https, www and non-www) carry the same markup. The Rich Results Test does not support site names: use the Schema Markup Validator, then URL Inspection.

**Breadcrumbs [M11]:** available on desktop in all regions and languages where Google Search is available. A `BreadcrumbList` needs at least two `ListItem` entries, and Google recommends breadcrumbs that reflect a typical user path rather than mirroring the URL.

**Events [M10]:** each event needs its name, start date and location. A physical event needs a street address. An online event uses a `VirtualLocation` with the URL where people join, and its start date must include a UTC offset. `eventAttendanceMode` records whether it is offline, online or mixed. Each event needs its own URL; pages listing schedules or several events are not supported. Products, services, sales, business hours and coupons are not events. The ticket offer price is the lowest available price including fees and service charges. The feature is available in a listed set of countries and languages, including Australia, the United Kingdom, Canada, India and the United States in English.

**Q&A [M12]:** users must be able to submit answers. A site-written FAQ, a product page with many questions, and a how-to guide, blog post or essay that answers a question are invalid uses. Google describes a separate education exception for user-submitted homework questions answered or selected by in-house experts.

**Products [M08, M09]:** product snippets suit pages where people cannot buy directly; merchant listings suit pages where they can, and the required merchant listing properties also make a page eligible for product snippets. Google recommends nesting the return policy and loyalty programme markup under `Organization`. Merchant Center's own guidance says its structured data must be in the HTML returned by the server and must match the values shown to users.

**Local business [M20]:** `name` and `address` are required; `telephone`, `url`, opening hours and others are recommended. Use the most specific `LocalBusiness` subtype possible, and give several types as an array rather than with `additionalType`. Review properties are recommended only for sites that capture reviews about other local businesses.

**Organization [M13]:** markup on the home page can help Google understand the organisation's administrative details and tell it apart from others; some properties can influence the logo shown. Google lists no required properties and recommends adding the ones that apply.

**Reviews:** see [policy risks](policy-risks.md), section 2.

## 6. Generative AI features

**Google guidance [M14]:** structured data isn't required for generative AI search and there's no special Schema.org markup to add. Google says sites don't need new machine-readable files, AI text files, markup or Markdown to appear in Google Search, and it doesn't use llms.txt.

Treat any request for "AI schema", markup for AI citations, or markup as a route into AI Overviews or AI Mode as a request to decline. Structured data stays useful for documented features and accurate machine-readable facts. Participation in Google's generative AI features is controlled and measured separately from markup.
