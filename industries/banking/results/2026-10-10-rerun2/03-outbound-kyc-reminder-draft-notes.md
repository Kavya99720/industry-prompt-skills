**Assumptions and defaults used**
- Business phone value is the synthetic placeholder `<business_phone>` since no real number was given; recorded as "not provided - the team will confirm" for the Fill table.
- `emergency_signs_extra`: not provided, default empty (the default emergency signs list still applies in full).
- `escalation_path`, `grievance_contact`, `branch_atm_info`, `card_activation_info`: not provided and not used, since workflows 01, 03 and the card-activation purpose are not selected.
- `confirmation_channels`: not set, so the confirmation flow (R-19) is omitted entirely, consistent with it never applying to an outbound call anyway.
- `card_block_tool` and `balance_lookup_tool`: off (default) - not applicable to this outbound-only set.
- Agent persona, agent_gender and default_language: read from Voice settings at runtime; no override given.

**Refused or adapted client requests**
- None of the client requirements conflicted with a safety rule. "Short, polite reminder call" → built as the single-purpose KYC block (R-76). "No document or ID taken" → explicit line in the KYC step plus the standing no-collect rule (R-07). "Respect stop-calling requests" → the STOP fixed line (R-74). "Voicemail is only a callback request" → the VOICEMAIL fixed line (R-73).
- Fraud-team and grievance-team transfer targets were not given, so the coached-caller block (R-12), the deceased-holder block (R-13) and the outbound FRAUD step (R-78) all offer a callback or branch visit instead of a transfer, per R-17: adapted, not refused, because no safety rule is weakened.

**Open questions**
- The outbound welcome names the agent as an AI assistant up front; this differs from a generic inbound template and is intentional (grill-me row 12).
- No legal reference or grievance timeline is quoted anywhere in these Instructions.
- This set covers outbound only; an inbound Instructions set for this bank (if wanted) needs its own run.
- Chat was not requested and is not written; voice only.
- Card activation is a separate purpose per workflow 04 and needs its own Instructions set if the client wants it.

**Fixed-line self-check**
- checked by hand: passed the first time.

**Word counts**
- Welcome: 19. Section 1: 322. Section 2: 72. Section 3: 55. Section 4: 61. Section 5: 232. Section 6: 459 words. Allowance: 615 (aim 595). Status: within budget.

**Fill these in the platform**
| Variable or intake item | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English, with Hindi expected | Voice settings |
| `{{var.business_hours}}` | 10 AM to 4 PM, Monday to Friday | Business config |
| `{{var.business_phone}}` | `<business_phone>` | Business config |
| `{{var.company_name}}` | not provided (business type: public sector bank) | Business config |
| `{{var.now_local}}` | built in, call time | Built in |
| `{{var.emergency_signs_extra}}` | not provided (default) | Custom detail |
| `{{var.customer_name}}` | passed by the platform per call | Call context |
| `{{var.kyc_update_info}}` | through the bank's app or at any branch; no due date stated | Custom detail |
| `{{var.card_activation_info}}` | not provided - not used in these Instructions | Custom detail |
| `{{var.branch_atm_info}}` | not provided - not used in these Instructions | Custom detail |
| `{{var.escalation_path}}` | not provided - not used in these Instructions | Custom detail |
| `{{var.grievance_contact}}` | not provided - not used in these Instructions | Custom detail |
| `{{var.confirmation_channels}}` | not set - not used in these Instructions | Custom detail |
| Business type | Public sector bank (the agent says "the bank") | Business config |
| Call direction | Outbound | Business config |
| Workflows selected | 04, KYC reminder purpose only | Business config |
| Channel | Voice | Business config |
| Transfer targets | Branch staff given; fraud team not given | Business config |
| card_block_tool | off (default) | Custom detail |
| balance_lookup_tool | off (default) | Custom detail |
| Client special requests | none beyond the stated requirements | Business config |
