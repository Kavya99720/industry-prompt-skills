**Assumptions and defaults used**
- Workflow 01 limited to STOCK and OUT OF STOCK lines only (no STORE line), matching "no sales, no offers, no medicine talk": `business_info` and `store_address` are not used in this Instructions set.
- No store-manager transfer target was given (only "pharmacist on duty"), so complaints/angry-caller escalation offers a callback instead of a transfer (intake default, R-21).
- `max_qty_without_pharmacist` not given: default "more than 1 month's typical pack" applies.
- No extra emergency signs given: only the compact default list is written; it needs clinical-team review per R-07.
- `default_language` and `agent_gender` not specified: left as platform variables, filled in Voice settings.
- Workflow 04 (delivery and returns) not selected, per the client's config: `delivery_info` and `return_policy` are not used.
- Outbound closing line used alone ("Thank you for your time. Have a good day."); the inbound closing line is left out, per direction matching (R-39).

**Refused or adapted client requests**
- none. "Refill reminders only, no sales/offers/medicine talk" and "normal order gates apply if the customer wants the refill" both match existing rules (R-63, R-50/51/52) already built into the skill; nothing needed to be refused or changed.

**Open questions**
- Whether the platform actually passes `{{var.customer_name}}` and `{{var.refill_details}}` on outbound calls (status: unconfirmed in variables.json).
- Whether the platform supports voicemail detection, or a do-not-call tool for "stop calling me" requests.
- What counts as a valid prescription, and the exact controlled/prescription-only medicine schedules — both flagged as "to be confirmed by the industry expert" in core rules R-11/R-12.
- Whether `place_order` already holds a saved delivery address, relevant to the "team confirms delivery" line for outbound continuation orders (R-56).
- Whether an outbound call must disclose "AI assistant" up front rather than only on request (legal/lead decision, currently unresolved; the client's welcome template is followed as given).
- Store-manager transfer target was not provided; confirm whether one should be added later.

**Word counts**
- Welcome: 13. Section 1: 536. Section 2: 197. Section 3: 172. Section 4: 138. Section 5: 703.
- Section 6: 595 words. Allowance: 615 (no roster). Status: within budget (20 words below allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 7 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided (pharmacy chain, synthetic) | Your business |
| `{{var.now_local}}` | — | Built in, filled automatically |
| `{{var.prescription_upload_method}}` | whatsapp | Your business, Add a detail |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided | Your business, Add a detail |
| `{{var.customer_name}}` | passed by the platform on outbound calls, unconfirmed | Call context |
| `{{var.refill_details}}` | passed by the platform on outbound calls, unconfirmed | Call context |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
