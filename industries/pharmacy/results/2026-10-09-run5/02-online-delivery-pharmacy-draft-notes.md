**Assumptions and defaults used**
- Business word used throughout is "our online pharmacy" / "the pharmacy", per the profile.
- No extra emergency signs given, so `{{var.emergency_signs_extra}}` is not referenced; only the default list is written.
- `max_qty_without_pharmacist` not given a specific value in the profile; default "more than 1 month's typical pack" applies until the client sets the custom detail.
- Store address and services (`{{var.store_address}}`, `{{var.business_info}}`) not given; agent says the team will confirm if asked, since this is an online/delivery pharmacy.
- Channel assumed voice (not stated otherwise).
- Default language assumed English per profile ("English start, Hindi expected"); Hindi handled by section 3's standard language switching, no special instruction needed.

**Refused or adapted client requests**
- None. The profile's only emphasis ("callers often ask where their order is") is handled by workflow 04's STATUS line as designed — no order-status tool exists, so the agent never guesses a status; this matches the brief and was not weakened.

**Open questions**
- Whether `check_stock` actually returns the prescription-needed/controlled flags (R-12) is unconfirmed by the platform team.
- Whether `send_confirmation` is the platform's real WhatsApp/email send tool name is unconfirmed.
- Exact legal definition of a "valid prescription" and controlled-medicine schedules: to be confirmed by the industry expert.
- Chat channel was not requested, so no chat Instructions were written (not applicable here since voice was specified).
- Transfer target "delivery desk" is never spoken by name (R-75 forbids naming a desk/team); it is only configured as a transfer destination in the platform, not referenced in the text.

**Word counts**
- Welcome: 13. Section 1: 349. Section 2: 110. Section 3: 115. Section 4: 83. Section 5: 416.
- Section 6: 573 words. Allowance: 615 (no roster). Status: within budget (42 words under, margin met).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (start), Hindi expected | Voice settings |
| `{{var.business_hours}}` | 9 AM to 9 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | — | Built in |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.business_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | whatsapp | Your business, Add a detail |
| `{{var.return_policy}}` | unopened, unexpired items returnable within 7 days with the bill; wrong, damaged or expired items go to staff | Your business, Add a detail |
| `{{var.delivery_info}}` | delivery in the city and nearby areas; charges and usual timing as the business states | Your business, Add a detail |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided — default "more than 1 month's typical pack" applies | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none given | not used in these Instructions |
| Business type | online or delivery pharmacy, home delivery | — |
| Call direction | inbound | — |
| Workflows | 01 Enquiry, 02 Order and prescription, 03 Refill (inbound), 04 Delivery and returns | — |
| Channel | voice (assumed, not stated) | — |
| Prescription upload | whatsapp | — |
| Pickup or delivery | home delivery only | — |
| Return policy | as given above | — |
| Payment modes | as given above | — |
| Transfer targets | pharmacist on duty, store manager, delivery desk (spoken only as "our team"/"our pharmacist", per R-75) | — |
| Business hours | 9 AM to 9 PM, Monday to Saturday | — |
| Store address | not provided | — |
| Languages | English start, Hindi expected (all 11 platform languages supported by section 3) | — |
| Extra emergency signs | none | not used in these Instructions |
| Always-hand-off medicines | none given | not used in these Instructions |
| Special client rules | none | not used in these Instructions |
| Largest quantity without pharmacist | not given | not used in these Instructions (default applies) |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
