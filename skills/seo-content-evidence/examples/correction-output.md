# Targeted Check Output

Expected output for a correction to the page in the [ready input](ready-input.md). Synthetic example.

Request: "Our annual inspection price goes up to $310 from 1 December. Check the evidence for the termite inspections page before we update it." Supplied with it:

- S13: email from Mei Tan, 25 Nov 2026: "Annual inspections are $310 from 1 December."
- S14: price list revision 6, draft, unsigned: "Annual inspection $310 + GST. Effective 1 Dec 2026."
- S15: page source export of `/termite-inspections/`, 25 Nov 2026, from the agency.
- S04 (price list revision 5) and dossier ED-07 revision 1 from the earlier dossier.

## 1. Status and summary

**Evidence gaps: Proof requests open**

The new annual price can't be released yet, because the two records disagree on GST: Mei's email gives $310 with no tax basis, and the draft price list says $310 plus GST, which is $341 including GST. The old price of $295 appears in three places in the page export (the pricing table, the meta description and the structured data), and possibly in a price graphic and a PDF that weren't supplied. Every one needs the same corrected figure once Mei confirms it, and the change shouldn't go live before 1 December.

Page `https://banksiapest.example/termite-inspections/`. Targeted check mode. Dossier ED-07, revision 2, dated 27 Nov 2026. Evidence cut-off 25 Nov 2026.

Claims checked: 2. Client confirmation required 1, Verified with qualification 1 (unchanged). Two proof requests are open.

`Dossier approval: Awaiting approval`

`This dossier does not approve publication or any claim on the business's behalf.`

`Brief handoff: None yet`

## 2. Page decision and scope

- Correction to the annual inspection price on `/termite-inspections/`, requested by Mei Tan (owner). No new brief is needed.
- Baseline: CL-22 in ED-07 revision 1, "Annual inspection $295 and pre-purchase inspection $340, both including GST, for single-storey homes up to 250 m²; larger homes are quoted", from S04 revision 5.
- Scope: the annual price and every place it appears. The pre-purchase price is not changing (S13 and S14 mention only the annual price).
- The revision 1 approval does not carry over to revision 2.

## 3. Sources

| ID | Source | Type | Version or date | Checked | Label | Locations used | Permitted use | Limits |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S04 | Price list | Commercial record | Rev 5, effective 1 Nov 2026 | 27 Nov 2026 | Owner statement | Annual and pre-purchase rows | Current prices until 30 Nov 2026 | Superseded from 1 Dec 2026 if rev 6 is approved |
| S13 | Owner email | Business record | 25 Nov 2026 | 27 Nov 2026 | Owner statement | Whole email | New price and date | No tax basis |
| S14 | Price list, draft | Commercial record | Rev 6, unsigned | 27 Nov 2026 | Supplied | Annual row | None until approved | Not approved. Says "+ GST" |
| S15 | Page source export | Page content | 25 Nov 2026 | 27 Nov 2026 | Supplied | Body, title, meta description, JSON-LD | Locations of the current price | Export, not the live page |

Not verified: the price graphic `/images/inspection-prices.png` and the PDF `/files/price-guide.pdf`, which are linked from the page but were not supplied, and the Business Profile.

## 4. Claim register

| ID | Proposed claim and intended meaning | Type | Where used | Source and location | Status | Conditions and qualifications | Confidence | Owner | Review needed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CL-24 | Annual inspection $310 from 1 Dec 2026, single-storey homes up to 250 m² | Commercial | Every location in section 9 | S13, S14 annual row | Client confirmation required | PR-05: the GST basis and an approved rev 6 | Low | Mei Tan | No |
| CL-22 | Pre-purchase inspection $340 including GST, same conditions | Commercial | Pricing table | S04 rev 5 | Verified with qualification | Unchanged. Recheck when rev 6 is approved | High | Mei Tan | No |

## 5. Figures, quotes and comparisons

- **Tax basis:** S13 says $310. S14 says $310 + GST, which at 10% is $341 including GST. Revision 5 showed prices including GST, so the page states GST-inclusive prices. Until the basis is confirmed, the page can't show either figure.
- **Effective date:** both S13 and S14 say 1 Dec 2026. The current price of $295 stays correct until then.
- **Conditions:** home size and the quote condition for larger homes carry over unchanged.

## 6. People, experience and review

Not applicable. No people, experience or regulated claims are affected.

## 7. Assets and permissions

The price graphic `/images/inspection-prices.png` shows prices as an image. It was not supplied, so its text is `Not verified`. It must be checked and replaced along with the page text.

## 8. Conflicts, gaps and proof requests

- **GST basis:** S13 and S14 conflict. Not resolved.

| ID | Claim | Exact fact or asset needed | Why it matters | Acceptable evidence | Who can supply it | Can the page proceed without it? | State |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PR-05 | CL-24 | Whether the new annual price is $310 including GST or $310 plus GST, and the approved price list revision 6 | The page states GST-inclusive prices, and the wrong figure would misstate the price by $31 | Signed revision 6 | Mei Tan | No. Keep $295 until 1 Dec and until PR-05 closes | Open |
| PR-06 | CL-24 | The price graphic and price guide PDF | They may still show $295 after the text changes | The files, or screenshots of the live versions | Agency | Yes for the check. Both must be updated before release | Open |

## 9. Brief handoff

Not needed: this is a correction, and it goes to the editor once PR-05 closes. Every location that shows the annual price must change together:

```text
Body pricing table: annual row (S15, main content)
Title element: no price (S15), no change
Meta description: "Annual termite inspections from $295" (S15)
JSON-LD Offer for the annual inspection: price 295 (S15), to schema review with CL-24 once confirmed
Price graphic /images/inspection-prices.png: Not verified (PR-06)
Price guide PDF /files/price-guide.pdf: Not verified (PR-06)
Business Profile service prices: to local SEO, to match the page
```

## 10. Freshness and review

- **CL-24:** release on or after 1 Dec 2026, once PR-05 and PR-06 close. Recheck the live page, its meta description and structured data after release.
- **CL-22:** recheck when revision 6 is approved, in case the pre-purchase price changes too.
- A price change is a real update to the page. Any visible "updated" date should reflect it accurately, without implying a wider review.

No ranking, traffic, AI citation or timing outcome is claimed.
