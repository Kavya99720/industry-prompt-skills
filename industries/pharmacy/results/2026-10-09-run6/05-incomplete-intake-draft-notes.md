**Assumptions and defaults used**
- Prescription upload: not provided — the team will confirm; default behaviour used: ask the customer to bring the prescription to the store, or offer a staff callback (`{{var.prescription_upload_method}}` left unset).
- Pickup or home delivery terms (areas, charges, timing): not provided — the team will confirm; the agent still asks pickup-or-delivery and takes an address for delivery, as workflow 02 requires, but names no terms.
- Return policy: not provided — the team will confirm. Not used in these Instructions since workflow 04 (Delivery and returns) was not selected.
- Payment modes: not provided — the team will confirm (`{{var.payment_modes}}` left unset).
- Store address: not provided — the team will confirm (`{{var.store_address}}` left unset).
- Transfer targets (pharmacist, store manager): not provided — default used: the agent offers a callback instead of a transfer wherever no target is configured; listed below as an open item.
- Languages: not provided — `{{var.default_language}}` is left as the platform Voice-settings default; section 3's 11 supported languages apply regardless.
- Always-hand-off medicines list: not provided — default used: rely on `check_stock`'s prescription-needed and controlled flags, and treat a missing flag as prescription-needed (R-12 safety fallback).
- Special client rules: none given — none applied.
- Largest quantity without the pharmacist: not provided — default used: more than 1 month's typical pack (`{{var.max_qty_without_pharmacist}}` left unset).
- Confirmation channels for order confirmations: not provided — default used: no confirmation offered (`{{var.confirmation_channels}}` left unset; the flow in section 5 skips entirely until set).
- Extra emergency signs: none given — the default emergency signs list only.
- Workflows: the client asked only for stock questions and orders, so only 01 (Enquiry) and 02 (Order and prescription) were built; 03 (Refill) and 04 (Delivery and returns) were not, per the client's own scope choice, not a gap default.

**Refused or adapted client requests**
- none

**Open questions**
- No transfer target was given for the pharmacist or the store manager. Until the client configures one, every handoff written here falls back to a callback offer (R-22); confirm the platform's `transfer` routing for the pharmacist.
- Workflows 03 (Refill) and 04 (Delivery and returns) were not built since the client said "we have not decided the rest." If delivery, returns or refill reminders are wanted later, they need their own run.
- `check_stock` result fields (in stock, price, prescription-needed, controlled) are assumed per core.md; to be confirmed with the platform lead. Until confirmed, a missing flag is always treated as prescription-needed.
- What counts as a valid prescription is to be confirmed by the industry expert.
- Controlled/habit-forming medicine schedules are to be confirmed by the industry expert; no list is typed into the prompt.
- Exact DPDP Act 2023 provisions for notice, purpose and minimisation are to be confirmed by the industry expert.
- The default emergency signs list needs review by the client's clinical team.
- Whether the After-the-call trigger reads the transcript or extracted fields (channel, email address, order number) is unconfirmed; until then the agent states the channel and reads any email address back aloud in the call.

**Word counts**
- Welcome: 14. Section 1: 822. Section 2: 212. Section 3: 172. Section 4: 165. Section 5: 953.
- Section 6: 380 words. Allowance: 615 (no roster). Status: within budget (235 words below allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | given (as `{{var.business_hours}}`) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided (filled in automatically) | Your business |
| `{{var.now_local}}` | — (built in) | — |
| `{{var.business_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.payment_modes}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.confirmation_channels}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided | not used in these Instructions |
| `{{var.return_policy}}` | not provided | not used in these Instructions |
| `{{var.emergency_signs_extra}}` | not provided | not used in these Instructions |
| `{{var.customer_name}}` | — | not used in these Instructions (outbound only) |
| `{{var.refill_details}}` | — | not used in these Instructions (outbound only) |
| Business type | Small independent pharmacy, "our pharmacy" | Intake (given) |
| Call direction | Inbound | Intake (given) |
| Workflows | 01 Enquiry, 02 Order and prescription | Intake (given) |
| Channel | Voice | Intake (given) |
| Prescription upload | not provided — the team will confirm | Intake |
| Pickup or delivery | not provided — the team will confirm | Intake |
| Return policy | not provided — the team will confirm | Intake (not used in these Instructions) |
| Payment modes | not provided — the team will confirm | Intake |
| Transfer targets | not provided — the team will confirm | Intake (open item) |
| Business hours | given (as `{{var.business_hours}}`) | Intake (given) |
| Store address | not provided — the team will confirm | Intake |
| Languages | not provided | Intake |
| Extra emergency signs | not provided | Intake |
| Always-hand-off medicines | not provided | Intake |
| Special client rules | none | Intake |
| Largest quantity without the pharmacist | not provided — the team will confirm | Intake |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
