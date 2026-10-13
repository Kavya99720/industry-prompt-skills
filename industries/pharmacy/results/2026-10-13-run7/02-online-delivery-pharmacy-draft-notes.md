**Assumptions and defaults used**
- Store address and general business-info (services/branches) were not given; both default to empty, so the agent says the team will confirm if asked (online pharmacies may leave the address empty).
- Largest order quantity allowed without the pharmacist was not given; the default applies: any order above one pack or strip goes to the pharmacist.
- Medicines the client wants always handed to the pharmacist were not given; the agent relies on the stock tool's prescription and controlled flags plus "when unsure."
- Confirmation channels for order confirmations were not given, so no post-order confirmation offer is included; the prescription upload link flow is still included since the upload method (WhatsApp) was given.
- Default language was set to English, matching "English start, Hindi expected"; Hindi is already one of the eleven supported languages handled by section 3.
- Business type is written as "our online pharmacy" per the client's wording.

**Refused or adapted client requests**
- None. Nothing in this profile conflicts with a critical rule.

**Open questions**
- What a valid prescription looks like, and the exact controlled-medicine schedules, are for the industry expert to confirm; no list is typed into the prompt.
- Whether the stock-check tool reliably returns the prescription-needed and controlled flags is unconfirmed; until then a missing flag is always treated as prescription-needed.
- Chat was not requested, so only the voice Instructions were written; if chat is wanted later, that needs its own setup.
- Whether a customer's address is already held by the order-placing tool, or must be taken fresh on every call, is still open.

**Word counts**
- Welcome: 13. Section 1: 319. Section 2: 143. Section 3: 143. Section 4: 110. Section 5: 486.
- Section 6: 584 words. Allowance: 615 (no roster). Status: within budget (31 words of margin).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English, with Hindi expected | Voice settings |
| `{{var.business_hours}}` | 9 AM to 9 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided — the team will confirm | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | — | Built in |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.business_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | whatsapp | Your business, Add a detail |
| `{{var.return_policy}}` | unopened, unexpired items returnable within 7 days with the bill; wrong, damaged or expired items go to staff | Your business, Add a detail |
| `{{var.delivery_info}}` | delivery in the city and nearby areas; charges and usual timing as the business states | Your business, Add a detail |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided — default (above one pack or strip goes to the pharmacist) applies | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none given | Your business, Add a detail (not used in these Instructions) |
| `{{var.confirmation_channels}}` | not provided — no confirmation offered | Your business, Add a detail (not used in these Instructions) |
| Business type | online pharmacy with home delivery | — |
| Call direction | inbound | — |
| Workflows | medicine enquiry, order and prescription, refill, delivery status and returns | — |
| Channel | voice | — |
| Prescription upload | whatsapp | — |
| Pickup or delivery | home delivery | — |
| Return policy | as above | — |
| Payment modes | as above | — |
| Transfer targets | pharmacist on duty, store manager, delivery desk | — |
| Business hours | 9 AM to 9 PM, Monday to Saturday | — |
| Store address | not provided — the team will confirm | — |
| Languages | English start, Hindi expected | — |
| Extra emergency signs | none | — |
| Always-hand-off medicines | none given | — |
| Special client rules | none | — |
| Largest quantity without the pharmacist | not provided — default applies | — |
