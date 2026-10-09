**Assumptions and defaults used**
- Store address and business_info: not provided — the team will confirm.
- Delivery info and return policy: not provided — not used in these Instructions since workflow 04 (Delivery and returns) was not selected.
- Default language: not provided — assumed the platform default; confirm with the client.
- Agent gender: not provided — left to Voice settings.
- Extra emergency signs: none given — default list only, nothing added.
- Max quantity without pharmacist: not given — default "more than 1 month's typical pack".
- Transfer targets beyond the pharmacist (store manager, staff, delivery): not given — these use the generic team phrase ("I'll connect you to our team.") rather than a named person.

**Refused or adapted client requests**
- "No medicine talk" on refill calls: adapted, not refused. Section 5 and section 6 enforce "reminder only, no sales or offers," but the mandatory pharmacist handoff ("Our pharmacist will help you with that.") is kept for any dosage, usage or stopped-medicine question the caller raises mid-call — dropping it would weaken critical rule R-09.
- Home-delivery address on the outbound ORDER step: changed from the inbound workflow's "take the address and read it back" to "the team will confirm the delivery address" — R-56 forbids saying or taking an address on an outbound call.

**Open questions**
- `{{var.customer_name}}` and `{{var.refill_details}}` are unconfirmed platform variables — whether the platform actually passes them on outbound calls needs confirmation.
- Whether the platform passes the order number for comparison, detects voicemail/no-answer, or offers a do-not-call tool is unconfirmed; R-59 and R-62 are written to the current fallback.
- Whether `check_stock` returns in-stock, price, prescription-needed and controlled flags is unconfirmed; the safety fallback (treat as prescription-needed) is in S1/S6 until confirmed.
- Whether the send tool is actually named `send_confirmation` on the platform is unconfirmed.
- Whether outbound calls must state "AI assistant" up front (vs. only on request) is pending a legal/product decision; current default follows the given welcome template and answers honestly only if clearly asked.
- The actual transfer target for store-manager/staff handoffs was not given; confirm who the team phrase should route to.

**Word counts**
- Welcome: 14. Section 1: 742. Section 2: 191. Section 3: 172. Section 4: 138. Section 5: 836.
- Section 6: 583 words. Allowance: 615 (no roster). Status: within budget (23 words below the 595 margin target).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 7 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business (filled in automatically from Variables) |
| `{{var.now_local}}` | — | Built in |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | whatsapp | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided (default: more than 1 month's typical pack) | Your business, Add a detail |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `{{var.customer_name}}` | passed by platform on outbound calls, unconfirmed | Call context |
| `{{var.refill_details}}` | passed by platform on outbound calls, unconfirmed | Call context |
| delivery_info | not provided | not used in these Instructions |
| return_policy | not provided | not used in these Instructions |

| Intake item | Value given / default used | Note |
|---|---|---|
| Business type | Pharmacy chain ("our pharmacy") | — |
| Call direction | Outbound | — |
| Workflows | 03 Refill (outbound), 02 Order and prescription, 01 Enquiry (STOCK and OUT OF STOCK lines only) | 04 Delivery and returns not selected |
| Channel | Voice | — |
| Prescription upload | whatsapp | — |
| Pickup or delivery; delivery areas/charges/timing | not provided | not used in these Instructions (04 not selected) |
| Return policy | not provided | not used in these Instructions (04 not selected) |
| Payment modes | cash on delivery and UPI on delivery | — |
| Transfer targets | Pharmacist on duty | store manager/staff/delivery targets not given — generic team phrase used |
| Business hours | 9 AM to 7 PM, Monday to Saturday | — |
| Store address, services, branches | not provided | team will confirm if asked |
| Languages | not provided | assumed platform default |
| Extra emergency signs | none given | default list only |
| Medicines always handed to the pharmacist | none given | relies on check_stock flags (R-12) |
| Special client rules | "Refill reminders only, no sales, no offers, no medicine talk" | implemented via R-63 / S5 reminder-only line |
| Max quantity without pharmacist | not given | default: more than 1 month's typical pack |
