# Pass Gates

Everything in this file is operating method, not Google guidance. The gates follow the stage order in the Content Evidence, Briefing and Publishing QA playbook: the claims stage needs the human-approved editorial revision, the value and policy stage needs claims clearance, and publishing needs value and policy clearance.

## 1. The three passes

| Pass | Playbook stage | Question | Gate before it starts |
| --- | --- | --- | --- |
| Pass 1 Editorial | C1 Human Editorial Pass | Is this revision clear, in the right voice, true to the brief, with its qualifications intact? | The approved brief revision and the exact revision to check |
| Pass 2 Claims | C2 Fact, Claim and Commercial QA | Does every material claim match its evidence, approved meaning and conditions? | A person's approval of this exact revision after the editorial pass, and the evidence |
| Pass 3 Value and policy | C3 Reader Value, Originality and Spam-Policy QA | Does the page complete its task, deliver its contribution, stay distinct and avoid a policy concern? | Pass 2 cleared on this same revision |

The passes stay separate so a style improvement cannot quietly clear a factual failure, and a factual pass cannot stand in for a judgement on value.

## 2. Where a run starts

Start at the earliest pass whose gate record is missing:

- No record that a person approved this revision after an editorial pass: start at pass 1.
- A record names this exact revision as approved after the editorial pass: start at pass 2, and record pass 1 as `Recorded earlier` with the approver, role, date and revision.
- A record shows pass 2 cleared this exact revision, from an earlier run or a named reviewer: start at pass 3, and record passes 1 and 2 as `Recorded earlier`.

A gate record names the person, their role, the date, the exact revision and what they approved or cleared. A name alone, "looks good", an approval of a different revision, a calendar deadline or silence does not open a gate. Never record an approval that was not supplied.

## 3. How far one run goes

Run the passes in order on the same revision, as far as the gates allow:

- In full QA, pass 1 always ends the run. Its proposed edits, and the revision itself, need a person's approval before pass 2.
- When pass 2 clears, run pass 3 in the same turn on the same revision.
- When a pass returns corrections, stop. Later passes show `Not run: waiting for pass N clearance`.
- In a targeted check, the approved change request and the existing authority for the change stand in for the editorial approval, so the passes in scope run in one turn. Passes outside the scope are `Not applicable`. Record which passes were combined and what independence that cost. If the check finds the change is bigger than its authority covers, stop and say so; a bigger change needs full QA.

Never run a pass on a different revision from the one named in `Revision checked`. Never run a later pass to make up for an earlier one that failed or did not run, even if the user asks for "everything at once". Explain the gate in one sentence and run what the gates allow.

## 4. Pass states

Use exactly one state for each pass line in section 1:

| State | Meaning |
| --- | --- |
| `Cleared` | The pass ran on this revision. No publication blocker or material improvement is open. Minor corrections may be listed |
| `Cleared with proposed edits` | Pass 1 only. Every finding is resolved by the proposed edits, which change no claim beyond its approved meaning. A person applies them and approves the resulting revision |
| `Corrections needed` | At least one publication blocker or material improvement is open |
| `Recorded earlier` | A supplied record shows this pass was done on this exact revision. Name who, role, date and revision after the state |
| `Not run` | Follow with the missing gate or input, for example `Not run: waiting for approval of r3` |
| `Not applicable` | Outside the scope of a targeted check. Say why |

The pass states lead to the report status as follows. In full QA, pass 1 `Cleared` or `Cleared with proposed edits` gives **Editorial pass complete: Awaiting revision approval**, because the resulting revision still needs a person's approval. Any `Corrections needed` gives **Corrections needed: Returned to owner**. Every pass in scope `Cleared` or `Recorded earlier` on this revision gives **Cleared within scope: Ready for publishing handoff**.

## 5. Reopening a gate

- A corrected revision re-enters at the pass that returned it, with a bounded recheck. Record who made the corrections and who approved the corrected revision for recheck.
- Any change that adds, removes or rewords a claim, comparison, price, promise, attribution or disclosure goes to pass 2 for that passage, whoever made it and whenever it was made.
- A change to passages that were not returned goes through pass 1 for those passages before pass 2.
- New or changed release fields after a pass (title, meta description, headings, captions, alt text, structured data facts, call to action text) go back to pass 2 for their claims, and to pass 3 if they change the page's promise.
- Clearance belongs to one revision. It does not carry to a later revision without the recheck.

## 6. Independence

Start every pass from the brief, the evidence and the exact revision, not from the writer's account of it. If this session drafted or edited the page, say so in section 7 and recommend running passes 2 and 3 in a fresh context. A different account or model is not proof of independence, and the same one is not proof of failure. Never approve your own output, and never present an AI check as a human or specialist review. Record what independence was unavailable, especially when a targeted check combines passes.

## 7. What clearance is not

| State | Meaning |
| --- | --- |
| Draft or under review | Work in progress, not approved for release |
| Cleared within scope | This skill's checks are complete for this revision, with limits recorded |
| Approved | The responsible person actually approved this content and scope |
| Authorised for release | Existing or newly recorded authority covers the publishing action |
| Implemented | The change was applied. Production still needs checking |
| Technically verified | The live output and customer path were checked |
| Outcome reviewed | Search and business evidence was assessed over a suitable period |

A QA report can move a revision to `Cleared within scope`. Every other state needs its own person, record or check.
