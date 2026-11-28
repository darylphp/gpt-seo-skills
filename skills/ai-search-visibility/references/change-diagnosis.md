# Change Diagnosis

Everything in this file is operating method unless a source ID says otherwise.

## 1. Confirm the change

- Name the measure that changed: AI impressions, observed links, Search clicks, visits or qualified outcomes.
- Check that the compared periods use the same property, report, filters, search type and date basis (Pacific Time). Recent days can be preliminary.
- Treat exported zeros that were `~` or `-` in the report as unavailable [G-002, G-003].
- Check the report still appears for the property. A missing report means checking the setting and impression volume [G-002].

## 2. Check, in this order

1. **Documented data problems:** Search Console data anomalies for the period [G-026] and Google documentation changes [G-017].
2. **The Search generative AI control:** the effective setting for every property covering the affected pages, overrides on child properties, and when and by whom any change was made. An exclusion removes links, impressions and traffic from the covered features [G-004].
3. **Eligibility of the affected pages:** index status, canonical, snippet rules in HTML and headers, robots.txt and rendering [G-009].
4. **Releases:** templates, plugins, CDN and security rules, migrations, robots.txt and content changes, with dates converted to Pacific Time.
5. **Segments:** page, page group, country, device and search type, and the same pages' standard Search performance.
6. **Demand and season:** whether searches for the topics changed.
7. **Product changes:** feature availability in the market, presentation changes and model changes Google has announced. AI Mode and AI Overviews may use different models, so they can move differently [G-010].
8. **Ranking updates:** Google's Search Status Dashboard for the period, checked live.

## 3. Weigh competing causes

| Possible cause | Evidence for | Evidence against | Check that would settle it | Confidence |
| --- | --- | --- | --- | --- |

Keep three confidences apart: that a defect exists, that it caused the change, and that the proposed action will help. Timing alone doesn't prove a cause. Where a verified defect already explains the change, fix it first rather than inventing other causes.

## 4. Decide

- Fix verified defects first, starting with those that keep priority pages out of Search or its AI features.
- Don't rewrite content to chase a previous AI answer.
- Don't call a drop a penalty without a manual action or policy evidence.
- Hand crawl, indexing and rendering problems to technical SEO work, and content gaps to content evidence work.
- Set a review date that allows for the documented timing of the change, and compare like with like.
