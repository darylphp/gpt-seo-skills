# Local SEO Audit Skill

Draft v0.1.0, under review. Audit one real business location's Google Business Profile, linked website page, review process and local measurement from supplied evidence and accessible public pages. Return a 10-section report with evidence labels, priorities, action-specific approval, acceptance checks and open questions.

## Use the draft

Supply the real trading name, one identified location, profile/website URLs, business model, customer action, approved facts and available evidence. Use [input requirements](references/input-requirements.md) and the labelled [synthetic fixture](examples/ready-input.md). Ask: "Use the Local SEO Audit Skill to audit this location from these facts and evidence."

Ready means ready for human review. Existing permission is recorded by action, without a repeated request. The audit performs no edits, calls, form submissions, customer messages, appeals or review replies and does not promise rankings or growth. Public-only findings can be useful; account-only checks remain Not verified. For a defined batch, keep a separate report per location.

## Files and platforms

- Runtime: [SKILL.md](SKILL.md) and [references](references/input-requirements.md). No runtime scripts, paid tools or service dependencies.
- Optional Codex interface: `agents/openai.yaml`.
- Setup: [ChatGPT/Codex](platforms/chatgpt.md) and [Claude/Claude Code](platforms/claude.md). Intended compatibility is not verified installation.
- Examples: labelled synthetic ready, blocked and incident cases.
- Validation: [acceptance cases and status](tests/acceptance-tests.md), plus dated direct-file outputs when run. Package checks and model runs are not platform activation tests.

Keep SKILL.md and references together. Follow the live platform upload requirements. There is no tested stable release or approved download yet.

## Provenance and limits

Adapted from the public Claude Local SEO Audit draft at `4e30f9102fcbfbc318bde1b9e0ffae53c4551b22`, using the Local SEO and GBP Operating Playbook v1.2. The runtime is self-contained and does not require the private project playbooks. [Source register](references/source-register.md) records primary guidance, 27 November 2026 review scope and adaptation changes. Measurement and schema work is routed to specialist workflows when needed. No client records, credentials or real business results are included.
