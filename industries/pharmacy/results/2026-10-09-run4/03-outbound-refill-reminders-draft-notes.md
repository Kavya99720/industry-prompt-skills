**Assumptions and defaults used**
- Business word: client specified "our pharmacy" explicitly (overriding the usual default option of "our store" for a chain); used everywhere except where the caller hears {{var.company_name}}.
- Workflows 03 (outbound), 02, and 01 (STOCK and OUT OF STOCK lines only) selected per profile; 01's STORE line and workflow 04 (delivery/returns) excluded, so `{{var.store_address}}` and `{{var.business_info}}` are not used.
- `default_language` and `agent_gender` not given: left as platform variables, no value assumed; listed as "not provided" below.
- `{{var.emergency_signs_extra}}` not given: default list only, nothing added.
- `{{var.max_qty_without_pharmacist}}` not given: default "more than 1 month's typical pack" assumed per intake table.
- Transfer target given was "Pharmacist on duty" only; no store manager target was given (see open items).
- The core HANDOFF main-line text ("Complaints and angry callers go to the store manager") is kept verbatim as the fixed core block; it is not itself routed to a confirmed target yet.
- check_stock's prescription-needed/controlled fields are assumed per core's documented fallback (R-12): a missing flag is always treated as prescription-needed.

**Refused or adapted client requests**
- none. "Refill reminders only, no sales, no offers, no medicine talk" matches the Instructions' existing R-63 rule and required no change or refusal.

**Open questions**
- Whether the platform actually passes `{{var.customer_name}}` and `{{var.refill_details}}` on outbound calls (both marked "unconfirmed" in variables.json).
- Whether the platform detects voicemail or no-answer and signals it to the agent (R-59 assumes it does).
- Whether a do-not-call tool exists; until confirmed the agent never claims the stop-calling request is completed (R-62).
- No store manager transfer target was given in this profile, only "Pharmacist on duty"; complaints routing in the core HANDOFF line has no confirmed target.
- Whether `check_stock` reliably returns the prescription-needed and controlled flags (R-12 fallback relied on until confirmed).
- Whether outbound calls must state "AI assistant" up front as a matter of policy (currently: only on a clear question, per R-06).
- Chat channel: not requested, not written (voice only, per profile).

**Word counts**
- Welcome: 14. Section 1: 681. Section 2: 197. Section 3: 173. Section 4: 138. Section 5: 795.
- Section 6: 564 words. Allowance: 615 (no roster). Status: within budget (51 words below allowance, margin requirement of ≤595 met).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.business_hours}}` | 9 AM to 7 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.prescription_upload_method}}` | whatsapp | Your business, Add a detail |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `{{var.now_local}}` | — (built in, no value to set) | Built in |
| `{{var.customer_name}}` | — (passed by the platform on outbound calls, unconfirmed) | Call context |
| `{{var.refill_details}}` | — (passed by the platform on outbound calls, unconfirmed) | Call context |
