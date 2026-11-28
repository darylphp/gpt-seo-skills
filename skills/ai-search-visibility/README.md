# AI Search Visibility Skill

Check whether one site's priority pages can appear as sources in Google's AI Overviews and AI Mode, which controls govern how its content is used, what can and can't be measured, and what has actually been observed. The skill returns a 10-section report: the status and summary, scope and access, eligibility, controls, measurement, observations, contribution and accuracy, claims and proposals screened, actions and handoffs, and verification and unknowns.

It has three modes. A **baseline check** establishes where a site stands, for example before buying an "AI SEO" service. A **control decision** maps the owner's goal, such as leaving AI Overviews or limiting AI training, to the control that serves it, with the consequences and a change record to approve. A **change diagnosis** explains a drop in AI impressions or citations, weighing competing causes before naming one.

## Start here

1. Describe the site: the domain, its Search Console properties (the Domain property and any URL-prefix properties), the pages that matter, the market, and who decides on controls. See [scope and intake](references/scope-and-intake.md) and the [synthetic input](examples/ready-input.md).
2. Supply what you have: robots.txt, URL Inspection results, screenshots of Settings, then Search generative AI, for every property that covers the pages, the Generative AI performance report export, and any notes from searches you've run.
3. Ask for a report. Example request: "Use the AI Search Visibility Skill on our site. Tell us whether our pages can appear in AI Overviews and AI Mode, which AI controls we have and why, and what's worth doing."
4. Review the findings and decide the actions. The skill changes nothing itself.

The status line says what happens next. **Ready for review: Visibility plan** and **Ready for review: Control decision** are ready for the owner. **Checks open: Provisional findings** names the checks still needed. **Urgent: Possible unintended exclusion** means priority pages are being kept out of Search or its AI features with no decision on record. **Blocked: Confirm the scope** and **Blocked: Supply the evidence** name what's missing.

## What it does not do

- Change a Search Console setting, robots.txt, a header or a page, or approve a control change.
- Treat Google-Extended as a way out of AI Overviews, a missing report as zero exposure, or an observation as a ranking.
- Query Google automatically, or claim access to an account or report it didn't see.
- Apply Google's rules to ChatGPT, Perplexity or Copilot. Each platform is checked against its own documentation.
- Recommend llms.txt, special "AI schema", content chunking, a page per fan-out query, or bought mentions for Google Search.
- Promise rankings, citations, traffic or timing.

## Package layout

- [SKILL.md](SKILL.md) and `references/` are the runtime files, intended for Claude, ChatGPT and Codex. Compatibility is not verified until platform tests are recorded.
- `agents/openai.yaml` is optional interface metadata for Codex. Claude does not use it.
- `examples/` contains a synthetic baseline check with its output, a blocked request, and an urgent change diagnosis.
- [Acceptance tests](tests/acceptance-tests.md) define behaviour and package checks, and `tests/check-package.py` runs the automatable checks.
- [Claude setup](platforms/claude.md) and [ChatGPT and Codex setup](platforms/chatgpt.md) cover installation.
- [Changelog](CHANGELOG.md) tracks revisions.

## Status

Unreleased draft. Package checks have passed. No behaviour case has been run, and the skill has not been installed or invoked on any platform. The [acceptance tests](tests/acceptance-tests.md) record each state separately.

## Installation

Keep the runtime folder named `ai-search-visibility` when staging it for installation. Copy `SKILL.md` and `references/` together, preserving relative paths. The runtime uses Markdown only and has no scripts or service dependencies.

## Where it fits

The skill works on its own, and runs when an AI search question comes up rather than at a fixed point in the content process. It hands page decisions, such as whether a fan-out page should exist, to the Site Architecture Skill (`skills/site-architecture/`), missing proof and outdated claims to the SEO Content Evidence Skill (`skills/seo-content-evidence/`), crawl, indexing and rendering defects to the Technical SEO Audit Skill (`skills/technical-seo-audit/`), structured data questions to the Schema Markup Skill (`skills/schema-markup/`), and Business Profile facts to the Local SEO Audit Skill (`skills/local-seo-audit/`). The SEO Strategy Skill (`skills/seo-strategy/`) routes AI feature questions to an AI visibility check, which this skill provides. Each of those skills is under review in its own pull request. Equivalent records from your own process work in their place.

## Workflow provenance

The method follows the Google Generative AI Search Operating Playbook v1.4 (File 06): the eligibility gate, content-use and preview controls, the measurement framework, the manual observation protocol and the suspected-loss workflow. It keeps the evidence IDs from the Evidence and Observation Ledger v1.4 (File 07). Google's 24 November 2026 pages on generative AI controls, attribution and ranking principles were published after both files, so the [source register](references/source-register.md) records them as additions, along with every difference from the playbook. Other platforms are covered from their own documentation, which File 06 leaves outside its Google scope. The examples are synthetic, and no employer, client or private material is included.
