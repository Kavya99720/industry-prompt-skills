**Assumptions and defaults used**
- Business word: used "our pharmacy" everywhere except the welcome, closing, AI-disclosure and voicemail lines, per the client's explicit instruction overriding the usual chain default "the pharmacy."
- `default_language` not given: left as the variable with no forced value; the client fills it in Voice settings (no English default invented).
- `agent_gender` not given: left as the variable; no value assumed.
- Store-manager transfer target not given (only "Pharmacist on duty" was named): HANDOFF still names the store manager role per core R-21, but no transfer target was configured for it — the agent falls back to a callback for anything that would otherwise go to a store manager, per R-43.
- `max_qty_without_pharmacist` not given: default "more than 1 month's typical pack" applies (R-70).
- Store address, business services, delivery terms and return policy were not requested and are correctly left out, since the client excluded workflow 04 (delivery and returns) and did not select the STORE line of workflow 01.
- Payment modes and prescription upload method (whatsapp) were given and are referenced only through their variables, never hard-coded.

**Refused or adapted client requests**
- none — "refill reminders only, no sales, no offers, no medicine talk" and "normal order gates apply if the customer wants the refill" are both standard behaviour (R-63, R-57) and are written in as given, not refusals.

**Open questions**
- Whether the platform actually passes `{{var.customer_name}}` and `{{var.refill_details}}` on an outbound call (both marked unconfirmed in variables.json).
- Whether the platform detects voicemail or no-answer on an outbound call, so R-59's voicemail line can fire correctly.
- Whether a do-not-call tool exists; until then the agent only says it has "noted" the request, never that calls are stopped (R-62).
- Whether `check_stock` actually returns in-stock, price, prescription-needed and controlled flags; until confirmed a missing flag is treated as prescription-needed (R-12, R-50).
- What counts as a "valid prescription," and the exact controlled/habit-forming medicine schedules — both flagged for the industry expert, no list is typed into the prompt.
- Must the outbound call state "AI assistant" up front, beyond the honesty-on-request rule already written in Section 1? (legal/product sign-off pending)
- No store-manager transfer target was given — confirm with the client whether one exists or a callback should always be used for complaints on this profile.

**Word counts**
- Welcome: 14. Section 1: 509. Section 2: 185. Section 3: 172. Section 4: 139. Section 5: 502.
- Section 6: 564 words. Allowance: 615 (no roster). Status: within budget (51 words below the allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 7 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided (synthetic pharmacy chain) | Your business |
| `{{var.now_local}}` | — (built in, no entry needed) | Built in |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided | Your business, Add a detail |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | whatsapp | Your business, Add a detail |
| `{{var.customer_name}}` | passed by the platform on outbound calls, unconfirmed | Call context |
| `{{var.refill_details}}` | passed by the platform on outbound calls, unconfirmed | Call context |
