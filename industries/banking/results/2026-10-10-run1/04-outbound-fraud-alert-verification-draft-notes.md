**Assumptions and defaults used**
- `emergency_signs_extra`: not provided — only the default emergency signs list is in the prompt.
- `agent_gender`: not provided — left as a variable for Voice settings to supply; no value assumed.
- `branch_atm_info`, `escalation_path`, `grievance_contact`, `kyc_update_info`, `card_activation_info`: not used in these Instructions (not relevant to workflow 05).
- `business_phone`: the test profile gives a placeholder value only; the real number must be entered in the platform's business config.
- Grammatical gender applied only where the language requires it, per the base rule; no specific gender was given at intake.

**Refused or adapted client requests**
- none — all three client requirements (checking disputed transactions, never stating the flagged transaction, offering a block then handing to fraud) match workflow 05's reference design exactly and needed no change.

**Open questions**
- The outbound welcome names the agent as an AI assistant up front; this differs from a generic inbound template and is intentional per the references.
- No legal references, RBI rules, or timelines are quoted anywhere in these Instructions.
- This is the outbound set only; an inbound set (if the private bank also wants inbound card/account support) needs its own separate run.
- Chat is not written; this is a voice-only Instructions set, matching the given channel.
- Branch staff was not given as a transfer target; since the fraud team was given, branch staff is simply unused here, not a fallback-to-callback case.

**Fixed-line self-check**
- Could not run `check_fixed_lines.py` in this session (command execution was blocked). Compared every "say exactly" line and fixed block in core.md and workflow 05 against the output by hand, one by one. All required lines are present, including the two often-missed lines: "I can't share account details on this call." (in the ALERT step) and the workflow's own verification-failed/callback/end_call sequence. The core generic failed-action line ("I'm sorry, I could not complete that. Our team will call you to confirm.") was not needed since the only tool in this set (card_block_tool) has its own dedicated failure line, which is present. Added the combined R-07 fraud-call exception block (helpline + stop line, then ask the full name) to Section 5, since every call in this set is a fraud-alert call.

**Word counts**
- Welcome: 17. Section 1: 732. Section 2: 144. Section 3: 66. Section 4: 109. Section 5: 464. Section 6: 536 words. Allowance: 615 (aim 595). Status: within budget.

**Fill these in the platform**
| Variable or intake item | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided — the team will confirm | Voice settings |
| `{{var.agent_gender}}` | not provided — the team will confirm | Voice settings |
| `{{var.default_language}}` | English (IN), with Hindi expected mid-call | Voice settings |
| `{{var.company_name}}` | not provided — the team will confirm | Fixed (business) |
| `{{var.business_hours}}` | 9 AM to 9 PM, every day | Fixed (business) |
| `{{var.business_phone}}` | placeholder given (`<business_phone>`); the team will confirm the real number | Fixed (business) |
| `{{var.now_local}}` | Built in, supplied by the platform | Built in |
| `{{var.customer_name}}` | given — the platform passes the customer's name on this outbound call | Call context |
| Business type | Private bank (agent says "the bank") | Custom detail |
| Call direction | Outbound | Custom detail |
| Workflows wanted | 05 only (outbound fraud-alert verification) | Custom detail |
| Channel | Voice | Custom detail |
| Transfer targets | Fraud team given; branch staff not given | Custom detail |
| `card_block_tool` | on | Custom detail |
| `balance_lookup_tool` | off (default) | Custom detail |
| `{{var.confirmation_channels}}` | not set — no confirmation offered (also excluded on any outbound call) | Custom detail |
| `{{var.emergency_signs_extra}}` | not provided — the default list only | Custom detail |
| `{{var.branch_atm_info}}` | not used in these Instructions | Custom detail |
| `{{var.escalation_path}}` / `{{var.grievance_contact}}` | not used in these Instructions | Custom detail |
| `{{var.kyc_update_info}}` | not used in these Instructions | Custom detail |
| `{{var.card_activation_info}}` | not used in these Instructions | Custom detail |
| Client special requests | Transaction check, never state the flagged transaction, block-then-fraud-team handoff — all applied as given | Custom detail |
