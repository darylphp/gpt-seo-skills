# Observations

Everything in this file is operating method unless a source ID says otherwise.

## 1. What an observation can show

A manual observation records what was visible for one query or prompt, on one platform and feature, in one market, on one device and account state, at one time. It supplements Search Console. It is not a ranking position, a controlled experiment, a cause or a market-wide result. Google says AI Mode and AI Overviews may use different models and techniques, so the responses and links they show will vary [G-010]. Record them as separate features.

## 2. Plan the observation set

Before running anything, record:

- the query or prompt, word for word, and the query family and intent it represents
- the platform and feature (AI Overview, AI Mode, Discover, or another platform's feature) and any Labs or experiment status
- the country, language and location, and the device and browser
- the account state: signed in or out, and any known personalisation, such as preferred sources
- whether it's a fresh conversation or a follow-up, and the earlier prompts
- the capture method: manual, or a provider whose collection method is documented
- the owned page being evaluated, if any

Use more than one wording for a topic. One prompt isn't a topic.

## 3. Capture each run

| Field | Values |
| --- | --- |
| ID, date, time and time zone | For example `OB-01`, 21 Nov 2026, 09:40 AEST |
| Collection state | Successful, Failed (with the reason) or Feature unavailable in this market |
| Feature shown | Yes, No, or Not assessed. Recorded for successful collections only |
| Owned link | Yes or No, with the URL |
| Link placement | Inline link icon, grouped source card, expandable carousel or another layout seen. Google lists these formats [G-022]. Record what actually appeared |
| Brand mentioned without a link | Yes or No |
| Does the linked page support the nearby statement? | Yes, Partly, No or Unclear |
| Error or outdated claim in the answer | The statement and the page it cited |
| Screenshot | File name and where it's stored |
| Difference from earlier runs | What changed |

## 4. Repeat before describing a pattern

Run an important query on at least three separate dates under the same conditions before calling a result repeated. This is a project convention, not a Google requirement or a statistical guarantee. Keep contrary results. Repeat on another device or account state when personalisation could matter.

## 5. Support rates

Define the unit and the denominators before comparing periods. Count each observation once, even if it has several owned links.

| Rate | Calculation | Show with it |
| --- | --- | --- |
| All successful runs | Successful observations with an owned link / all successful observations | Includes runs where no AI feature appeared |
| Feature present | Successful observations with an owned link / successful observations where the feature appeared | The feature-present sample size |
| Collection coverage | Successful collections / scheduled attempts | The failed and unavailable counts and reasons |

Exclude failed collections and unavailable markets from both support rates, and report them separately. If a denominator is zero, write `Not applicable`, not 0%. Show the numerator, denominator, dates, query mix and method with every rate. Report unlinked mentions as a separate count.

## 6. Collection rules

- Never run, script or design automated queries to Google Search without express permission. Google's spam policies cover automated queries, including scraping results for rank checking [G-011].
- If a provider collects observations, record its platforms, markets, devices, sampling, freshness and method, and treat its figures as vendor data.
- Store screenshots with the observation record. Don't keep personal data from the results page.

## 7. Conclusions an observation can't support

- "Our page ranks first in AI Mode."
- "This source has a stable position."
- "The wording, schema, length or a link caused the citation."
- "No link means a penalty or a technical fault."
- "One signed-in result represents the market."
- "A cited page got a click or a sale."
