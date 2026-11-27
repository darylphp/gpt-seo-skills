# Claude app and Claude Code

Documentation checked 28 November 2026. For v0.1.0, installation has not been tested and invocation has not been confirmed in the Claude app or Claude Code. No behaviour case has been run.

## Claude app

1. Stage the runtime files in a folder named `seo-content-writing/`, containing `SKILL.md` and `references/`. The folder name must match the `name` field in `SKILL.md`.
2. ZIP the folder itself so every entry starts with `seo-content-writing/`. From the parent folder, run `zip -r seo-content-writing.zip seo-content-writing/SKILL.md seo-content-writing/references/`, then `unzip -l seo-content-writing.zip` to confirm the layout.
3. Turn on code execution. On Team and Enterprise plans an owner may need to enable skills in organisation settings.
4. Upload the ZIP, then turn the skill on under **Customize**, then **Skills**.

Anthropic's help page on custom skills, opened on 28 November 2026 (it showed "Updated over 3 weeks ago" and no date), sets a 64-character limit for `name` and a 200-character limit for `description`, and says the ZIP must hold the skill folder at its root with the folder named after the skill. The `name` and description are within both limits. The plan list (Free, Pro, Max, Ultra, Team and Enterprise, with code execution enabled) is carried forward from the library's 27 November check of the "Use skills in Claude" page, which was not reopened today.

[Anthropic Help Center: How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) · [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Claude Code

Copy the runtime folder to `.claude/skills/seo-content-writing/` for a project or `~/.claude/skills/seo-content-writing/` for your user account. Keep `SKILL.md` and `references/` together. Type `/seo-content-writing` with the brief and dossier, or ask Claude to draft a page from an approved brief and let it load the skill from its description. The skill paths and `/skill-name` invocation were confirmed by opening the documentation page on 28 November 2026.

[Claude Code documentation: Extend Claude with skills](https://code.claude.com/docs/en/skills)

## Use

Attach or paste the approved brief with its approval record, the approved dossier, the editorial profile if there is one, and, for a change to an existing page, the current text of the sections in scope. Ask for one page at a time. Check that the output keeps the 9 sections in order, uses one exact status, and prints the approval, no-clearance and handoff lines in section 1. For voice rules, ask for profile mode and check the 8 profile sections.
