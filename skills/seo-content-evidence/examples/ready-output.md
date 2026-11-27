# Ready Output

Expected output for the [ready input](ready-input.md). Synthetic example: it demonstrates the method, and none of the figures is real data or a client result.

## 1. Status and summary

**Ready for review: Evidence dossier**

The termite inspections page can say what an inspection covers, what it can't detect, how long it usually takes, what it costs and when the report arrives, all from the owner's approved records. Its strongest contribution is first-party: technicians recorded live termites or active workings at 157 of 412 inspections this year, which the page can use only with its period, definition and sample attached. None of the nine lines in the AI-assisted draft is usable as written, and three have supported replacements.

Page `https://banksiapest.example/termite-inspections/`. Full dossier mode. Dossier ED-07, revision 1, dated 27 Nov 2026. Evidence cut-off 15 Nov 2026.

Claims: 23. Verified for use 5, Verified with qualification 7, Approved attributable opinion or experience 1, Client confirmation required 2, Contradicted 3, Unsupported 5. Three optional proof requests are open, and one check (PR-03) must close before release.

`Dossier approval: Awaiting approval`

`This dossier does not approve publication or any claim on the business's behalf.`

`Brief handoff: Ready for B3`

## 2. Page decision and scope

- Page decision PD-07 (architecture plan SA-2026-11), approved by Mei Tan, owner, 18 Nov 2026: Improve, as a substantial rewrite, of the commercial service page `https://banksiapest.example/termite-inspections/`.
- Reader task: decide whether to book an annual or pre-purchase termite inspection, understand what it involves and costs, and book at `/book/`.
- Audience and market: homeowners and buyers in Perth's northern suburbs, Western Australia. Australian English.
- Boundary: `/termite-treatment/` owns treatment options and products. This page does not discuss treatment chemicals.
- Owners: Mei Tan confirms business facts and is the business's licensed pest manager. Sam Ortiz approves the dossier for briefing. No specialist reviewer is named.

## 3. Sources

| ID | Source | Type | Version or date | Checked | Label | Locations used | Permitted use | Limits |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Service scope sheet | Approved business record | Rev 3, 10 Nov 2026 | 27 Nov 2026 | Owner statement | Lines 1 to 8 | Business facts on this page | Technical statements in it rest on the owner's expertise |
| S02 | Licence record screenshots | Credential record | 12 Nov 2026 | 27 Nov 2026 | Supplied | Two records | Named technicians' licences | Not checked against the issuing register. No record for Ana Ruiz |
| S03 | Job log export | First-party data | 1 Jan to 31 Oct 2026 | 27 Nov 2026 | Supplied | "Activity found" field, time on site, header note | Counts and median with conditions | Customers who booked, recorded by technicians, not audited |
| S04 | Price list | Commercial record | Rev 5, effective 1 Nov 2026 | 27 Nov 2026 | Owner statement | Annual and pre-purchase rows | Prices with conditions | Changes at the next revision |
| S05 | Customer email | Testimonial | 3 Sep 2026 | 27 Nov 2026 | Supplied | Whole email | First name and suburb only | One customer's experience |
| S06 | Draft copy, AI-assisted | Proposed claims | 14 Nov 2026 | 27 Nov 2026 | Supplied | Lines 1 to 9 | None as evidence | Proposals, not proof |
| S07 | Franchise blog article | Third-party article | Undated | 27 Nov 2026 | Third-party claim | Cost figure | None | No source given |
| S08 | Pest association fact sheet | Secondary source | 2019, citing a 2009 survey | 27 Nov 2026 | Third-party claim | Cost figure | Research note only | The survey itself was not supplied |
| S09 | Owner note | Business record | 15 Nov 2026 | 27 Nov 2026 | Owner statement | Whole note | Career and business start dates | Not checked against a business register |
| S10 | Competitor page, as reported by the agency | Competitor claim | Not dated | 27 Nov 2026 | Third-party claim | Inspection time | None | What one competitor says about itself |
| S11 | Job photos A01 to A06 | Assets | 2026 | 27 Nov 2026 | Supplied | Six files | See section 7 | A06 shows a house number |
| S12 | Booking terms | Permission record | Clause 9 | 27 Nov 2026 | Owner statement | Clause 9 | Photo use without identifying details | Does not cover identifying details |

Not verified: the 2009 survey behind S08, and S07 and S10 online. None could be opened, and none is needed for a usable claim. Ana Ruiz's licence record was not supplied.

## 4. Claim register

| ID | Proposed claim and intended meaning | Type | Where used | Source and location | Status | Conditions and qualifications | Confidence | Owner | Review needed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CL-01 | Two inspection types, annual and pre-purchase, in the 14 listed northern suburbs | Factual, commercial | Intro, service area | S01 lines 1 and 2 | Verified for use | Use the listed suburbs | High | Mei Tan | No |
| CL-02 | What is checked: accessible interior rooms, roof void, subfloor where there is access, garden and fences within 50 m | Factual | What's included | S01 line 3 | Verified with qualification | Keep "accessible" and "where there is access" | High | Mei Tan | No |
| CL-03 | Visual inspection with a moisture meter and thermal camera, which help find areas to check more closely, cannot see inside walls, and no method finds all activity | Factual | Method | S01 line 4 | Verified with qualification | The limit travels with every mention of the tools | High | Mei Tan | No |
| CL-04 | "Our thermal imaging detects 100% of termite activity" | Factual | Draft line 2 | S06 line 2 against S01 line 4 | Contradicted | Remove. Replace with CL-03 | High | Mei Tan | No |
| CL-05 | Typically 60 to 90 minutes on site for a single-storey home up to 250 m², longer for larger or two-storey homes | Numerical | What to expect | S01 line 5, consistent with S03 | Verified with qualification | Keep the home size and storey conditions | High | Mei Tan | No |
| CL-06 | "Faster than other inspectors: we're done in under an hour" | Comparative, numerical | Draft line 8 | S06 line 8, S10, against S01 line 5 and S03 | Contradicted | Remove. Under an hour conflicts with CL-05 and CL-16, and one competitor's stated time is not a comparison | High | Mei Tan | No |
| CL-07 | The written report is emailed within one business day | Commercial | What to expect | S01 line 6 | Verified for use | Business days | High | Mei Tan | No |
| CL-08 | "Same-day reports" | Commercial | Draft line 3 | S06 line 3 against S01 line 6 | Contradicted | Remove. Replace with CL-07 | High | Mei Tan | No |
| CL-09 | No chemicals are applied during an inspection; treatment is quoted separately | Factual, commercial | What to expect | S01 line 7 | Verified for use | Link treatment questions to `/termite-treatment/` | High | Mei Tan | No |
| CL-10 | "Safe for kids and pets" | Regulated, safety | Draft line 5 | S06 line 5, no evidence | Unsupported | Remove. A safety claim about treatment products is outside this page | High | Treatment page owner | Yes, before any use on any page |
| CL-11 | "All our technicians are licensed" | Factual, credential | Trust | S02, two of three records | Client confirmation required | PR-01. Use CL-12 meanwhile | Medium | Mei Tan | No |
| CL-12 | Mei Tan and Leo Brandt hold current pest management licences, expiring in 2027 | Factual, credential | Trust | S02 | Verified with qualification | Name only these two. Recheck on the issuing register before release (PR-03) | Medium | Mei Tan | No |
| CL-13 | "Over 20 years' experience" | Numerical, experiential | Draft line 9 | S06 line 9 against S09 | Unsupported | Remove. Mei's 20 years is not "over 20", and the business is 15 years old. Replace with CL-14 | High | Mei Tan | No |
| CL-14 | Mei Tan has carried out timber pest inspections since 2006, and started Banksia Pest Services in 2011 | Factual, experiential | About the inspector | S09 | Verified for use | State the years, not a rounded total | Medium | Mei Tan | No |
| CL-15 | Of 412 inspections completed from 1 Jan to 31 Oct 2026, technicians recorded live termites or active workings at 157 (38%) | Numerical, first-party | Point of difference | S03 | Verified with qualification | Always state the period and definition (old damage alone is not counted). Customers who booked, often suspecting termites: not a rate for Perth homes or a risk for any one home | Medium | Mei Tan | No |
| CL-16 | Median time on site was 74 minutes across 398 timed inspections in the same period | Numerical, first-party | What to expect | S03 | Verified with qualification | State the period and that 14 inspections had no recorded time | Medium | Mei Tan | No |
| CL-17 | "1 in 3 Perth homes has termites" | Numerical | Draft line 7 | S06 line 7, no source | Unsupported | Remove. Must not be derived from CL-15, whose sample is customers who booked | High | Sam Ortiz | No |
| CL-18 | "Termites cause $1.5 billion of damage to Australian homes every year" | Numerical | Draft line 4 | S06 line 4, S07, S08 | Unsupported | Remove. S07 cites nothing, S08 gives a different figure from a 2009 survey, and neither is a primary source. Research note R1 | High | Sam Ortiz | No |
| CL-19 | "Australia's most trusted termite inspectors" | Comparative | Draft line 1 | S06 line 1, no evidence | Unsupported | Remove | High | Sam Ortiz | No |
| CL-20 | "All inspections comply with Australian Standards" | Regulated, technical | Draft line 6 | S06 line 6, no record | Client confirmation required | PR-02. Optional: the page can omit it | Low | Mei Tan | Yes, Mei as licensed pest manager |
| CL-21 | Jas P., Wanneroo: they found termites in the roof that the last inspector missed | Experiential | Testimonial | S05 | Approved attributable opinion or experience | First name and suburb only. One customer's experience, not a claim about other inspectors | High | Mei Tan | No |
| CL-22 | Annual inspection $295 and pre-purchase inspection $340, both including GST, for single-storey homes up to 250 m²; larger homes are quoted | Commercial | Pricing | S04 rev 5 | Verified with qualification | Keep GST, home size and the quote condition together. Recheck before release | High | Mei Tan | No |
| CL-23 | Strata complexes over four units and commercial buildings are not covered | Commercial | Who it's for | S01 line 8 | Verified for use | None | High | Mei Tan | No |

## 5. Figures, quotes and comparisons

- **CL-15:** 157 of 412 is 38.1%, so "38%" is correct when rounded. The count covers completed inspections from 1 Jan to 31 Oct 2026. "Activity found" means live termites or active workings seen by the technician; old damage alone is recorded as N. The sample is people who booked, often because they suspected termites, so the figure cannot describe Perth homes in general.
- **CL-16:** 398 of 412 rows have a time recorded. The median of 74 minutes is consistent with CL-05.
- **CL-22:** prices include GST and apply to single-storey homes up to 250 m². Larger homes are quoted, so "from" or "for homes up to 250 m²" must stay with the figure.
- **CL-13 and CL-14:** 2006 to 2026 is 20 years, not over 20. The business started in 2011.
- **CL-18:** S07 says $1.5 billion with no source. S08 says more than $1 billion, citing a 2009 survey that was not supplied. The figures conflict and neither is primary.
- **Quotes:** CL-21 is the customer's own wording from S05, with permission for first name and suburb.
- **Comparisons:** CL-06 and CL-19 compare the business with others without comparable evidence. No comparison is usable.

## 6. People, experience and review

- **Mei Tan:** owner and licensed pest manager (S02), inspecting since 2006 (S09). She approved the scope sheet and price list. She has not reviewed the AI-assisted draft (S06).
- **Leo Brandt:** licensed technician (S02). He took the job photos (S11).
- **Ana Ruiz:** technician whose licence record is pending (PR-01). Do not name her until it is supplied.
- **Sam Ortiz:** approves the dossier for briefing. Sam is not a technical reviewer.
- **First person:** "we" fits the business facts in S01 and S04, and "our technicians recorded" fits CL-15. The page must not imply testing of detection methods, a guarantee of finding termites, or experience beyond S09.
- **Regulated claims:** CL-10 is a safety claim about treatment products. It is outside this page, and any use on the treatment page needs a qualified review against the product's label and the rules that apply in Western Australia. CL-20 needs Mei to name the standard and what the report follows. This dossier does not decide whether either claim meets any law or standard.
- **AI assistance:** S06 was AI-assisted. All nine lines were checked against the business records. None is usable as written.

## 7. Assets and permissions

| ID | Asset | Provenance | What it shows | Permission and scope | Privacy check | Use limits | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A01 to A05 | Job photos | Leo Brandt, 2026 inspections (S11) | Mud tubes and workings in roof voids and subfloors | S12 clause 9, without identifying details | No identifying details visible | Captions describe what is shown. No "your home" or typical-result wording | Verified with qualification |
| A06 | Job photo | Leo Brandt, 2026 (S11) | Workings on an exterior wall | S12 clause 9 does not cover identifying details | House number visible | Do not use as supplied. A cropped version can be rechecked (PR-04) | Prohibited |

The testimonial (CL-21) is covered in section 4. No other assets were supplied.

## 8. Conflicts, gaps and proof requests

- **Inspection time:** S06 line 8 (under an hour) conflicts with S01 line 5 and S03. Resolved by the owner's scope sheet and the job log: CL-05 and CL-16.
- **Report timing:** S06 line 3 (same day) conflicts with S01 line 6. Resolved by S01: CL-07.
- **Damage cost:** S07 and S08 disagree, and neither is primary. Not resolved, and not needed for the reader's task.

| ID | Claim | Exact fact or asset needed | Why it matters | Acceptable evidence | Who can supply it | Can the page proceed without it? | State |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PR-01 | CL-11 | Ana Ruiz's current licence record, or confirmation that only Mei and Leo carry out inspections | Lets the page say all inspectors are licensed | Licence record or the issuing register entry | Mei Tan | Yes. The page names the two verified technicians (CL-12) | Open |
| PR-02 | CL-20 | The name and edition of the standard the inspection report follows, and which parts | A standards claim must name what it covers | Mei's written confirmation with the standard's reference | Mei Tan | Yes. The page omits the standards claim | Open |
| PR-03 | CL-12 | Both licences checked on the issuing register | The screenshots are supplied, not independently checked | Register entries with expiry dates | Sam Ortiz or Mei Tan | Yes for briefing. Must close before release | Open |
| PR-04 | A06 | A cropped photo with no house number | Adds one more real photo | Cropped file, rechecked for identifying details | Leo Brandt | Yes. Five photos remain | Open |

Research note R1: a national damage-cost figure could help a general guide later, but only from a primary source with its date and method. It is not production copy.

## 9. Brief handoff

Basis: evidence dossier. The page can offer something the reader can't get from a generic list: what technicians actually recorded across 412 inspections in 2026, real job photos, and a plain account of what an inspection covers and can't detect, from the owner's approved scope.

```text
Permitted claims: CL-01, CL-02 (accessible areas only), CL-03 (with its limit), CL-05 (home size and storeys), CL-07, CL-09 (link to /termite-treatment/), CL-12 (two named technicians), CL-14, CL-15 (period, definition, sample), CL-16 (period), CL-21 (first name and suburb), CL-22 (GST, size, quote condition), CL-23; assets A01 to A05 with descriptive captions
Do not use: CL-04 (use CL-03), CL-06, CL-08 (use CL-07), CL-10, CL-11 until PR-01, CL-13 (use CL-14), CL-17, CL-18, CL-19, CL-20 until PR-02, A06 as supplied
Open proof requests: PR-01, PR-02 and PR-04 are optional; PR-03 must close before release
Required reviews: CL-10 needs a qualified review on the treatment page before any use; CL-20 needs Mei's confirmation
Handoffs: prices (CL-22) and service area (CL-01) to schema review for any Service or Offer markup, with no review or rating markup from CL-21 without that review; the suburb list and prices to local SEO, to match the Business Profile; CL-10 to the treatment page owner
```

## 10. Freshness and review

- **CL-22:** recheck within seven days of release and at the next price list revision.
- **CL-12:** recheck on the register before release (PR-03) and before the 2027 expiry dates.
- **CL-15 and CL-16:** the data period ends 31 Oct 2026. Update only from a new export with the same field definitions, and state the period wherever the figures appear.
- **CL-01 to CL-03, CL-05, CL-07, CL-09 and CL-23:** recheck at the next scope sheet revision.
- **CL-21:** remove if the customer withdraws permission.
- A new licence record, a named standard or a cropped photo would move CL-11, CL-20 or A06. Sam Ortiz owns the next dossier review, and Mei Tan owns the business facts.

No ranking, traffic, AI citation or timing outcome is claimed.
