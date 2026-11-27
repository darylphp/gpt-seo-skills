# ChatGPT and Codex

For v0.1.0, no ChatGPT upload, installed activation or Codex discovery test has been completed, and no behaviour case has been run. Results from Claude would not show how ChatGPT or Codex behaves.

The same `SKILL.md` and `references/` files are intended for both platforms. The source folder in `claude-seo-skills` is the single editable copy, and the `gpt-seo-skills` package is generated from the same reviewed revision, so each rule is edited in one place.

## ChatGPT

OpenAI's help page could not be opened on 28 November 2026, as on 27 November. Its search result text on 28 November described opening **Plugins** in the sidebar, then **Skills**, **Create** and **Upload from your computer**. It listed Personal Skills as generally available for ChatGPT Business, Enterprise, Healthcare and Edu users, subject to workspace settings, said uploaded skills are scanned before they become available, and said OpenAI skills follow the Agent Skills open standard. Follow the live dialog.

**[needs platform verification]** The search result text does not state the accepted archive layout, any frontmatter or description limits, or whether Free, Plus and Pro users can upload skills. A test upload of the same ZIP used for Claude, with `seo-content-writing/` at the archive root, would settle the layout and whether one package works on both platforms.

Upload only `SKILL.md` and `references/`. The optional `agents/openai.yaml` supplies Codex interface metadata. Keep examples, tests and package documentation out of the runtime upload. A GitHub link or files attached to an ordinary chat do not install a skill. For a direct-file review, supply the runtime folder and ask the model to read `SKILL.md` and each reference it needs, and label the result a direct-file run, not installed activation.

[OpenAI Help Center: Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

## Codex

OpenAI's Codex skills documentation, from its search result text on 28 November 2026, says Codex scans `.agents/skills` in every folder from the current working directory up to the repository root, that `$` mentions a skill in the CLI or IDE, and that `agents/openai.yaml` is optional metadata for appearance and dependencies. Place the runtime folder at `.agents/skills/seo-content-writing/` in a repository, keeping `references/` beside `SKILL.md`, and invoke `$seo-content-writing` with the brief and dossier. The user location `~/.agents/skills/seo-content-writing/` is carried forward from the library's 27 November notes and was not reconfirmed. Invocation of this package has not been tested.

[Codex: Agent Skills](https://developers.openai.com/codex/skills)

## Use

Suggested request: "Use the SEO Content Writing Skill to draft this page from the approved brief and dossier. Mark each claim, and list anything you couldn't support." Check that the output keeps the 9 sections in order, uses one exact status, and prints the approval, no-clearance and handoff lines in section 1.
