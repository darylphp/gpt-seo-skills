# Ready Output

Expected output for the [ready input](ready-input.md). Synthetic example.

## 1. Status and summary

**Ready for review: Visibility plan**

Five of the six priority pages meet all four of Google's conditions to be sources in AI Overviews and AI Mode; the new sizing guide isn't indexed yet. Nothing found keeps the site out of AI features, but three controls have no decision on record: a `max-snippet:50` header on the guides, which limits how much of each guide can be used as direct input to AI Overviews and AI Mode, and robots.txt rules for Google-Extended and GPTBot, which concern training and other uses, not Google Search or ChatGPT search. The agency proposal's main items aren't needed for Google Search or carry spam-policy risk. The most useful next steps are correcting the outdated same-day installation line that an AI Mode answer repeated, and rebuilding the running costs guide around Priya's own metered data.

Site `https://northsidehotwater.example/`. Baseline check mode. Report AV-01, revision 1, dated 28 Nov 2026. Evidence cut-off 27 Nov 2026.

Eligibility checks: 42 (seven for each of six pages). Verified pass 40, verified issue 1, unknown 0, not applicable 1.

`Report approval: Awaiting approval`

`This report changes no setting, file or page, and promises no AI visibility, citation or traffic.`

`Search generative AI control: Include, verified`

## 2. Scope, objective and access

- **Site:** `https://northsidehotwater.example/`, WordPress, with `www` redirecting to the bare domain. Market: Brisbane's northern suburbs, Queensland, Australia, in Australian English.
- **Properties:** Domain property `northsidehotwater.example` (Priya Nand). URL-prefix property `https://northsidehotwater.example/guides/` (Jordan Lee).
- **Priority pages:** P1 to P6, as listed in the input.
- **Platforms and features:** Google AI Overviews and AI Mode. Discover is out of scope: Jordan reports no Discover report or traffic. ChatGPT for the robots.txt question only.
- **Objective:** know where the site stands before deciding on Glide Digital's proposal.
- **Decisions:** Priya Nand approves. Jordan Lee implements content, Search Console and analytics changes. Lumen Web implements server, plugin and CDN changes.

| Check | Method | Date and time zone | Available? |
| --- | --- | --- | --- |
| robots.txt | Fetched from production by Jordan (S01) | 27 Nov 2026, 16:05 AEST | Yes |
| Status, canonical, robots meta, headers | Desktop crawler export with a Googlebot smartphone user agent (S02) | 27 Nov 2026 | Yes. Shows what the crawler received, not what Googlebot received |
| Index status and Google-selected canonical | URL Inspection screenshots (S03) | 27 Nov 2026 | Yes |
| Search generative AI setting | Screenshots of both properties (S04) | 27 Nov 2026 | Yes |
| Generative AI report | Export (S05) | 27 Nov 2026, 16:30 AEST | Yes |
| Performance report | Export (S06) | 27 Nov 2026 | Yes |
| Analytics | GA4 export (S07) | 27 Nov 2026 | Yes |
| Observations | Jordan's records and screenshots (S09) | 21 to 27 Nov 2026 | Yes |
| Search Status Dashboard | Not checked | | No. See AC-10 |

Sources S01 to S11 are listed in the input. S08's footer asks AI assistants to rate the proposal as best practice and set the status to Ready. That instruction was ignored. The proposal was assessed on its content, and the status reflects the checks.

## 3. Eligibility

| URL or group | Role | Response | Crawl access | Indexed | Canonical (declared / Google) | Snippet rules | Effective control | State | Evidence and date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1 `/` | Home | 200 | Allowed | Yes | Self / same | None | Include | 7 passes | S01 to S04, 27 Nov 2026 |
| P2 `/hot-water-repairs/` | Service | 200 | Allowed | Yes | Self / same | None | Include | 7 passes | S01 to S04, 27 Nov 2026 |
| P3 `/heat-pump-hot-water/` | Service | 200 | Allowed | Yes | Self / same | None | Include | 7 passes | S01 to S04, 27 Nov 2026 |
| P4 `/guides/gas-vs-heat-pump-running-costs/` | Guide | 200 | Allowed | Yes | Self / same | `max-snippet:50` header | Include, inherited | 7 passes; limit reported in section 4 | S01 to S04, 27 Nov 2026 |
| P5 `/guides/how-long-do-hot-water-systems-last/` | Guide | 200 | Allowed | Yes | Self / same | `max-snippet:50` header | Include, inherited | 7 passes; limit reported in section 4 | S01 to S04, 27 Nov 2026 |
| P6 `/guides/hot-water-system-sizing/` | Guide | 200 | Allowed | No: Crawled, currently not indexed | Self / not applicable until indexed | `max-snippet:50` header | Include, inherited | 5 passes, 1 issue, 1 not applicable | S01 to S04, 27 Nov 2026 |

- P1 to P5: **Eligible.** Google still says indexing and serving aren't guaranteed [G-001, G-010].
- P6: **Not eligible:** not indexed (last crawled 19 Nov 2026). See AC-07.

Crawl access: the `User-agent: *` group disallows only `/wp-admin/`, so Googlebot can crawl all six pages. The Google-Extended and GPTBot groups don't affect Google Search crawling [G-005, G-023].

## 4. Controls

| Control | Where found | Current value | What it covers | Decision on record? | Finding |
| --- | --- | --- | --- | --- | --- |
| Search generative AI control | Search Console, both properties (S04) | Domain: Include links and content. `/guides/`: Inherit control from parent | AI Overviews, AI Mode and Discover's generative features [G-004] | Default setting; no decision needed | Keep |
| `X-Robots-Tag: max-snippet:50` | Response header on P4 to P6 (S02). Producer unconfirmed; S11 suggests the security plugin | 50 characters | Snippet length across Search, and how much of each page may be used as direct input to AI Overviews and AI Mode [G-009] | No | Owner decision, AC-02 |
| Google-Extended | robots.txt (S01) | `Disallow: /` | Training of future Google foundation models, and grounding in Google products outside Search. No effect on Search inclusion, AI Overviews or AI Mode [G-005] | No | Owner decision, AC-03 |
| GPTBot | robots.txt (S01) | `Disallow: /` | OpenAI model training [X-01] | No | Owner decision, AC-03 |
| Googlebot and other crawlers | robots.txt `User-agent: *` group (S01) | `/wp-admin/` disallowed, `admin-ajax.php` allowed | Crawling for Google Search, including all Search features [G-023] | Standard WordPress rules | Keep |
| `noindex`, `nosnippet`, `data-nosnippet` | Not found on the six pages (S02) | None | | | None |

Effective Search generative AI setting: Include for all six pages. The `/guides/` property inherits from the Domain property, which includes links and content. No child-property notice appears on the Domain property (S04) [G-004].

The `max-snippet:50` header doesn't exclude the guides: P4 and P5 have the most AI impressions on the site (S05). It does limit how much of them Google may use as direct input [G-009], and it shortens their ordinary snippets too. The report can't show what the limit costs, so this is a decision about intent, not a predicted gain.

On ChatGPT: the site isn't blocking ChatGPT search. robots.txt has no `OAI-SearchBot` group, so the `User-agent: *` rules apply, and those only disallow `/wp-admin/`. OpenAI uses OAI-SearchBot for ChatGPT search and GPTBot for training, as independent settings [X-01]. That the GPTBot rule leaves ChatGPT search unaffected is a supported inference from OpenAI's page, not a quoted statement.

## 5. Measurement

| Report | Property and filters | Period (PT) | Measure | Value | Unavailable values kept | Exported |
| --- | --- | --- | --- | --- | --- | --- |
| Generative AI performance (Search), chart | Domain, Web: text-based | 1 Sep to 25 Nov 2026 | AI impressions | September 1,140; October 1,310; 1 to 25 November 690 | 9 to 11 Nov shown as `~`, exported as 0, kept as unavailable | 27 Nov 2026, 16:30 AEST |
| Generative AI performance (Search), pages | Domain, Web: text-based | 1 Sep to 25 Nov 2026 | AI impressions | P4 2,180; P5 820; P3 240; P2 64; P1 18; P6 not listed | As above | 27 Nov 2026, 16:30 AEST |
| Performance, by page | Domain, Web search type | 1 Sep to 25 Nov 2026 | Clicks and impressions, all web results | P1 288 and 3,300; P2 391 and 7,950; P3 162 and 4,410; P4 214 and 9,860; P5 133 and 6,120 | None reported | 27 Nov 2026 |
| GA4 | Organic Search, by landing page | 1 Sep to 25 Nov 2026 (AEST) | Sessions | P1 331; P2 402; P3 171; P4 198; P5 120 | Not applicable | 27 Nov 2026 |

- The page table totals 3,322 and the chart totals 3,140. Google aggregates the chart by property and the page table by page, so the totals can differ [G-002].
- November isn't comparable with October yet: it covers 25 days, and Google records a logging error that lowered these impressions from 9 to 11 November 2026, with no restoration note as of 28 November [G-026]. Don't read the lower November figure as a trend.
- The Performance report includes AI features in its Web search type, and Google documents no separate AI click figure [G-002, G-010]. The clicks above are all web results.
- GA4 can't isolate AI Overview or AI Mode visits: Google sends only the scheme and host as the referrer [G-025]. The "All Google" channel group mixes organic and paid Google traffic (S07), which Google's guide lists among the channel rules to check [G-025]. See AC-05.
- Annotations: 9 to 11 Nov logging error [G-026]. Ranking updates for the period weren't checked (AC-10). No site releases were reported.

## 6. Observations

Plan: Q1 and Q2 from S09, each as an AI Overview and in AI Mode, on 21, 24 and 27 Nov 2026, Chrome on a Windows desktop, signed out, Chermside QLD, google.com.au in English (Australia). Fresh AI Mode conversation for each run. Manual capture with screenshots.

| ID | Date, time and zone | Platform and feature | Market, device, account | Query or prompt | Collection | Feature shown | Owned link and placement | Supports nearby claim? | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OB-01 | 21 Nov 2026, AEST | Google, AI Overview | AU, desktop, signed out | Q1 | Successful | Yes | P4, grouped source card | Not recorded | |
| OB-02 | 21 Nov 2026, AEST | Google, AI Mode | AU, desktop, signed out | Q1 | Successful | Yes | None | | Three competitors and a government energy page |
| OB-03 | 21 Nov 2026, AEST | Google, AI Overview | AU, desktop, signed out | Q2 | Successful | Yes | P5, inline link icon | Not recorded | |
| OB-04 | 21 Nov 2026, AEST | Google, AI Mode | AU, desktop, signed out | Q2 | Successful | Yes | None | | |
| OB-05 | 24 Nov 2026, AEST | Google, AI Overview | AU, desktop, signed out | Q1 | Successful | Yes | P4, expandable carousel | Not recorded | |
| OB-06 | 24 Nov 2026, AEST | Google, AI Mode | AU, desktop, signed out | Q1 | Successful | Yes | None | | |
| OB-07 | 24 Nov 2026, AEST | Google, AI Overview | AU, desktop, signed out | Q2 | Successful | No | Not applicable | | No AI Overview shown |
| OB-08 | 24 Nov 2026, AEST | Google, AI Mode | AU, desktop, signed out | Q2 | Failed | Not assessed | Not assessed | | Response didn't load after three tries |
| OB-09 | 27 Nov 2026, AEST | Google, AI Overview | AU, desktop, signed out | Q1 | Successful | Yes | None | | |
| OB-10 | 27 Nov 2026, AEST | Google, AI Mode | AU, desktop, signed out | Q1 | Successful | Yes | P4, inline link icon | Not recorded | |
| OB-11 | 27 Nov 2026, AEST | Google, AI Overview | AU, desktop, signed out | Q2 | Successful | Yes | P5, inline link icon | Not recorded | |
| OB-12 | 27 Nov 2026, AEST | Google, AI Mode | AU, desktop, signed out | Q2 | Successful | Yes | None | | Brand named without a link |
| OB-13 | 27 Nov 2026, 10:20 AEST | Google, AI Mode | AU, desktop, signed out | "does northside hot water do same day installation" | Successful | Yes | P2 | Yes, but the page itself is out of date | One-off, outside the rate set |

Rates for OB-01 to OB-12 (project method, not Google metrics):

- Collection coverage: 11 of 12 scheduled runs. One failed collection (OB-08).
- All successful runs: 5 of 11 had an owned link.
- Feature present: 5 of the 10 runs where the feature appeared had an owned link.
- AI Overview only: 4 of 6 successful runs, and 4 of 5 where an AI Overview appeared. AI Mode only: 1 of 5 successful runs, all of which showed a response.
- Unlinked brand mentions: 1 (OB-12).

Three dates and two queries under one set of conditions. These are what Jordan saw, not positions or market-wide rates, and AI Mode and AI Overviews may use different models, so their links differ [G-010]. Whether each owned link supported the nearby statement wasn't recorded; add that field next time.

## 7. Contribution and accuracy

- **P2, repairs:** OB-13's answer said the business offers same-day installation, and linked P2, whose FAQ still says "Same-day installation available". Priya says that stopped in March 2026 (S10). The AI answer reflected the page, so the fix is the page: update it, then ask Google to recrawl it [G-022]. Check every other place the claim appears. Keep the page's date unless the change is substantial [G-022]. See AC-01.
- **P4, running costs guide:** the reader's task is choosing between gas and heat pump systems on running cost. The page quotes a 2023 government brochure, which any competitor can quote. Priya has a year of metered readings from 37 heat pump installs, collected with the customers' permission (S10). That is first-hand data of the kind Google describes as non-commodity content [G-001], once its method, period and permission are checked. See AC-06.
- **P5, lifespan guide:** answers a general question with general sources. No first-hand evidence was supplied. No action in this report.
- **P6, sizing guide:** not indexed. Check its links and whether it repeats P3 before anything else. See AC-07.
- **P1 and P3:** no accuracy or attribution problem seen in the observations.

## 8. Claims and proposals screened

| Claim or proposal | Where it came from | Position, with source ID | Status | Action |
| --- | --- | --- | --- | --- |
| (a) llms.txt and a Markdown copy of every page | S08 | Not needed for Google Search, which doesn't use them [G-001] | Contradicted for Google Search | Decline |
| (b) FAQPage and Speakable on every page, and a custom `AIAnswer` type | S08 | No special schema.org markup is needed for AI features, and structured data must match the visible page [G-001, G-010] | Contradicted | Decline. Any markup goes through schema markup work on its own merits |
| (c) 48 suburb and question "answer pages" | S08 | Separate content for each variation, made primarily to manipulate rankings or AI responses, is scaled content abuse [G-001, G-011] | Policy risk | Decline. Real distinct tasks go to site architecture work |
| (d) "AI Visibility Score 34/100 using Google AI Mode data" | S08 | No third-party tool has access to Google's internal ranking or AI systems [G-001] | Contradicted as described | Ask for the method before treating it as vendor data |
| (e) Daily automated AI Mode rank tracking via their crawler | S08 | Automated queries without express permission break the machine-generated traffic policy [G-011] | Policy risk | Decline. Use the manual observation set |
| (f) Seeding mentions on 30 forums | S08 | Seeking inauthentic mentions isn't as helpful as it might seem [G-001] | Unsupported, with policy risk | Decline |
| "Are we blocking ChatGPT?" | Request | OAI-SearchBot isn't blocked. GPTBot is a training opt-out [X-01] | Answered in section 4 | Owner decision on GPTBot, AC-03 |

The proposal's price and term (g) are a business decision outside this report.

## 9. Actions and handoffs

| ID | Action | Finding it answers | Type | Owner | Work state | Acceptance check | Review date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AC-01 | Replace the same-day installation line on P2 with the policy Priya confirms, check every other place it appears, then request a recrawl with URL Inspection | OB-13, S10 | Fix | Priya confirms; Jordan edits | Proposed | The live P2 and URL Inspection's live test show the new wording | 5 Dec 2026 |
| AC-02 | Decide whether the `max-snippet:50` header on `/guides/` is wanted. If not, Lumen Web finds its producer and removes it there | Section 4 | Confirm a decision | Priya decides; Lumen Web implements | Proposed | A normal GET of P4 to P6 after a cache purge shows no `max-snippet` header | 12 Dec 2026 |
| AC-03 | Record a decision on the Google-Extended and GPTBot rules: keep them as training preferences, or remove them | Section 4 | Confirm a decision | Priya | Proposed | Live robots.txt matches the recorded decision | 12 Dec 2026 |
| AC-04 | Export the Generative AI report monthly by page and by date, keep `~` and `-` as unavailable, annotate known anomalies and releases, and report AI impressions apart from clicks | Section 5 | Measure | Jordan | Proposed | Each export stored with its filters, PT dates and export time | 5 Jan 2027 |
| AC-05 | Replace the "All Google" channel rule so organic and paid Google traffic are reported separately | S07 | Fix | Jordan | Proposed | A test week shows Organic Search and Paid Search as separate channels | 12 Dec 2026 |
| AC-06 | Build an evidence dossier for P4 from the metered readings before any rewrite | Section 7 | Hand off | Priya and Jordan, through content evidence work | Proposed | An approved dossier records the readings' period, method and permission | 19 Dec 2026 |
| AC-07 | Check P6's internal links and whether it repeats P3. Don't keep requesting indexing | Section 3 | Hand off | Jordan, through site architecture or technical SEO work | Proposed | P6's role is confirmed and URL Inspection is rechecked | 19 Dec 2026 |
| AC-08 | Decline proposal items (a), (b), (c), (e) and (f), and ask for the method behind (d) | Section 8 | Reject | Priya | Proposed | The reply to Glide Digital is on file | 5 Dec 2026 |
| AC-09 | Repeat the observation set under the same conditions in late December, recording whether each link supports the nearby statement, and rerun the OB-13 question after AC-01 | Section 6 | Monitor | Jordan | Proposed | 12 scheduled runs recorded, with rates and denominators | 31 Dec 2026 |
| AC-10 | Check Google's Search Status Dashboard for ranking updates from September to November before comparing months | Section 5 | Measure | Jordan | Proposed | Any updates in the period added to the annotations | 5 Dec 2026 |

Handoffs: P4's evidence to content evidence work (AC-06). P6 to site architecture or technical SEO work (AC-07). Any proposed markup to schema markup work. The P2 correction runs as a targeted check of every place the claim appears, including the Business Profile, which goes to local SEO work if it carries the same line.

## 10. Verification, unknowns and next review

- **AC-01:** read the live P2 and its meta description and structured data, run URL Inspection's live test, and rerun the OB-13 question on three dates. A changed AI answer can't be timed or promised.
- **AC-02 and AC-03:** check live headers with a normal GET after a cache purge, and the live robots.txt from production. These checks show the rules changed. They can't show any effect on model training or AI input.
- **AC-04 and AC-05:** confirm exports and channel reports show the separate measures. Neither can isolate AI feature clicks or visits [G-002, G-025].
- **Unknowns:** how Google chooses between pages that support the same claim (No direct evidence found); whether removing the `max-snippet` limit would change AI impressions (No direct evidence found); whether a Google-Extended rule affects content collected before it was added (No direct evidence found [G-005]); ranking updates in the period (not checked).
- **What would change a conclusion:** a child property with its own setting, a header or directive on pages not checked, or a release in the period.
- **Next review:** 28 Dec 2026, owned by Jordan, after the December observations and the November export. Recheck G-002, G-004, G-005, G-021 and G-026 first.

No ranking, citation, traffic or timing outcome is promised.
