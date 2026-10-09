**Assumptions and defaults used**
- Business type: profile names "small independent pharmacy" and states the agent says "our pharmacy" — used that plain word everywhere except where the caller hears the name (R-41).
- Call direction: inbound (given).
- Workflows: only 01 Enquiry and 02 Order and prescription written in, per the client's explicit "just take orders and answer stock questions" scope — narrower than the inbound default (01–04); 03 and 04 were not built.
- Channel: voice (given/default).
- Prescription upload method not given → default used: not set — agent asks the customer to bring the prescription to the store, or offers a staff callback (intake item 5).
- Delivery/pickup terms not given → agent still asks pickup or home delivery (workflow 02), but `{{var.delivery_info}}` is not used in these Instructions since workflow 04 was not selected.
- Return policy not given → not applicable; `{{var.return_policy}}` not used since workflow 04 was not selected.
- Payment modes not given → default used: state modes only from `{{var.payment_modes}}`; if empty, say "Our team will confirm that for you." (R-74, R-55).
- Transfer targets not given (required item, no default) → agent uses the generic `transfer` tool for the pharmacist and the fixed team phrase for staff/store-manager handoffs; listed as an open item.
- Business hours: given only as the variable `{{var.business_hours}}`, no literal value — used wherever hours are needed.
- Store address not given → default used: give `{{var.store_address}}` only if asked for directions; if empty, say the team will confirm.
- Languages not given → default used: start in `{{var.default_language}}`; the 11 platform languages are handled by section 3.
- Extra emergency signs: none given → default list only, `{{var.emergency_signs_extra}}` left empty.
- Medicines always handed to the pharmacist: none given → default used: rely on the stock tool's controlled/prescription flags and "when unsure" (R-12); no list typed into the prompt.
- Special client rules: none given.
- Max quantity without the pharmacist not given → default used: more than 1 month's typical pack (`{{var.max_qty_without_pharmacist}}`).

**Refused or adapted client requests**
- none

**Open questions**
- Transfer targets not provided — the team will confirm what the `transfer` tool actually routes to for the pharmacist and for staff/store-manager handoffs.
- Delivery info: not provided — the team will confirm (not used in these Instructions; needs workflow 04 once decided).
- Return policy: not provided — the team will confirm (not used in these Instructions; needs workflow 04 once decided).
- Payment modes: not provided — the team will confirm.
- Store address: not provided — the team will confirm.
- Prescription upload method not set — confirm whether whatsapp, email or in_store once decided.
- Languages beyond the default were not specified — confirm which of the 11 supported languages matter for this caller base.
- `check_stock` result fields (in stock, price, prescription-needed, controlled flags) are assumed per core.md; to be confirmed by the platform team.
- Exact controlled/prescription-only medicine schedules: to be confirmed by the industry expert.
- What counts as a "valid prescription": to be confirmed by the industry expert.

**Word counts**
- Welcome: 13. Section 1: 897. Section 2: 197. Section 3: 172. Section 4: 138. Section 5: 743.
- Section 6: 371 words. Allowance: 615 (no roster). Status: within budget (244 words of margin).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | given as the variable only, no literal value | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | n/a | Built in |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | not provided | Your business, Add a detail |
| `{{var.payment_modes}}` | not provided | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| Business type | Small independent pharmacy | Intake — used as "our pharmacy" |
| Call direction | Inbound | Intake |
| Workflows wanted | 01 Enquiry, 02 Order and prescription | Intake |
| Channel | Voice | Intake |
| Prescription upload | not provided | Intake — default used (bring to store or staff callback) |
| Pickup or delivery; delivery terms | not provided | Intake — not used in these Instructions |
| Return policy | not provided | Intake — not used in these Instructions |
| Payment modes | not provided | Intake — default used (team will confirm) |
| Transfer targets | not provided | Intake — open item, generic transfer used |
| Business hours | `{{var.business_hours}}` given, no value | Intake |
| Store address | not provided | Intake — default used (team will confirm) |
| Languages | not provided | Intake — default used (default_language + section 3) |
| Extra emergency signs | not provided | Intake — default used (none) |
| Medicines always to pharmacist | not provided | Intake — default used (none; relies on tool flags) |
| Special client rules | not provided | Intake — none |
| Max quantity without pharmacist | not provided | Intake — default used (more than 1 month's pack) |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
