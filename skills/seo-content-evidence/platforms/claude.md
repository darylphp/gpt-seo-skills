# Claude app and Claude Code

Documentation checked 27 November 2026. For v0.1.0, installation has not been tested and invocation has not been confirmed in the Claude app or Claude Code. No behaviour case has been run.

## Claude app

1. Stage the runtime files in a folder named `seo-content-evidence/`, containing `SKILL.md` and `references/`. The folder name must match the `name` field in `SKILL.md`.
2. ZIP the folder itself so every entry starts with `seo-content-evidence/`. From the parent folder, run `zip -r seo-content-evidence.zip seo-content-evidence/SKILL.md seo-content-evidence/references/`, then `unzip -l seo-content-evidence.zip` to confirm the layout.
3. Turn on code execution. Anthropic's help page lists skills on Free, Pro, Max, Ultra, Team and Enterprise plans, with code execution enabled. On Team and Enterprise plans an owner may need to enable skills in organisation settings.
4. Upload the ZIP, then turn the skill on under **Customize**, then **Skills**.

The description is within the 200-character limit on Anthropic's help page, and the `name` is within its 64-character limit.

[Anthropic Help Center: How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) · [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Claude Code

Copy the runtime folder to `.claude/skills/seo-content-evidence/` for a project or `~/.claude/skills/seo-content-evidence/` for your user account. Keep `SKILL.md` and `references/` together. Type `/seo-content-evidence` with the page decision and the sources, or ask what a page can claim and let Claude load the skill from its description. The skill paths and `/skill-name` invocation were confirmed from the documentation's search result text on 27 November 2026; the page itself was not opened.

[Claude Code documentation: Extend Claude with skills](https://code.claude.com/docs/en/skills)

## Use

Attach or paste the page decision, the business records, any existing page text or draft, and the sources you want checked. Ask for one page at a time. Check that the dossier keeps the 10 sections in order, uses one exact status, and prints the approval and handoff lines in section 1.
