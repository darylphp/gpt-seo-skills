# Ready Input

Synthetic fixture. The business, people, URLs, phone numbers, address, plugins, prices, reviews and screenshots are fictional and supplied for simulation only. Nothing here is real search data, a real business record or a client result.

## Request

"Audit the structured data on our home page, our class pages and the knife set product page. Our developer says the SEO plugin handles schema. We'd like review stars next to our name in Google and FAQ rich results on the class pages, and we've heard schema helps with AI Overviews. Nadia approves any change and Tomás makes it."

## Page record

- Business: Saltbush Kitchen School, a cooking school with one teaching kitchen in West End, Brisbane, Queensland, Australia. Students attend classes at the kitchen or online. Australian English.
- Platform: WordPress with a theme, an SEO plugin, an events plugin that creates one page per class session, a shop plugin, a page cache plugin, and a review widget that shows the school's Business Profile rating on the home page.
- Owners: Nadia Cole (owner) confirms business facts and approves changes. Tomás Reyes (contract developer) implements.
- In scope, all self-canonical, indexable and returning 200 in Tomás's crawl export of 27 Nov 2026:
  - **U1** home page `https://saltbushkitchen.example/`
  - **U2** in-person class session `https://saltbushkitchen.example/classes/dumpling-night-2026-12-12/`
  - **U3** online class session `https://saltbushkitchen.example/classes/knife-skills-online-2026-12-05/`
  - **U4** product `https://saltbushkitchen.example/shop/three-piece-knife-set/`

## Evidence

All supplied by Tomás on 27 Nov 2026 unless stated.

| ID | Evidence |
| --- | --- |
| E01 | Saved page source for U1 to U4 |
| E02 | Rendered output from browser developer tools for U1 to U4, desktop, logged out, cookies accepted |
| E03 | Rich Results Test exports for U2 and U4, smartphone. U2: one valid Event item, no errors. U4: valid Product snippet and Merchant listing items, no errors, warnings for optional shipping, return policy and global identifier fields |
| E04 | Settings screenshots. SEO plugin: organisation type and details editable, site name "Saltbush Kitchen School", schema type for the "class" post type set to Article, FAQ block on. Theme: "Output business schema: On" (the theme's only schema output). Events plugin: "Structured data: On" |
| E05 | Note from Nadia Cole, 26 Nov 2026: "Our name is Saltbush Kitchen School, and plenty of people call us Saltbush Kitchen. Our number changed to (07) 5550 0456 in August; the old one was (07) 5550 0123. Students come to us at 3/48 Brolga Lane, West End QLD 4101. The knife set sale ended on 15 November, so it's $189 again. We don't use Merchant Center." |
| E06 | Search Console screenshots, 27 Nov 2026: no manual actions; Events report 2 valid items; Product snippets report 1 valid item |
| E07 | Class booking terms: U2 is "$95 per person plus a $4.50 booking fee per ticket"; U3 is "$45 per household plus a $2.00 booking fee" |

## What the pages and markup show

### U1 home page

Visible: the logo and the name "Saltbush Kitchen School"; phone (07) 5550 0456 and the West End address in the footer; links to `https://instagram.example/saltbushkitchen` and `https://facebook.example/saltbushkitchen`; the review widget showing "4.9 from 96 Google reviews"; an FAQ section with five questions the school wrote; footer office hours "Mon to Fri 9 am to 4 pm".

| Block | Producer | In | Content |
| --- | --- | --- | --- |
| B1 | SEO plugin | Source, every page | `WebSite` `https://saltbushkitchen.example/#website` (name "Saltbush Kitchen School", url, publisher) and `Organization` `https://saltbushkitchen.example/#organization` (name "Saltbush Kitchen School", url, logo `https://saltbushkitchen.example/assets/logo.png`, sameAs the two profile URLs), plus a `WebPage` node per page |
| B2 | SEO plugin FAQ block | Source, U1 | `FAQPage` with the five visible questions and answers |
| B3 | Theme | Source, every page | `LocalBusiness` with no `@id`, name "Saltbush Kitchen", telephone "(07) 5550 0123", the West End address, and `aggregateRating` 4.9 from 96 reviews filled from the review widget |

### U2 in-person class

Visible: "Dumpling night", Saturday 12 December 2026, 6 pm to 9 pm, at the West End kitchen with its address, "$95 per person plus $4.50 booking fee", "8 places left", a Book now link to `#book`, a class photo, and the breadcrumb Home > Classes > Dumpling night.

| Block | Producer | In | Content |
| --- | --- | --- | --- |
| B4 | SEO plugin | Source, every class page | `Article` with headline "Dumpling night", author `Person` named "admin", datePublished 2026-10-02 and dateModified 2026-11-27 (the plugin changes it on every save), and a `BreadcrumbList` matching the visible trail |
| B5 | Events plugin | Source | `Event`: startDate `2026-12-12T18:00`, endDate `2026-12-12T21:00`, offline attendance mode, scheduled status, `Place` with the school's name and West End address, image, description, offer price `95.00` AUD, availability InStock, booking URL, and `organizer` as an `Organization` named "Saltbush Kitchen" with the home page URL and no `@id` |

### U3 online class

Visible: "Knife skills online", Saturday 5 December 2026, 10 am to 11.30 am Brisbane time, "Live online class. Join at `https://saltbushkitchen.example/live/knife-skills/` after booking (login required)", "$45 per household plus $2.00 booking fee", a Book now link and the same breadcrumb pattern.

Markup: B4 as on U2, and B6 from the events plugin: `Event` with startDate `2026-12-05T10:00` and endDate `2026-12-05T11:30` (no UTC offset), online attendance mode, and a `Place` named "Online" carrying the West End street address, which the plugin copies from its default venue. Offer price `45.00` AUD. Organizer as in B5.

### U4 product

Visible: "Three-piece knife set", $189.00 including GST, "In stock", "Ships Australia-wide", 14 reviews from verified buyers averaging 4.6 shown on the page, "30-day returns" linking to `/returns/`, brand "Saltbush Kitchen School", SKU SKS-KNIFE-3.

Markup: B7 from the shop plugin in the source: `Product` with name, image, description, sku, brand, an `Offer` priced `169.00` AUD with availability InStock and the product URL, and `aggregateRating` 4.6 from 14 reviews. The shop plugin's sale price field still holds $169 with no end date. B1 and B3 also appear on U2, U3 and U4.

## Not supplied

The contact page (Nadia's note doesn't mention hours, and Tomás says the contact page shows 9 am to 5 pm), the Business Profile itself, any GTIN for the knife set (the supplier's specification lists none), shipping rates by product, Search Console Performance data, and any approval of a change.
