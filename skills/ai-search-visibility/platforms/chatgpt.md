# ChatGPT and Codex

For v0.1.0, no ChatGPT upload, installed activation or Codex discovery test has been completed, and no behaviour case has been run. Results from Claude would not show how ChatGPT or Codex behaves.

The same `SKILL.md` and `references/` files are intended for both platforms. The source folder in `claude-seo-skills` is the single editable copy, and the `gpt-seo-skills` package is generated from the same reviewed revision, so each rule is edited in one place.

## ChatGPT

OpenAI's help page, opened on 28 November 2026, says skills are available to eligible ChatGPT Business, Enterprise, Healthcare and Edu users, subject to workspace settings and product availability. Enterprise and Edu admins control access under **Permissions & roles**. To upload, select **Plugins** in the sidebar, open the **Skills** tab, select **Add**, then **Upload from your computer**. ChatGPT scans an uploaded skill before it becomes available, and may mark it **Needs Review** or **Blocked**. OpenAI notes that the scan doesn't replace your own review.

**[needs platform verification]** The help page doesn't state the accepted archive layout or any frontmatter limits. A test upload of the same ZIP used for Claude, with `ai-search-visibility/` at the archive root, would settle the layout and whether one package works on both platforms.

Upload only `SKILL.md` and `references/`. The optional `agents/openai.yaml` supplies Codex interface metadata. Keep examples, tests and package documentation out of the runtime upload. A GitHub link or files attached to an ordinary chat do not install a skill. For a direct-file review, supply the runtime folder and ask the model to read `SKILL.md` and each reference it needs, and label the result a direct-file run, not installed activation.

[OpenAI Help Center: Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

## Codex

OpenAI's skills documentation, opened on 28 November 2026, says Codex looks for repository skills in `.agents/skills` in the current folder, its parent and the repository root, and for user skills in `$HOME/.agents/skills`. Place the runtime folder at `.agents/skills/ai-search-visibility/` in a repository, or `~/.agents/skills/ai-search-visibility/` for your user account, and keep `references/` beside `SKILL.md`. Invoke it with `$ai-search-visibility`, or through `/skills`. Codex can also choose it when a task matches the description. The optional `agents/openai.yaml` sets display metadata. Invocation of this package hasn't been tested.

[Build skills](https://learn.chatgpt.com/docs/build-skills)

## Use

Suggested request: "Use the AI Search Visibility Skill on this site. Tell me whether our pages can appear in AI Overviews and AI Mode, which AI controls are set and why, and what we can actually measure." Check that the report keeps the 10 sections in order, uses one exact status, and prints the approval, no-change and control lines in section 1.
