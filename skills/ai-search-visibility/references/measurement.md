# Measurement

## 1. Keep the chain apart

This section is operating method. Measure each link of the chain separately, and only where data exists:

1. **Eligibility**: indexed, snippet-eligible and included by the control.
2. **AI impressions**: links shown in Search or Discover generative features.
3. **Observed links**: a link seen in a recorded observation.
4. **Clicks and visits**: Search clicks and analytics sessions.
5. **Engagement**: meaningful actions on the site.
6. **Qualified outcomes**: enquiries, sales or bookings that meet the business's definition.

Never call impressions traffic, or an observed citation a visit.

## 2. Generative AI performance report (Search)

From Google's help page [G-002]:

- It covers AI Overviews and AI Mode. Data from Search Labs experiments is excluded.
- Its one metric is impressions: how often links to the site appeared in a generative AI feature.
- Data can be grouped by page, country, date and device (desktop, tablet, mobile). A search type filter separates "Web: text-based" from "Web: multimodal" searches, which include Google Lens and Circle to Search.
- Dates are in Pacific Time.
- The report usually doesn't appear when a site hasn't had enough impressions in these features. It may also be missing if the site is excluded.
- Data grouped by country, device or date is aggregated by property, and data grouped by page is aggregated by page, so chart and table totals can differ.
- Chart and table data can be exported. Values shown as `~` or `-` become zeros in the export.
- The data is included in the standard Performance report's Web search type, and the usual 1,000-row limit applies.
- Pages are grouped by the final URL after redirects, and most data is assigned to the canonical URL.

Operating rules: record the property, filters, search type, date range in Pacific Time and export time. Keep unavailable values as unavailable, not zero. Don't add the report's impressions to Performance report totals, which already include them. A missing report means checking the setting and impression volume; it isn't proof of zero exposure or a penalty.

## 3. Performance report and clicks

Google counts AI features in the standard Performance report under the Web search type [G-010], and the Generative AI report includes data from that search type [G-002]. Google doesn't document a separate click metric for AI features, so clicks from AI Overviews and AI Mode are blended with other web results. Report Search clicks as Search clicks.

## 4. Discover generative features

The Discover report is separate [G-003]. An impression counts each link that scrolls into view, once per result per session. Data can be grouped by page, country and date, in Pacific Time. The Pages dimension shows the canonical page that supplied the information, not the page a user landed on. Access is staged, so a missing report can also mean the property doesn't have it yet. Daily chart values under a threshold can be hidden but still count in totals, and `~` or `-` become zeros in exports. Keep Search and Discover figures apart: their counting rules differ, so their totals can't be added.

## 5. Analytics

Google Search uses an origin referrer policy, so the referrer contains only the scheme and host [G-025]. Analytics tools usually classify these visits as organic search. If they show as referral or direct, check custom channel rules, referral exclusions and filters [G-025]. Google's guide describes no parameter or referrer that separates AI Overview or AI Mode visits [G-025]. Don't claim analytics isolates them unless a verified source shows how.

Other platforms differ. OpenAI says ChatGPT adds `utm_source=chatgpt.com` to referral URLs [X-02]. See [other platforms](other-platforms.md).

## 6. Annotations

Annotate the period before comparing:

- Documented Search Console data anomalies [G-026]. As checked on 28 November 2026, a logging error lowered Generative AI report impressions for Search from 9 to 11 November 2026, with no note that the data was restored. A similar error from 13 to 17 August 2026 was restored on 21 August.
- Google documentation changes [G-017], and ranking updates on Google's Search Status Dashboard, checked live for the period.
- Site releases, template and plugin changes, migrations, robots.txt and control changes, outages and tracking changes.

## 7. Baseline procedure

Operating method:

1. Confirm access to each report and record availability. If a report isn't available, record why, who can fix access, the fallback, and what the fallback can't show.
2. Export at least three months before any planned change, by page and by date.
3. Record the property, report, filters, search type, Pacific Time dates and export time. Convert local release times to Pacific Time before comparing days.
4. Group URLs by role, template and purpose.
5. Add the annotations above.
6. Compare changed pages with similar pages that didn't change, where possible.
7. Use analytics for landing-page outcomes and conversions, without claiming it isolates AI features.
8. Report direction, size, uncertainty and other explanations. Avoid false precision on small numbers.

## 8. Measures and their limits

| Measure | Use | Limit |
| --- | --- | --- |
| Search generative AI impressions | Trend and page-level visibility in AI Overviews and AI Mode | Not clicks, rankings, queries or conversions |
| Discover generative AI impressions | Trend for publishers in Discover | Counted differently from Search |
| Search clicks | Demand captured from Search overall | AI feature clicks are blended in |
| Organic landing sessions | Behaviour on the site | Consent, attribution and channel rules apply. Can't isolate AI features |
| Qualified outcomes | Business value | Needs clean definitions and CRM checks |
| Observed link rate | Directional presence in defined observations | See [observations](observations.md). Not a market-wide rate |

## 9. Reporting language

Use: "This page meets the documented conditions, but appearance isn't guaranteed." "The report shows impressions; it doesn't show the queries or the clicks behind them." "We saw this link under these conditions; it may differ by user, market and date." "The drop started after the change, but the data doesn't prove the change caused it."

Avoid: "We'll rank in AI Overviews." "Schema makes Google cite the page." "This tool shows Google's internal AI score." "More citations mean more traffic."
