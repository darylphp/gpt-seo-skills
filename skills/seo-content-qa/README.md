# SEO Content QA Skill

Check one exact revision of a page before it goes live, in three passes that run in order: editorial, then claims and commercial facts, then reader value, originality and spam policy. The skill returns a 10-section QA report: the status and pass record, the revision and scope, one section for each pass, a findings register, what was checked and how independent the check was, approvals, the publishing handoff and a recheck plan.

Every finding gets a location, its evidence, one severity (Publication blocker, Material improvement, Minor correction or Research note) and one owner to return it to. Claims are checked against the same statuses the SEO Content Evidence Skill gives them.

## Start here

1. Supply the exact revision with an ID, the approved brief (or the approved change request for a correction), the approved evidence dossier or the records behind the page's claims, and the nearest pages it must stay distinct from. See [scope and intake](references/scope-and-intake.md) and the [synthetic input](examples/ready-input.md).
2. Say who approves the editorial revision and who approves the release. If someone has already approved this exact revision after an editorial pass, include that record so the skill starts at the claims pass.
3. Ask for QA. Example request: "Use the SEO Content QA Skill on WD-07 revision 2 of our termite inspections page. Sam signs off the editorial revision, and Mei approves anything that goes live."
4. Apply or reject the proposed edits, approve the resulting revision, and run the skill again. A cleared report goes to publishing with the exact revision and its conditions.

The status line says what happens next. **Editorial pass complete: Awaiting revision approval** needs a person to approve the edited revision. **Corrections needed: Returned to owner** names who fixes what. **Cleared within scope: Ready for publishing handoff** goes to publishing once the release is approved. **Blocked: Confirm the revision** and **Blocked: Supply the evidence** name what is missing.

For a correction, such as a changed price, use targeted check mode: the skill checks the changed fact everywhere it appears, including the meta description, image text and structured data, and records which passes it combined.

## What it does not do

- Rewrite the page, add claims, or invent sources, quotes, reviewers, credentials, tests or results.
- Clear a claim because it sounds right, a competitor says it, an AI wrote it or someone insists.
- Use AI-detector results, optimisation scores, readability scores, keyword density or word counts to pass or fail a page.
- Give legal, medical, financial or safety clearance, or decide whether a claim meets any law or standard.
- Approve the revision or the release on anyone's behalf, or publish anything.
- Promise rankings, traffic, AI citations or timing.

## Package layout

- [SKILL.md](SKILL.md) and `references/` are the runtime files, intended for Claude, ChatGPT and Codex. Compatibility is not verified until platform tests are recorded.
- `agents/openai.yaml` is optional interface metadata for Codex. Claude does not use it.
- `examples/` contains one synthetic page, picked up from the SEO Content Writing Skill's draft, followed through an editorial pass, a claims pass that returns corrections, and a recheck that clears, plus a blocked request.
- [Acceptance tests](tests/acceptance-tests.md) define behaviour and package checks, and `tests/check-package.py` runs the automatable checks.
- [Claude setup](platforms/claude.md) and [ChatGPT and Codex setup](platforms/chatgpt.md) cover installation.
- [Changelog](CHANGELOG.md) tracks revisions.

## Status

Unreleased draft. Package checks have passed. No behaviour case has been run, and the skill has not been installed or invoked on any platform. The [acceptance tests](tests/acceptance-tests.md) record each state separately.

## Installation

Keep the runtime folder named `seo-content-qa` when staging it for installation. Copy `SKILL.md` and `references/` together, preserving relative paths. The runtime uses Markdown only and has no scripts or service dependencies.

## Where it fits

The skill works on its own. It checks a draft written by the SEO Content Writing Skill (`skills/seo-content-writing/`), whose ready draft hands off with `QA handoff: Ready for C1 editorial pass`, against a brief built with the SEO Content Brief Skill (`skills/seo-content-brief/`). Its claims pass reads a dossier built with the SEO Content Evidence Skill (`skills/seo-content-evidence/`). A cleared report is the input a publishing step needs: `Publishing handoff: Ready for D1`. Structured data facts go to the Schema Markup Skill (`skills/schema-markup/`), Business Profile consistency to the Local SEO Audit Skill (`skills/local-seo-audit/`), and page-set questions to the Site Architecture Skill (`skills/site-architecture/`). Each of those skills is under review in its own pull request, and the publishing skill is not built yet. Equivalent records from your own process work in their place.

## Workflow provenance

The method follows the Content Evidence, Briefing and Publishing QA playbook v1.2 (File 12): the stage gates in section 6, independent QA in section 7, the editorial, factual and reader-value reviews and severity table in section 8, and the approval states in section 9. It covers the playbook stages "C1 Human Editorial Pass", "C2 Fact, Claim and Commercial QA" and "C3 Reader Value, Originality and Spam-Policy QA" as three gated passes in one skill, as planned in the Stage 1 structure review. The presentation checks in pass 3 are adapted from the proposed Visual Semantics and Page Presentation playbook v1.0, which is not yet in the playbook's index. Google guidance is paraphrased with source IDs and check dates in the [source register](references/source-register.md), which keeps File 12's IDs and records the differences from it. The examples are synthetic, and no employer, client or private material is included.
