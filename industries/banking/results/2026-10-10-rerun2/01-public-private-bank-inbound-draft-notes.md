**Assumptions and defaults used**
- Business type: private bank, so the agent says "the bank" throughout (never a specific product name).
- Direction: inbound, so the Instructions use the inbound welcome and no "calling from" line; the outbound set (workflows 04/05) is a separate run.
- Workflows: 01, 02, 03 selected, matching the inbound default; 04 and 05 not written.
- `card_block_tool`: ON — section 6 uses the FRAUD (block on) and BLOCK blocks.
- `balance_lookup_tool`: ON — section 6 uses the ACCOUNT (lookup on) block; callers may hear their balance and last few transactions only after full three-item verification and a tool match.
- Transfer targets: fraud team, grievance team and branch staff all given, so handoffs transfer rather than fall back to a callback-only offer.
- Business phone given as a placeholder; real value goes in the Fill table below, never hard-coded.
- Default language: English (IN) at start, with Hindi (and the other supported languages) available on mid-call switch.
- `emergency_signs_extra`: "a person trapped in an ATM lobby" added to the default emergency signs list; defaults were never removed.
- Channel: voice (not asked explicitly, but implied by "voice" in the business config and the Direction/Channel row).

**Refused or adapted client requests**
- Tone "calm, brisk": adapted into section 4 as "calm, brisk and security-first" — kept the required security-first core (R-32) and added brisk pacing language; nothing in this request weakened a safety rule, so no refusal was needed.
- All other client requests (self-serve card block with everything else to the fraud team; complaints noted and passed to the grievance team with the escalation path said when asked; WhatsApp/email confirmation after a card block or noted complaint when the call ends without a transfer) match the default workflow and core behaviour exactly as written in the references, so none were refused or changed.
- none refused outright.

**Open questions**
- Chat is not written; this run is voice only, as configured.
- Legal references and timelines are not quoted anywhere; the agent says only the configured escalation path and contact, or "Our team will confirm that for you."
- The outbound direction needs its own separate run if the client later wants outbound KYC reminder, card activation, or fraud-alert verification calls.
- The outbound welcome naming "an AI assistant" does not apply here since this run is inbound.

**Fixed-line self-check**
- checked by hand: passed the first time.

**Word counts**
- Welcome: 13. Section 1: 845. Section 2: 170. Section 3: 71. Section 4: 114. Section 5: 632. Section 6: 559 words. Allowance: 615 (aim 595). Status: within budget.

**Fill these in the platform**
| Variable or intake item | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (IN), Hindi expected as a switch | Voice settings |
| `{{var.company_name}}` | not provided | Business config |
| `{{var.business_hours}}` | 9 AM to 6 PM, Monday to Saturday | Business config |
| `{{var.business_phone}}` | <business_phone> (placeholder given) | Business config |
| `{{var.now_local}}` | Built in, not set by client | Call context |
| `{{var.branch_atm_info}}` | One main branch with a 24-hour ATM lobby; other branches and counters listed on the bank's website | Custom detail |
| `{{var.escalation_path}}` | First the branch manager, then the grievance officer, then the banking ombudsman | Custom detail |
| `{{var.grievance_contact}}` | The grievance email shown on the bank's website | Custom detail |
| `{{var.confirmation_channels}}` | whatsapp, email | Custom detail |
| `{{var.emergency_signs_extra}}` | a person trapped in an ATM lobby | Custom detail |
| Business type | Private bank | Intake |
| Call direction | Inbound | Intake |
| Workflows | 01, 02, 03 | Intake |
| Channel | Voice | Intake |
| Transfer targets | Fraud team, grievance team, branch staff — all given | Intake |
| `card_block_tool` | on | Intake |
| `balance_lookup_tool` | on | Intake |
| `{{var.kyc_update_info}}` | not used in these Instructions | Intake |
| `{{var.card_activation_info}}` | not used in these Instructions | Intake |
| `{{var.customer_name}}` | not used in these Instructions | Intake |
| Client special requests | Calm, brisk tone; agent blocks lost/stolen cards itself; complaints noted and passed to grievance team; confirmation offered after card block or noted complaint with no transfer | Intake |
