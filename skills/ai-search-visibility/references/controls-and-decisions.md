# Controls and Decisions

## 1. What each control covers

Google describes three uses of crawled content: training foundation models, grounding answers in products outside Search, and grounding AI features in Search. It says its controls let site owners manage them separately [G-021].

| Control | Set in | Covers | Doesn't do |
| --- | --- | --- | --- |
| Search generative AI control | Search Console: Settings, then Search generative AI | Whether content is used for grounding or shown, links included, in AI Overviews, AI Mode and Discover's generative features [G-004, G-021] | Doesn't affect AI training, Merchant Center or Google Ads choices, and isn't a ranking or inclusion signal for the rest of Search [G-004] |
| Google-Extended | robots.txt | Whether content is used to train future generations of foundation models for commercially available Google generative AI products, and for grounding in those products apart from Search [G-005] | Doesn't affect inclusion in Google Search and isn't a ranking signal. Grounding in Search AI features is managed by the Search Console control [G-005] |
| GoogleOther | robots.txt | Google's generic crawler for non-Search fetches, such as research and development crawls [G-021, G-023] | Doesn't affect Search [G-021] |
| Preview controls: `nosnippet`, `max-snippet`, `data-nosnippet` | Robots meta tag, `X-Robots-Tag` header, or HTML attribute | Snippets and previews across Search, AI Overviews and AI Mode included. `nosnippet` and `max-snippet` also stop or limit content used as direct input for AI Overviews and AI Mode [G-009, G-021] | They apply to all of Search, not only AI features. Robots meta limits don't stop the use of structured data, apart from `article.description` and other creative-work descriptions [G-009] |
| `noindex` | Robots meta tag or `X-Robots-Tag` | Keeps the page out of Search, AI features included [G-021] | Can't remove a page from AI features alone |
| Googlebot rules in robots.txt | robots.txt | Crawling for Google Search, including Discover and all Search features [G-023] | A disallowed page's own robots rules can't be read [G-009]. A crawl block isn't an AI-only control |

Google-Extended has no separate crawler or user agent string. Google's other crawlers record each page's Google-Extended status when they crawl it [G-005, G-023]. Google states that it intends to support a shared machine-readable training preference signal in early 2027 [G-005, G-021]. Treat that as a stated plan, not a current control, and recheck before advising on it.

## 2. Goal to control

Google's controls page maps goals to settings [G-021]:

| Goal | Control |
| --- | --- |
| Take part in everything | Change nothing: allow Googlebot, don't disallow Google-Extended, and leave the Search Console control on include |
| Leave Search AI features, stay in Search, allow training | Set the Search Console control to exclude. Don't disallow Google-Extended |
| Stay in Search and its AI features, limit training and grounding in other Google products | Disallow Google-Extended in robots.txt |
| Leave Search AI features and limit training and other grounding | Both of the above |
| Keep a passage out of snippets, or limit their length | `data-nosnippet`, `max-snippet` or `nosnippet` |
| Leave Search completely | `noindex` |
| Make paywalled content available, with a snippet in AI Overviews and AI Mode | Paywalled content structured data with `data-nosnippet` or `max-snippet` |

## 3. Consequences to state before any change

- **Excluding in Search Console:** the site's links and content won't appear in the covered features, and it gets no traffic or impressions from them. Other sites' content can still appear and may look similar. Crawled content can't be used as input for an AI response or preview. Google says changes generally take a few days, with content typically excluded within one to two days after the control goes live, and some content taking longer because of caching and propagation [G-004].
- **`nosnippet` or `max-snippet:0`:** ordinary text snippets go too, across Search [G-009].
- **Disallowing Google-Extended:** no change to Search inclusion, AI Overviews or AI Mode [G-005]. Google's page doesn't say what happens to content collected before the rule. No direct evidence found for removal from a model already trained.
- **`noindex`:** the page leaves Search entirely [G-021].
- **Merchant Center and Google Ads:** separate choices that the Search Console control doesn't override [G-004].

## 4. Deciding and recording

Everything in this section is operating method.

- A control decision belongs to the site owner, because it turns on licensing, revenue, privacy and brand objectives, not on SEO alone. Lay out the options and consequences. Never make, schedule or simulate the change.
- Record the current effective setting and rules before proposing any change. Never propose a change blind.
- robots.txt and Search Console settings are not access controls. Use authentication for confidential content.
- A control with no decision on record is a question for the owner. Report **Urgent: Possible unintended exclusion** only when it keeps priority pages out of Search or its AI features. A Google-Extended disallow or a GoogleOther rule never meets that test on its own, because neither affects Search.
- Draft a change record for approval:

```text
Site, hosts, paths and Search Console properties:
Objective: Search participation / previews / training / non-Search grounding / removal from Search
Control and where it is set:
Source IDs and the date they were checked:
Current value and effective setting, with its source property:
Requested value:
Consequences, including lost impressions and traffic:
Uses and products not affected:
Dependencies: plugins, CDN, templates, Merchant Center, Ads:
Approver and authority:
Implementation date, time and time zone:
Expected timing, with its source:
Technical check after the change:
Outcome evidence, or Unverified:
Recovery action, owner and trigger:
Next review:
```

## 5. Where controls hide

- SEO plugins can set robots rules per post, per taxonomy or site-wide. Themes, server configuration, CDNs and security plugins can add `X-Robots-Tag` headers. Check the rendered page and the response headers, not only the plugin screen.
- robots.txt can be a static file, generated by the CMS or rewritten by a plugin or CDN. Fetch the live file from the production host.
- A migration can carry staging rules into production.
- After an authorised change, recheck the live headers, HTML and robots.txt, then the Search Console setting for every covering property. Record the time, and compare the reports later without treating timing as proof.
