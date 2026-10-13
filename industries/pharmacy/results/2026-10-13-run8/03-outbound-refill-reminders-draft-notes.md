**Assumptions and defaults used**
- Business type given as "pharmacy chain", with the plain word "our pharmacy" as you specified, used everywhere except the welcome message.
- Channel: voice (not given; default used).
- Store address, business services and the full medicine-enquiry workflow were not selected, so `store_address` and `business_info` are not used.
- Return policy, delivery terms, confirmation channels and extra emergency signs were not given, so none of those are used; a missing value is covered by "Our team will confirm that for you."
- Store manager or staff transfer target was not given (only the pharmacist on duty was). Non-pharmacist handoffs default to a callback instead of a transfer.
- Largest quantity without the pharmacist was not given; the default of more than 3 packs, strips or bottles of the same medicine applies.
- Medicines always handed to the pharmacist were not named; the agent relies on the stock tool's flags and hands off when unsure.
- Languages: starts in the default voice-settings language; all 11 supported languages are handled as usual.
- The outbound closing line ("Thank you for your time. Have a good day.") is a proposed wording, not yet signed off.

**Refused or adapted client requests**
- none — "refill reminders only, no sales, no offers, no medicine talk" and "normal order gates apply if the customer wants the refill" both match the required behaviour for this call type as written, so nothing needed to be refused or changed.

**Open questions**
- Whether the platform actually passes `customer_name` and `refill_details` on outbound calls (unconfirmed platform variables).
- Whether the platform detects voicemail or no-answer on outbound calls.
- Whether a do-not-call tool exists; until then, a "stop calling me" request is acknowledged but never said to be completed.
- Exact medicine schedules for what counts as controlled or prescription-only are for your pharmacist or compliance lead to confirm; none are typed into the prompt.
- What counts as a valid prescription is for your pharmacist or compliance lead to confirm.
- Delivery and returns were not selected for this setup; if you want those handled on a call, that needs its own addition.
- Inbound calls (for customers who call in) need a separate Instructions set; this one is outbound only.
- Chat is not set up yet; this is the voice version.

**Word counts**
- Welcome: 14. Section 1: 792. Section 2: 220. Section 3: 170. Section 4: 141. Section 5: 930.
- Section 6: 545 words. Allowance: 615 (no roster). Status: within budget (70 words below allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 7 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | Built in, no setup needed | Built in |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | whatsapp | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided | Your business, Add a detail |
| `{{var.customer_name}}` | passed by the platform on outbound calls, unconfirmed | Call context |
| `{{var.refill_details}}` | passed by the platform on outbound calls, unconfirmed | Call context |
| `{{var.store_address}}` | not provided | Your business, Add a detail — not used in these Instructions |
| `{{var.business_info}}` | not provided | Your business, Add a detail — not used in these Instructions |
| `{{var.return_policy}}` | not provided | Your business, Add a detail — not used in these Instructions |
| `{{var.delivery_info}}` | not provided | Your business, Add a detail — not used in these Instructions |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail — not used in these Instructions |
| `{{var.confirmation_channels}}` | not provided | Your business, Add a detail — not used in these Instructions |
| Business type | pharmacy chain, spoken as "our pharmacy" | — |
| Call direction | outbound (refill reminders) | — |
| Workflows | refill reminder, order and prescription, and medicine stock/out-of-stock lines only | — |
| Channel | voice (default) | — |
| Prescription upload | whatsapp | — |
| Pickup or delivery | not provided — the team will confirm | — |
| Return policy | not provided — the team will confirm | — |
| Payment modes | cash on delivery and UPI on delivery | — |
| Transfer targets | pharmacist on duty; no store manager or staff target given, so a callback is offered instead | — |
| Business hours | 9 AM to 7 PM, Monday to Saturday | — |
| Store address | not provided — the team will confirm | — |
| Languages | not provided; all 11 supported languages apply | — |
| Extra emergency signs | not provided — default list only | — |
| Always-hand-off medicines | not provided | — |
| Special client rules | refill reminders only, no sales, no offers, no medicine talk; normal order gates apply if the customer wants the refill | — |
| Largest quantity without the pharmacist | not provided — default of more than 3 packs, strips or bottles applies | — |
