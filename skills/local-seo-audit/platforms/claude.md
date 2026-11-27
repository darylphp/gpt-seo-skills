# Claude app and Claude Code

Documentation reviewed 27 November 2026. This revision has not been installation- or invocation-tested in either surface.

## Claude app

Follow [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) and the live upload dialog. Enable code execution/file creation and Skills as required by the account or organisation settings. Open Customize > Skills to upload a custom skill. Package the runtime as a ZIP whose root contains the `local-seo-audit/` folder with SKILL.md and references inside. Keep the folder name aligned with the frontmatter name. Availability and navigation can change; the account's current settings decide access.

## Claude Code

Follow [Claude Code skills](https://code.claude.com/docs/en/skills). Put the runtime in `.claude/skills/local-seo-audit/` for a project or `~/.claude/skills/local-seo-audit/` for the user. `/local-seo-audit` is the documented invocation after discovery; invocation of this package has not been tested. Keep references beside SKILL.md.

The GPT and Claude drafts share the audit runtime, but platform notes, interface metadata and test records are separate. A direct-file GPT behaviour run does not establish Claude behaviour or installed activation on either platform.
