# SEO Content Brief Skill

Turn one validated page opportunity and an approved evidence pack into a page-specific SEO brief for a writer. The workflow stage is **B3. Differentiation and Content Brief Builder**.

## Start here

1. Supply one approved page decision, exact URL and boundary, reader task, market, query intent, relevant voice rules and the page evidence dossier. See [input requirements](references/input-requirements.md) and the [synthetic input](examples/ready-input.md).
2. Ask the skill to prepare the B3 brief and flag missing approvals or evidence. Review the section plan, source mapping and page boundaries.
3. Record approval of the exact brief revision before drafting. Keep any required specialist approval explicit.

Example request: “Use the SEO Content Brief Skill to build one brief from the attached approved pack. Keep the existing URL boundary and record the current approval state.”

Ready identifies the writer route. The approval field records whether drafting can begin. An unresolved page decision returns to B1. A material evidence gap returns to B2.

## Package layout

- [SKILL.md](SKILL.md) and `references/` are the shared runtime files.
- `examples/` contains synthetic ready and blocked cases.
- [Acceptance tests](tests/acceptance-tests.md) define review and behaviour checks.
- [ChatGPT and Codex setup](platforms/chatgpt.md) covers installation.
- [Changelog](CHANGELOG.md) tracks package revisions.

Keep the runtime folder named `seo-content-brief` when staging it for installation. Copy `SKILL.md` and `references/` together, preserving relative paths. The package uses Markdown and has no runtime scripts or service dependencies.

## Workflow provenance

The package follows Content Evidence, Briefing and Publishing QA v1.2, sections 2 to 6 and 9, and the B1, B2 and B3 workflow contracts. Query handoff and URL boundaries follow the Keyword, Query Family and Intent Research Playbook v1.1 and the Patent-Informed Cluster Build Framework v3.2 as operating methods. Visual planning borrows task, proof and accessibility checks from Visual Semantics and Page Presentation v1.0. The runtime carries the applicable rules in its own references.
