# Other Platforms

## 1. Rules

These rules are operating method:

- Keep a separate record for each platform: the product and feature, market, account state and date.
- Use the platform's own current documentation. Never transfer Google's eligibility conditions, controls, report definitions or myths to another platform, or the reverse.
- The entries below were checked on 28 November 2026. Recheck the platform's page before advising on a control.
- Promise no inclusion, citation or traffic on any platform.
- Keep each platform's measures apart. Google impressions, Bing citations and ChatGPT referrals are counted differently and can't be added together.

## 2. ChatGPT search (OpenAI)

From OpenAI's crawler overview [X-01] and publisher FAQ [X-02]:

| User agent | What OpenAI says it does | robots.txt effect |
| --- | --- | --- |
| `OAI-SearchBot` | Surfaces websites in ChatGPT search results | Sites opted out won't be shown in ChatGPT search answers, though they can still appear as navigational links [X-01]. OpenAI says not to block it if you want content included in summaries and snippets [X-02] |
| `GPTBot` | Crawls content that may be used to train OpenAI's generative AI foundation models | Disallowing it indicates the content shouldn't be used for that training [X-01] |
| `ChatGPT-User` | Visits pages when a user asks ChatGPT or a custom GPT a question, and supports GPT Actions. Not used for automatic crawling | Because visits are user-initiated, robots.txt rules may not apply [X-01] |
| `OAI-AdsBot` | Checks the safety of landing pages submitted as ads, and only visits those pages | Its data isn't used to train foundation models [X-01] |

- OpenAI describes each setting as independent [X-01]. Its page doesn't say that blocking GPTBot affects search, so "GPTBot rules leave ChatGPT search unaffected" is a supported inference, not a quoted statement.
- After a robots.txt change, OpenAI says its search systems can take about 24 hours to adjust [X-01].
- To keep a page out, OpenAI points to `noindex`, which its crawler can read only if it's allowed to crawl the page. A disallowed page may still surface as a link and title in ChatGPT Atlas [X-02].
- ChatGPT adds `utm_source=chatgpt.com` to referral URLs [X-02].
- OpenAI publishes IP address lists for each crawler [X-01].

## 3. Perplexity

From Perplexity's crawler page [X-03]:

- `PerplexityBot` is designed to surface and link websites in Perplexity search results, and isn't used to crawl content for AI foundation models. Perplexity recommends allowing it so a site appears in search results.
- `Perplexity-User` supports user actions. Because a user requested the fetch, it generally ignores robots.txt rules.
- Changes can take up to 24 hours to show in Perplexity's systems. Perplexity publishes its IP ranges as JSON files.

## 4. Microsoft Copilot and Bing

Microsoft announced AI Performance in Bing Webmaster Tools as a public preview on 10 February 2026 [X-04]. It reports citations across Microsoft Copilot, AI-generated summaries in Bing and select partner integrations: total citations, average cited pages, grounding queries (a sample of citation activity), page-level citations and trends over time. Microsoft says citation data doesn't indicate ranking, authority or a page's role in an answer. The announcement doesn't describe click or traffic data. Microsoft says Bing respects preferences expressed through robots.txt and other supported control mechanisms. Check Microsoft's current documentation before advising on a Copilot-specific control; none was verified for this register.

## 5. Platforms not listed

For Gemini apps, Claude or any other assistant, no entry was checked for this register. Find the platform's own documentation, record its check date, and write "No direct evidence found" where it's silent. Google-Extended covers grounding in Google's own products outside Search [G-005]. It doesn't control other companies' crawlers.
