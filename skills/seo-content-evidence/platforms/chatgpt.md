# ChatGPT and Codex

For v0.1.0, no ChatGPT upload, installed activation or Codex discovery test has been completed, and no behaviour case has been run. Results from Claude would not show how ChatGPT or Codex behaves.

The same `SKILL.md` and `references/` files are intended for both platforms. The source folder in `claude-seo-skills` is the single editable copy, and the `gpt-seo-skills` package is generated from the same reviewed revision, so each rule is edited in one place.

## ChatGPT

OpenAI's help page could not be opened on 27 November 2026. Its search result text on that date described opening **Plugins** in the sidebar, then **Skills**, **Create** and **Upload from your computer**, listed skills for eligible ChatGPT Business, Enterprise, Healthcare and Edu users, subject to workspace settings, and said uploaded skills are scanned before they become available. Earlier notes in this library record the path as **Skills**, **Create**, **Upload from your computer** (20 November 2026) and as **Plugins**, **Skills**, **Add**, **Upload from your computer** (27 November 2026, Local SEO Audit draft). Follow the live dialog.

**[needs platform verification]** The help page does not state the accepted archive layout, any frontmatter or description limits, or whether Free, Plus and Pro users can upload skills. A test upload of the same ZIP used for Claude, with `seo-content-evidence/` at the archive root, would settle the layout and whether one package works on both platforms.

Upload only `SKILL.md` and `references/`. The optional `agents/openai.yaml` supplies Codex interface metadata. Keep examples, tests and package documentation out of the runtime upload. A GitHub link or files attached to an ordinary chat do not install a skill. For a direct-file review, supply the runtime folder and ask the model to read `SKILL.md` and each reference it needs, and label the result a direct-file run, not installed activation.

[OpenAI Help Center: Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

## Codex

OpenAI's skills documentation, from its search result text on 27 November 2026, describes repository skills in `.agents/skills/` and an optional `agents/openai.yaml` for appearance and dependencies. Place the runtime folder at `.agents/skills/seo-content-evidence/` in a repository, and keep `references/` beside `SKILL.md`. The user location `~/.agents/skills/seo-content-evidence/` is carried forward from the Local SEO Audit draft's notes of the same date. Invoke `$seo-content-evidence` with the page decision and sources. Invocation of this package has not been tested.

[Build skills](https://learn.chatgpt.com/docs/build-skills)

## Use

Suggested request: "Use the SEO Content Evidence Skill to build the evidence and claims dossier for this page. Tell me what we can claim, what we can't, and what proof is missing." Check that the dossier keeps the 10 sections in order, uses one exact status, and prints the approval and handoff lines in section 1.
