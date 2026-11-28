# Claude App and Claude Code

Documentation checked 28 November 2026. For v0.1.0, installation has not been tested and invocation has not been confirmed in the Claude app or Claude Code. No behaviour case has been run.

## Claude app

1. Stage the runtime files in a folder named `ai-search-visibility/`, containing `SKILL.md` and `references/`. The folder name must match the `name` field in `SKILL.md`.
2. ZIP the folder itself so every entry starts with `ai-search-visibility/`. From the parent folder, run `zip -r ai-search-visibility.zip ai-search-visibility/SKILL.md ai-search-visibility/references/`, then `unzip -l ai-search-visibility.zip` to confirm the layout.
3. Turn on code execution. Anthropic's help page lists skills on Free, Pro, Max, Ultra, Team and Enterprise plans, and says the feature requires code execution. Your organisation's settings may also control skills on Team and Enterprise plans; that wasn't rechecked for this draft.
4. Add the skill under **Customize**, then **Skills**, and turn it on there.

The description is within the 200-character limit on Anthropic's help page, and the `name` is within its 64-character limit.

[Anthropic Help Center: How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

## Claude Code

Copy the runtime folder to `.claude/skills/ai-search-visibility/` in a project, or to `~/.claude/skills/ai-search-visibility/` for your user account. Keep `SKILL.md` and `references/` together. Type `/ai-search-visibility` with the site details and evidence, or ask about a site's AI Overview visibility and let Claude load the skill from its description. The documentation opened on 28 November 2026 confirms both locations, the `/skill-name` command and loading from the description.

[Claude Code documentation: Extend Claude with skills](https://code.claude.com/docs/en/skills)

## Use

Attach or paste the site, its Search Console properties, the priority pages, and whatever evidence you have: robots.txt, URL Inspection results, screenshots of the Search generative AI setting for every property that covers the pages, the Generative AI report export and any observation records. Ask for one site at a time. Check that the report keeps the 10 sections in order, uses one exact status, and prints the approval, no-change and control lines in section 1.
