**Assumptions and defaults used**
- Business phone (`{{var.business_phone}}`) not provided as a real value: "not provided - the team will confirm" (R-15). It is only optional for inbound.
- `default_language` assumed English (IN) from "English start, Hindi expected"; Hindi is a supported mid-call switch (R-31), not the start language.
- `agent_name` and `agent_gender` come from Voice settings; no persona name was given, per the client's own instruction that the persona comes from voice settings.
- `company_name` not given a real value: shown as `{{var.company_name}}` for the platform to fill.
- Card and account enquiry (workflow 01) built in the `balance_lookup_tool` ON state; fraud and lost-card (workflow 02) built in the `card_block_tool` ON state, since both tools are ON for this profile.
- Workflows 04 and 05 (outbound) were not selected and are not in section 6.
- "The bank says 'the bank'" wording used throughout per business type; no public-facing company descriptor beyond `{{var.company_name}}` in the welcome, closing and AI-disclosure lines.

**Refused or adapted client requests**
- None. All client requirements (calm brisk tone, card block handled in-house with fraud otherwise routed to the fraud team, complaints noted and routed to the grievance team with escalation path on request, WhatsApp/email confirmation after a block or a noted complaint when the call ends without a transfer) fit the existing rules and were built in as given.

**Open questions**
- The other call direction (outbound) was not requested in this run; it would need its own separate Instructions set if wanted later.
- Chat was not requested; voice-only Instructions were written (R-28). If chat is wanted, that is a separate open item.
- Legal references, grievance timelines and ombudsman procedural detail are never quoted beyond the configured `{{var.escalation_path}}` text (R-29).
- Whether `{{var.business_phone}}` will ever be shown to callers (it is currently used only for the "language not supported" callback offer) depends on the team filling in a real value.

**Word counts**
- Welcome: 13. Section 1: 978. Section 2: 170. Section 3: 66. Section 4: 109. Section 5: 545. Section 6: 550 words. Allowance: 615 (aim 595). Status: within budget.

**Fill these in the platform**

| Variable or intake item | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (Hindi expected mid-call) | Voice settings |
| `{{var.company_name}}` | not provided | Fixed (business name) |
| `{{var.business_hours}}` | 9 AM to 6 PM, Monday to Saturday | Fixed |
| `{{var.business_phone}}` | not provided - the team will confirm | Fixed |
| `{{var.branch_atm_info}}` | One main branch with a 24-hour ATM lobby; other branches and counters are listed on the bank's website | Custom detail |
| `{{var.escalation_path}}` | First the branch manager, then the grievance officer, then the banking ombudsman | Custom detail |
| `{{var.grievance_contact}}` | The grievance email shown on the bank's website | Custom detail |
| `{{var.confirmation_channels}}` | whatsapp, email | Custom detail |
| `{{var.emergency_signs_extra}}` | A person trapped in an ATM lobby | Custom detail |
| `{{var.now_local}}` | Call-time value | Built in |
| Business type | Private bank (agent says "the bank") | Intake |
| Call direction | Inbound | Intake |
| Channel | Voice | Intake |
| Workflows selected | 01 account and card enquiry, 02 lost or stolen card and fraud, 03 disputes and complaints | Intake |
| Transfer targets | Fraud team, grievance team, branch staff (all given) | Intake |
| `card_block_tool` | ON | Intake (Custom detail flag) |
| `balance_lookup_tool` | ON | Intake (Custom detail flag) |
| `{{var.kyc_update_info}}` | not used in these Instructions (no outbound workflow 04) | Custom detail |
| `{{var.card_activation_info}}` | not used in these Instructions (no outbound workflow 04) | Custom detail |
| `{{var.customer_name}}` | not used in these Instructions (inbound call) | Call context |
| Client special requests | Calm brisk tone; card block handled in-house with all other fraud to the fraud team; complaints noted and routed to grievance team, escalation path stated on request; WhatsApp/email confirmation offered after a block or noted complaint when the call ends without a transfer | Intake |
