# Claude app and Claude Code

Documentation checked 28 November 2026. For v0.1.0, installation has not been tested and invocation has not been confirmed in the Claude app or Claude Code. No behaviour case has been run.

## Claude app

1. Stage the runtime files in a folder named `seo-content-qa/`, containing `SKILL.md` and `references/`. The folder name must match the `name` field in `SKILL.md`.
2. ZIP the folder itself so every entry starts with `seo-content-qa/`. From the parent folder, run `zip -r seo-content-qa.zip seo-content-qa/SKILL.md seo-content-qa/references/`, then `unzip -l seo-content-qa.zip` to confirm the layout.
3. Turn on code execution. Anthropic's help pages list custom skills on Free, Pro, Max, Ultra, Team and Enterprise plans, with code execution enabled. On individual plans it's under **Settings**, then **Capabilities**. On Enterprise plans an owner enables code execution and skills in organisation settings; Team plans have them on by default.
4. Upload the ZIP, then turn the skill on under **Customize**, then **Skills**.

The description is 188 characters, within the 200-character limit on Anthropic's help page, and the `name` is within its 64-character limit.

[Anthropic Help Center: How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) · [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Claude Code

Copy the runtime folder to `.claude/skills/seo-content-qa/` for a project or `~/.claude/skills/seo-content-qa/` for your user account. Keep `SKILL.md` and `references/` together. Type `/seo-content-qa` with the revision, the brief and the evidence, or ask for a QA check on a page revision and let Claude load the skill from its description. The skill paths, `/skill-name` invocation and loading from the description were confirmed on the documentation page on 28 November 2026.

[Claude Code documentation: Extend Claude with skills](https://code.claude.com/docs/en/skills)

## Use

Attach or paste the exact revision with its ID, the approved brief, the evidence dossier or records, and any approval records so far. Ask for one page at a time. Check that the report keeps the 10 sections in order, uses one exact status, and prints the revision line, three pass lines, the approval line and the handoff line in section 1.
