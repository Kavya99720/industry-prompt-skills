**Assumptions and defaults used**
- Business word: "our store" (per config), used everywhere except where the caller hears the name.
- Prescription upload method: in_store (given) — agent asks the customer to bring the prescription to the store, or offers a staff callback.
- Delivery info not provided — not provided — the team will confirm, when a delivery question comes up (R-66/R-74). "Home delivery only for some stores" is business context, not a spoken variable; it is not typed into the prompt.
- Return policy not provided — not provided — the team will confirm, when a return question comes up (R-67/R-74).
- Store address not provided — not provided — the team will confirm, if a caller asks for directions.
- max_qty_without_pharmacist not provided — default used: more than 1 month's typical pack (R-70).
- Only two transfer targets given (pharmacist on duty, store manager). No separate "staff" role was given, so general team handoffs (delivery status, returns, complaints) are assumed to route to the store manager.
- No medicines were named as "always hand to the pharmacist" — the agent relies on the stock tool's prescription-needed and controlled flags, and hands off when unsure, per R-12.
- Default language assumed English (IN) from "English start"; mid-call switches to Hindi and Kannada are already covered by the standard 11-language base in section 3, no change needed.
- No extra emergency signs given — default list only.

**Refused or adapted client requests**
- none. "Callers may order any medicine the stock tool shows as not prescription-only and not controlled" matches the skill's default order gate (R-50) exactly; no change to the rules was needed.

**Open questions**
- Stock tool fields: does `check_stock` reliably return in-stock, price, prescription-needed and controlled flags? Until confirmed, any missing flag is treated as prescription-needed (R-12).
- What counts as a valid prescription — to be confirmed by the industry expert (R-11).
- Exact controlled/habit-forming medicine schedules — to be confirmed by the industry expert (R-12).
- Confirm `send_confirmation` is the platform's correct tool name for a WhatsApp or email send (not exercised in this profile since upload method is in_store).
- Confirm whether a separate "staff" transfer destination exists, or whether all non-pharmacist handoffs should go to the store manager.
- Confirm whether delivery availability needs to vary by store, since this chain offers home delivery at only some locations.
- Exact DPDP Act 2023 provisions for notice, purpose and data minimisation — to be confirmed by the industry expert.

**Word counts**
- Welcome: 13. Section 1: 779. Section 2: 197. Section 3: 172. Section 4: 138. Section 5: 794.
- Section 6: 573 words. Allowance: 615 (no roster). Status: within budget (42 words under allowance, margin exceeds the 20-word target).

**Fill these in the platform**

| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (IN), assumed from "English start" | Voice settings |
| `{{var.business_hours}}` | 8 AM to 10 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business (filled in automatically from Variables) |
| `{{var.now_local}}` | — | Built in |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | not provided (lists store services, per client) | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | Your business, Add a detail |
| `{{var.return_policy}}` | not provided | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided | Your business, Add a detail |
| `{{var.payment_modes}}` | cash and UPI at the counter | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided — default more than 1 month's typical pack | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided (empty — default list only) | Your business, Add a detail |

| Intake item | Value you gave | Note |
|---|---|---|
| Business type | Retail pharmacy or chain | — |
| Call direction | Inbound | — |
| Workflows | 01 Enquiry, 02 Order and prescription, 03 Refill (inbound), 04 Delivery and returns | — |
| Channel | Voice | — |
| Prescription upload | in_store | — |
| Pickup or delivery | Store pickup; home delivery only for some stores | delivery_info not provided — not used in these Instructions beyond R-66/R-74 fallback |
| Return policy | not provided | — |
| Payment modes | Cash and UPI at the counter | — |
| Transfer targets | Pharmacist on duty; store manager | No separate "staff" target given |
| Business hours | 8 AM to 10 PM, every day | — |
| Store address, services, branches | business_info lists store services; store_address not provided | — |
| Languages | English start; Hindi and Kannada expected mid-call | Covered by standard section 3 base |
| Extra emergency signs | None | — |
| Medicines always to pharmacist | None specified | Relies on stock tool flags (R-12) |
| Special client rules | None | — |
| Max quantity without pharmacist | not provided | default: more than 1 month's typical pack |
