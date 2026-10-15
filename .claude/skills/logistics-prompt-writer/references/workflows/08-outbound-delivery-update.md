# Workflow 08: Outbound delivery update

Selected together with workflow 07 (the outbound frame). Core rules apply on top of everything here.

**Purpose.** Tell the receiver about their delivery using only the call data, note any reaction for the team, and end with a clear next step.

| Item | Value |
|---|---|
| Trigger | The platform places a call about a delivery: out for delivery, a failed attempt, a reschedule confirmation or an address confirmation. The facts arrive in `{{var.call_details}}` with the reference in `{{var.tracking_number}}` |
| Direction | Outbound |
| Business types | Courier and parcel (any business that delivers to receivers) |

## Steps

1. After the frame's identity, language and time steps, say the update in one or two sentences, only from `{{var.call_details}}`: the status and any date or window it gives, read as given with the weekday. Say the reference one character at a time if you give it.
2. If `{{var.call_details}}` has no date or window, do not give one. A date the receiver asks for gets the missing-fact line. Never promise a time.
3. Ask whether they have a question. Questions beyond the call data follow the frame's step 8.
4. A request to reschedule, change the address or landmark, or refuse the parcel: with the matching tool on, read the details back, wait for a clear yes and call it, saying it is done only on success (core R-19); otherwise say exactly "I have noted your request. Our team will confirm the next step." with the reference and the change wanted collected. Never say it is changed, rescheduled or cancelled, and never promise a slot.
5. A failed-attempt call may upset the receiver: one short care line, no blame, no compensation talk; a complaint or a claim goes to the team by core R-22.
6. Someone asks for an OTP, money or card details on this call, or a "pay to release" story comes up: core R-09 stop line, or the scam block from core R-11.
7. Summary and closing from the frame.

## Unhappy paths

- The receiver says they did not expect a parcel: do not argue or explain; say exactly "I have noted your request. Our team will confirm the next step." with the details collected; offer support.
- The receiver says it was already delivered: note it for the team; do not mark anything as delivered.
- The receiver asks for compensation for the delay: core R-15 line; no outcome.
- The call data is empty or unclear: do not guess an update; offer support by transfer or a callback.
- The receiver asks for the COD amount: only from the call data; core R-14 for anything beyond that.

## Data and variables

Variables used: `{{var.now_local}}`, `{{var.contact_name}}`, `{{var.tracking_number}}`, `{{var.call_details}}`. Collected: the receiver's request in one line, a callback number only if different. Never Aadhaar, PAN, bank, card or UPI details, OTP, CVV, or any payment.

## Tools

`transfer`, `change_language`, `end_call`; `reschedule_tool` and `address_change_tool` optional, default OFF.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-37 | **Outbound delivery update.** The call uses only the per-call fields (name, tracking reference and the update). Confirm the named person first, state the update as given, never add a time, and offer a reschedule or address change only through the matching tool (core R-19) or the callback note (core R-18). Questions beyond the update follow the inbound verification rule. Scope: every outbound delivery-update call. | Grill-me: outbound delivery updates | major | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-27 | Outbound delivery update (out for delivery, failed attempt, reschedule or address confirmation) | Confirms the person, states the update as given, no added time (R-33, R-37, R-15) | S6 |
| S-70 | "I did not order anything" | The noted line with details collected; no argument (R-37) | S6 |
| S-71 | "Deliver it on Sunday instead and compensate me for the delay" | Reschedule per the tool state; the no-promise line for compensation; support (R-15, R-18, R-19) | S6 |

## Manual-test checks

- The update contains only call-data facts; no time or date is added.
- No reschedule is called done without a tool success.

## Main-prompt lines (draft, used for the word budget)

```main-lines
UPDATE: Say the update in one or two sentences from {{var.call_details}} only: the status and any date or window it gives. If it has no date, give none. A reschedule, address change or refusal: tool on, read back and wait for a yes; tool off or failed, say exactly "I have noted your request. Our team will confirm the next step." Never promise a slot or compensation.
```
