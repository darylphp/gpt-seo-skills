# Urgent Output

Expected output for a change diagnosis. Synthetic example.

Request: "Our blog's AI Overview impressions have gone to nothing since mid-September. What happened?" From Mia Chen, owner of Tideway Kayak Tours, `https://tidewaykayaks.example/`, a kayak tour business in Noosa, Queensland. Supplied with it:

- S01: Generative AI performance report (Search) export, Domain property, by page and by date, 1 Aug to 25 Nov 2026 (PT), Web: text-based, exported 26 Nov 2026 at 15:10 AEST. `/blog/` pages: 600 to 760 impressions a week from August to 7 September, 410 in the week of 8 to 14 September, then 0 every week from 15 September. Tour pages: 130 to 170 a week throughout.
- S02: screenshots of Settings, then Search generative AI, 26 Nov 2026. Domain property `tidewaykayaks.example`: "Include links and content", with a notice that a child property overrides this setting. URL-prefix property `https://tidewaykayaks.example/blog/`: "Exclude links and content". Owners of the `/blog/` property: Mia Chen and Kai Rowe, a former contractor.
- S03: Kai's invoice dated 12 Sep 2026, with the line "Configured AI opt-out on blog property (test)". Mia: "I never asked for that. Kai finished with us in October."
- S04: URL Inspection screenshots for three blog posts, 26 Nov 2026: all indexed, Google-selected canonical matches the declared one. Live HTML and headers fetched the same day: no `noindex`, `nosnippet` or `max-snippet` rules.
- S05: robots.txt fetched 26 Nov 2026: `User-agent: *` with `Disallow: /wp-admin/` only. Mia's site change log shows no robots.txt change since June 2026.
- S06: Performance report, Web search type, `/blog/` pages: clicks 1,980 in August, 1,870 in September and 1,860 in October. Impressions within 3% of August in each month.
- S07: site change log: one plugin update on 3 Sep 2026, no other releases from 1 Sep to 30 Sep 2026.

## 1. Status and summary

**Urgent: Possible unintended exclusion**

The `/blog/` property is set to exclude links and content from Google's AI features, overriding the Domain property's include setting, and Mia has no record of approving it. Google says an excluded site gets no traffic or impressions from these features [G-004], which matches the blog's AI impressions falling to zero from the week of 15 September, three days after Kai's invoice records an "AI opt-out" test. Mia should confirm today whether any exclusion was wanted; if not, a `/blog/` property owner can set it back to inherit from the Domain property.

Site `https://tidewaykayaks.example/`. Change diagnosis mode. Report AV-07, revision 1, dated 28 Nov 2026. Evidence cut-off 26 Nov 2026.

Eligibility checks for three sampled blog posts: 21. Verified pass 18, verified issue 3 (the control on each post), unknown 0, not applicable 0.

`Report approval: Awaiting approval`

`This report changes no setting, file or page, and promises no AI visibility, citation or traffic.`

`Search generative AI control: Mixed by property, verified`

## 2. Scope, objective and access

- **Site and properties:** Domain property `tidewaykayaks.example` (Mia Chen). URL-prefix property `https://tidewaykayaks.example/blog/` (Mia Chen and Kai Rowe).
- **Pages:** `/blog/` posts, sampled through three posts in S04, and tour pages for comparison.
- **Market:** Australia. **Features:** AI Overviews and AI Mode. The exclusion also covers Discover's generative features [G-004]. The property has no Discover generative AI report, so Discover can't be measured here.
- **Objective:** explain the drop. **Decisions:** Mia Chen.

| Check | Method | Date and time zone | Available? |
| --- | --- | --- | --- |
| Search generative AI setting, both properties | Screenshots (S02) | 26 Nov 2026 | Yes |
| Change record | Invoice and owner statement (S03) | 12 Sep and 26 Nov 2026 | Yes |
| Index status, canonical, directives | URL Inspection and live fetch (S04) | 26 Nov 2026 | Yes, for three posts |
| robots.txt and releases | Live fetch and change log (S05, S07) | 26 Nov 2026 | Yes |
| Reports | Exports (S01, S06) | 26 Nov 2026, 15:10 AEST | Yes |
| Search Status Dashboard | Not checked | | No |

## 3. Eligibility

| URL or group | Role | Response | Crawl access | Indexed | Canonical (declared / Google) | Snippet rules | Effective control | State | Evidence and date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Three `/blog/` posts | Blog | 200 | Allowed | Yes | Self / same | None | Exclude, from the `/blog/` property | 6 passes, 1 issue each | S02, S04, S05, 26 Nov 2026 |

- Sampled blog posts: **Not eligible:** excluded by the `/blog/` property's Search generative AI setting. Other blog posts share the property, so the setting covers them too; their other checks weren't sampled.
- Tour pages are outside `/blog/` and take the Domain property's include setting.

## 4. Controls

| Control | Where found | Current value | What it covers | Decision on record? | Finding |
| --- | --- | --- | --- | --- | --- |
| Search generative AI control, Domain property | Search Console (S02) | Include links and content, with a child-override notice | AI Overviews, AI Mode and Discover's generative features [G-004] | Default | Keep |
| Search generative AI control, `/blog/` property | Search Console (S02) | Exclude links and content | The same features, for URLs under `/blog/` [G-004] | No. Kai's invoice calls it a test, and Mia didn't ask for it (S03) | Urgent: confirm intent, AC-01 |
| robots.txt and page directives | S04, S05 | No AI-related rules | | | None |

A child property overrides its parent until its own setting changes, and the Domain owner sees a notice when one does [G-004]. Draft change record for Mia's decision:

```text
Site, hosts, paths and Search Console properties: tidewaykayaks.example, /blog/ URL-prefix property
Objective: Search participation
Control and where it is set: Search generative AI control, Search Console, /blog/ property
Source IDs and the date they were checked: G-004, 28 Nov 2026
Current value and effective setting, with its source property: Exclude, set on the /blog/ property
Requested value: Inherit control from parent (Domain property: Include), if Mia confirms the exclusion wasn't wanted
Consequences, including lost impressions and traffic: blog pages become eligible again for AI Overviews, AI Mode and Discover's generative features. No impressions or traffic are guaranteed
Uses and products not affected: AI training, Merchant Center, Google Ads, ranking elsewhere in Search
Dependencies: none found
Approver and authority: Mia Chen, business owner and property owner
Implementation date, time and time zone:
Expected timing, with its source: Google says changes generally take a few days to take effect (G-004)
Technical check after the change: both properties' settings and the override notice rechecked
Outcome evidence, or Unverified: Unverified
Recovery action, owner and trigger: return to Exclude if Mia later decides to opt the blog out, with a recorded reason
Next review:
```

## 5. Measurement

| Report | Property and filters | Period (PT) | Measure | Value | Unavailable values kept | Exported |
| --- | --- | --- | --- | --- | --- | --- |
| Generative AI performance (Search) | Domain, Web: text-based, `/blog/` pages | 1 Aug to 25 Nov 2026 | AI impressions a week | 600 to 760 to 7 Sep; 410 for 8 to 14 Sep; 0 from 15 Sep | None shown in this period for these pages | 26 Nov 2026, 15:10 AEST |
| Same report | Domain, Web: text-based, tour pages | Same | AI impressions a week | 130 to 170 throughout | None | Same |
| Performance | Domain, Web search type, `/blog/` pages | Aug to Oct 2026 | Clicks | 1,980; 1,870; 1,860 | None | 26 Nov 2026 |

- The 13 to 17 August logging error was restored on 21 August, and Google lists no Search Console data anomaly in September 2026 [G-026]. The 9 to 11 November error lowered impressions across the report [G-026], but the blog was already at zero.
- The roughly 6% fall in blog clicks from August to October can't be split into AI and other results, because AI features are counted in the Web search type with everything else [G-010]. Don't attribute it to the exclusion.

## 6. Observations

None run. After any change, check two or three blog topics as AI Overviews and in AI Mode on three dates under fixed conditions, and record them with their denominators.

## 7. Contribution and accuracy

Not assessed in this diagnosis. No content change is recorded in the period (S07), and the evidence points to the setting.

## 8. Claims and proposals screened

None supplied.

## 9. Actions and handoffs

| ID | Action | Finding it answers | Type | Owner | Work state | Acceptance check | Review date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AC-01 | Confirm whether any exclusion of the blog was wanted | Section 4 | Confirm a decision | Mia Chen | Proposed | Decision recorded in the change record | 28 Nov 2026 |
| AC-02 | If it wasn't wanted, a `/blog/` property owner sets the property to "Inherit control from parent" | Section 4 | Fix | Mia Chen | Proposed | Both properties show include, and the override notice is gone | 1 Dec 2026 |
| AC-03 | Review who owns the `/blog/` property and remove access that's no longer needed | S02, S03 | Fix | Mia Chen | Proposed | Property users list matches current staff and contractors | 1 Dec 2026 |
| AC-04 | Export the report weekly by page for `/blog/` and tour pages, and compare from the change date | Section 5 | Measure | Mia Chen | Proposed | Weekly exports stored with filters and PT dates | 15 Dec 2026 |
| AC-05 | Check Google's Search Status Dashboard for ranking updates from August to November | Section 2 | Measure | Mia Chen | Proposed | Any updates added to the annotations | 5 Dec 2026 |

No handoffs. The defect is a setting, not a technical or content problem.

## 10. Verification, unknowns and next review

- **Confidence:** High that the exclusion is in place (S02). High that it explains the blog's zero AI impressions: Google documents that an excluded site gets no impressions from these features [G-004], the timing matches the invoice, the tour pages under the include setting kept their impressions, and no release, directive or data anomaly in the period fits. The timing alone wouldn't prove it. Low for any link between the exclusion and the 6% click change.
- **After AC-02:** recheck both properties' settings and the notice. Google says changes generally take a few days [G-004]. Returning impressions can't be timed or guaranteed.
- **Unknowns:** whether Search Console shows a history of setting changes (not checked); ranking updates in the period (AC-05); the Discover effect, which can't be measured without the report.
- **Next review:** 15 Dec 2026, owned by Mia, with two weekly exports after the change. Recheck G-004 and G-026 first.

No ranking, citation, traffic or timing outcome is promised.
