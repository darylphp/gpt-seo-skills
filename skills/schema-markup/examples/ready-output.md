# Ready Output

Expected output for the [ready input](ready-input.md). Synthetic example: the business, people, URLs, prices and screenshots are fictional, and every figure is illustrative.

## 1. Status and summary

**Ready for review: Schema report**

The site sends two different identities for the school on every page, with an old phone number and a review rating that can't earn stars on the school's own pages, and the class and product markup states prices that don't match what customers pay. The fix is one business node owned by the SEO plugin, event prices that include the booking fee, a proper online location for the online class, and the knife set's current price. Review stars for the school's name, FAQ rich results and "schema for AI Overviews" are declined below, with what can be done instead.

Page set: U1 home page, U2 in-person class, U3 online class, U4 product. Mode: Audit. Report SM-2026-11-01, revision 1, dated 28 Nov 2026. Evidence cut-off 27 Nov 2026. Decisions: 1 Consolidate, 4 Repair, 3 Remove, 1 Keep, 1 Defer.

`Implementation approval: Awaiting approval`

`This report does not approve deployment or confirm any fact on the business's behalf.`

`Developer handoff: Ready after approval`

## 2. Page record

| ID | URL | Purpose and main entity | Canonical and indexing |
| --- | --- | --- | --- |
| U1 | `https://saltbushkitchen.example/` | Home page; the school | Self-canonical, indexable |
| U2 | `https://saltbushkitchen.example/classes/dumpling-night-2026-12-12/` | One in-person class session | Self-canonical, indexable |
| U3 | `https://saltbushkitchen.example/classes/knife-skills-online-2026-12-05/` | One online class session | Self-canonical, indexable |
| U4 | `https://saltbushkitchen.example/shop/three-piece-knife-set/` | One product people can buy | Self-canonical, indexable |

U2 and U3 represent the two variants of the events plugin's class template. Market: Brisbane, Australia, in English. Platform: WordPress with a theme, an SEO plugin, an events plugin, a shop plugin, a page cache plugin and a review widget. Nadia Cole confirms facts and approves; Tomás Reyes implements. The request asks for review stars next to the school's name, FAQ rich results on class pages and help with AI Overviews.

## 3. Evidence and access

| ID | Source | What it showed | Date | Settings or conditions | Label | Limits |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | Saved page source, U1 to U4 | Blocks B1 to B7 in the source HTML | 27 Nov 2026 | Saved by Tomás | Supplied | One saved copy per URL |
| E02 | Rendered output, U1 to U4 | No extra blocks added by scripts | 27 Nov 2026 | Desktop, logged out, cookies accepted | Supplied | Not checked with cookies declined or on mobile |
| E03 | Rich Results Test, U2 and U4 | U2: one valid Event. U4: valid Product snippet and Merchant listing, optional-field warnings | 27 Nov 2026 | Smartphone | Supplied | U1 and U3 not tested |
| E04 | Plugin and theme settings | Which component outputs which block; class post type set to Article | 27 Nov 2026 | Screenshots | Supplied | Settings, not output |
| E05 | Nadia's note | Name, alternate name, current phone, address, current knife set price, no Merchant Center | 26 Nov 2026 | Owner statement | Supplied | Hours not covered |
| E06 | Search Console | No manual actions; Events 2 valid; Product snippets 1 valid | 27 Nov 2026 | Screenshots | Supplied | No Performance data |
| E07 | Booking terms | Ticket prices and booking fees for U2 and U3 | Current | Owner's terms | Supplied | |

Not verified: the contact page's office hours; the phone number on the Business Profile; whether the events plugin can include booking fees and UTC offsets in its markup; rendered output with cookies declined; whether a more specific `LocalBusiness` subtype fits a cooking school. No page, account or tool was opened in this run. Every source above is Supplied.

## 4. Current markup and producers

| Block | URL or variant | Format | Types and `@id` | Producer | Source or rendered only | Key facts | Conflicts or gaps |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | Every page | JSON-LD | `WebSite` `#website`, `Organization` `#organization`, `WebPage` | SEO plugin | Source | Name "Saltbush Kitchen School", logo, two profile links | Second identity from B3 on every page |
| B2 | U1 | JSON-LD | `FAQPage` | SEO plugin FAQ block | Source | Five visible questions | Retired Google feature |
| B3 | Every page | JSON-LD | `LocalBusiness`, no `@id` | Theme | Source | Name "Saltbush Kitchen", phone (07) 5550 0123, address, rating 4.9 from 96 | Old phone; second identity; self-serving rating taken from another site |
| B4 | U2, U3 | JSON-LD | `Article`, `BreadcrumbList` | SEO plugin | Source | Author "admin"; dateModified moves on every save; visible breadcrumb trail | A class session is not an article |
| B5 | U2 | JSON-LD | `Event` | Events plugin | Source | Offline, West End `Place`, price 95.00 AUD, organizer "Saltbush Kitchen" with no `@id` | Price excludes the $4.50 fee; no UTC offset; organizer doesn't match the business node |
| B6 | U3 | JSON-LD | `Event` | Events plugin | Source | Online mode, `Place` "Online" with the West End street address, price 45.00 AUD | Wrong location type; required UTC offset missing; fee excluded |
| B7 | U4 | JSON-LD | `Product` with `Offer` and `AggregateRating` | Shop plugin | Source | Price 169.00 AUD, InStock, rating 4.6 from 14 | Stale sale price |

## 5. Feature fit

| Type | Outcome it serves | Feature status | Source ID and check date | Requirements and limits that matter here |
| --- | --- | --- | --- | --- |
| `WebSite` | Site name preference | Google feature | M06, 28 Nov 2026 | Home page of the domain; one `WebSite` node; not supported in the Rich Results Test |
| `LocalBusiness` | Business identity and details | Google feature | M20, 28 Nov 2026 | `name` and `address` required; `telephone` and `url` recommended; most specific subtype |
| `AggregateRating` on the business | Review stars | Restricted | M07, 28 Nov 2026 | Self-serving for the school's own pages, including widget reviews; ratings from another site not allowed |
| `FAQPage` | FAQ rich result | Retired | M15, 28 Nov 2026 | Documentation removed 15 Jun 2026 |
| `Article` | None on a class page | Restricted | M01, M03, 28 Nov 2026 | Article is a Google feature, but markup must reflect the page and a class session is not an article |
| `BreadcrumbList` | Breadcrumb in results | Google feature | M11, 28 Nov 2026 | Desktop only; at least two items; typical user path |
| `Event` | Event experience | Google feature | M10, 28 Nov 2026 | One event per URL; price includes fees; online events use `VirtualLocation` and a UTC offset; available in Australia in English |
| `Product` with `Offer` | Merchant listing and product snippet | Google feature | M08, 28 Nov 2026 | Price and availability must match the page; reviews must be genuine and visible [M07] |

The six outcomes stay separate. E03 and E06 show valid syntax and detected items for some pages. They don't show that the facts are right, that the pages are eligible, or that any feature will appear.

## 6. Decisions

| ID | URL or template | Node | Decision | Reason | Priority | Producer and owner | Work state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D01 | U1 (every page) | `WebSite` `#website` | Repair | Add "Saltbush Kitchen" as `alternateName`, which Nadia confirms is a genuine name [M06] | Planned | SEO plugin; Tomás | Proposed |
| D02 | Every page | Business node | Consolidate | Two identities with different names and phones. Keep one `LocalBusiness` node at `#organization`, owned by the SEO plugin, with the current phone, and turn off the theme's business schema (its only output) | High | SEO plugin and theme; Tomás | Proposed |
| D03 | Every page | `aggregateRating` on the business | Remove | Self-serving and taken from the Business Profile [M07]. It doesn't move to the consolidated node. The visible widget can stay | High | Theme (goes with D02); Tomás | Proposed |
| D04 | U1 | `FAQPage` | Remove | No Google FAQ rich result since June 2026 [M15] and no other consumer named. The visible FAQ section stays | Optional | SEO plugin FAQ block setting; Tomás | Proposed |
| D05 | Class template | `Article` | Remove | A class session is not an article [M01]; placeholder author; dateModified changes on every save. Set the class post type's schema to `WebPage` | Planned | SEO plugin; Tomás | Proposed |
| D06 | Class template | `BreadcrumbList` | Keep | Matches the visible trail and has three items [M11] | Not applicable | SEO plugin | Not applicable |
| D07 | Class template, in person (U2) | `Event` | Repair | Price must include the booking fee: 99.50 AUD [M10]. Add the +10:00 offset to start and end. Point `organizer` at `#organization` with the confirmed name and URL | High | Events plugin; Tomás | Proposed |
| D08 | Class template, online (U3) | `Event` | Repair | Replace the `Place` with a `VirtualLocation` using the visible join URL, add the required +10:00 offset, set the price to 47.00 AUD, and point `organizer` at `#organization` [M10] | High | Events plugin; Tomás | Proposed |
| D09 | U4 | `Product` `Offer` | Repair | Markup says 169.00 while the page and Nadia say 189.00. Clear the expired sale price field in the shop plugin. Keep the genuine, visible rating of 4.6 from 14 reviews | High | Shop plugin product data; Tomás, confirmed by Nadia | Proposed |
| D10 | Shop | Return policy and shipping markup | Defer | Optional fields. Whether the 30-day policy and shipping terms apply to every product isn't confirmed. The test warnings are not errors | Optional | Shop or SEO plugin; Nadia to confirm | Proposed |

Declined requests:

- **Review stars next to the school's name.** The school controls the reviews about itself, so its `LocalBusiness` pages aren't eligible for star snippets, including reviews shown through a widget, and ratings from other sites can't be aggregated into markup [M07]. Genuine product reviews on product pages, like the knife set's, can stay in `Product` markup.
- **FAQ rich results on class pages.** Google removed the FAQ rich result documentation on 15 June 2026 after the feature stopped appearing [M15]. Useful questions can still go on the page for readers.
- **Schema for AI Overviews.** Structured data isn't required for Google's generative AI features and no special markup is needed [M14]. These changes are for accurate facts and documented features only.

## 7. Property map

| Node | Property | Value | Visible where | Authoritative source | Owner | Guide marks it | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `WebSite` | `name` | Saltbush Kitchen School | Logo, header | E05 | Nadia | Required [M06] | Confirmed |
| `WebSite` | `url` | `https://saltbushkitchen.example/` | Address bar | Canonical | Tomás | Required [M06] | Confirmed |
| `WebSite` | `alternateName` | Saltbush Kitchen | Not on page; a name people use | E05 | Nadia | Optional [M06] | Confirmed |
| Business | `name` | Saltbush Kitchen School | Header, footer | E05 | Nadia | Required [M20] | Confirmed |
| Business | `address` | 3/48 Brolga Lane, West End QLD 4101, AU | Footer | E05 | Nadia | Required [M20] | Confirmed |
| Business | `telephone` | +61 7 5550 0456 | Footer, as (07) 5550 0456 | E05 | Nadia | Recommended [M20] | Confirmed |
| Business | `url` | `https://saltbushkitchen.example/` | Address bar | Canonical | Tomás | Recommended [M20] | Confirmed |
| Business | `logo` | `https://saltbushkitchen.example/assets/logo.png` | Header | B1 | Tomás | Not checked | Confirmed |
| Business | `sameAs` | The two profile URLs | Footer icons | B1 | Nadia | Not checked | Confirmed |
| Business | `openingHoursSpecification` | Omitted | Footer says 4 pm; contact page reportedly 5 pm | None | Nadia | Recommended [M20] | Conflicting |
| `Event` U2 | `offers.price` | 99.50 AUD | "$95 plus $4.50 booking fee" | E07 | Nadia | Lowest price including fees [M10] | Confirmed |
| `Event` U2 | `startDate`, `endDate` | 2026-12-12T18:00:00+10:00 to 21:00:00+10:00 | Class details | Event record | Tomás | Start date required [M10] | Confirmed |
| `Event` U3 | `location` | `VirtualLocation`, url `https://saltbushkitchen.example/live/knife-skills/` | "Join at ..." | Class page | Tomás | Required for online events [M10] | Confirmed |
| `Event` U3 | `startDate`, `endDate` | 2026-12-05T10:00:00+10:00 to 11:30:00+10:00 | Class details, Brisbane time | Event record | Tomás | Offset required online [M10] | Confirmed |
| `Event` U3 | `offers.price` | 47.00 AUD | "$45 plus $2.00 booking fee" | E07 | Nadia | Lowest price including fees [M10] | Confirmed |
| `Event` both | `organizer` | `#organization`, Saltbush Kitchen School, home URL | Class page footer | E05 | Tomás | Not checked | Confirmed |
| `Product` | `offers.price` | 189.00 AUD | Price block | E05 | Nadia | Not checked | Confirmed |
| `Product` | `aggregateRating` | 4.6 from 14 | Reviews section | Shop plugin review records | Nadia | Review guidelines [M07] | Confirmed |
| `Product` | `gtin` | Omitted: none exists | None | Supplier specification lists none | Nadia | Not checked | Missing |

Queensland doesn't use daylight saving, so +10:00 applies to every session on these dates.

Confirmation list (none blocks a decision in this revision):

1. Office hours: the footer and the contact page reportedly differ. Nadia confirms the current hours and fixes the page that's wrong; then `openingHoursSpecification` can be added.
2. Shipping and returns: Nadia confirms whether the 30-day policy and the shipping terms apply to every product (D10).
3. Business Profile phone: the Local SEO Audit Skill or Nadia checks that the profile shows (07) 5550 0456.

## 8. Draft markup and changes

**D01 to D03, SEO plugin and theme settings.** In the SEO plugin, set the organisation type to `LocalBusiness`, enter the phone and address, and add the alternate site name. In the theme, set "Output business schema" to Off. Expected output on every page, `Draft for developer review`, assuming the SEO plugin keeps its existing `@id` values:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://saltbushkitchen.example/#website",
      "url": "https://saltbushkitchen.example/",
      "name": "Saltbush Kitchen School",
      "alternateName": "Saltbush Kitchen",
      "publisher": { "@id": "https://saltbushkitchen.example/#organization" }
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://saltbushkitchen.example/#organization",
      "name": "Saltbush Kitchen School",
      "url": "https://saltbushkitchen.example/",
      "logo": "https://saltbushkitchen.example/assets/logo.png",
      "telephone": "+61 7 5550 0456",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "3/48 Brolga Lane",
        "addressLocality": "West End",
        "addressRegion": "QLD",
        "postalCode": "4101",
        "addressCountry": "AU"
      },
      "sameAs": [
        "https://instagram.example/saltbushkitchen",
        "https://facebook.example/saltbushkitchen"
      ]
    }
  ]
}
```

**D04 and D05, SEO plugin.** Turn off the FAQ block's schema output, keeping the visible block. Set the schema type for the "class" post type to `WebPage`, which removes the `Article` node and its placeholder author and leaves the `BreadcrumbList` in place.

**D07 and D08, events plugin.** If the plugin has settings for including fees in the price, the time zone offset and the online location, use them. If it doesn't, adjust the plugin's own `Event` node with a filter in a small site-specific plugin. Don't add a second `Event` block. Expected values inside the existing nodes, `Draft for developer review` (fragments, not standalone blocks):

```json
{
  "startDate": "2026-12-12T18:00:00+10:00",
  "endDate": "2026-12-12T21:00:00+10:00",
  "offers": {
    "@type": "Offer",
    "price": "99.50",
    "priceCurrency": "AUD",
    "availability": "https://schema.org/InStock",
    "url": "https://saltbushkitchen.example/classes/dumpling-night-2026-12-12/#book"
  },
  "organizer": {
    "@type": "LocalBusiness",
    "@id": "https://saltbushkitchen.example/#organization",
    "name": "Saltbush Kitchen School",
    "url": "https://saltbushkitchen.example/"
  }
}
```

```json
{
  "startDate": "2026-12-05T10:00:00+10:00",
  "endDate": "2026-12-05T11:30:00+10:00",
  "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
  "location": {
    "@type": "VirtualLocation",
    "url": "https://saltbushkitchen.example/live/knife-skills/"
  },
  "offers": {
    "@type": "Offer",
    "price": "47.00",
    "priceCurrency": "AUD"
  },
  "organizer": {
    "@type": "LocalBusiness",
    "@id": "https://saltbushkitchen.example/#organization",
    "name": "Saltbush Kitchen School",
    "url": "https://saltbushkitchen.example/"
  }
}
```

The fee and offset rules apply to every session the template produces, not only U2 and U3. The U3 offer keeps the plugin's existing availability and booking URL.

**D09, shop plugin.** Clear the expired $169 sale price on the knife set. Expected `Offer` price: `"189.00"` with `"priceCurrency": "AUD"`. Check other products for sale prices that outlived their sale.

## 9. Validation and release

| Decision | Validation route | Cases that must pass | Cases that must stay unaffected |
| --- | --- | --- | --- |
| D01 to D03 | Schema Markup Validator on U1 to U4; URL Inspection on U1. The site name isn't supported in the Rich Results Test [M06] | One business node with phone +61 7 5550 0456 on every sampled page; no `aggregateRating` on it; `alternateName` present | The visible review widget |
| D04, D05 | Page source of U1, U2 and U3 | No `FAQPage`; no `Article` on class pages | The visible FAQ section; the `BreadcrumbList` |
| D07, D08 | Rich Results Test on U2, U3 and one more session of each kind [M04] | Prices 99.50 and 47.00 AUD; offsets present; U3 uses `VirtualLocation` | Every other session still has its `Event` node |
| D09 | Rich Results Test on U4 | Price 189.00 AUD | Rating 4.6 from 14; availability InStock |
| All | URL Inspection live test on U1 to U4 [M01] | Google can fetch and render each page | |

Release order: export the SEO plugin and events plugin settings first, so they can be restored. Make the changes on U1 to U4 and their templates, purge the page cache, then check the source and rendered output again with cookies accepted and declined. Turning the theme setting back on would restore the old phone number, so recovery uses the exported SEO plugin settings instead. Tomás verifies production and records the date, tool and result for each row.

## 10. Measurement, monitoring and open items

Measure separately: test results (valid, warnings, errors); detection in URL Inspection and the Search Console Events, Product snippets and Merchant listings reports; eligibility against the current guides; appearance, where Search Console reports a matching search appearance; and organic clicks and impressions for the four URLs and the class template. A change in clicks after release can't be credited to markup without a comparison and other explanations ruled out [M02]. Review once URL Inspection shows the new markup on U1 to U4, then monthly for three months.

Recheck triggers: any update to the SEO, events or shop plugins or the theme; a new class format; a price, fee or phone change; and any new error in the Search Console reports.

Open items and handoffs:

- Office hours conflict: Nadia fixes the page first, then hours can be added to the business node.
- Business Profile phone: to the Local SEO Audit Skill.
- Shipping and returns markup: waits for Nadia's confirmation (D10).
- A more specific `LocalBusiness` subtype: optional. Check Schema.org's subtypes before release, and use an array if a second type is accurate [M20].

Every change is proposed. None is approved, implemented or verified. No rich result, ranking, traffic, AI citation or timing outcome is promised.
