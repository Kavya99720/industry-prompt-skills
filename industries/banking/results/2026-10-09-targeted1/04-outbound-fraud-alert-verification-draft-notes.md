**Assumptions and defaults used**
- Confirmation channels not set: the confirmation flow is left out entirely (also excluded on any outbound call).
- Emergency extra signs (`{{var.emergency_signs_extra}}`) not provided: default empty; only the default signs list applies.
- Branch, ATM, escalation, grievance, KYC-update and card-activation info: not applicable to this workflow (05 only), so not referenced.
- `business_hours` was given but is not referenced as a variable in these Instructions: the fraud team is a given transfer target, so every handoff in this set transfers rather than offering a no-target callback with hours.

**Refused or adapted client requests**
- None. All three client requirements (verify before discussing the alert, never state the flagged transaction, block-with-consent then hand to fraud team on "no") match workflow 05 and `card_block_tool` ON exactly as written in the references; nothing needed to be refused or adapted.

**Open questions**
- The outbound welcome names an AI assistant up front, which differs from the inbound template; the client's welcome must keep that wording (grill-me row 12, open question 8/22 in platform-contract.md).
- No legal references or timelines are quoted anywhere in this set (R-29); none were requested here.
- This run covers outbound only; if the same bank also wants an inbound set (workflows 01–03), that needs its own separate run.
- Chat is not written; this is a voice-only Instructions set (R-28).
- Whether the platform actually passes `customer_name` and alert context on outbound calls is still an open platform question (platform-contract.md, question 21); if it does not, the WHO step's empty-name fallback line is used instead.

**Word counts**
- Welcome: 17. Section 1: 733. Section 2: 160. Section 3: 67. Section 4: 104. Section 5: 435. Section 6: 450 words. Allowance: 615 (aim 595). Status: within budget.

**Fill these in the platform**

| Variable or intake item | Value you gave | Where to set it |
|---|---|---|
| Business type | Private bank | Voice settings / business profile |
| Call direction | Outbound | Voice settings |
| Workflows wanted | 05 (fraud-alert verification) only | Skill config |
| Channel | Voice | Voice settings |
| Transfer targets | Fraud team given; branch staff not given | Voice settings — transfer targets |
| `{{var.business_hours}}` | 9 AM to 9 PM, every day | Business config — hours (not used in these Instructions; see assumptions) |
| `{{var.business_phone}}` | not provided - the team will confirm | Business config — phone |
| `{{var.confirmation_channels}}` | not set | Business config — confirmation channels |
| `{{var.emergency_signs_extra}}` | none | Business config — custom detail |
| `card_block_tool` | on | Custom detail / tool config |
| `balance_lookup_tool` | off (default) | Custom detail / tool config — not used in these Instructions |
| `{{var.branch_atm_info}}` | not provided - the team will confirm | Custom detail — not used in these Instructions |
| `{{var.escalation_path}}` / `{{var.grievance_contact}}` | not provided - the team will confirm | Custom detail — not used in these Instructions |
| `{{var.kyc_update_info}}` | not provided - the team will confirm | Custom detail — not used in these Instructions |
| `{{var.card_activation_info}}` | not provided - the team will confirm | Custom detail — not used in these Instructions |
| `{{var.customer_name}}` | given (platform passes it) | Call context |
| `{{var.agent_name}}` | not provided - the team will confirm | Voice settings |
| `{{var.agent_gender}}` | not provided - the team will confirm | Voice settings |
| `{{var.default_language}}` | English | Voice settings |
| `{{var.company_name}}` | not provided - the team will confirm | Business config — business name |
| `{{var.now_local}}` | Built in (call time) | Platform, automatic |
| Client special requests | none beyond workflow 05's standard flow | Skill config |
