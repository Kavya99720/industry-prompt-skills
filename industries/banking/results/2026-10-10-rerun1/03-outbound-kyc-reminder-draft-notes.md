**Assumptions and defaults used**
- Business type: public sector bank, agent always says "the bank" (given).
- Call direction: outbound, single purpose = KYC reminder (workflow 04, KYC block only; CARD block not written).
- card_block_tool: off (default, not given). balance_lookup_tool: off (default, not given). No fixed line or step names either tool.
- Transfer targets: only "branch staff" configured; no separate "fraud team" target exists, so every handoff (emergency, claimed role, coached caller, deceased holder, out-of-scope, fraud report, missing value, failed action) transfers to the one configured target rather than a named desk, per R-16 (never invent a department name).
- confirmation_channels: not set — the confirmation flow (R-19) is omitted entirely; it is also excluded on every outbound call regardless.
- emergency_signs_extra: none given — left as the variable slot with only the default signs listed.
- card_activation_info: not provided — not used anywhere in this Instructions set, since the purpose is KYC reminder only, not card activation.
- No due date is stated in {{var.kyc_update_info}}, so the KYC step never states one (R-76).
- Languages: default_language assumed English (IN); Hindi switch handled by the standard change_language rule (R-31).

**Refused or adapted client requests**
- none

**Open questions**
- The outbound welcome names the agent as an AI assistant; this differs from a generic template and must be kept word for word in the platform's welcome field.
- No legal references or timelines are quoted anywhere (R-29); if the customer asks about KYC consequences, the agent only says the team will confirm.
- Inbound Instructions for this bank (if ever needed) require a separate run; nothing inbound is written here.
- Chat channel was not requested, so only voice Instructions were written; chat is not covered.
- Whether the platform actually passes {{var.customer_name}} and reliably signals voicemail are open platform questions carried from workflow 04.

**Fixed-line self-check**
- checked by hand: passed the first time.

**Word counts**
- Welcome: 21. Section 1: 372. Section 2: 95. Section 3: 62. Section 4: 83. Section 5: 263. Section 6: 489 words. Allowance: 615 (aim 595). Status: within budget.

**Fill these in the platform**
| Variable or intake item | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided - the team will confirm | Voice settings |
| `{{var.agent_gender}}` | not provided - the team will confirm | Voice settings |
| `{{var.default_language}}` | English (assumed start language) | Voice settings |
| `{{var.business_hours}}` | 10 AM to 4 PM, Monday to Friday | Fixed |
| `{{var.business_phone}}` | given (business_phone placeholder) | Fixed |
| `{{var.company_name}}` | not provided - the team will confirm | Fixed |
| `{{var.now_local}}` | Built in, not set by client | Built in |
| `{{var.emergency_signs_extra}}` | none | Custom detail |
| `{{var.kyc_update_info}}` | through the bank's app or at any branch; no due date stated | Custom detail |
| `{{var.customer_name}}` | given (platform passes customer's name) | Call context |
| `{{var.card_activation_info}}` | not provided | Custom detail — not used in these Instructions |
| `{{var.confirmation_channels}}` | not set | Custom detail — not used in these Instructions |
| Business type | Public sector bank | Intake |
| Call direction | Outbound | Intake |
| Channel | Voice | Intake |
| Workflows selected | 04, KYC reminder purpose only | Intake |
| Transfer targets | Branch staff; fraud team not given | Intake |
| card_block_tool | off (default) | Intake |
| balance_lookup_tool | off (default) | Intake |
| Custom details | none | Intake |
