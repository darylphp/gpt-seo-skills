# SEO Content Evidence Skill

Decide what one page can truthfully claim before it is briefed or changed. The skill returns a 10-section evidence and claims dossier: the status and summary, the page decision and scope, the sources, a claim register, figure, quote and comparison checks, people, experience and review, assets and permissions, conflicts and proof requests, the brief handoff, and freshness triggers.

Each claim gets one status. Four are usable: Verified for use, Verified with qualification, Supported inference, and Approved attributable opinion or experience. Five are not: Client confirmation required, Contradicted, Unsupported, Prohibited and Stale.

## Start here

1. Describe the page: its URL or proposed URL, its role, the reader's task, the market, the approved action, and who confirms business facts and approves the dossier. See [scope and intake](references/scope-and-intake.md) and the [synthetic input](examples/ready-input.md).
2. Supply the evidence you have: service and price records, licences or credentials, job or order data, customer feedback with consent, photos, the existing page or draft, and any public sources you want to rely on.
3. Ask for a dossier. Example request: "Use the SEO Content Evidence Skill on this page decision and these records. Tell us what we can and can't claim, and what proof is missing."
4. Review the statuses, conditions and proof requests, then approve the exact dossier revision before it goes to the brief.

The status line says what happens next. **Ready for review: Evidence dossier** and **Ready for review: Source-led dossier** are ready for a person to review and approve. **Evidence gaps: Proof requests open** names the proof to collect first. **Blocked: Confirm the page decision** and **Blocked: Supply the evidence** name what is missing.

For a correction, such as a price change, use targeted check mode: the skill checks the corrected fact and every place it appears, including the meta description, structured data and image text. See the [targeted check example](examples/correction-output.md).

## What it does not do

- Write page copy, quotes or testimonials, or invent sources, credentials, tests, results or reviewers.
- Treat an owner's approval, a competitor page, AI output or a search snippet as proof of a technical or comparative claim.
- Give legal, medical, financial or safety clearance, or decide whether a claim meets any law or standard.
- Approve the dossier, the brief or publication on anyone's behalf.
- Mark up structured data or edit a Business Profile. It hands those facts on with their claim IDs.
- Promise rankings, traffic, AI citations or timing.

## Package layout

- [SKILL.md](SKILL.md) and `references/` are the runtime files, intended for Claude, ChatGPT and Codex. Compatibility is not verified until platform tests are recorded.
- `agents/openai.yaml` is optional interface metadata for Codex. Claude does not use it.
- `examples/` contains a synthetic ready case with its output, a blocked case and a targeted check for a price correction.
- [Acceptance tests](tests/acceptance-tests.md) define behaviour and package checks, and `tests/check-package.py` runs the automatable checks.
- [Claude setup](platforms/claude.md) and [ChatGPT and Codex setup](platforms/chatgpt.md) cover installation.
- [Changelog](CHANGELOG.md) tracks revisions.

## Status

Unreleased draft. Package checks have passed. No behaviour case has been run, and the skill has not been installed or invoked on any platform. The [acceptance tests](tests/acceptance-tests.md) record each state separately.

## Installation

Keep the runtime folder named `seo-content-evidence` when staging it for installation. Copy `SKILL.md` and `references/` together, preserving relative paths. The runtime uses Markdown only and has no scripts or service dependencies.

## Where it fits

The skill works on its own. It takes the page record from the Site Architecture Skill (`skills/site-architecture/`), or an equivalent approved page decision, and its approved dossier is the evidence input the SEO Content Brief Skill (`skills/seo-content-brief/`) asks for: `Brief handoff: Ready for B3` or `Ready for B3 as source-led`. The claim statuses are the ones the brief accepts. Structured data facts go to schema review, Business Profile facts to the Local SEO Audit Skill (`skills/local-seo-audit/`), and page-decision questions back to site architecture work. Each of those skills is under review in its own pull request. Equivalent records from your own process work in their place.

## Workflow provenance

The method follows the Content Evidence, Briefing and Publishing QA playbook v1.2 (File 12), section 3 (the evidence and claims dossier), with the authorship, review and AI-assistance controls from sections 4.2 and 7 and the asset checks from section 10. It covers the playbook stage "B2 Evidence and Claims Dossier Builder". Google guidance is paraphrased with source IDs and check dates in the [source register](references/source-register.md), which keeps File 12's IDs and records the differences from it. The examples are synthetic, and no employer, client or private material is included.
