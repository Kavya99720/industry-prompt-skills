**Assumptions and defaults used**
- Business type: private bank, agent always says "the bank" (given).
- Direction: inbound (given); outbound not requested.
- Workflows: 01 account and card enquiry, 02 lost or stolen card and fraud, 03 disputes and complaints selected (given); 04 and 05 not selected.
- Channel: voice (default; chat not requested).
- `card_block_tool`: ON (given). `balance_lookup_tool`: ON (given).
- Transfer targets: fraud team, grievance team, branch staff all given — no callback-only fallback needed, though the generic "no target" fixed-line wording is kept as the reference text writes it.
- `{{var.business_hours}}` = 9 AM to 6 PM, Monday to Saturday (given).
- `{{var.business_phone}}` given as a placeholder value; optional for inbound but recorded.
- `{{var.branch_atm_info}}`, `{{var.escalation_path}}`, `{{var.grievance_contact}}` all given as free text — not written literally into the Instructions, only referenced as variables.
- `{{var.confirmation_channels}}` = whatsapp, email (given); used only as the intake flag that includes the confirmation flow in Section 5 — not referenced literally in the Instructions text, since R-19's own fixed lines already name WhatsApp and email.
- `{{var.emergency_signs_extra}}`: client gave "a person trapped in an ATM lobby" as the custom detail value. Per the no-hard-coding rule this value is NOT written into the Instructions; only the variable reference is. The actual text goes into the platform's custom detail field (see Fill table).
- `{{var.default_language}}`: English (IN), matching "English start"; Hindi is handled by the standard mid-call language-switch rule (R-31), no extra config needed.
- `agent_name`, `agent_gender`, `company_name`: not given — standard Voice settings/Fixed values, "not provided - the team will confirm."
- `kyc_update_info`, `card_activation_info`, `customer_name`: not used (workflows 04/05 not selected).

**Refused or adapted client requests**
- "Calm, brisk tone": adapted — added "brisk" into the Section 4 tone line alongside the existing calm/firm/security-first base; does not weaken any safety rule.
- Balance and last-few-transactions by voice after full verification; agent blocks a lost/stolen card itself, else fraud team; complaints noted and passed to grievance team with escalation path said when asked; confirmation offer after a card block or noted complaint when the call ends without a transfer: none of these needed a refusal or change — each matches an existing core/workflow rule (R-41 tool-ON block, R-51/R-52, R-61/R-62, R-19) exactly as written, so the client's config simply turns on the already-built behaviour.

**Open questions**
- The outbound welcome names an AI assistant, which differs from the shared template — not applicable here since this set is inbound only; outbound would need its own separate run.
- Legal references and timelines are not quoted anywhere (R-29); the escalation path is said only in the configured words.
- Chat is not written; voice only, per default.
- Workflows 04 and 05 (outbound KYC/card-activation, outbound fraud-alert verification) were not selected; if needed later, they require a separate Instructions set.

**Fixed-line self-check**
- checked by hand: rewritten once — added the missing generic failed-action line ("I'm sorry, I could not complete that. Our team will call you to confirm.") to the ACCOUNT step for a `balance_lookup_tool` failure or timeout (R-18), which workflow 01's draft main-lines did not include (it only covered the no-match case).
- All other fixed lines (helpline, emergency, self-harm, money-movement, claimed-role, vulnerable-caller block, deceased-holder, out-of-scope, missing-value, team phrase, AI-disclosure, no-collect stop line plus its fraud-call exception block, privacy line, confirmation flow lines, closing line, card-block success/fail lines, complaint-noted line) were checked one by one against core.md and workflows 01-03 and are present word for word with their actions.

**Word counts**
- Welcome: 13. Section 1: ~900 (not budget-gated). Section 2: ~140 (not budget-gated). Section 3: ~70 (not budget-gated). Section 4: ~90 (not budget-gated). Section 5: ~320 (not budget-gated). Section 6: 534 words. Allowance: 615 (aim 595). Status: within budget.

**Fill these in the platform**
| Variable or intake item | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided - the team will confirm | Voice settings |
| `{{var.agent_gender}}` | not provided - the team will confirm | Voice settings |
| `{{var.default_language}}` | English (IN), with Hindi expected mid-call | Voice settings |
| `{{var.company_name}}` | not provided - the team will confirm | Business config (Fixed) |
| `{{var.business_hours}}` | 9 AM to 6 PM, Monday to Saturday | Business config (Fixed) |
| `{{var.business_phone}}` | <business_phone> (placeholder given) | Business config (Fixed) |
| `{{var.now_local}}` | n/a | Built in (platform supplies) |
| `{{var.branch_atm_info}}` | One main branch with a 24-hour ATM lobby; other branches and counters on the bank's website | Business config (Custom detail) |
| `{{var.escalation_path}}` | First the branch manager, then the grievance officer, then the banking ombudsman | Business config (Custom detail) |
| `{{var.grievance_contact}}` | The grievance email shown on the bank's website | Business config (Custom detail) |
| `{{var.emergency_signs_extra}}` | A person trapped in an ATM lobby | Business config (Custom detail) |
| `confirmation_channels` | whatsapp, email | Business config (Custom detail) — intake flag; not used in these Instructions as a literal variable |
| `card_block_tool` | on | Custom detail (intake flag) |
| `balance_lookup_tool` | on | Custom detail (intake flag) |
| Transfer targets | Fraud team, grievance team, branch staff all given | Transfer configuration |
| Channel | voice (default) | Business config |
| Workflows selected | 01, 02, 03 | Skill intake |
| `kyc_update_info` | not used in these Instructions | n/a — workflow 04 not selected |
| `card_activation_info` | not used in these Instructions | n/a — workflow 04 not selected |
| `customer_name` | not used in these Instructions | n/a — inbound call, workflows 04/05 not selected |
