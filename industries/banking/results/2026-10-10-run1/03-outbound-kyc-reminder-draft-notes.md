**Assumptions and defaults used**
- card_block_tool: off (default, not selected). balance_lookup_tool: off (default, not selected).
- emergency_signs_extra: not provided - default signs list only.
- confirmation_channels: not set - no confirmation flow is offered (also excluded on outbound calls regardless).
- card_activation_info: not used - this set is the KYC reminder purpose only; card activation needs its own Instructions set.
- Fraud team transfer target not given: fraud-specific handoffs (coached caller, fraud/lost-card report) offer a branch visit or a callback instead of a transfer.
- Branch staff given: used as the generic team transfer target for claimed-role, deceased-holder, out-of-scope and other generic handoffs.
- default_language assumed English (IN) per "English start, Hindi expected"; Hindi is reachable via mid-call switch, no other languages confirmed.

**Refused or changed client requests**
- None. All four client requirements matched the reference rules as written: "no document or ID number taken" (R-07/R-76), "respect stop-calling requests" (R-74), "voicemail: only a callback request" (R-73), "short, polite reminder call" (standard R-76 KYC block) — no change was needed to any safety rule.

**Open items**
- The outbound welcome names an AI assistant up front (differs from a non-banking template); this wording is required and kept as written.
- Legal references and timelines (penalties, due dates) are not quoted anywhere; only what is in {{var.kyc_update_info}} is said.
- The inbound direction for this business is not covered by this run; it needs its own Instructions set.
- Chat is not written; this is a voice-only set.
- Whether the platform detects voicemail, or offers a do-not-call tool, is unconfirmed; until confirmed the agent never claims a stop-calling request is "done".

**Section 6 word count**
- 383 words. Allowance: 615 (aim 595). Status: within budget.
