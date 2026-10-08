**Assumptions and defaults used**
- Business type: client said "small independent pharmacy" and that the agent should say "our pharmacy"; used as the plain word throughout instead of "the pharmacy" or "our store".
- Workflows: client's instruction "just take orders and answer stock questions" matches exactly workflows 01 (Enquiry) and 02 (Order and prescription); no workflow 03 (Refill) or 04 (Delivery and returns) was written.
- Prescription upload method not given → default used (intake #5): agent asks the customer to bring the prescription to the store, or offers a staff callback; `{{var.prescription_upload_method}}` left for the client to set later.
- Delivery info not given → no delivery terms are stated; the generic "team will confirm" fallback (R-18/R-74) covers any delivery-charge or timing question, since workflow 04 was not selected.
- Return policy not given → not addressed in these Instructions; workflow 04 (returns) was not selected, so no return line was written.
- Payment modes not given → default used (intake #8): agent states modes only from `{{var.payment_modes}}`; if empty, the agent says the team will confirm.
- Store address and services not given → default used (intake #11): `{{var.store_address}}` and `{{var.business_info}}` left empty; the agent says the team will confirm if asked.
- Transfer targets not given → default used (intake #9): the agent offers a callback as the alternative built into each handoff rule; no pharmacist or store-manager transfer target is configured.
- Languages not given → default used (intake #12): calls start in `{{var.default_language}}`; the standard 11-language switching behaviour applies.
- Max quantity without pharmacist not given → default used (intake #16): more than 1 month's typical pack.
- Extra emergency signs not given → default used: no additions; only the compact default list is written.
- Custom details: none given beyond the above, so no further custom-detail variables were used.

**Refused or adapted client requests**
- none — the client's instruction to limit scope to orders and stock checks matches workflows 01 and 02 exactly; nothing in the request asked to remove a safety or critical rule.

**Open questions**
- No transfer target is configured for the pharmacist, store manager or staff; the agent can only offer a callback until a target is set (intake #9).
- Prescription upload method, delivery info, return policy, payment modes and store address are all unset; recommend filling these in before go-live, since workflow 02 asks pickup-or-delivery and payment on every order call.
- `check_stock` result fields (in stock, price, prescription-needed, controlled) are assumed per core.md; not yet confirmed with the platform team.
- What counts as a "valid prescription" is to be confirmed by the industry expert (R-11).
- Exact controlled/flagged medicine schedules are to be confirmed by the industry expert (R-12).
- Workflows 03 (refill) and 04 (delivery and returns) were not selected; if the client later wants refill reminders or home-delivery/returns support, those need their own run.
- Channel: voice only, as given; a chat version would need its own run (R-45).

**Word counts**
- Welcome: 13. Section 1: 597. Section 2: 185. Section 3: 172. Section 4: 138. Section 5: 704.
- Section 6: 384 words. Allowance: 615 (no roster). Status: within budget, well below the 595-word margin.

**Fill these in the platform**

| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | given, exact value not provided in text | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | not provided | Your business, Add a detail |
| `{{var.payment_modes}}` | not provided | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided | Your business, Add a detail |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
`{{var.now_local}}` is built in and needs no setup.
