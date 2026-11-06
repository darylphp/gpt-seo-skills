# ChatGPT and Codex

Documentation checked 6 November 2026.

## ChatGPT

On an eligible workspace with skill upload enabled, open **Plugins**, then **Skills**, then **Create** and **Upload from your computer**. Use the runtime files listed in the repository README. ChatGPT scans uploaded skills before making them available.

Check the upload dialog for its accepted file type and archive layout. **[needs confirmation]** The cited ChatGPT documentation does not specify the archive layout for a multi-file upload. Installation in a particular account depends on workspace eligibility, settings and access.

[OpenAI Help Center: Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

## Codex local discovery

Place the runtime folder at `.agents/skills/seo-content-brief/` for the repository or at `~/.agents/skills/seo-content-brief/` for the local user. The entry point is `seo-content-brief/SKILL.md` with `references/` beside it. Explicitly invoke `$seo-content-brief` in a Codex session with access to the source pack.

[OpenAI documentation: Build skills](https://learn.chatgpt.com/docs/build-skills)
