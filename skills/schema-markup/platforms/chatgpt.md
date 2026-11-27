# ChatGPT and Codex

For v0.1.0, no ChatGPT upload, installed activation or Codex discovery test has been completed, and no behaviour case has been run. Results from Claude would not show how ChatGPT or Codex behaves.

The same `SKILL.md` and `references/` files are intended for both platforms. The source folder in `claude-seo-skills` is the single editable copy, and the `gpt-seo-skills` package is generated from the same reviewed revision, so each rule is edited in one place.

## ChatGPT

OpenAI's help page could not be opened on 28 November 2026. Its search result text on that date said personal skills are generally available for ChatGPT Business, Enterprise, Healthcare and Edu users, subject to workspace settings, and are added separately on desktop and on web and mobile. It described opening **Plugins** in the sidebar, then the **Skills** tab, then **Create** and **Upload from your computer**, and said ChatGPT scans an uploaded skill before it becomes available. The page showed "Updated: 25 days ago" in the search result. Follow the live dialog.

**[needs platform verification]** The search result text does not state the accepted archive layout, any frontmatter or description limits, or whether Free, Plus and Pro users can upload skills. A test upload of the same ZIP used for Claude, with `schema-markup/` at the archive root, would settle the layout and whether one package works on both platforms.

Upload only `SKILL.md` and `references/`. The optional `agents/openai.yaml` supplies Codex interface metadata. Keep examples, tests and package documentation out of the runtime upload. A GitHub link or files attached to an ordinary chat do not install a skill. For a direct-file review, supply the runtime folder and ask the model to read `SKILL.md` and each reference it needs, and label the result a direct-file run, not installed activation.

[OpenAI Help Center: Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

## Codex

OpenAI's skills documentation, from its search result text on 28 November 2026, says Codex scans `.agents/skills` in every directory from the current working directory up to the repository root, that `agents/openai.yaml` is optional metadata for appearance and dependencies, and that a skill can be invoked explicitly by typing `$` and its name or chosen implicitly from its description. Place the runtime folder at `.agents/skills/schema-markup/` in a repository, keep `references/` beside `SKILL.md`, and invoke `$schema-markup` with the page and its evidence. Invocation of this package has not been tested.

[Build skills](https://learn.chatgpt.com/docs/build-skills)

## Use

Suggested request: "Use the Schema Markup Skill on this page. Tell me which structured data it should carry, what to fix or remove, and how to check the change." Check that the report keeps the 10 sections in order, uses one exact status, and prints the approval and handoff lines in section 1.
