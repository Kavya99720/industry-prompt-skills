**Assumptions and defaults used**
- `card_block_tool` ON, `balance_lookup_tool` ON — as given.
- Transfer targets (fraud team, grievance team, branch staff) all given, so every handoff uses a transfer, not a callback fallback, except where a named tool call fails.
- `{{var.business_hours}}` = 9 AM to 6 PM, Monday to Saturday — as given.
- `{{var.business_phone}}` — client supplied only the placeholder "<business_phone>", not an actual number, so it is treated as not provided; recorded as "not provided - the team will confirm" until the real number is set in the platform.
- `{{var.branch_atm_info}}`, `{{var.escalation_path}}`, `{{var.grievance_contact}}`, `{{var.confirmation_channels}}` ({{var.confirmation_channels}} = whatsapp, email), `{{var.emergency_signs_extra}}` (a person trapped in an ATM lobby) — all as given; the exact wording goes into the platform's custom-detail fields, not into the Instructions.
- `{{var.agent_gender}}` not given at intake; left as a Voice-settings variable with no default value typed in.
- Default language English; Hindi handled by the standard mid-call language-switch rule (R-31) — no extra config needed.

**Refused or adapted client requests**
- "Calm, brisk tone": adapted. Added "brisk" into the Section 4 tone line alongside the required "calm, firm and security-first" base wording — a safe style word that touches no safety rule.
- All other requirements (balance/transactions by voice after full verification; agent blocks the card itself, everything else to the fraud team; complaints noted and passed to the grievance team with the escalation path said on request; WhatsApp/email confirmation offered after a card block or noted complaint when the call ends without a transfer) already match the standard rule behaviour for `card_block_tool` ON, `balance_lookup_tool` ON and the confirmation flow (R-19) exactly as written — no change was needed, so nothing was refused.

**Open questions**
- Workflows 04 and 05 (outbound) were not selected and are not in this Instructions set; an outbound run needs its own separate set.
- Chat was not requested; this is a voice-only Instructions set.
- Legal references, RBI rules and resolution timelines are never quoted; only the configured `{{var.escalation_path}}` wording is said on a complaint call.
- The fixed-line self-check script could not be run in this environment (execution was blocked); the fixed lines from core.md and workflows 01, 02 and 03 were compared by hand against the Instructions. Two lines were missing on the first pass and were added: the combined helpline-plus-stop-line block for a secret read out during a fraud call (R-07 exception), and the failed-action line for a `balance_lookup_tool` error (R-18) in the ACCOUNT step.

**Section 6 word count**
- 515 words (allowance 615, aim 595 — within budget).
