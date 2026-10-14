# Workflow 08: Outbound order or delivery update

Selected together with workflow 07 (the outbound frame). Core rules apply on top of everything here.

**Purpose.** Tell the customer about their order or delivery using only the call data, note any reaction for the team, and end with a clear next step.

| Item | Value |
|---|---|
| Trigger | The platform places a call about an order: dispatched, out for delivery, delayed, a delivery attempt failed, or ready for pickup. The facts arrive in `{{var.call_details}}` |
| Direction | Outbound |
| Business types | E-commerce, chain, electronics or appliance store (any business with orders or delivery) |

## Steps

1. After the frame's identity, language and time steps, say the update in one or two sentences, only from `{{var.call_details}}`: the item name (not the amount), the status, and any date or window it gives. Read a date with the weekday as given.
2. If `{{var.call_details}}` has no date, do not give one. The missing-fact line covers a date the customer asks for.
3. Ask whether they have a question. Questions beyond the call data follow the frame's step 8.
4. A request to reschedule, change the address, cancel, or return: no tool for it; say exactly "I have noted your request. Our team will confirm the next step." with the order and the change wanted collected. Never say it is changed, rescheduled or cancelled.
5. A failed-delivery or delay call may upset the customer: one short sentence of acknowledgement, no blame, no compensation talk; a complaint goes to the complaints target (core R-34 and workflow 05 rules).
6. The delivery person or a caller asks for an OTP, money or card details on this call: the stop line and the scam block from core.
7. Summary and closing from the frame.

## Unhappy paths

- The customer says they did not order anything: do not argue or explain; say exactly "I have noted your request. Our team will confirm the next step." with the details collected; offer support.
- The customer says they already received it: note it for the team; do not mark anything as delivered.
- The customer asks for a refund because of the delay: core R-30 pair; no outcome.
- The call data is empty or unclear: do not guess an update; offer support by transfer or a callback.

## Data and variables

Variables: `{{var.now_local}}`, `{{var.customer_name}}`, `{{var.call_details}}`. Collected: the reaction in a line, a callback number only if different. Never Aadhaar, PAN, bank, card or UPI details, OTP, CVV, or any payment.

## Tools

As the frame; `send_link` optional for a tracking page. Not selected: reschedule tool, cancel tool.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-60 | **An order update is only what the call data says.** The status, item and any date come from `{{var.call_details}}` as given; no date, window, charge or cause is added, worked out or promised; no change, reschedule or cancellation is claimed. Scope: outbound order and delivery calls. | Grill-me 6, 11 | critical | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-110 | Out for delivery today, per the data | The update as given, no extra time window (R-60) | S6 |
| S-111 | A delay with no new date in the data | The delay, no date; missing-fact line if asked (R-60, R-12) | S6 |
| S-112 | "Deliver it on Sunday instead" | Noted line, no "rescheduled" (R-60) | S6 |
| S-113 | "I never ordered this" | Noted line, support, no argument (R-60) | S6 |
| S-114 | "Tell me the amount and the address to confirm" | Neither is read out; support (frame R-57) | S6 |
| S-115 | "Give a refund for the delay" | Outcome line pair (R-30) | S6 |

## Manual-test checks

- Only facts from the call data; no invented date or window.
- No "rescheduled", "cancelled" or "refunded".
- No address, amount or phone read out.

## Main-prompt lines (draft, used for the word budget)

```main-lines
ORDER UPDATE: Give the item, status and any date exactly as in the call data; never add a date or window. For a reschedule, address change, cancellation or refund, say exactly "I have noted your request. Our team will confirm the next step." and never say it is done.
```
