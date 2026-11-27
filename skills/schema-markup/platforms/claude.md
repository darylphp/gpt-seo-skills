# Claude app and Claude Code

Documentation checked 28 November 2026 from search result text; the pages themselves were not opened. For v0.1.0, installation has not been tested and invocation has not been confirmed in the Claude app or Claude Code. No behaviour case has been run.

## Claude app

1. Stage the runtime files in a folder named `schema-markup/`, containing `SKILL.md` and `references/`. The folder name must match the `name` field in `SKILL.md`.
2. ZIP the folder itself so every entry starts with `schema-markup/`. From the parent folder, run `zip -r schema-markup.zip schema-markup/SKILL.md schema-markup/references/`, then `unzip -l schema-markup.zip` to confirm the layout. Anthropic's help page says the ZIP must contain the skill folder as its root, not loose files.
3. Turn on code execution. The plan list carried forward from the 27 November 2026 notes for this library is Free, Pro, Max, Ultra, Team and Enterprise, with code execution enabled. On Team and Enterprise plans an owner may need to enable skills in organisation settings. Recheck the help page before relying on it.
4. Upload the ZIP, then turn the skill on under **Customize**, then **Skills**.

Anthropic's help page gives a 64-character limit for the name and a 200-character limit for the description. This package's name is 13 characters and its description is within the limit; `tests/check-package.py` checks both.

[Anthropic Help Center: How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) · [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Claude Code

Copy the runtime folder to `.claude/skills/schema-markup/` for a project or `~/.claude/skills/schema-markup/` for your user account. Keep `SKILL.md` and `references/` together. Type `/schema-markup` with the page and its evidence, or describe a structured data task and let Claude load the skill from its description. The skill locations and `/skill-name` invocation were confirmed from the documentation's search result text on 28 November 2026.

[Claude Code documentation: Extend Claude with skills](https://code.claude.com/docs/en/skills)

## Use

Attach or paste the page URL or template, the page source or a saved copy, any testing-tool exports or Search Console screenshots, the plugin or theme settings that output markup, and the business facts the page shows. Ask for one page or template at a time. Check that the report keeps the 10 sections in order, uses one exact status, and prints the approval and handoff lines in section 1.
