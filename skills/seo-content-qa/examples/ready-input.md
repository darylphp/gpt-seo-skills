# Ready Input

Synthetic fixture. The business, people, URLs, records, figures, approvals and draft text are fictional and supplied for simulation only. Nothing here is real search data, a real licence record or a client result. It continues the termite inspections example from the SEO Content Evidence and SEO Content Writing Skills: the writing skill's draft WD-07 revision 1 has been reworked by a person, and that revision comes to QA. The records QA needs are restated so this package stands alone.

## Request

"Use the SEO Content QA Skill on WD-07 revision 2 of our termite inspections page. Sam Ortiz signs off the editorial revision, and Mei Tan approves anything that goes live."

## Page and approvals

| Record | Detail |
| --- | --- |
| Page | Improve, as a substantial rewrite, `https://banksiapest.example/termite-inspections/`, a commercial service page. Homeowners and buyers in Perth's northern suburbs, Western Australia. Australian English. |
| ED-07 r2 | Evidence dossier revision 2, approved by Sam Ortiz (agency content lead) on 27 Nov 2026. PR-03 closed on 26 Nov 2026, when both licences were checked on the issuing register. |
| CB-07 r1 | Content brief revision 1, route W1 Local Service Content Writer, approved by Mei Tan (owner) on 28 Nov 2026 for a full rewrite of the body copy. No specialist review required. |
| EP-01 r1 | Editorial profile, approved by Mei Tan on 20 Nov 2026. |
| WD-07 r1 | Draft from the SEO Content Writing Skill, 28 Nov 2026, status `Draft ready for review: C1 editorial pass`, with claim markers and handoff notes (below). |
| WD-07 r2 | Priya Nair (agency writer) reworked r1 on 28 Nov 2026 at 10:30 am with an AI writing tool "to make it punchier", and added a proposed title, meta description and alt text for A01 and A03 as handoff notes, marked not cleared. No one has approved r2. |
| Owners | Sam Ortiz approves editorial revisions. Mei Tan owns business facts and approves publication. The agency web team implements in WordPress. |

## Permitted claims (ED-07 r2)

| ID | Permitted meaning | Conditions |
| --- | --- | --- |
| CL-01 | Two inspection types, annual and pre-purchase, in 14 northern suburbs: Ashby, Banksia Grove, Butler, Clarkson, Hocking, Joondalup, Merriwa, Mindarie, Pearsall, Quinns Rocks, Ridgewood, Sinagra, Tapping and Wanneroo | Use the listed suburbs |
| CL-02 | Checks accessible interior rooms, the roof void, the subfloor where there is access, and the garden and fences within 50 m of the house | Keep "accessible" and "where there is access" |
| CL-03 | Visual inspection with a moisture meter and thermal camera, which help find areas to check more closely; they can't see inside walls, and no method finds all termite activity | The limit travels with every mention of the tools |
| CL-05 | Typically 60 to 90 minutes on site for a single-storey home up to 250 m²; larger or two-storey homes take longer | Keep the home size and storey conditions |
| CL-07 | The written report is emailed within one business day | Business days |
| CL-09 | No chemicals are applied during an inspection; treatment is quoted separately | Link treatment questions to `/termite-treatment/` |
| CL-12 | Mei Tan and Leo Brandt hold current pest management licences | Name only these two. Checked on the issuing register 26 Nov 2026 |
| CL-14 | Mei Tan has carried out timber pest inspections since 2006, and started Banksia Pest Services in 2011 | State the years, not a rounded total |
| CL-15 | Of 412 inspections completed from 1 Jan to 31 Oct 2026, technicians recorded live termites or active workings at 157 (38%) | State the period and definition (old damage alone is not counted). Customers who booked, often suspecting termites: not a rate for Perth homes or a risk for any one home |
| CL-16 | Median time on site was 74 minutes across 398 timed inspections in the same period | State the period and that 14 inspections had no recorded time |
| CL-21 | Jas P., Wanneroo: "They found termites in the roof that the last inspector missed." | First name and suburb only. One customer's experience, not a claim about other inspectors |
| CL-22 | Annual inspection $295 and pre-purchase inspection $340, both including GST, for single-storey homes up to 250 m²; larger homes are quoted. Source: price list revision 5, effective 1 Nov 2026 | Keep GST, home size and the quote condition together. Recheck before release |
| CL-23 | Strata complexes over four units and commercial buildings are not covered | None |
| CL-24 | The annual inspection is for owners checking a home they already own; the pre-purchase inspection is for buyers who want a report before they commit to buying | None |
| A01 to A05 | Job photos from Leo Brandt's 2026 inspections: mud tubes and workings, no identifying details. A01 and A02 are roof voids; A03 to A05 are subfloors. The job location is not recorded | Captions say what the photo shows. No "your home", location or typical-result wording |

**Do not use:** CL-04 (100% detection), CL-06 (faster than other inspectors, done in under an hour), CL-08 (same-day reports), CL-10 (safe for kids and pets), CL-11 ("all our technicians are licensed", until PR-01 closes), CL-13 (over 20 years' experience), CL-17 (1 in 3 Perth homes), CL-18 ($1.5 billion damage figure), CL-19 (most trusted), CL-20 (Australian Standards, until PR-02 closes), A06. No insurance claim is recorded.

## Brief CB-07 r1, as QA needs it

- **Reader outcome:** a reader can tell which inspection fits them, what it covers and can't see, how long it takes, what it costs and how to book.
- **Boundary:** `/termite-treatment/` owns treatment options and products. This page links there from S02.
- **Contribution:** what technicians recorded across 412 inspections in 2026 (CL-15), real job photos, and a plain account of what an inspection covers and can't detect.
- **Voice (EP-01 r1):** Australian English, metric units, prices "including GST". "We" is Banksia Pest Services. Plain and calm. "Termite activity", and "infestation" only where one was found. Avoid "peace of mind", "don't wait", "the experts", superlatives, urgency and damage-cost scare lines. Headings say what the section answers. CTA wording: "Book an inspection".
- **Links:** `/book/` after S06 as the primary call to action. `/termite-treatment/` in S02.
- **Acceptance tests:** (a) the detection limit wherever the tools are mentioned; (b) CL-15 with its period, definition and sample limit; (c) both prices with GST and the home-size condition; (d) the service area listed once, as a list readers can scan, and not repeated in headings or body; (e) nothing about treatment products; (f) no do-not-use claim; (g) no word count target.

| ID | Purpose | Claims | Completion test |
| --- | --- | --- | --- |
| S01 | Which inspection, where | CL-01, CL-24, CL-23 | Reader can tell the two types apart, check their suburb and see the exclusions |
| S02 | Coverage and limits | CL-02, CL-03, CL-09 | "Accessible" conditions and the detection limit appear together; treatment goes to its page |
| S03 | Timing and report | CL-05, CL-16, CL-07 | Typical time keeps its home conditions; the median keeps its period and count |
| S04 | What we found in 2026 | CL-15, A01 to A05 | Period, definition and sample limit stated with the figure |
| S05 | Price | CL-22 | GST and home-size conditions travel with both prices |
| S06 | Who inspects | CL-14, CL-12, CL-21 | Only the two verified licences named; testimonial attributed as permitted |
| S07 | Book | None | Links to `/book/` |

Nearest page, supplied text: `/termite-treatment/` has the headings "Treatment options", "Chemical barriers", "Baiting systems", "Treatment prices" and "Book a treatment quote". No rendered page or preview of the draft is available.

## WD-07 r1 handoff notes (from the writing skill)

- Editorial pass: check that the two-sentence explanation of CL-15 in S04 reads plainly, and that "Who we are" works as the S06 heading.
- Claims pass: recheck CL-22 against the current price list; check CL-16's wording of the 14 untimed inspections.
- Value and policy pass: confirm that the S01 suburb list reads as a coverage check for readers, and that the page stays distinct from `/termite-treatment/`.
- Release fields go to publishing. Remove claim markers and section comments before release.

## WD-07 revision 2 (Priya Nair, 28 Nov 2026, 10:30 am)

Handoff notes, not cleared:

- Proposed title: "Termite Inspections in Perth's Northern Suburbs | Fully Insured | Banksia Pest"
- Proposed meta description: "Termite inspections from $295 across Perth. Our thermal cameras find hidden termites fast. Book today."
- A01 alt text: "termite inspection Perth termite damage Perth pest control Perth"
- A03 alt text: "Termite workings in a subfloor"

```markdown
<!-- S01 -->
# Annual and pre-purchase termite inspections

Termites don't take holidays, and neither should your vigilance. We carry out two kinds of termite inspection, also called timber pest inspections, for homes in 14 of Perth's northern suburbs. [CL-01]

- **Annual inspection:** for owners checking a home they already own.
- **Pre-purchase inspection:** for buyers who want a report on a home before they commit to buying it. [CL-24]

We cover Ashby, Banksia Grove, Butler, Clarkson, Hocking, Joondalup, Merriwa, Mindarie, Pearsall, Quinns Rocks, Ridgewood, Sinagra, Tapping and Wanneroo. [CL-01]

We don't inspect commercial buildings, or strata complexes with more than four units. [CL-23]

<!-- S02 -->
## What we check

We check:

- the interior rooms we can get into
- the roof void
- the subfloor, where there's access
- the garden and fences within 50 m of the house [CL-02]

This is a visual inspection, backed by a moisture meter and a thermal camera that pinpoint termite activity. [CL-03]

We don't apply any chemicals during an inspection, and treatment is quoted separately. [See termite treatment](https://banksiapest.example/termite-treatment/). [CL-09]

<!-- S03 -->
## How long it takes, and when you get the report

For a single-storey home up to 250 m², expect us on site for 60 to 90 minutes. Larger and two-storey homes take longer. [CL-05]

From 1 January to 31 October 2026, the median time on site was 74 minutes, across the 398 inspections with a recorded time. Another 14 had no time recorded. [CL-16]

We email your written report within one business day. [CL-07]

<!-- S04 -->
## What our technicians recorded in 2026

Termites are more common than you think: our technicians found active termites in 38% of homes we inspected this year. [CL-15]

[Asset A01: caption "Mud tubes in a roof void, 2026 inspection"]

[Asset A03: caption "Workings in a subfloor, 2026 inspection"]

<!-- S05 -->
## Price

| Inspection | Price, including GST |
| --- | --- |
| Annual inspection | $295 |
| Pre-purchase inspection | $340 |

These prices are for single-storey homes up to 250 m². Larger homes are quoted. [CL-22] Book today. Book today to secure your spot!

<!-- S06 -->
## Why choose Banksia Pest?

Mei Tan has carried out timber pest inspections since 2006, and started Banksia Pest Services in 2011. [CL-14] Mei and Leo Brandt hold current pest management licenses. [CL-12]

> "They found termites in the roof that the last inspector missed."
>
> Jas P., Wanneroo [CL-21]

<!-- S07 -->
## Book an inspection

[Get a free quote](https://banksiapest.example/book/)
```

## WD-07 revision 3 (Sam Ortiz, 28 Nov 2026, 1:40 pm)

Sam applied the editorial pass's proposed edits to r2, except where noted, and made these changes of his own:

- **Meta description:** rejected the proposed text and wrote: "Annual termite inspections from $295 in Perth's northern suburbs. Licensed, fully insured technicians. Reports within one business day."
- **Title:** left unchanged.
- **S03:** shortened the first paragraph to "Most inspections take about an hour on site. [CL-05]"
- **S04:** after the restored CL-15 sentences, added: "That's why every home in Perth's northern suburbs should be inspected every year."
- **A03 caption:** "Termite workings found in a Joondalup subfloor"
- **S06 heading:** "Termites other inspectors miss" instead of the proposed heading.

Approval record: "Sam Ortiz, agency content lead, approved WD-07 r3 for claims QA on 28 Nov 2026."

## WD-07 revision 4 (Priya Nair, 28 Nov 2026, 3:50 pm)

Priya changed only the passages returned by the claims pass on r3 (seven findings in six locations):

- **Title:** Termite Inspections in Perth's Northern Suburbs | Banksia Pest
- **Meta description:** Annual and pre-purchase termite inspections in 14 of Perth's northern suburbs: what we check, what no inspection can see, prices and booking.
- **S03 first paragraph:** "For a single-storey home up to 250 m², expect us on site for 60 to 90 mintues. Larger and two-storey homes take longer. [CL-05]"
- **S04:** removed the sentence added in r3.
- **A03 caption:** "Workings in a subfloor, 2026 inspection"
- **S06 heading:** "Who we are"

Sam raised PR-05 to Mei Tan for the insurance certificate and what it covers. The insurance claim stays off the page until it closes.

Approval record: "Sam Ortiz, agency content lead, approved WD-07 r4 for recheck on 28 Nov 2026. Only the returned passages changed."
