# Schema Markup Skill

Decide which structured data one page or template should carry, check the markup it already has, and plan how a change is validated on production. The skill returns a 10-section report: the status and summary, the page record, evidence and access, the current markup and its producers, feature fit, decisions, a property map, draft markup and changes, validation and release, and measurement and open items.

Each node gets one decision: Add, Keep, Repair, Consolidate, Remove, Defer or No markup. Each type gets one feature status: Google feature, Descriptive only, Retired, Restricted or Needs verification. Syntax, vocabulary, feature support, eligibility, appearance and any ranking or traffic change are reported separately.

## Start here

1. Name the page or template: its URL (or a representative URL for each template variant), what it's for, what it's mainly about, and who confirms facts, implements and approves. See [scope and intake](references/scope-and-intake.md) and the [synthetic input](examples/ready-input.md).
2. Supply what you have: the page source or a saved copy, the rendered output, Rich Results Test or Search Console screenshots, the plugin and theme settings that output markup, and the business facts the page shows.
3. Ask for a report. Example request: "Use the Schema Markup Skill on our home page and class template. Tell us what structured data each should carry, what to fix or remove, and how to check it."
4. Review the decisions, the property map and any draft, then approve the exact report revision before anyone changes the site.

The status line says what happens next. **Ready for review: Schema report** is ready for a person to review and approve. **Facts needed: Confirmation list open** names the facts to confirm first. **Escalate first: Misleading markup or manual action** leads with a correction. **Blocked: Confirm the page and purpose** and **Blocked: Supply page and markup evidence** name what is missing.

For a deployed change, use release check mode: the skill compares production output with the approved decisions and records which are implemented and which are technically verified.

## What it does not do

- Edit a site, plugin, theme or Search Console, request indexing, or approve a change on anyone's behalf.
- Invent reviews, ratings, prices, identifiers, dates, authors, addresses or phone numbers, or fill a property because a tool warns it is missing.
- Promise rich results, rankings, traffic, AI citations or timing. Google says no special markup is needed for its generative AI features.
- Recommend AI-specific schema, `FAQPage` for Google FAQ rich results, review stars on a business's own pages, or `LocalBusiness` for places that don't exist.
- Decide whether a page should exist, prove the claims a page makes, or audit a Business Profile. It hands those questions on.

## Package layout

- [SKILL.md](SKILL.md) and `references/` are the runtime files, intended for Claude, ChatGPT and Codex. Compatibility is not verified until platform tests are recorded.
- `agents/openai.yaml` is optional interface metadata for Codex. Claude does not use it.
- `examples/` contains a synthetic ready case with its output, a blocked case and an escalation for an invented rating under a manual action.
- [Acceptance tests](tests/acceptance-tests.md) define behaviour and package checks, and `tests/check-package.py` runs the automatable checks.
- [Claude setup](platforms/claude.md) and [ChatGPT and Codex setup](platforms/chatgpt.md) cover installation.
- [Changelog](CHANGELOG.md) tracks revisions.

## Status

Unreleased draft. Package checks have passed. No behaviour case has been run, and the skill has not been installed or invoked on any platform. The [acceptance tests](tests/acceptance-tests.md) record each state separately.

## Installation

Keep the runtime folder named `schema-markup` when staging it for installation. Copy `SKILL.md` and `references/` together, preserving relative paths. The runtime uses Markdown only and has no scripts or service dependencies.

## Where it fits

The skill works on its own, and it is the schema review the other skills in this library hand on to. The Technical SEO Audit Skill (`skills/technical-seo-audit/`) routes structured data changes here after it has found every producer of the markup. The SEO Content Evidence Skill (`skills/seo-content-evidence/`) sends facts headed for markup with their claim IDs, and this skill sends unproven page claims back to it. Business Profile facts go to the Local SEO Audit Skill (`skills/local-seo-audit/`), and page decisions to the Site Architecture Skill (`skills/site-architecture/`). Each of those skills is under review in its own pull request. Equivalent records from your own process work in their place.

## Workflow provenance

The method follows the Schema Markup Implementation and Validation Playbook v1.3 (File 05): its six outcomes, decision matrix, selection process, decision and release record, WordPress rules, review guardrails, conditional feature checks and QA checklist. Google guidance is paraphrased with source IDs and check dates in the [source register](references/source-register.md), which records where current Google documentation differs from the playbook, including online events. The examples are synthetic, and no employer, client or private material is included.
