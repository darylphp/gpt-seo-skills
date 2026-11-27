# ChatGPT and Codex

For v0.1.0, no ChatGPT upload, installed activation or Codex discovery test has been completed, and no behaviour case has been run. Results from Claude would not show how ChatGPT or Codex behaves.

The same `SKILL.md` and `references/` files are intended for both platforms. The source folder in `claude-seo-skills` is the single editable copy, and the `gpt-seo-skills` package is generated from the same reviewed revision, so each rule is edited in one place.

## ChatGPT

OpenAI's help page could not be opened on 28 November 2026. Its search result text on that date described opening **Plugins** in the sidebar, then **Skills**, and uploading with **Create**, then **Upload from your computer**. It listed Personal Skills as generally available for ChatGPT Business, Enterprise, Healthcare and Edu users, subject to workspace settings, said uploaded skills are scanned before they become available, and said OpenAI skills follow the Agent Skills open standard. Follow the live dialog.

**[needs platform verification]** The help page text seen does not state the accepted archive layout, any frontmatter or description limits, or whether Free, Plus and Pro users can upload skills. A test upload of the same ZIP used for Claude, with `seo-content-qa/` at the archive root, would settle the layout and whether one package works on both platforms.

Upload only `SKILL.md` and `references/`. The optional `agents/openai.yaml` supplies Codex interface metadata. Keep examples, tests and package documentation out of the runtime upload. A GitHub link or files attached to an ordinary chat do not install a skill. For a direct-file review, supply the runtime folder and ask the model to read `SKILL.md` and each reference it needs, and label the result a direct-file run, not installed activation.

[OpenAI Help Center: Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

## Codex

OpenAI's skills documentation, opened on 28 November 2026, says Codex looks for repository skills in `.agents/skills` in each folder from the current working directory up to the repository root, and for user skills in `$HOME/.agents/skills`. It describes `agents/openai.yaml` as optional metadata for appearance, invocation policy and tool dependencies, and explicit invocation by typing `$` with the skill name or running `/skills`. Place the runtime folder at `.agents/skills/seo-content-qa/` in a repository, keeping `references/` beside `SKILL.md`, and invoke `$seo-content-qa` with the revision, brief and evidence. Invocation of this package has not been tested.

[Build skills](https://learn.chatgpt.com/docs/build-skills)

## Use

Suggested request: "Use the SEO Content QA Skill on revision 2 of this page. Here are the approved brief and the evidence dossier. Sam approves the editorial revision and Mei approves the release." Check that the report keeps the 10 sections in order, uses one exact status, and prints the revision line, three pass lines, the approval line and the handoff line in section 1.
