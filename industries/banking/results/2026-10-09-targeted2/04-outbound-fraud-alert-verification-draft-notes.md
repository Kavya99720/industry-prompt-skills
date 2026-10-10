**Assumptions and defaults used**
- business_type: Private bank, agent always says "the bank" (given).
- direction: Outbound, single purpose, workflow 05 only (given).
- channel: voice (given; default matches anyway).
- card_block_tool: ON (given).
- balance_lookup_tool: OFF (given; not used by workflow 05 in any case).
- business_hours: "9 AM to 9 PM, every day" (given) -> value for the Fill table.
- business_phone: given as a variable; actual digits not supplied in this run -> "not provided - the team will confirm" in the Fill table, platform fills the real number.
- transfer target, fraud team: given -> used for all transfers in workflow 05.
- transfer target, branch staff: not given -> not referenced anywhere in this Instructions set (workflow 05 does not use a branch transfer).
- customer_name: given as passed by the platform -> used in the WHO step.
- confirmation_channels: not set -> the confirmation flow (R-19) is omitted entirely from section 5 (also excluded on every outbound call regardless).
- default_language: English (IN) (assumed from "English start"); Hindi is already in the always-listed supported-language set in section 3, no change needed.
- agent_name, agent_gender: not provided -> "not provided - the team will confirm" in the Fill table (Voice settings, set in the platform).
- emergency_signs_extra: not provided -> default signs only, no additions.
- escalation_path, grievance_contact, branch_atm_info, kyc_update_info, card_activation_info: not used by workflow 05 -> "not used in these Instructions".

**Refused or adapted client requests**
- none: the client's three requirements (verify before discussing transactions, never state the flagged transaction, and offer a card block plus fraud-team handoff on "not mine") all match workflow 05 and core as written; nothing needed refusing or adapting.

**Open questions**
- The outbound welcome names the agent as an AI assistant, which differs from the shared (non-banking) template; this wording is intentional for banking.
- Legal references and timelines (RBI rules, grievance periods) are never quoted; only "Our team will confirm that for you." is said.
- The inbound direction for this business is not covered here and needs its own run if wanted.
- Chat is not written; this is a voice-only Instructions set.
- Branch staff as a transfer target was not given and is not used; a future branch-staff handoff path would need a separate workflow (01/02/03) run.

**Fixed-line self-check**
- could not run (compared by hand): the checker script required an approval this session could not grant, so every "say exactly" line and fixed block in core.md and workflow 05 was compared one by one against the Instructions above, including "I can't share account details on this call." (present, ALERT step) and the block-failure line "I'm sorry, I could not block your card." (present, NO step). All required fixed lines for R-01, R-04, R-05, R-06, R-07, R-09, R-10, R-11, R-12, R-13, R-14, R-15, R-16, R-20, R-21, R-22, R-29, R-30, R-81, R-82, R-83 are present word for word with their actions.

**Word counts**
- Welcome: 16. Section 1: 325. Section 2: 95. Section 3: 62. Section 4: 73. Section 5: 183. Section 6: 383 words. Allowance: 615 (aim 595). Status: within budget.

**Fill these in the platform**
| Variable or intake item | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided - the team will confirm | Voice settings |
| `{{var.agent_gender}}` | not provided - the team will confirm | Voice settings |
| `{{var.default_language}}` | English (IN) | Voice settings |
| `{{var.company_name}}` | not provided - the team will confirm (private bank name) | Fixed |
| `{{var.business_hours}}` | 9 AM to 9 PM, every day | Fixed |
| `{{var.business_phone}}` | not provided - the team will confirm | Fixed |
| `{{var.now_local}}` | Built in, set by the platform | Built in |
| `{{var.customer_name}}` | passed by the platform on the outbound call | Call context |
| business type | Private bank | Intake |
| call direction | Outbound | Intake |
| workflows selected | 05 only | Intake |
| channel | Voice | Intake |
| transfer target: fraud team | given | Intake |
| transfer target: branch staff | not given - not used in this set | Intake |
| confirmation_channels | not set - no confirmation offered | Intake |
| emergency_signs_extra | none | Intake |
| card_block_tool | on | Intake |
| balance_lookup_tool | off (default) | Intake |
| branch_atm_info | not provided - not used in these Instructions | Intake |
| escalation_path | not provided - not used in these Instructions | Intake |
| grievance_contact | not provided - not used in these Instructions | Intake |
| kyc_update_info | not provided - not used in these Instructions | Intake |
| card_activation_info | not provided - not used in these Instructions | Intake |
| client special requests | the three requirements listed above, all adopted as given | Intake |
