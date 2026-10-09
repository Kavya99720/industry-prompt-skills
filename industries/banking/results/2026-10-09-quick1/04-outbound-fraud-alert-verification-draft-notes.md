**Assumptions and defaults used**
- `balance_lookup_tool`: given as OFF; not used by workflow 05 in any case.
- `{{var.emergency_signs_extra}}`: not provided — default: none (the default sign list still applies in full).
- `{{var.confirmation_channels}}`: not set — the whole confirmation flow (R-19) is left out of sections 5 and 6, as the rules require.
- Branch staff transfer target: not given. Every handoff that is not the fraud outcome (claimed role, out-of-scope, deceased holder, the general HANDOFF line) falls back to "offer a callback during `{{var.business_hours}}`" since no non-fraud target exists (R-17). Only the fraud outcome (R-83) has a real transfer target.
- `{{var.branch_atm_info}}`, `{{var.escalation_path}}`, `{{var.grievance_contact}}`, `{{var.kyc_update_info}}`, `{{var.card_activation_info}}`: not used — workflows 01, 03 and 04 were not selected for this set.
- `{{var.agent_name}}`, `{{var.agent_gender}}`, `{{var.default_language}}`: no value given in the profile; these are Voice settings and are left as variables for the platform to fill.

**Refused or adapted client requests**
- None. All three client requirements (verify recent transactions, never state the flagged transaction, block the card on a clear "not mine" and connect to the fraud team) match workflow 05's built-in design exactly for the `card_block_tool` ON state, so nothing needed to be refused or changed.

**Open questions**
- The outbound welcome names the agent as an AI assistant up front; this differs from the shared (non-banking) template but is the approved banking-specific wording.
- No legal references or timelines are quoted anywhere in these Instructions (R-29); none were configured.
- Only the outbound fraud-alert-verification set (workflow 05) was written. Inbound call handling for this bank needs its own separate Instructions run.
- Chat was not requested and is not written; voice only (R-28).
- No target was given for anything other than the fraud team (branch staff not given), so claimed-role, out-of-scope, and deceased-holder handoffs in this set all resolve to a callback rather than a transfer — confirm with the client whether a general staff/branch target should be added later.

**Word counts**
- Welcome: 17. Section 1: 268. Section 2: 95. Section 3: 66. Section 4: 83. Section 5: 229. Section 6: 532 words. Allowance: 615 (aim 595). Status: within budget.

**Fill these in the platform**
| Variable or intake item | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (start language) | Voice settings |
| `{{var.now_local}}` | Built in, no value to set | Built in |
| `{{var.business_hours}}` | 9 AM to 9 PM, every day | Fixed (business) |
| `{{var.business_phone}}` | `<business_phone>` | Fixed (business) |
| `{{var.company_name}}` | not provided | Fixed (business) |
| `{{var.customer_name}}` | given — passed by the platform on the outbound call | Call context |
| `{{var.emergency_signs_extra}}` | not provided — default: none | Custom detail |
| `{{var.confirmation_channels}}` | not set | Custom detail — not used in these Instructions |
| `{{var.branch_atm_info}}` | not provided | Custom detail — not used in these Instructions |
| `{{var.escalation_path}}` | not provided | Custom detail — not used in these Instructions |
| `{{var.grievance_contact}}` | not provided | Custom detail — not used in these Instructions |
| `{{var.kyc_update_info}}` | not provided | Custom detail — not used in these Instructions |
| `{{var.card_activation_info}}` | not provided | Custom detail — not used in these Instructions |
| `card_block_tool` | ON (given) | Custom detail (intake flag) |
| `balance_lookup_tool` | OFF (given) | Custom detail (intake flag) — not used in these Instructions |
| Transfer targets | Fraud team given; branch staff not given | Voice settings / transfer config |
| Business type | Private bank (agent says "the bank") | Voice settings |
| Call direction | Outbound | Voice settings |
| Channel | Voice | Voice settings |
