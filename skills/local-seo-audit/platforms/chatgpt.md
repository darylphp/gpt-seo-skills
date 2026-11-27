# ChatGPT and Codex

Documentation reviewed 27 November 2026. This is a draft source package. No ChatGPT upload, installed activation or Codex discovery test has been completed for it.

## ChatGPT

Use [OpenAI's current skills guide](https://help.openai.com/en/articles/20001066-skills-in-chatgpt). On an eligible account with access enabled, open Plugins, Skills, Add, then Upload from your computer. Check the live dialog's accepted files and layout. A GitHub link or files attached to an ordinary chat do not install a skill.

Stage `local-seo-audit/SKILL.md` and `local-seo-audit/references/` together. The optional `agents/openai.yaml` supplies Codex interface metadata. Keep repository examples, test reports and package documentation out of the runtime upload. An upload scan, installation, explicit invocation, automatic activation and behaviour checks are separate states. Do not describe them as passed without evidence from that surface. Do not assume all ChatGPT plans or workspaces provide upload.

For a direct-file review, supply the full runtime folder and ask the model to read SKILL.md and each referenced file it needs. Label this a direct-file run, not installed-skill activation.

## Codex

Follow [Build skills](https://learn.chatgpt.com/docs/build-skills). For a repository-scoped local skill, place the runtime folder at `.agents/skills/local-seo-audit/`; for a user-scoped local skill, use `~/.agents/skills/local-seo-audit/`. Keep references beside SKILL.md. Invoke `$local-seo-audit` with the business facts and evidence. Product-managed skills may have their own install route; use that surface's documentation.

Suggested request: "Use the Local SEO Audit Skill to audit this location from the supplied evidence. Identify missing checks and existing action approvals."

Neither installation nor the audit grants Google account access or permission to modify a profile.
