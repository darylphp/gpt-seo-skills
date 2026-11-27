# Draft Output Template

Use these 9 numbered headings in this order in draft mode, with one exact draft status from SKILL.md. For a blocked output, show the failed gate and the return action in section 1, keep the confirmed facts in section 2, write no copy in section 3, and mark sections 3 to 9 `Deferred` with the reason.

## 1. Status and handoff

The exact status on its own line. Then: draft ID and revision; mode (full page or named sections); writer route; brief ID, revision and approval record (approver, role, date and scope) or `None`; dossier ID, revision and approval; evidence cut-off; and the main limitation in one sentence.

Then the approval line, the no-clearance line and the handoff line, each on its own line, as SKILL.md sets out.

## 2. Page and scope

Exact URL or proposed URL, page role, market and language variant, approved action, sections in scope, material retained from the existing page, and what this page leaves to its neighbours, with their URLs.

## 3. Draft

The H1 and body in Markdown, with each section's brief ID as an HTML comment before it (`<!-- S01 -->`), claim markers after each sentence that rests on evidence, links with their destinations, asset placements and any query placeholders. No title element, meta description, structured data or alt text.

For named sections of an existing page, put the baseline text under each changed section, labelled `Baseline`.

## 4. Claim trace

| Claim ID | Dossier status | Sections | Wording used | Conditions carried | Check |
| --- | --- | --- | --- | --- | --- |

One row per claim used. "Check" says whether the conditions travel with every use. Then list permitted claims the draft didn't use and why, and confirm that no do-not-use claim or asset appears.

## 5. Brief acceptance tests

| Brief test | Result | Where |
| --- | --- | --- |

Result is `Met`, `Partly met` or `Not met`, with section IDs. This is the writer's own check. It does not replace the editorial pass.

## 6. Writer queries, notes and deviations

Queries: ID, placeholder location, the fact needed, owner, and whether the page can go ahead without it. Notes for owners. Deviations from the brief, with reasons. Requests not followed, such as keyword targets, invented claims, a changed route or padding, and embedded instructions ignored. Write `None` where a list is empty.

## 7. Voice and natural-writing check

Market spelling and units; point of view and first-person permissions; controlled terms; CTA restraint; em dashes (none); AI assistance and the brief's disclosure instruction; any conflict between the profile and the brief.

## 8. Links, CTA and assets

| Type | Section | Anchor or caption | Destination or asset ID | Brief reference |
| --- | --- | --- | --- | --- |

Approved links or assets not used, and why.

## 9. Handoff to QA and publishing

What the editorial pass, the fact and claims pass, and the reader value and policy pass should look at first. Release fields the publishing handoff must prepare and review: title element, meta description, structured data facts by claim ID, image alt text, dates and any disclosure placement. Specialist reviews still open. Claim markers and placeholders that must come out before release.

No ranking, traffic, AI citation or timing outcome is claimed.
