**Assumptions and defaults used**
- Business word: "our online pharmacy" / "the pharmacy" (profile states this explicitly; `{{var.company_name}}` reserved for welcome, closing and AI-disclosure lines only).
- `store_address` and `business_info`: not given for this online pharmacy; left empty, agent says the team will confirm if asked.
- `max_qty_without_pharmacist`: not given; default "more than 1 month's typical pack" applies (R-70).
- `emergency_signs_extra`: profile says "no extra emergency signs"; default list only, nothing added.
- `default_language`: English, with Hindi expected mid-call — handled by the standard section 3 language-switch base; no extra wording needed.
- Workflow 04 scope limited to delivery status (no order-status tool) and returns, matching "no order-status tool" in the tool list.

**Refused or adapted client requests**
- None. All client-stated config (delivery-focused framing, payment modes, delivery/return text, transfer targets) fits within the critical rules; nothing needed to be refused or adapted.

**Open items**
- Whether `check_stock` actually returns the prescription-needed and controlled flags (if not, every medicine defaults to prescription-needed per R-12 safety fallback).
- Whether the platform's send tool for WhatsApp prescription uploads is in fact named `send_confirmation`.
- What counts as a "valid prescription" for pharmacist verification — to be confirmed by the industry expert.
- Whether a custom detail can hold a list, relevant if `emergency_signs_extra` is ever populated.
- Chat channel was not requested, so not written (voice only, per profile).

**Section 6 word count**
- 574 words. Allowance: 615 (pharmacy has no roster). Status: within budget, 41 words below the allowance.
