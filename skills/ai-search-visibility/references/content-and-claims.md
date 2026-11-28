# Content and Claims

## 1. How Google says links are chosen

Google's attribution page describes the process [G-022]:

- For AI Overviews on web searches, the system first checks that ranked results are relevant to the query, and snippets from those pages go to the model as a basis for the overview.
- The model may run related searches across the Search index, which Google calls query fan-out, to find pages covering other parts of the question.
- The response is written from the results found, then the pages that support the information are cited and linked.
- Links can appear as inline link icons, grouped source cards and expandable carousels. Google balances relevance and quality signals with a clear layout and a diverse set of sources.
- Google's systems hold sensitive topics to a higher bar, and are designed not to show an AI response where it could pose a safety risk, break Search policies or lack reliable consensus. Google's examples are sensitive "Your Money or Your Life" topics and breaking news with limited coverage.

Google says AI Overviews are evaluated with the same criteria as other results, and that no result receives preferential treatment [G-024]. It publishes no weights, citation score or rule for choosing between pages that support a claim equally well. No direct evidence found for any such formula.

## 2. What it means for priority pages

These points are supported interpretations and operating method:

- A page has to work as an ordinary search result before it can be a source.
- Fan-out means a page can be linked for one part of a question. Answer the real follow-up questions within the page that owns the task. Don't create a URL for each fan-out query: Google says creating separate content for each variation, primarily to manipulate rankings or generative AI responses, violates its scaled content abuse policy, and that a high quantity of pages doesn't make a site higher quality [G-001]. Send page decisions to site architecture work.
- Google describes non-commodity content as unique expert or experienced takes that go beyond common knowledge, and gives a first-hand review as an example of a unique perspective [G-001]. Record what each priority page adds: first-hand experience, original data, an expert's view, a tool or a clear decision aid. A source-led page mustn't imply first-hand work. Send claim and evidence gaps to content evidence work.
- Google advises making important information available as text, and building trust with clear sourcing and author or About pages [G-022].

## 3. Screening claims and proposals

| Claim or proposal | Google's position | Status for Google Search |
| --- | --- | --- |
| Add llms.txt, AI text files or Markdown copies | Not needed to appear in Google Search, and Google Search doesn't use them [G-001] | Contradicted |
| Add special "AI schema" | Structured data isn't required for generative AI search, and there's no special schema.org markup to add. It still helps rich result eligibility and must match the visible page [G-001, G-010] | Contradicted |
| Break content into small chunks | No requirement to do so [G-001] | Contradicted |
| Rewrite for AI or add long-tail phrasing | Not needed [G-001] | Contradicted |
| Seed or buy mentions | Seeking inauthentic mentions isn't as helpful as it might seem [G-001]. Buying links for ranking is link spam [G-011] | Unsupported, with policy risk |
| Build a page per fan-out query | Scaled content abuse when made primarily to manipulate rankings or generative AI responses [G-001, G-011] | Policy risk |
| A tool reports Google's internal AI data or score | No third-party tool has access to Google's internal ranking or AI systems [G-001] | Contradicted. Treat the figure as vendor data with its method |
| Block Google-Extended to leave AI Overviews | Google-Extended doesn't affect Search inclusion, and the Search Console control governs Search AI features [G-005, G-021] | Contradicted |
| Track AI Mode by scraping Google | Automated queries without express permission break the machine-generated traffic policy [G-011] | Policy risk |
| Refresh dates to look current | Avoid changing a page's date unless the content has substantially changed [G-022] | Contradicted |
| A guarantee of citation or placement | Indexing and serving aren't guaranteed [G-001] | Unsupported |

These statuses follow the project's claim register: Contradicted means primary documentation says otherwise, Unsupported means no direct evidence was found, and Policy risk means the proposal could break a spam policy. Record where each screened claim came from. A claim about another platform needs that platform's own documentation.

## 4. When an AI answer is wrong about the business

From Google's attribution page [G-022]:

- For inaccurate attribution, use the Feedback link below the AI response.
- If the error comes from the business's own page, update the page, then ask Google to recrawl it.
- For urgent cases, the Removals tool takes a URL out of all of Google Search for about six months, not only out of AI features. That's the owner's decision.
- Where copied content is credited to another site, ask syndication partners to block indexing, or file a copyright removal request. Legal decisions are the owner's.

Record the answer as an observation with a screenshot. Check the cited page's own claims before blaming the AI answer. Keep the page's date unchanged unless the content substantially changes [G-022].

## 5. Handoffs

| Finding | Hand to |
| --- | --- |
| Whether a page should exist, merge or serve a task | Site architecture work |
| What a page can truthfully claim, and the proof | Content evidence work |
| Crawl, indexing, rendering or response defects | Technical SEO work |
| Business Profile facts or Merchant Center data | Local SEO work, or the feed owner. Google says these feeds and profiles can help products and services appear in AI responses and other results [G-001] |
| Structured data accuracy, or markup proposed for AI features | Schema markup work |
| Analytics and conversion tracking | The analytics owner |
