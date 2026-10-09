**Assumptions and defaults used**
- Business word: "our pharmacy", as the client specified for this chain.
- `agent_gender`, `default_language`, `agent_name`: not given in the profile — left as Voice settings for the client to fill in; not invented.
- `max_qty_without_pharmacist`: not given — default used is "more than 1 month's typical pack" (Intake #16 default).
- `confirmation_channels`: not given — default is "empty (no confirmation offered)"; the conditional flow is written in section 5 so it activates once the client sets it, but is skipped until then.
- `emergency_signs_extra`: not given — no signs added beyond the always-present default list (Intake #13 default).
- `store_address`, `business_info`, `return_policy`, `delivery_info`: not provided — the team will confirm. These are not used in these Instructions because workflow 01's STORE line and workflow 04 were not selected for this profile.
- Outbound closing line used is the proposal from core.md ("Thank you for your time. Have a good day.") — not yet signed off per the open question in platform-contract.md.
- AI-disclosure line for outbound calls follows the documented default: the client's chosen welcome template is used as-is, and the honesty rule applies only if clearly asked (no confirmed requirement to disclose "AI assistant" up front).
- `check_stock` result fields (in-stock, price, prescription-needed, controlled) are assumed per core.md; if a flag is missing, the medicine is treated as prescription-needed and handed to the pharmacist.

**Refused or adapted client requests**
- none. Both client requirements ("refill reminders only, no sales/offers/medicine talk" and "normal order gates apply if the customer wants the refill") match the standard outbound-refill design (R-63, R-50/R-57) and required no change.

**Open questions**
- Does the platform actually pass `{{var.customer_name}}` and `{{var.refill_details}}` on outbound calls? Both are marked "unconfirmed" in variables.json.
- Does the platform detect voicemail or no-answer and tell the agent? R-59 is written as if it does.
- Is there a do-not-call tool? Until confirmed, the agent only says it has "noted" the request (R-62), never that it is done.
- What exactly counts as a "valid prescription" for the pharmacist to verify (R-11) — to be confirmed by the industry expert.
- The exact controlled/prescription-only medicine schedules are not typed into the prompt; the agent relies entirely on the `check_stock` tool's flags (R-12).
- Chat channel was not requested for this profile, so it is not covered; voice only, per R-45.
- Whether `place_order` already holds a delivery address field for outbound orders (noted in workflow 02 as a question for the lead).

**Word counts**
- Welcome: 14. Section 1: 665. Section 2: 200. Section 3: 172. Section 4: 148. Section 5: 1062.
- Section 6: 542 words. Allowance: 615 (no roster). Status: within budget (73 words below allowance, margin requirement of ≤595 met).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 7 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided (pharmacy chain name) | Your business |
| `{{var.now_local}}` | — | Built in |
| `{{var.store_address}}` | not provided — the team will confirm | not used in these Instructions |
| `{{var.business_info}}` | not provided — the team will confirm | not used in these Instructions |
| `{{var.prescription_upload_method}}` | whatsapp | Your business, Add a detail |
| `{{var.return_policy}}` | not provided — the team will confirm | not used in these Instructions |
| `{{var.delivery_info}}` | not provided — the team will confirm | not used in these Instructions |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided (default: more than 1 month's typical pack) | Your business, Add a detail |
| `{{var.confirmation_channels}}` | not provided (default: no confirmation offered) | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided (no extra signs) | Your business, Add a detail |
| `{{var.customer_name}}` | passed by the platform on outbound calls, unconfirmed | Call context |
| `{{var.refill_details}}` | passed by the platform on outbound calls, unconfirmed | Call context |
| Business type | Pharmacy chain ("our pharmacy") | Intake |
| Call direction | Outbound (refill reminders) | Intake |
| Workflows | 03 Refill (outbound), 02 Order and prescription, 01 Medicine enquiry (STOCK and OUT OF STOCK lines only); 04 Delivery and returns not selected | Intake |
| Channel | Voice | Intake |
| Prescription upload | whatsapp | Intake |
| Pickup or delivery | not specified — team will confirm delivery terms; address never taken on outbound calls (R-56) | Intake |
| Return policy | not provided — the team will confirm | not used in these Instructions |
| Payment modes | cash on delivery and UPI on delivery | Intake |
| Transfer targets | Pharmacist on duty | Intake |
| Business hours | 9 AM to 7 PM, Monday to Saturday | Intake |
| Store address | not provided — the team will confirm | not used in these Instructions |
| Languages | not specified; default_language left for client to set, 11 platform languages supported | Intake |
| Extra emergency signs | not provided (no extra signs) | Intake |
| Always-hand-off medicines | not provided; relies on check_stock flags | Intake |
| Special client rules | "Refill reminders only, no sales/offers/medicine talk" and "normal order gates apply" — both already the standard design, no change needed | Intake |
| Largest quantity without pharmacist | not provided (default: more than 1 month's typical pack) | Intake |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
