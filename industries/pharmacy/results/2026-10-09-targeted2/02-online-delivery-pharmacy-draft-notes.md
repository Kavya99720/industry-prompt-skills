**Assumptions and defaults used**
- Business word used throughout is "our online pharmacy" / "the pharmacy", matching the stated business type.
- Store address, services and branches: not provided — the team will confirm. `{{var.store_address}}` and `{{var.business_info}}` left for the client to fill; the agent gives directions or services only when asked and only from these variables.
- Medicines the client always wants handed to the pharmacist: not specified. The agent relies only on the `check_stock` tool's prescription-needed and controlled flags, and the "when unsure, hand off" default.
- Largest quantity without the pharmacist (`{{var.max_qty_without_pharmacist}}`): not specified. Default applied: more than 1 month's typical pack.
- Special client rules: none given, so none added.
- Extra emergency signs: none given. The default emergency signs list is used as is; `{{var.emergency_signs_extra}}` is not referenced in the Instructions since it is empty.
- Languages: call starts in English (`{{var.default_language}}`); Hindi and the other nine platform languages are handled by section 3 as written, no change needed.
- Channel confirmed as voice; Instructions written for voice only.

**Refused or adapted client requests**
- none

**Open questions**
- Whether `check_stock` reliably returns the prescription-needed and controlled flags (platform open question). Until confirmed, a missing flag is treated as prescription-needed.
- Store address, services/branches, medicines always sent to the pharmacist, and the maximum order quantity are all left as defaults above; the client should confirm these values when ready.
- Whether a custom detail can hold a list, for a future addition to `{{var.emergency_signs_extra}}` if the client later adds signs.

**Word counts**
- Welcome: 13. Section 1: 779. Section 2: 185. Section 3: 172. Section 4: 138. Section 5: 840.
- Section 6: 573 words. Allowance: 615 (no roster). Status: within budget (42 words below allowance, meets the 20-word margin).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English, start; Hindi expected | Voice settings |
| `{{var.business_hours}}` | 9 AM to 9 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business (filled in automatically from Variables) |
| `{{var.now_local}}` | Built in, no value to give | Built in |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.business_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | whatsapp | Your business, Add a detail |
| `{{var.return_policy}}` | unopened, unexpired items returnable within 7 days with the bill; wrong, damaged or expired items go to staff | Your business, Add a detail |
| `{{var.delivery_info}}` | delivery in the city and nearby areas; charges and usual timing as the business states | Your business, Add a detail |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided — default: more than 1 month's typical pack | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none given | not used in these Instructions |
| `{{var.customer_name}}` | n/a (outbound only) | not used in these Instructions |
| `{{var.refill_details}}` | n/a (outbound only) | not used in these Instructions |
| Business type | online or delivery pharmacy with home delivery | Your business |
| Call direction | inbound | Your business |
| Workflows | 01 Enquiry, 02 Order and prescription, 03 Refill (inbound), 04 Delivery status and returns | Your business |
| Channel | voice | Your business |
| Prescription upload | whatsapp | Your business, Add a detail |
| Pickup or delivery | home delivery | Your business, Add a detail |
| Return policy | as given above | Your business, Add a detail |
| Payment modes | cash on delivery and UPI on delivery | Your business, Add a detail |
| Transfer targets | pharmacist on duty; store manager; delivery desk | Your business |
| Business hours | 9 AM to 9 PM, Monday to Saturday | Your business |
| Store address | not provided — the team will confirm | Your business |
| Languages | English start, Hindi expected | Voice settings |
| Extra emergency signs | none given | not used in these Instructions |
| Medicines always handed to pharmacist | not specified | not used in these Instructions |
| Special client rules | none | not used in these Instructions |
| Largest quantity without pharmacist | not provided — default more than 1 month's typical pack | Your business, Add a detail |
