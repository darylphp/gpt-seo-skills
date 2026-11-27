# Measurement and Diagnosis

IDs in brackets refer to the [source register](source-register.md). Text marked **Google guidance** paraphrases that source. Everything else is operating method.

## 1. Baseline

Record for each location: the date range, the comparison period, the time zone, the source of each number, which metrics are available, missing values and known changes in the period. Keep blanks, unavailable values and zeros distinct.

**Google guidance [G10]:** GBP performance data is available only for verified profiles, shows only the metrics that apply to the business, and includes both organic and Google Ads activity. Calls are clicks on the call button. Website clicks are clicks on the profile's website link. The searches report lists terms the profile appeared for and is not a rank report.

| Layer | Use | Do not claim |
| --- | --- | --- |
| Profile interactions | Location-level GBP metrics with their definitions | Every view is a unique prospect, or all activity is organic |
| Website visits | Tagged profile visits in analytics, with Search Console page and query data kept separate | Search Console isolates every profile or Maps visit |
| Enquiries | Tested calls, forms and bookings, with the tracking method | A click proves an enquiry |
| Business outcome | Qualified enquiries, booked work or revenue from business records | Every change came from SEO without attribution evidence |
| Visibility samples | Query, surface, location or grid points, device, date and tool | One sample represents every customer |

Do not add numbers from overlapping systems as if they counted separate people.

## 2. Tagging profile links

**Google guidance [G17]:** campaign parameters identify source, medium and campaign, and their values are case-sensitive.

**Operating method:** a starting pattern is `utm_source=google&utm_medium=organic&utm_campaign=gbp&utm_content=[location-id]`, adjusted to the business's existing naming. Use lower case and no personal data. Tag only the profile's links to the website, not internal navigation. Verify the tagged acquisition visit and the enquiry event separately. A working campaign tag does not prove a form was delivered, received or qualified. Check event trigger/counting, duplicates and test traffic, consent, reporting scope and business records where relevant. Mark each unavailable test Not verified; the audit does not submit a form or place a call without specific authority.

## 3. Diagnosing a visibility or enquiry problem

**Google guidance [G18]:** local results are mainly based on relevance, distance and prominence, which Google also calls popularity. Complete information, verification and genuine reviews can help. Nobody can pay for or request a better local ranking, and Google does not publish weights.

1. **Define the loss.** Missing profile, lower sampled position, fewer website visits or fewer enquiries. Compare like periods and check that collection stayed consistent.
2. **Check integrity.** Profile status, unexpected edits, changed category, address or hours, broken destinations and real business changes.
3. **Separate surfaces.** Map results, ordinary organic results, ads and AI features. Check whether the searcher location or query mix changed.
4. **Compare relevance and competition fairly.** A competitor's keyword-filled name or category is not something to copy.
5. **Check the rest of the funnel.** Website, tracking, demand, seasonality, campaigns and capacity, alongside SEO causes.
6. **Choose an action.** Fix an evidenced defect, improve a weak customer task, run a bounded test, collect data or monitor. State competing explanations and confidence.
7. **Set checks.** Record an acceptance check and a review trigger. Do not promise recovery within a fixed time.

Keep repeated rank or grid samples consistent: same queries, points, tool, device, language and timing where possible. Record failed or missing samples. A grid is a sample, not proof of cause or a universal ranking radius.

