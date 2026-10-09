**Assumptions and defaults used**
- Channel: not stated beyond "Voice" in the profile header; taken as voice (matches the given channel, chat not requested).
- `agent_name`, `agent_gender`: not provided — Voice settings, "not provided - the team will confirm" (persona comes from voice settings per the client's own instruction).
- `default_language`: not given a platform code; taken as English (IN) start, matching "English start, Hindi expected."
- `company_name`: not provided (synthetic test business, no real name given) — "not provided - the team will confirm".
- `business_phone`: profile gives the placeholder `<business_phone>` only — "not provided - the team will confirm"; the team fills in the real number.
- Workflows 01, 02, 03 used (inbound default and explicit selection); 04 and 05 excluded as instructed.
- `card_block_tool` and `balance_lookup_tool`: both ON, as given.
- Confirmation channels (whatsapp, email): both configured, so the confirmation flow in Section 5 offers both by name; the literal `{{var.confirmation_channels}}` token is not written into the Instructions (see open items).

**Refused or adapted client requests**
- "Calm, brisk tone": adapted — added "brisk" to the Section 4 tone line ("Calm, firm, brisk and security-first"); safe wording change, does not touch any safety rule.
- All other requests (balance and transactions after full verification, agent blocks a lost/stolen card itself and routes everything else to fraud, complaints noted and passed to grievance with the escalation path on request, WhatsApp/email confirmation after a card block or noted complaint when the call ends without a transfer) already match the default workflow 01/02/03 and R-19 behaviour exactly — no change needed, nothing refused.

**Open questions**
- This is the inbound Instructions set only; the bank's outbound calls (workflow 04 or 05) would need a separate run.
- Chat is not written; this is the voice Instructions only.
- No legal reference, RBI rule or grievance timeline is quoted anywhere; the escalation path is said only in the client's configured words.
- `confirmation_channels` is listed in `docs/shared/variables.json` for healthcare and pharmacy only, not banking; this run follows `core.md`'s R-19 and uses the fully-written-out flow instead of the bare token. Flag for the platform/variables.json update.
- Branch/ATM detail mentions a 24-hour ATM lobby; "a person trapped in an ATM lobby" was added to the emergency signs list via `{{var.emergency_signs_extra}}` per the custom detail given.

**Word counts**
- Welcome: 13. Section 1: 928. Section 2: 170. Section 3: 66. Section 4: 110. Section 5: 521. Section 6: 471 words. Allowance: 615 (aim 595). Status: within budget.

**Fill these in the platform**
| Variable or intake item | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English start (Hindi expected) | Voice settings |
| `{{var.company_name}}` | not provided - the team will confirm | Business config |
| `{{var.business_hours}}` | 9 AM to 6 PM, Monday to Saturday | Business config |
| `{{var.business_phone}}` | not provided (`<business_phone>` placeholder) - the team will confirm | Business config |
| `{{var.now_local}}` | Built in (call time) | Built in |
| `{{var.branch_atm_info}}` | One main branch with a 24-hour ATM lobby; other branches and counters are listed on the bank's website | Custom detail |
| `{{var.escalation_path}}` | First the branch manager, then the grievance officer, then the banking ombudsman | Custom detail |
| `{{var.grievance_contact}}` | The grievance email shown on the bank's website | Custom detail |
| `{{var.emergency_signs_extra}}` | A person trapped in an ATM lobby | Custom detail |
| Business type | Private bank (agent always says "the bank") | Business config |
| Call direction | Inbound | Business config |
| Channel | Voice | Business config |
| Workflows | 01 account and card enquiry, 02 lost or stolen card and fraud, 03 disputes and complaints | Workflow selection |
| Transfer targets | Fraud team, grievance team, branch staff — all given | Transfer target config |
| Confirmation channels | whatsapp, email | Custom detail / confirmation setting |
| `card_block_tool` | on | Custom detail (intake flag) |
| `balance_lookup_tool` | on | Custom detail (intake flag) |
| KYC update info | not used in these Instructions | — |
| Card activation info | not used in these Instructions | — |
| Customer name (outbound) | not used in these Instructions | — |
| Client special requests | calm/brisk tone, verified balance by voice, agent blocks card itself, complaints to grievance with escalation path, confirmation after block/complaint with no transfer | See "Refused or adapted" above |
