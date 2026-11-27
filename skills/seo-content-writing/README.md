# SEO Content Writing Skill

Draft one page from an approved content brief and its approved evidence dossier, without inventing facts. The skill follows the writer route the brief chose, carries every claim with its conditions, marks each one with its claim ID for review, and sends gaps to their owner as numbered queries. It returns a 9-section output: the status and handoff, page and scope, the draft, a claim trace, the brief's acceptance tests, writer queries and deviations, a voice check, links and assets, and a handoff to QA and publishing.

A second mode, profile mode, builds the brand voice and editorial profile that briefs and drafts follow, from approved style rules, real writing samples, customer language and past corrections. It returns an 8-section profile.

## The six writer routes

| Route | Use it for | It never |
| --- | --- | --- |
| W1. Local Service | A real local service page | Invents local presence or swaps town names |
| W2. Affiliate Review and Comparison | An independent review, comparison or shortlist | Implies testing that didn't happen or picks winners by commission |
| W3. SaaS and B2B | A product, feature, use case or buying decision | Invents features, integrations, security claims or results |
| W4. Ecommerce Category | A collection readers browse and narrow | Writes filler for every facet |
| W5. Ecommerce Product | One product or a variant group | Changes specifications or offer terms |
| W6. Expert-Led Article | Research, an expert contribution or source-led analysis | Invents expertise, interviews, quotes or findings |

## Start here

1. Bring an approved brief with its route, the approval record for that exact revision, and the approved evidence dossier it references. See the [synthetic input](examples/ready-input.md).
2. For a change to an existing page, bring the current text of the sections in scope.
3. Ask for the draft. Example request: "Use the SEO Content Writing Skill to draft this page from brief CB-07 revision 1 and dossier ED-07 revision 2."
4. Answer any writer queries, then send the draft to the editorial pass.

The status line says what happens next. **Draft ready for review: C1 editorial pass** goes to an editor. **Draft with writer queries: Owner answers needed** lists the facts to confirm first. **Blocked: Return to B3** and **Blocked: Return to B2** name what is missing from the brief or the evidence.

For voice rules, use profile mode: "Use the SEO Content Writing Skill in profile mode to set our voice rules from these pages, style notes and corrections." See the [profile example](examples/profile-output.md).

## What it does not do

- Draft without an approved brief for the exact revision, or without the approved dossier.
- Add, strengthen or loosen a claim, or invent people, quotes, credentials, testing, results, locations or reviews.
- Write town, product or facet variants by swapping names into shared copy.
- Meet keyword density, word count or AI-detector targets.
- Write the final title element, meta description, structured data or alt text. It lists them for the publishing handoff.
- Edit, fact-check, policy-check, approve or publish the draft.
- Give legal, medical, financial or safety clearance.
- Promise rankings, traffic, AI citations or timing.

## Package layout

- [SKILL.md](SKILL.md) and `references/` are the runtime files, intended for Claude, ChatGPT and Codex. Compatibility is not verified until platform tests are recorded.
- `agents/openai.yaml` is optional interface metadata for Codex. Claude does not use it.
- `examples/` contains a synthetic ready draft with its input, a blocked case and a profile with its input.
- [Acceptance tests](tests/acceptance-tests.md) define behaviour and package checks, and `tests/check-package.py` runs the automatable checks.
- [Claude setup](platforms/claude.md) and [ChatGPT and Codex setup](platforms/chatgpt.md) cover installation.
- [Changelog](CHANGELOG.md) tracks revisions.

## Status

Unreleased draft. Package checks have passed. No behaviour case has been run, and the skill has not been installed or invoked on any platform. The [acceptance tests](tests/acceptance-tests.md) record each state separately.

## Installation

Keep the runtime folder named `seo-content-writing` when staging it for installation. Copy `SKILL.md` and `references/` together, preserving relative paths. The runtime uses Markdown only and has no scripts or service dependencies.

## Where it fits

The skill works on its own. It takes the brief from the SEO Content Brief Skill (`skills/seo-content-brief/`), which chooses the W-series route, and the dossier from the SEO Content Evidence Skill (`skills/seo-content-evidence/`), whose claim statuses it carries into copy. Its profile mode supplies the voice rules the brief records. A ready draft goes to the editorial, fact and claims, and reader value and policy passes, then to publishing, where release fields and structured data are prepared. Each of those skills is under review in its own pull request or planned. Equivalent records from your own process work in their place.

## Workflow provenance

The method follows the Content Evidence, Briefing and Publishing QA playbook v1.2 (File 12): section 6 (drafting through the specialist writer routes W1 to W6), section 4.1 (the evidence-led editorial profile, stage A2), section 4.2 (authorship), section 7 (AI assistance) and the drafting prompt in section 13.3. Google guidance is paraphrased with source IDs and check dates in the [source register](references/source-register.md), which keeps File 12's IDs and records the differences from it. The examples are synthetic, and no employer, client or private material is included.
