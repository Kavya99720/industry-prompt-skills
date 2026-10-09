**Assumptions and defaults used**
- Prescription upload: in_store, as given — the upload-link flow (WhatsApp/email) stays written for if the client later changes it, but right now the agent asks the customer to bring the prescription to the store, or offers a staff callback.
- Confirmation channels not given — defaulted to "not set": no order or upload confirmation is offered until `{{var.confirmation_channels}}` is set.
- Return policy not provided — the team will confirm.
- Delivery info not provided — the team will confirm.
- Store address not provided — the team will confirm when a caller asks for directions.
- Largest order quantity without the pharmacist not given — defaulted to "more than 1 month's typical pack"; the client can set `{{var.max_qty_without_pharmacist}}` to a specific number of strips or packs.
- No medicines were named for always-hand-off — the agent relies only on the stock tool's prescription/controlled flags, with the safety fallback (treat a missing flag as prescription-needed).
- "Staff" and delivery handoffs (workflow 04) route to the store manager transfer target, since only "pharmacist on duty" and "store manager" were given — no separate on-duty staff target.
- `business_phone` and `agent_gender` were not given — left as variables for the client to fill in the platform.
- Business word used throughout: "our store" (the client allowed either "our store" or "the pharmacy"; a few fixed lines inherited from the reference workflows keep "the pharmacy" / "pharmacist", which the client already accepted).

**Refused or adapted client requests**
- none — the one client requirement ("callers may order any medicine the stock tool shows as not prescription-only and not controlled") already matches the order gate rule (R-50) exactly, so no change was needed.

**Open questions**
- Whether `check_stock` actually returns the in-stock, price, prescription-needed and controlled fields; until confirmed, a missing flag is always treated as prescription-needed and handed to the pharmacist (R-12).
- What counts as a valid prescription (R-11) — to be confirmed by the industry expert.
- Exact controlled/habit-forming medicine schedules — to be confirmed by the industry expert; none are typed into the prompt.
- Workflow 04 (delivery status and returns) is included because some stores offer home delivery; confirm this is wanted chain-wide, since not every store delivers.
- Chat was not requested, so no chat Instructions were written (voice only).

**Word counts**
- Welcome: 13. Section 1: approx. 745 (not counted against the budget). Section 2: approx. 196 (not counted). Section 3: approx. 172 (not counted). Section 4: approx. 179 (not counted). Section 5: approx. 520 (not counted).
- Section 6: 571 words. Allowance: 615 (no roster). Status: within budget, 44 words under, 24 words below the 595-word margin target.

**Fill these in the platform**

| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (start language) | Voice settings |
| `{{var.business_hours}}` | 8 AM to 10 PM, every day | Your business |
| `{{var.business_phone}}` | not provided — the team will confirm | Your business |
| `{{var.company_name}}` | not provided | Your business (filled in automatically from Variables) |
| `{{var.now_local}}` | — | Built in |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.business_info}}` | store services list (not provided here) | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | Your business, Add a detail |
| `{{var.payment_modes}}` | cash and UPI at the counter | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.return_policy}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided — defaulted to more than 1 month's typical pack | Your business, Add a detail |
| `{{var.confirmation_channels}}` | not provided — no confirmation offered | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none | Your business, Add a detail |
| Business type | Retail pharmacy chain ("our store" / "the pharmacy") | — |
| Call direction | Inbound | — |
| Workflows | 01 Enquiry, 02 Order and prescription, 03 Refill (inbound only), 04 Delivery and returns | — |
| Channel | Voice | — |
| Prescription upload | in_store | — |
| Pickup or delivery | Store pickup; home delivery only for some stores | — |
| Return policy | not provided — the team will confirm | — |
| Payment modes | cash and UPI at the counter | — |
| Transfer targets | Pharmacist on duty; store manager | — |
| Business hours | 8 AM to 10 PM, every day | — |
| Store address | not provided — the team will confirm | — |
| Languages | English start; Hindi and Kannada expected | — |
| Extra emergency signs | none | — |
| Always-hand-off medicines | none given | — |
| Special client rules | none | — |
| Largest quantity without the pharmacist | not provided — defaulted to more than 1 month's typical pack | — |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
