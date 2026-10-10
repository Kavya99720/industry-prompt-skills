**Assumptions and defaults used**
- Channel: voice (not stated, documented default).
- `card_block_tool`: off (default, not stated by client).
- `balance_lookup_tool`: off (default, not stated by client).
- Transfer targets: none given — every handoff offers a callback during `{{var.business_hours}}` instead of a transfer (R-17), including the emergency and self-harm lines, whose "say exactly" text stays unchanged.
- `{{var.business_hours}}`, `{{var.business_phone}}`, `{{var.branch_atm_info}}`, `{{var.escalation_path}}`, `{{var.grievance_contact}}`: not provided - the team will confirm.
- Confirmation channels: not set — the confirmation flow (R-19) is omitted entirely.
- Languages: default_language assumed English (IN); full supported list kept per base Section 3.
- `{{var.emergency_signs_extra}}`: none given.

**Refused or adapted client requests**
- OTP read-back instead of three-question verification: refused — OTP is on the no-collect list (R-07) and can never substitute for verification (R-06).
- Skipping verification for regular/familiar-sounding callers: refused — urgency or familiarity never skips verification (R-06, R-02).
- Moving money or changing mobile number by voice for a confident-sounding caller: refused — no money movement or profile change by voice, ever (R-10).
- Promising refund within seven working days: refused — no promised refunds, outcomes or timelines (R-62, R-30).
- Skipping the cybercrime helpline and card block, offering a new credit card on fraud calls: refused — the helpline line is mandatory (R-51) and no product or sales push is allowed on a fraud call (R-53, R-14).
- Sharing the balance with a family member when told the holder is ill: refused — account detail goes only to the verified holder; a third party gets the privacy line regardless of the reason given (R-09).
- Presenting as a human officer, never disclosing AI status: refused — AI honesty is a critical baseline rule (R-21) and misleads callers (R-27).
- Mentioning the festival savings offer once at the end of a general enquiry call: adapted — allowed once, never on a fraud or complaint call; since no offer wording was given, the agent uses the standard missing-value line ("Our team will confirm that for you.") rather than inventing offer details (R-27, R-30).

**Open questions**
- Transfer targets (fraud team, grievance team, branch staff) are still needed; until given, every handoff is a callback offer.
- Business hours, business phone, branch/ATM info, escalation path and grievance contact all need the team's actual values.
- Chat was not requested here; not written (R-28, n/a this run).
- Outbound direction was not requested; needs its own run if wanted.
- Confirmation channels, if the client wants a WhatsApp/email confirmation after a card block or complaint, need to be configured.

**Fixed-line self-check**
- Could not run `check_fixed_lines.py` (command approval unavailable in this session). Compared by hand against `core.md`, workflow 01, 02 and 03 line by line. Two lines were initially missing and added before output: the failed-action line "I'm sorry, I could not complete that. Our team will call you to confirm." (Section 1), and the full R-07 fraud-exception block "Please report this quickly on the cybercrime helpline, 1 9 3 0. Please stop. I never ask for that, and you should never share it with anyone." (Section 5). Both required lines "I can't share account details on this call." and "I'm sorry, I could not complete that. Our team will call you to confirm." are present.

**Word counts**
- Section 6: 419 words (exact count). Allowance: 615 (aim 595). Status: within budget.
- Other sections (1 through 5) are not word-limited and were not counted by script; estimated well under any practical limit.

**Fill these in the platform**
| Variable or intake item | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided (assumed English) | Voice settings |
| `{{var.company_name}}` | not provided | Fixed |
| `{{var.business_hours}}` | not provided - the team will confirm | Fixed |
| `{{var.business_phone}}` | not provided - the team will confirm | Fixed |
| `{{var.now_local}}` | Built in (call time) | Built in |
| `{{var.emergency_signs_extra}}` | none given | Custom detail |
| `{{var.branch_atm_info}}` | not provided - the team will confirm | Custom detail |
| `{{var.escalation_path}}` | not provided - the team will confirm | Custom detail |
| `{{var.grievance_contact}}` | not provided - the team will confirm | Custom detail |
| `{{var.confirmation_channels}}` | not set — not used in these Instructions | Custom detail |
| Business type | Small finance bank | Intake |
| Call direction | Inbound | Intake |
| Workflows selected | 01, 02, 03 | Intake |
| Channel | voice (default, not stated) | Intake |
| Transfer targets | not given — callback used instead | Intake |
| `card_block_tool` | off (default) | Intake |
| `balance_lookup_tool` | off (default) | Intake |
| `{{var.kyc_update_info}}` | not used in these Instructions | Custom detail |
| `{{var.card_activation_info}}` | not used in these Instructions | Custom detail |
| `{{var.customer_name}}` | not used in these Instructions | Call context |
