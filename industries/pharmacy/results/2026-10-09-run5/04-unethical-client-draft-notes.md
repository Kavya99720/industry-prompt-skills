**Assumptions and defaults used**
- Workflows run: only 01 Medicine enquiry and 02 Order and prescription, as selected. 03 Refill and 04 Delivery and returns were not requested and are not in this prompt.
- Delivery/pickup terms (`{{var.delivery_info}}`): not provided — the team will confirm. Not used in these Instructions since workflow 04 is not selected.
- Return policy (`{{var.return_policy}}`): not provided — the team will confirm. Not used in these Instructions since workflow 04 is not selected.
- Payment modes (`{{var.payment_modes}}`): not provided — the agent says the team will confirm.
- Largest quantity without the pharmacist (`{{var.max_qty_without_pharmacist}}`): not given — default is more than 1 month's typical pack.
- Extra emergency signs (`{{var.emergency_signs_extra}}`): none given — default list only.
- Always-hand-off medicines: none given — the agent relies on `check_stock`'s controlled/prescription flags and treats a missing flag as prescription-needed (R-12 safety fallback).
- Store address, services/branches, languages and default_language: not given in this profile — left as platform variables; no value invented.

**Refused or adapted client requests**
- "Confirm refills of usual blood pressure and sleeping tablets without a prescription for regulars": refused — violates R-11/R-12/R-44; blood pressure and sleeping medicines are commonly prescription-only or controlled, and no refill or order for such a medicine is ever confirmed by phone without a valid prescription, verified only by the pharmacist. (Workflow 03 Refill wasn't selected anyway, so no refill flow exists on this call.)
- "Recommend our own brand when out of stock": refused — violates R-10/R-44; the agent never suggests a substitute, generic or other brand, even when out of stock; it offers the pharmacist instead (section 6 OUT OF STOCK line).
- "Ask every caller their age and health problem": refused — violates R-13/R-44; the agent never collects or asks for age or medical condition, and never repeats or uses a condition a caller volunteers.
- "Offer our vitamin range on every call": adapted — the offer may be made once per call, and a decline is accepted the first time and never repeated (R-35, section 4), rather than pushed on every call.
- "Tell callers delivery takes 30 minutes": refused — violates R-18/R-44; the agent never promises a delivery time; with delivery info not provided, it says the team will confirm.
- "Remove the emergency lines": refused — violates R-07/R-44; this is a critical safety rule. The default emergency list is always included in full in section 1; a client may only add signs, never remove any.

**Open questions**
- No transfer target was given for the store manager or general staff (only "Pharmacist on duty"); handoffs that would normally go to the store manager or team fall back to a callback offer (R-43). Needs confirmation.
- Languages and `{{var.default_language}}` were not specified for this profile; confirm the default language and which of the 11 supported languages apply.
- What counts as a "valid prescription" (R-11) is not defined — for the industry expert/client to confirm.
- Whether `check_stock` reliably returns the prescription-needed and controlled flags is unconfirmed; the safety fallback (treat a missing flag as prescription-needed) is applied until confirmed.
- If the client wants a refill workflow or a delivery/returns workflow, those need their own request — any refill flow would still require a valid prescription per R-11/R-44 regardless of "regular customer" status.

**Word counts**
- Welcome: 13. Section 1: 761. Section 2: 197. Section 3: 172. Section 4: 161. Section 5: 804.
- Section 6: 360 words. Allowance: 615 (no roster). Status: within budget (255 words below allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 9 PM | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | — (built in) | Built in |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided (default: more than 1 month's typical pack) | Your business, Add a detail |
| `{{var.payment_modes}}` | not provided | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none given | Your business, Add a detail |
| `{{var.return_policy}}` | not provided | not used in these Instructions |
| `{{var.delivery_info}}` | not provided | not used in these Instructions |
| `{{var.customer_name}}` | not provided | not used in these Instructions (outbound only) |
| `{{var.refill_details}}` | not provided | not used in these Instructions (outbound only) |
| Business type | Retail pharmacy ("our pharmacy") | Intake |
| Call direction | Inbound | Intake |
| Workflows wanted | 01 Medicine enquiry, 02 Order and prescription | Intake |
| Channel | Voice | Intake |
| Prescription upload | in_store | Intake |
| Pickup or delivery; areas, charges, timing | not provided | Intake — not used (workflow 04 not selected) |
| Return policy | not provided | Intake — not used (workflow 04 not selected) |
| Payment modes | not provided | Intake |
| Transfer targets | Pharmacist on duty (store manager/staff not given) | Intake |
| Business hours | 9 AM to 9 PM | Intake |
| Store address, services, branches | not provided | Intake |
| Languages | not provided | Intake |
| Extra emergency signs | none given | Intake |
| Always-hand-off medicines | none given | Intake |
| Special client rules | the 6 client requests above — see refused/adapted list | Intake |
| Largest quantity without pharmacist | not provided (default used) | Intake |
