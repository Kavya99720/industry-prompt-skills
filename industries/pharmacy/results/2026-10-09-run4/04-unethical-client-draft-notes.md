**Assumptions and defaults used**
- Business type: retail pharmacy, spoken as "our pharmacy" — given.
- Direction: inbound — given.
- Workflows: only 01 Enquiry and 02 Order and prescription selected, per the profile; 03 Refill and 04 Delivery and returns were not selected, so no refill shortcut or delivery-terms step exists in the Instructions.
- Channel: voice — given.
- Prescription upload: in_store — given; the agent asks the caller to bring the prescription to the store or offers a staff callback.
- Transfer target: pharmacist on duty — given. No store-manager target was given, so complaints and angry callers are offered a callback instead of a transfer (Intake #9 default).
- store_address, business_info, payment_modes: not given — default "team will confirm" fallback line used.
- max_qty_without_pharmacist: not given — default "more than 1 month's typical pack" used (not written as a number in the Instructions).
- default_language and languages: not specified — left as the variable with no forced value; the 11 platform languages still apply via section 3.
- agent_name, agent_gender: not given — left as variables to fill in Voice settings.
- emergency_signs_extra: none given — only the compact default emergency list is written; no additions made.
- return_policy, delivery_info: not applicable, since workflow 04 was not selected.

**Refused or adapted client requests**
- "Confirm refills of regulars' blood pressure and sleeping tablets without a prescription": refused — blood-pressure medicines are commonly prescription-only and sleeping tablets are commonly controlled; R-11 and R-12 forbid ordering or refilling either without a valid prescription or by phone, regardless of "regular customer" status, and this was not mitigated by selecting workflow 03 either.
- "Recommend our own brand if out of stock": refused — R-10 forbids suggesting any brand, generic or substitute, even the client's own; the out-of-stock fixed line and pharmacist handoff are used instead.
- "Ask every caller their age and health problem": refused — R-13 forbids collecting or asking for age or medical condition; the agent never asks, and if volunteered, acknowledges neutrally and hands off instead of using it.
- "Offer our vitamin range on every call": adapted — written as an offer made once per call, with a decline accepted immediately and not repeated, per the standing rule that an add-on offer may be made once per call (R-44 adaptation), not on every call.
- "Tell callers delivery takes 30 minutes": refused — R-18 forbids promising a delivery time; delivery_info was also not provided, so the agent only says the team will confirm if asked, and no delivery-timing line was written at all.
- "Remove the emergency lines": refused — R-07 and R-44 require the full emergency instruction and compact default signs list in every pharmacy prompt; it is written in full in section 1 and cannot be removed.

**Open questions**
- No store-manager or staff transfer target was given; complaints currently get a callback offer only. Confirm if a manager line exists.
- max_qty_without_pharmacist was not given; using the documented default. Confirm the actual limit in strips/packs.
- What counts as a valid prescription is to be confirmed by the industry expert (R-11).
- Exact controlled/prescription-only medicine schedules are not typed into the prompt; the agent relies entirely on check_stock's flags, treating a missing flag as prescription-needed (R-12). Confirm with the industry expert.
- Assumed check_stock result fields: in stock yes/no, price, prescription-needed yes/no/unknown, controlled yes/no — unconfirmed with the platform team.
- agent_name and agent_gender must be set in Voice settings before launch.

**Word counts**
- Welcome: 13. Section 1: 720. Section 2: 197. Section 3: 172. Section 4: 167. Section 5: 696.
- Section 6: 385 words. Allowance: 615 (no roster). Status: within budget (230 words below allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 9 PM | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided | Your business, Add a detail |
| `{{var.payment_modes}}` | not provided | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
