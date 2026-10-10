**Assumptions and defaults used**
- Channel: voice (default; chat not requested).
- `card_block_tool` = off (default), `balance_lookup_tool` = off (default), as the profile states.
- Fraud team and grievance team transfer targets not given: fraud and complaint handoffs offer a callback during {{var.business_hours}} instead of a transfer; branch staff remains the transfer target for the generic team handoff ("I'll connect you to our team.") since it is the only configured target.
- `{{var.confirmation_channels}}` not set: the confirmation flow (R-19) is left out entirely.
- `{{var.emergency_signs_extra}}` not provided: the default emergency signs list is used with no additions, and the unused variable is omitted from the Instructions.
- `{{var.kyc_update_info}}`, `{{var.card_activation_info}}`, `{{var.customer_name}}`: not applicable (outbound-only variables, workflows 04/05 not selected).
- Business phone: given as "<business_phone>" (placeholder); recorded as `{{var.business_phone}}`, used only in the Section 3 "language not supported" fallback since there is no voicemail or outbound line in this inbound, voice-only set.

**Refused or adapted client requests**
- None of the client's stated requirements asked to remove or weaken a safety rule; all were adaptations within the references, not refusals. No request was refused.

**Open questions**
- Chat channel was not requested, so only the voice Instructions were written.
- No legal references or timelines are quoted anywhere, since `{{var.escalation_path}}` was not provided.
- Outbound workflows (04, 05) were not selected and were not written; an outbound set for this co-operative bank would need its own run.
- Workflow 02's vulnerable/coached-caller protective handoff (R-12) and the deceased-holder handoff (R-13) both fall back to "offer a branch visit or a callback" rather than a transfer, since neither a fraud team nor a claims/grievance team target exists — only branch staff was given, and R-12/R-13 scope their transfer specifically to the fraud or claims team, not to branch staff generically.

**Fixed-line self-check**
- Could not run `check_fixed_lines.py` in this session (the tool call required approval that did not resolve); compared every "say exactly" line and fixed block from core.md and workflows 01, 02, 03 against the draft by hand, one by one. One line was missing on the first pass — the core failed-action line, "I'm sorry, I could not complete that. Our team will call you to confirm." — and was added to Section 6 as the FAILED step. After adding it, every fixed line, including the two most-often-missed ones ("I can't share account details on this call." and the failed-action line), is present word for word with its required action. Rewritten once.

**Word counts**
- Welcome: 11. Section 1: 885. Section 2: 170. Section 3: 66. Section 4: 109. Section 5: 494. Section 6: 408 words. Allowance: 615 (aim 595). Status: within budget.

**Fill these in the platform**
| Variable or intake item | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (start language) | Voice settings |
| `{{var.company_name}}` | not provided | Fixed (business) |
| `{{var.business_hours}}` | 10 AM to 4 PM, Monday to Friday | Fixed (business) |
| `{{var.business_phone}}` | <business_phone> | Fixed (business) |
| `{{var.now_local}}` | — | Built in |
| `{{var.branch_atm_info}}` | Two branches in the town; the ATM at the main branch is open 6 AM to 10 PM | Custom detail |
| `{{var.escalation_path}}` | not provided - the team will confirm | Custom detail |
| `{{var.grievance_contact}}` | not provided - the team will confirm | Custom detail |
| `{{var.emergency_signs_extra}}` | none | Custom detail — not used in these Instructions |
| `{{var.confirmation_channels}}` | not set | Custom detail — not used in these Instructions |
| Business type | Co-operative bank | Intake |
| Call direction | Inbound | Intake |
| Channel | Voice | Intake |
| Workflows selected | 01, 02, 03 (04, 05 not selected) | Intake |
| `card_block_tool` | off (default) | Intake flag |
| `balance_lookup_tool` | off (default) | Intake flag |
| Transfer targets | Branch staff only; fraud team not given; grievance team not given | Intake |
| Custom details | none beyond the ones above | Intake |
