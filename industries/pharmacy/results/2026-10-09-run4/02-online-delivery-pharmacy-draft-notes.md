**Assumptions and defaults used**
- Prescription upload method is whatsapp (given); PRESCRIPTION line written only for the WhatsApp path, since in_store/not-set branching is not needed for this profile.
- Channel: voice (given). Languages: start in English, Hindi expected — section 3 base already covers all 11 platform languages, so no extra lines needed.
- Custom detail store_address: left empty per intake default for an online pharmacy (no physical collection point stated); business_info left for the client to fill with services/branches if any.
- max_qty_without_pharmacist: not given a specific value by the client; left as a custom detail with the documented default (more than 1 month's typical pack) if the client leaves it unset.
- Transfer targets: client gave pharmacist on duty, store manager, and delivery desk. "Delivery desk" is used in place of the generic "staff" wording in STATUS and RETURNS to match the client's named target; store manager is used for complaints (HANDOFF), pharmacist for medicine/prescription/controlled matters.
- No extra emergency signs given, so {{var.emergency_signs_extra}} is not used; the default compact list stands alone.
- Workflow 03 is written inbound-only, per the test profile; the outbound reminder block, R-58 through R-64, and the outbound-only variables customer_name/refill_details are not included.

**Refused or adapted client requests**
- none

**Open questions**
- What counts as a valid prescription (R-11) — to be confirmed by the industry expert.
- Exact controlled/habit-forming medicine schedules (R-12) — to be confirmed by the industry expert.
- Whether check_stock reliably returns the prescription-needed and controlled flags — until confirmed, a missing flag is treated as prescription-needed (safety fallback).
- Chat channel was not requested, so it is out of scope for this run (R-45).
- DPDP Act 2023 exact provisions for notice, purpose and minimisation — to be confirmed by the industry expert.

**Word counts**
- Welcome: 13. Section 1: 300. Section 2: 197. Section 3: 172. Section 4: 161. Section 5: 760 (words counted across all of sections 1-5; see note below).
- Section 6: 562 words. Allowance: 615 (no roster). Status: within budget (53 words below allowance, margin target met).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (start), Hindi expected | Voice settings |
| `{{var.business_hours}}` | 9 AM to 9 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.delivery_info}}` | delivery in the city and nearby areas; charges and usual timing as the business states | Your business, Add a detail |
| `{{var.return_policy}}` | unopened, unexpired items returnable within 7 days with the bill; wrong, damaged or expired items go to staff | Your business, Add a detail |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
