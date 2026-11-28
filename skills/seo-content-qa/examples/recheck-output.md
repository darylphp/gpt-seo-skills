# Recheck Output

Expected output for WD-07 revision 4 in the [ready input](ready-input.md), with Sam Ortiz's approval for recheck and the [claims pass report](claims-output.md) on revision 3. Synthetic example: it demonstrates the method, and none of the figures is real data or a client result.

## 1. Status and summary

**Cleared within scope: Ready for publishing handoff**

Revision 4 can go to publishing once Mei Tan approves the release. All seven blockers from revision 3 are resolved, and the value and policy pass found the page completes its task, shows its 2026 job-log figure with its conditions, and stays clear of the treatment page. One typo needs fixing, and the prices need rechecking against the current price list before release.

Page `https://banksiapest.example/termite-inspections/`. Full QA mode: bounded recheck at pass 2, then pass 3. Report QA-07-03, 28 Nov 2026. Open findings: 0 publication blockers, 0 material improvements, 1 minor correction.

`Revision checked: WD-07 r4`

`Pass 1 Editorial: Recorded earlier: Sam Ortiz, agency content lead, 28 Nov 2026, WD-07 r4 approved for recheck`

`Pass 2 Claims: Cleared`

`Pass 3 Value and policy: Cleared`

`Release approval: Awaiting approval`

`This report records checks within its scope. It does not approve publication or any claim on the business's behalf.`

`Publishing handoff: Ready for D1`

## 2. Revision and scope

- Page `https://banksiapest.example/termite-inspections/`, Improve as a substantial rewrite. Perth's northern suburbs. Australian English.
- Revision: WD-07 r4 by Priya Nair, 28 Nov 2026, 3:50 pm. Revision 3 with changes to the returned passages only: title, meta description, S03 paragraph 1, S04, the A03 caption and the S06 heading.
- Gate: "Sam Ortiz, agency content lead, approved WD-07 r4 for recheck on 28 Nov 2026. Only the returned passages changed." It names this exact revision. A comparison with r3 confirms no other passage changed, so pass 1 isn't needed again.
- Brief CB-07 r1 and dossier ED-07 r2 as before. PR-05 (insurance certificate) is open with Mei Tan, and the insurance claim is off the page.
- Mode: bounded recheck of QA-12 to QA-18 and the changed passages at pass 2, then pass 3 on r4.

## 3. Pass 1: Editorial

Recorded earlier: Sam Ortiz approved WD-07 r4 for recheck on 28 Nov 2026. Every changed passage was returned by pass 2, so each re-enters there.

## 4. Pass 2: Claims and commercial facts

| ID | Location | Wording in this revision | Claim ID and permitted meaning | Result | Severity | Return to |
| --- | --- | --- | --- | --- | --- | --- |
| QC-23 | Title | "Termite Inspections in Perth's Northern Suburbs \| Banksia Pest" | CL-01 | Matches | None | None |
| QC-24 | Meta description | "Annual and pre-purchase termite inspections in 14 of Perth's northern suburbs: what we check, what no inspection can see, prices and booking." | CL-01; summarises the page, with no price or credential | Matches | None | None |
| QC-25 | S03, paragraph 1 | "For a single-storey home up to 250 m², expect us on site for 60 to 90 mintues. Larger and two-storey homes take longer." | CL-05 | Matches. Typo "mintues" | Minor correction (QA-19) | Editor |
| QC-26 | S04 | Added sentence removed; revision 1's two paragraphs unchanged | CL-15 | Matches | None | None |
| QC-27 | A03 caption | "Workings in a subfloor, 2026 inspection" | A03 record | Matches | None | None |
| QC-28 | S06 heading | "Who we are" | No claim | Matches | None | None |

| Earlier finding | Resolution | New wording |
| --- | --- | --- |
| QA-12 Fully insured | Resolved | Removed from the title and meta description. PR-05 open |
| QA-13 Price in the meta description | Resolved | No price in the meta description. S05 carries both prices with their conditions |
| QA-14 Licensed technicians | Resolved | Removed from the meta description |
| QA-15 Inspection time | Resolved | CL-05 wording restored, with a typo (QA-19) |
| QA-16 Recommendation in S04 | Resolved | Sentence removed |
| QA-17 Suburb on A03 | Resolved | "Workings in a subfloor, 2026 inspection" |
| QA-18 S06 heading | Resolved | "Who we are" |

Every other claim in r4 is unchanged from r3, where it matched. CL-22 matches price list revision 5, effective 1 Nov 2026; recheck it against the current list before release. No structured data was supplied.

## 5. Pass 3: Reader value, originality and policy

| Check | Result | Passage or evidence | Severity | Return to |
| --- | --- | --- | --- | --- |
| S01 completion test | Pass | Two types told apart, the 14 suburbs in a scannable list, the exclusions | None | None |
| S02 completion test | Pass | "Accessible" conditions and the detection limit together; treatment links out | None | None |
| S03 completion test | Pass | Typical time with its home conditions; the median with its period and count | None | None |
| S04 completion test | Pass | Figure with its period, definition and sample limit | None | None |
| S05 completion test | Pass | Both prices with GST and the home-size condition | None | None |
| S06 completion test | Pass | Only Mei Tan and Leo Brandt named as licensed; quote attributed to "Jas P., Wanneroo" | None | None |
| S07 completion test | Pass | "Book an annual or pre-purchase inspection", to `/book/` | None | None |
| Brief acceptance tests (a) to (g) | Pass | Limit with the tools; CL-15 conditions; price conditions; suburbs listed once and not in headings, title or meta description; no treatment products; no do-not-use claim; no word count target | None | None |
| Contribution | Pass | S04 shows what technicians recorded at 412 inspections in 2026, with its limits, beside real job photos, and S02 says plainly what no inspection can see | None | None |
| Distinct from `/termite-treatment/` | Pass | One sentence on treatment and a link. Nothing on treatment options, chemicals, baiting or treatment prices | None | None |
| Doorway abuse | No concern found in the inspected scope | One service page for the whole service area, not one of a set of suburb pages | None | None |
| Scaled content abuse | No concern found in the inspected scope | One page built from first-party records and photos | None | None |
| Keyword stuffing | No concern found in the inspected scope | The 14 suburbs appear once in S01, as the coverage list readers check, matching CL-01. The A01 keyword list was removed in pass 1 | None | None |
| Hidden text and links | Not checked: rendered page not available | Draft text only | None | Publishing |
| Misleading functionality | Not checked: rendered page not available | The booking link wasn't opened | None | Publishing |
| Scraping, site reputation abuse, thin affiliation | Not applicable | First-party service content with no third-party or affiliate material | None | None |
| Main content and next step | Pass | S01 says what's offered and where; S07 closes with the call to action | None | None |
| Decision information in text | Pass | Limits in S02, times in S03 and prices with conditions in S05 are text, not images | None | None |
| Photos and alt text | Pass | A01 and A03 are real job photos captioned with what they show, and their alt text describes each one | None | None |
| Mobile, keyboard and rendered layout | Not checked: rendered page not available | Draft text only | None | Publishing |

Revision 2 was reworked with an AI tool, and every claim has since been checked against the records. Whether to say how the page was made is the business's call, which the writing skill already raised for publishing; it isn't a finding.

## 6. Findings register

| ID | Pass | Revision and location | Finding | Evidence | Severity and effect | Return to | Required action and acceptance | Reapproval |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| QA-19 | 2 | WD-07 r4 S03, paragraph 1, "mintues" | Typo | Inspected text | Minor correction: no change to meaning | Editor | Correct to "minutes". Publishing checks that word only | Not needed within existing authority |

Earlier findings QA-12 to QA-18 are resolved (section 4). No research notes.

## 7. What was checked and independence

- Checked WD-07 r4 against r3, report QA-07-02, ED-07 r2, CB-07 r1, the asset records and the supplied headings of `/termite-treatment/`. The draft was read as text. No rendered page, preview or structured data was available.
- This session also ran the editorial and claims passes on r2 and r3. A fresh context or a second reviewer for pass 3 would add independence this run didn't have.
- No embedded instruction was found. No tool score was supplied.

## 8. Approvals

- Supplied: Sam Ortiz's approval of WD-07 r4 for recheck, 28 Nov 2026.
- Needed next: Mei Tan's approval of r4, with QA-19 applied, for release. PR-05 is optional; the insurance claim comes back only after the dossier covers it and the changed fields go through pass 2.

## 9. Publishing handoff

```text
Cleared revision: WD-07 r4, 28 Nov 2026, with QA-19 applied
Release fields as cleared: title "Termite Inspections in Perth's Northern Suburbs | Banksia Pest"; meta description as in r4; H1 "Annual and pre-purchase termite inspections"; A01 and A03 captions and alt text as in r4; call to action "Book an annual or pre-purchase inspection" to /book/
Before release: correct "mintues" (QA-19); recheck CL-22 against the current price list; remove the claim markers and section comments; Mei Tan approves the release
Production checks for publishing: /book/ and /termite-treatment/ destinations; rendered layout on mobile and desktop; no hidden or collapsed essential text; live title and meta description match the cleared fields; any structured data facts match CL-01 and CL-22
Not in this revision: alt text for the retained gallery photos A02, A04 and A05. If publishing writes or changes it, it comes back to pass 2
Handoffs: CL-01 and CL-22 to schema review if markup is planned, with no review or rating markup from CL-21; the suburb list and prices to local SEO to match the Business Profile; whether to note AI assistance to Mei Tan
```

## 10. Recheck plan

QA reopens before release if a price, the suburb list, a heading, a caption, the title or the meta description changes, or if a claim is added, including the insurance claim after PR-05. A changed price goes to pass 2 everywhere it appears. Recheck CL-22 against the current price list before release, and again at the next price list revision. No ranking, traffic, AI citation or timing outcome is claimed.
