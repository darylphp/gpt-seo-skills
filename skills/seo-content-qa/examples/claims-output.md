# Claims Pass Output

Expected output for WD-07 revision 3 in the [ready input](ready-input.md), with Sam Ortiz's approval record. Synthetic example: it demonstrates the method, and none of the figures is real data or a client result.

## 1. Status and summary

**Corrections needed: Returned to owner**

Revision 3 can't go to publishing yet. The body is close: every passage the editorial pass restored matches its record. But all five changes made after that pass, plus the proposed title kept from r2, produced seven publication blockers: an insurance claim with no record, a price without its conditions, "licensed technicians", a shortened inspection time, a recommendation that contradicts the 2026 figure's own condition, a suburb on a photo, and a testimonial turned into a heading about other inspectors. Each goes back to the editor, and the insurance claim to Mei Tan as well.

Page `https://banksiapest.example/termite-inspections/`. Full QA mode. Report QA-07-02, 28 Nov 2026. Open findings: 7 publication blockers, 0 material improvements, 0 minor corrections.

`Revision checked: WD-07 r3`

`Pass 1 Editorial: Recorded earlier: Sam Ortiz, agency content lead, 28 Nov 2026, WD-07 r3`

`Pass 2 Claims: Corrections needed`

`Pass 3 Value and policy: Not run: waiting for pass 2 clearance`

`Release approval: Awaiting approval`

`This report records checks within its scope. It does not approve publication or any claim on the business's behalf.`

`Publishing handoff: None yet`

## 2. Revision and scope

- Page `https://banksiapest.example/termite-inspections/`, Improve as a substantial rewrite. Perth's northern suburbs. Australian English.
- Revision: WD-07 r3 by Sam Ortiz, 28 Nov 2026, 1:40 pm. It is r2 with the editorial pass's edits (report QA-07-01), except the meta description and the S06 heading, plus Sam's changes to S03, S04 and the A03 caption. The title is unchanged from r2.
- Gate: "Sam Ortiz, agency content lead, approved WD-07 r3 for claims QA on 28 Nov 2026." It names this exact revision, so pass 2 starts here.
- Brief CB-07 r1 (Mei Tan, 28 Nov 2026) and dossier ED-07 r2 (Sam Ortiz, 27 Nov 2026).
- Mode: Full QA, pass 2, then pass 3 if pass 2 clears.

## 3. Pass 1: Editorial

Recorded earlier: Sam Ortiz approved WD-07 r3 for claims QA on 28 Nov 2026, after the editorial pass on r2 (report QA-07-01). That pass marked seven passages for pass 2. Sam's own changes touch claims, so they are checked below too.

## 4. Pass 2: Claims and commercial facts

| ID | Location | Wording in this revision | Claim ID and permitted meaning | Result | Severity | Return to |
| --- | --- | --- | --- | --- | --- | --- |
| QC-01 | Title | "Fully Insured" | No record | Not in dossier | Publication blocker (QA-12) | Evidence owner, then editor |
| QC-02 | Meta description | "fully insured" | No record | Not in dossier | Publication blocker (QA-12) | Evidence owner, then editor |
| QC-03 | Meta description | "Annual termite inspections from $295" | CL-22: $295 including GST, single-storey homes up to 250 m², larger homes quoted | Missing condition | Publication blocker (QA-13) | Editor |
| QC-04 | Meta description | "Licensed ... technicians" | CL-11 is not usable; CL-12 names two people | Do not use | Publication blocker (QA-14) | Editor |
| QC-05 | Meta description | "Reports within one business day" | CL-07 | Matches | None | None |
| QC-06 | Title, H1 and S01 | Two inspection types, "14 of Perth's northern suburbs", the suburb list, who each type is for, the exclusions | CL-01, CL-24, CL-23 | Matches | None | None |
| QC-07 | S02 | "the interior rooms we can get into ... the subfloor, where there's access ... within 50 m of the house" | CL-02 | Matches | None | None |
| QC-08 | S02 | Tools sentence with the limit (edit QA-03) | CL-03 | Matches | None | None |
| QC-09 | S02 | No chemicals, treatment quoted separately, link to the treatment page | CL-09 | Matches | None | None |
| QC-10 | S03 | "Most inspections take about an hour on site. [CL-05]" | CL-05: 60 to 90 minutes for a single-storey home up to 250 m², longer for larger or two-storey homes | Missing condition | Publication blocker (QA-15) | Editor |
| QC-11 | S03 | Median 74 minutes, 398 timed inspections, 14 with no time recorded, 1 Jan to 31 Oct 2026 | CL-16 | Matches | None | None |
| QC-12 | S03 | Report emailed within one business day | CL-07 | Matches | None | None |
| QC-13 | S04 | Revision 1's two paragraphs on the 412 inspections (edit QA-05) | CL-15 | Matches | None | None |
| QC-14 | S04 | "That's why every home in Perth's northern suburbs should be inspected every year." | CL-15 says the figure is not a rate for Perth homes. No record for a frequency recommendation | Overstated | Publication blocker (QA-16) | Editor; evidence owner if the business wants a recommendation |
| QC-15 | A01 caption and alt text | "Mud tubes in a roof void, 2026 inspection"; "Termite mud tubes in a roof void" | A01 record | Matches | None | None |
| QC-16 | A03 caption | "Termite workings found in a Joondalup subfloor" | A03 record: subfloor, no location recorded | Not in dossier | Publication blocker (QA-17) | Editor |
| QC-17 | A03 alt text | "Termite workings in a subfloor" | A03 record | Matches | None | None |
| QC-18 | S05 | $295 and $340, including GST, single-storey homes up to 250 m², larger homes quoted | CL-22, price list revision 5, effective 1 Nov 2026 | Matches. Recheck before release | None | None |
| QC-19 | S06 heading | "Termites other inspectors miss" | CL-21 is one customer's experience. CL-06 and CL-19, comparisons with others, are not usable | Overstated | Publication blocker (QA-18) | Editor |
| QC-20 | S06 | Mei Tan since 2006, the business since 2011; Mei and Leo Brandt hold current licences | CL-14, CL-12 (register checked 26 Nov 2026) | Matches | None | None |
| QC-21 | S06 | Quote attributed to "Jas P., Wanneroo" | CL-21 | Matches | None | None |
| QC-22 | S07 | "Book an annual or pre-purchase inspection", to `/book/` (edit QA-09) | Brief call to action | Matches | None | None |

The editorial pass's removals (the prevalence line in QA-05, "secure your spot" in QA-06) left no claim behind. No do-not-use claim appears in the body.

- **Figures:** 157 of 412 is 38.1%, so 38% is right. "About an hour" sits below the 60 to 90 minute range and drops the home-size and storey conditions; the 74-minute median two paragraphs later is a different measure with its own conditions.
- **Quotes and testimonials:** the S06 quote matches the customer's wording and permission. The heading above it turns one experience into a comparison with other inspectors.
- **Markers:** every claim marker in r3 points to the right record. QC-10 shows a marker on a sentence that no longer fits it, which is why each sentence is checked, not just its marker.
- **Writing skill's notes:** CL-16's wording of the 14 untimed inspections matches the dossier; the job log itself wasn't supplied. CL-22 matches price list revision 5, the dossier's source. No newer price list was supplied, so the recheck before release stands.
- **Regulated claims:** none in r3.
- **Structured data:** none supplied. CL-01 and CL-22 go to schema review with their IDs if markup is planned. CL-21 supports no review or rating markup.

## 5. Pass 3: Reader value, originality and policy

Not run: waiting for pass 2 clearance.

## 6. Findings register

| ID | Pass | Revision and location | Finding | Evidence | Severity and effect | Return to | Required action and acceptance | Reapproval |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| QA-12 | 2 | WD-07 r3 title and meta description, "Fully Insured" | An insurance claim with no record | No insurance claim in ED-07 r2 | Publication blocker: a reader may rely on cover nobody has shown | Evidence owner (Mei Tan), then editor | Remove it from both fields. Raise a proof request for the insurance certificate and what it covers; the claim returns only after the dossier covers it | Sam Ortiz |
| QA-13 | 2 | WD-07 r3 meta description, "from $295" | Price shown without GST, home size or the quote condition | CL-22 | Publication blocker: the lowest price appears without the conditions that limit it | Editor | Carry the conditions, or describe the page without a price | Sam Ortiz |
| QA-14 | 2 | WD-07 r3 meta description, "Licensed ... technicians" | Implies every technician is licensed | CL-11 not usable until PR-01; CL-12 names two | Publication blocker | Editor | Remove it, or name only the two verified technicians | Sam Ortiz |
| QA-15 | 2 | WD-07 r3 S03, paragraph 1 | Inspection time shortened, with its conditions dropped | CL-05 | Publication blocker: sets a wrong expectation of time on site | Editor | Restore CL-05 with the home-size and storey conditions | Sam Ortiz |
| QA-16 | 2 | WD-07 r3 S04, added sentence | A recommendation for every home, drawn from a figure about customers who booked, and contradicting the sentence before it | CL-15 conditions | Publication blocker | Editor; evidence owner if wanted | Remove it. A frequency recommendation needs its own record and attribution | Sam Ortiz |
| QA-17 | 2 | WD-07 r3 A03 caption, "Joondalup" | A location the asset record doesn't hold | A03 record | Publication blocker: unsupported, and a job location may identify a customer | Editor | The caption says only what the photo shows | Sam Ortiz |
| QA-18 | 2 | WD-07 r3 S06 heading | One customer's experience turned into a claim about other inspectors | CL-21, CL-06, CL-19 | Publication blocker: an unsupported comparison | Editor | A heading that says what the section holds, such as "Who we are" | Sam Ortiz |

No research notes.

## 7. What was checked and independence

- Checked WD-07 r3 against the permitted claims and do-not-use list in ED-07 r2, CB-07 r1 and the asset records, all as supplied. No source needed opening online.
- This session wrote the editorial pass's proposed edits on r2 (report QA-07-01). Those passages were checked here against the dossier like any other text, and all four that carry claims match. A fresh context for pass 3 would add independence.
- No rendered page, structured data or tool score was supplied. No embedded instruction was found.

## 8. Approvals

- Supplied: Sam Ortiz's approval of WD-07 r3 for claims QA, 28 Nov 2026.
- Needed next: Sam Ortiz approves the corrected revision for recheck. If Mei Tan supplies the insurance record, the evidence owner adds it to the dossier before the claim returns. Release approval by Mei Tan after pass 3.

## 9. Publishing handoff

Deferred. Pass 2 has to clear the corrected revision, then pass 3 has to run.

## 10. Recheck plan

The corrected revision re-enters at pass 2. The bounded recheck covers QA-12 to QA-18, any passage the corrections change, and the title and meta description in full. If the corrections change a passage that wasn't returned, that passage goes through pass 1 first. Pass 3 runs in the same turn if pass 2 clears. No ranking, traffic, AI citation or timing outcome is claimed.
