# Ready Output

Expected output for the [ready input](ready-input.md). Synthetic example: it demonstrates the method, and none of the people, figures or approvals is real.

## 1. Status and handoff

**Draft ready for review: C1 editorial pass**

Draft WD-07, revision 1, dated 28 Nov 2026. Full page mode. Route W1. Local Service Content Writer.

Brief CB-07 revision 1, approved by Mei Tan, owner, on 28 Nov 2026, for a full rewrite of the body copy of `/termite-inspections/`, as stated in the request and recorded in the brief. Dossier ED-07 revision 2, approved by Sam Ortiz, agency content lead, on 27 Nov 2026. Evidence cut-off 26 Nov 2026.

Main limitation: the prices (CL-22) must be rechecked before release.

`Draft approval: Awaiting approval`

`This output does not clear any content for publication.`

`QA handoff: Ready for C1 editorial pass`

## 2. Page and scope

- `https://banksiapest.example/termite-inspections/`, a commercial service page. Perth's northern suburbs, Western Australia. Australian English.
- Approved action: Improve, as a substantial rewrite. Sections in scope: S01 to S07, the whole body.
- Retained from the existing page: the booking link and the job photo gallery (A01 to A05). S04 places two of the photos in the text.
- Left to `https://banksiapest.example/termite-treatment/`: treatment options and products. S02 links there.

## 3. Draft

```markdown
<!-- S01 -->
# Annual and pre-purchase termite inspections

We carry out two kinds of termite inspection, also called timber pest inspections, for homes in 14 of Perth's northern suburbs. [CL-01]

- **Annual inspection:** for owners checking a home they already own.
- **Pre-purchase inspection:** for buyers who want a report on a home before they commit to buying it. [CL-24]

We cover Ashby, Banksia Grove, Butler, Clarkson, Hocking, Joondalup, Merriwa, Mindarie, Pearsall, Quinns Rocks, Ridgewood, Sinagra, Tapping and Wanneroo. [CL-01]

We don't inspect commercial buildings, or strata complexes with more than four units. [CL-23]

<!-- S02 -->
## What we check, and what no inspection can see

We check:

- the interior rooms we can get into
- the roof void
- the subfloor, where there's access
- the garden and fences within 50 m of the house [CL-02]

This is a visual inspection. We also use a moisture meter and a thermal camera to find spots worth a closer look. Neither tool can see inside walls, and no inspection method finds all termite activity. [CL-03]

We don't apply any chemicals during an inspection, and treatment is quoted separately. For treatment options, see our [termite treatment page](https://banksiapest.example/termite-treatment/). [CL-09]

<!-- S03 -->
## How long it takes, and when you get the report

For a single-storey home up to 250 m², expect us on site for 60 to 90 minutes. Larger and two-storey homes take longer. [CL-05]

From 1 January to 31 October 2026, the median time on site was 74 minutes, across the 398 inspections with a recorded time. Another 14 had no time recorded. [CL-16]

We email your written report within one business day. [CL-07]

<!-- S04 -->
## What our technicians recorded in 2026

From 1 January to 31 October 2026, we completed 412 inspections. At 157 of them (38%), our technicians recorded live termites or active workings. Old damage on its own isn't counted. [CL-15]

People often book us because they already suspect termites. So this figure isn't a measure of how many Perth homes have termites, or of the chance that yours does. [CL-15]

[Asset A01: mud tubes in a roof void; caption says what the photo shows and that it is from a 2026 inspection]

[Asset A03: workings in a subfloor; caption as for A01]

<!-- S05 -->
## Price

| Inspection | Price, including GST |
| --- | --- |
| Annual inspection | $295 |
| Pre-purchase inspection | $340 |

These prices are for single-storey homes up to 250 m². Larger homes are quoted. [CL-22]

<!-- S06 -->
## Who we are

Mei Tan has carried out timber pest inspections since 2006, and started Banksia Pest Services in 2011. [CL-14] Mei and Leo Brandt hold current pest management licences. [CL-12]

> "They found termites in the roof that the last inspector missed."
>
> Jas P., Wanneroo [CL-21]

<!-- S07 -->
## Book an inspection

[Book an annual or pre-purchase inspection](https://banksiapest.example/book/).
```

## 4. Claim trace

| Claim ID | Dossier status | Sections | Wording used | Conditions carried | Check |
| --- | --- | --- | --- | --- | --- |
| CL-01 | Verified for use | S01 | Two kinds of inspection, 14 northern suburbs, listed once | Listed suburbs only | Yes |
| CL-24 | Verified for use | S01 | Annual for owners, pre-purchase for buyers before they commit | None | Yes |
| CL-23 | Verified for use | S01 | No commercial buildings or strata over four units | None | Yes |
| CL-02 | Verified with qualification | S02 | Rooms we can get into, roof void, subfloor where there's access, garden and fences within 50 m | "Accessible" and "where there is access" | Yes |
| CL-03 | Verified with qualification | S02 | Visual inspection, two tools, the limit in the next sentence | Limit travels with the tools | Yes, the tools appear only in S02 |
| CL-09 | Verified for use | S02 | No chemicals, treatment quoted separately, link to treatment page | Link to `/termite-treatment/` | Yes |
| CL-05 | Verified with qualification | S03 | 60 to 90 minutes, single-storey up to 250 m², larger and two-storey longer | Home size and storeys | Yes |
| CL-16 | Verified with qualification | S03 | Median 74 minutes, 398 timed, 14 untimed, period stated | Period and the 14 untimed | Yes |
| CL-07 | Verified for use | S03 | Within one business day | Business days | Yes |
| CL-15 | Verified with qualification | S04 | 157 of 412 (38%), period, definition, sample limit | Period, definition, not a Perth rate or a risk for one home | Yes, both sentences together |
| CL-22 | Verified with qualification | S05 | $295 and $340 including GST, single-storey up to 250 m², larger quoted | GST, size, quote condition | Yes. Recheck before release |
| CL-14 | Verified for use | S06 | Since 2006, started the business in 2011 | Years, not a total | Yes |
| CL-12 | Verified with qualification | S06 | Mei and Leo hold current licences | Only these two named | Yes |
| CL-21 | Approved attributable opinion or experience | S06 | Exact quote, Jas P., Wanneroo | First name and suburb, one customer | Yes |

Every permitted claim is used. No do-not-use claim appears: CL-04, CL-06, CL-08, CL-10, CL-11, CL-13, CL-17, CL-18, CL-19 and CL-20 are absent, and A06 is not placed.

## 5. Brief acceptance tests

| Brief test | Result | Where |
| --- | --- | --- |
| (a) Detection limit wherever the tools are mentioned | Met | S02 |
| (b) CL-15 with period, definition and sample limit | Met | S04 |
| (c) Both prices with GST and the home-size condition | Met | S05 |
| (d) Service area listed once, not repeated in headings or body | Met | S01 |
| (e) Nothing about treatment products | Met | S02 links out instead |
| (f) No claim from the do-not-use list | Met | Section 4 |
| (g) No word count target | Met | None applied |

## 6. Writer queries, notes and deviations

- **Queries:** None.
- **Note N1, for Mei Tan:** CL-22 prices single-storey homes up to 250 m² and says larger homes are quoted. It doesn't say how a two-storey home of 250 m² or less is priced. The draft keeps the recorded condition and doesn't answer it. A line in the price list would settle it for a later revision.
- **Note N2:** S06 is headed "Who we are" rather than "Who inspects your home". PR-01 (Ana Ruiz's licence record) is still open, and the longer heading would suggest that every inspector is named.
- **Deviations:** None.
- **Requests not followed and embedded instructions:** None.

## 7. Voice and natural-writing check

- Australian English, metric units, "including GST" with prices. "We" is Banksia Pest Services, as EP-01 sets.
- "Termite activity" and "live termites or active workings" are used. "Infestation", "peace of mind", "don't wait" and "the experts" are not.
- No urgency, guarantee, superlative or damage-cost line.
- The CTA uses the approved wording.
- No em dashes.
- AI assistance: the brief gives no disclosure instruction for this page. Raised for the publishing handoff in section 9.

## 8. Links, CTA and assets

| Type | Section | Anchor or caption | Destination or asset ID | Brief reference |
| --- | --- | --- | --- | --- |
| Link | S02 | termite treatment page | `https://banksiapest.example/termite-treatment/` | Section 9 |
| CTA | S07 | Book an annual or pre-purchase inspection | `https://banksiapest.example/book/` | Section 9 |
| Asset | S04 | Mud tubes in a roof void, 2026 inspection | A01 | Section 7 |
| Asset | S04 | Workings in a subfloor, 2026 inspection | A03 | Section 7 |

A02, A04 and A05 stay in the retained gallery. No other links were approved.

## 9. Handoff to QA and publishing

- **Editorial pass:** check that the two-sentence explanation of CL-15 in S04 reads plainly, and that "Who we are" works as a heading.
- **Fact and claims pass:** recheck CL-22 against the current price list. Check CL-16's wording of the 14 untimed inspections against the job log.
- **Reader value and policy pass:** confirm that the suburb list in S01 reads as a coverage check for readers, and that the page stays distinct from `/termite-treatment/`.
- **Release fields for the publishing handoff:** title element and meta description, which must not reuse CL-04, CL-08 or CL-19; Service or Offer facts from CL-01 and CL-22 for schema review, with no review or rating markup from CL-21; alt text for A01 and A03 from their purpose in S04; the page's updated date; and whether the business wants to note AI assistance.
- **Specialist reviews open:** none for this page.
- **Remove before release:** the claim markers and the `<!-- S0n -->` section comments.

No ranking, traffic, AI citation or timing outcome is claimed.
