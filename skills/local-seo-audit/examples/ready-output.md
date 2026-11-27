# Ready Output

Synthetic output for [ready-input.md](ready-input.md). Fictional business and evidence.

## 1. Audit status and scope

- Status: Ready for review: Local SEO audit
- Location: Larkspur Plumbing, service-area profile based in Lara (BR-07)
- Audit date 6 November 2026. Evidence cut-off 5 November 2026.
- Evidence basis: supplied public profile screenshots, a GBP performance export, a website crawl export, a GA4 summary and owner-confirmed facts. No direct account access.
- Covered: eligibility, profile fields, phone, review requests, profile destination, local pages, measurement and the reported Maps drop. Not covered: citations, structured data, photos and review replies, for lack of evidence.
- Main limitation: the routing and control of PH-B are untested, and there is no comparable visibility baseline.

Implementation approval: Awaiting approval

## 2. Business record

Larkspur Plumbing is a service-area plumbing business. Its plumbers travel to customers from the owner's home base in Lara, which does not receive customers. The customer action that matters is a call or an enquiry form. BR-07, confirmed by Jo Tran on 3 November 2026, sets the approved name, eight service areas, weekday hours of 7:00 to 17:00, phone PH-A, four service groups and the Plumber category. Jo owns the profile. The requester manages it under written consent CON-1. Missing: who controls PH-B, any pending edits, and approval to reply to reviews.

## 3. Evidence inspected

| Source | What it showed | Date | Label | Limits |
| --- | --- | --- | --- | --- |
| E1 public profile | Name, address, hours, phone, categories, areas and link differ from BR-07 | 4 Nov 2026 | Supplied | Screenshots only. No edit history or verification state. |
| E2 crawl export | 26 near-identical suburb pages, 18 outside coverage | 5 Nov 2026 | Supplied | No structured data columns |
| E3 review card | Discount offered for a 5-star review | 3 Nov 2026 | Supplied | One card. Other request channels unknown. |
| E4 GBP export | Calls 212 and 241, website clicks 96 and 88, views down 9% | 4 Nov 2026 | Supplied | Includes organic and Ads activity. Calls are call-button clicks. |
| E5 GA4 summary | No campaign tags on the profile link. Form enquiries 31 and 29. | 5 Nov 2026 | Supplied | Profile visits cannot be isolated |
| E6 agency report | GBP calls reported as leads | Oct 2026 | Supplied | Definition error, not new data |
| E7 rank screenshot | Fifth for "plumber geelong" from Lara | 2 Nov 2026 | Supplied | One sample, no baseline, owner's own location |
| BR-07 | Approved facts | 3 Nov 2026 | Approved fact | None noted |

Not verified: PH-B control and routing, verification state, pending edits, citations, structured data, photos and existing review replies.

## 4. Eligibility, representation and access

The business makes in-person contact with customers at their premises, which fits a service-area profile [G01, G02]. Because the base does not receive customers, the address should be hidden [G01, G03]. The profile currently shows the owner's home address. E4 is a supplied historical performance export. Although Google limits performance access to verified profiles [G10], this does not establish the current verification state; it remains Not verified without current account evidence or owner confirmation. Ownership and manager consent are recorded. Reply approval is not, so no review replies should be posted on the business's behalf yet [G04]. Name, category and address edits can affect verification [G06, G07], so they should go in one approved, grouped change.

## 5. Profile accuracy

| Field | Observed | Approved fact | Finding | Evidence and confidence |
| --- | --- | --- | --- | --- |
| Name | Larkspur Plumbing Geelong 24/7 Emergency Plumber | Larkspur Plumbing | Keywords and availability text added to the name [G01] | E1 and BR-07, High |
| Categories | Plumber, Emergency plumber, Roofing contractor | Plumber | Two categories describe services the business does not offer | E1 and BR-07, High |
| Address | Lara street address shown | Hidden for a service-area business | Private address exposed | E1 and BR-07, High |
| Service areas | 20, including Melbourne, Werribee and Ballarat | Eight Geelong-region areas | Areas outside real coverage | E1 and BR-07, High |
| Hours | Open 24 hours | Mon to Fri, 7:00 to 17:00 | Customers may expect a service that does not exist | E1 and BR-07, High |
| Phone | PH-B, set up by the former agency | PH-A | Business control of PH-B not shown [G01] | E1 and notes, High for the gap, Low for any misrouting |
| Website link | `/geelong-plumber/` | Homepage holds the service detail | Link points to a template page | E1 and E2, Medium |
| Description, services, attributes, photos | Not supplied | Not supplied | Not verified | None |

## 6. Reviews and reputation

The request card offers a 10% discount for a 5-star review. That is an incentive and a rating request, both prohibited [G11]. Disclosure would not make it acceptable. Other request channels and reply quality were not supplied. No approval to reply is recorded.

## 7. Website, local pages, citations and structured data

The profile links to a suburb template page rather than the homepage that holds the service detail. The site has 26 suburb pages built from one 180-word template with swapped place names and the same stock photos. Eighteen of them describe areas the business does not serve. The set matches the doorway pattern of near-identical city pages funnelling to one contact page [G14]. There is no evidence of a manual action, so the spam-policy risk is Medium; the accuracy problem on the 18 out-of-area pages is High. Citations and structured data are Not verified.

## 8. Measurement and visibility baseline

Calls fell from 241 to 212 (down 12%) while website clicks rose from 88 to 96 (up 9%) and form enquiries moved from 29 to 31. GBP calls are call-button clicks, not answered calls, and the data includes Ads activity [G10]. The former agency's report counts those clicks as leads, which overstates what the metric shows. The comparison period is the business's busiest season, and the profile number is an untested tracking line. The profile link has no campaign tags, so profile visits cannot be separated in GA4. The single rank screenshot has no baseline and was taken at the owner's home, so it cannot show a drop [G18].

## 9. Prioritised findings and actions

| ID | Priority | Area | Finding | Evidence and confidence | Smallest action | Owner and approval needed | Acceptance check | Review trigger |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F1 | Urgent | Phone | PH-B is a former agency tracking number. Business control and routing are unknown. | E1 and notes. Gap High, misrouting Low. | With owner authorisation, test PH-B during and after hours. If the business cannot show control and correct routing, replace it with PH-A on the profile and wherever else PH-B appears. | Jo Tran approves. Manager submits under CON-1. | Tap-to-call on mobile reaches the business on a number it controls | Public check after processing. Answered calls for the next full month, noting the change date. |
| F2 | High | Reviews | Request card offers a discount for a 5-star review [G11]. | E3, High | Stop using the card now. Replace it with one neutral request for every customer, in wording the owner approves. Leave existing reviews alone. | Jo Tran approves the wording. | No request offers a reward or asks for a rating | Review all request materials in one month |
| F3 | High | Name and categories | Keywords in the name. Two unsupported categories. | E1 and BR-07, High | In one grouped edit: name "Larkspur Plumbing", primary category Plumber, remove Emergency plumber and Roofing contractor. Flag possible re-verification. | Jo Tran approves the grouped edit. | Public profile shows the approved name and categories | Edit status in the account, then a public recheck |
| F4 | High | Hours | Open 24 hours against weekday business hours. | E1 and BR-07, High | Set the approved hours in the same grouped edit. | As F3 | Public profile shows Mon to Fri, 7:00 to 17:00 | As F3 |
| F5 | High | Address | Owner's home address is public. | E1 and BR-07, High | Hide the address in the same grouped edit and keep the service-area setting. | As F3 | No street address shown, service areas still listed | As F3 |
| F6 | High | Service areas | Areas outside real coverage. | E1 and BR-07, High | Replace the list with the eight BR-07 areas in the same grouped edit. | As F3 | Only BR-07 areas listed | As F3 |
| F7 | High | Local pages | 18 suburb pages claim coverage the business does not offer. | E2 and BR-07. Accuracy High, policy risk Medium. | Remove the 18 pages so they return 404 or 410, and take them out of the sitemap and internal links. Do not redirect them all to the homepage. | Jo Tran approves. Site manager implements. | A fresh crawl finds none of the 18 URLs linked or in the sitemap, and each returns 404 or 410 | Search Console page indexing for those URLs over the following weeks |
| F8 | Planned | Local pages | The eight in-area pages share one template with no local information. | E2, Medium | Hand to a page-need review. Keep and improve a page only where the business can supply genuine local detail. Otherwise consolidate into one coverage section or page and redirect. | Owner and SEO lead decide. | Each remaining page has a distinct task and supported content | After the page decision |
| F9 | Planned | Profile link | Profile links to a template page. | E1 and E2, Medium | Point the profile link to the homepage with campaign tags. Revisit if a genuine location page is built. | Include in the grouped edit. | The link resolves to the homepage with a 200 status and tags intact | Tagged visits appear in GA4 |
| F10 | Planned | Measurement | No campaign tags. Call-button clicks reported as leads. | E5 and E6, High | Tag the profile link using the operating-method pattern. Report call-button clicks, form enquiries and booked jobs separately. | SEO lead, with owner agreement on the report | A live test click arrives in GA4 with `utm_campaign=gbp` | Next monthly report |
| F11 | Planned | Visibility | The reported Maps drop is not supported by the evidence. | E4, E5 and E7. Low confidence in any loss. | Monitor. Start a consistent monthly sample with fixed queries, points, device and tool. Compare with the same months last year if data exists. | SEO lead | First sample recorded with its method | Monthly |

No action:

- Do not add service areas, categories or suburb pages to cover more ground. The evidence points the other way.
- Do not create a second profile for any suburb.
- Do not reply to reviews until written reply approval exists [G04].
- No citation or directory work until there is evidence of a material error customers rely on.

## 10. Open questions and handoffs

- **PH-B control and routing:** the owner or former agency can confirm the provider account and destination. This settles F1.
- **Verification state and pending edits:** account access or a screenshot from the owner. This affects the timing of the grouped edit.
- **Structured data:** page source or a crawl with structured data extraction, to check which address and phone any markup uses. Hand to a schema workflow.
- **Same months last year:** a GBP export for August to October 2025 would show whether the call change is seasonal.
- **Citations:** a list of the directories customers actually use, if accuracy problems are suspected.
- **Handoffs:** F8 to a keyword research or page-opportunity workflow. F10 to measurement setup.
- **Action states:** every action above is proposed. None is approved, submitted or verified.

