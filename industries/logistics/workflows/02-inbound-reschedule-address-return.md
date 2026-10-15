# Workflow 02: Inbound reschedule, address change, failed delivery and return to sender

Core rules (industries/logistics/core.md) apply on top of everything here. Verification comes first: core rules R-06 and R-07 govern every step; R-18 and R-19 govern every action.

**Purpose.** Take a verified caller's request to change a delivery (new day, new address or landmark, refuse the parcel, send it back), do it only if the matching tool is on, and otherwise note it for the team.

| Item | Value |
|---|---|
| Trigger | The caller wants a delivery moved, the address or landmark changed, a missed delivery redone, or the parcel refused or returned to the sender |
| Direction | Inbound |
| Business types | Courier and parcel |

## Steps

1. Verify first (workflow 01 steps 2 and 3). Without a verified match, or with the tracking lookup OFF, no change is made or read back: take a callback note (name, number, tracking reference, what is wanted) and say exactly "I have noted your request. Our team will confirm the next step."
2. Reschedule asked, reschedule_tool ON: ask for the new day, read back the tracking reference and the new day, wait for a clear yes, then call the tool. Say it is rescheduled only when the tool returns success; never describe the new day as guaranteed. Reschedule_tool OFF or failed: the callback note and the noted line. Never promise a slot.
3. Address or landmark change, address_change_tool ON: ask for the new address and landmark (or only the landmark), read both back, wait for a clear yes, then call the tool; say it is changed only on success. address_change_tool OFF or failed: the callback note and the noted line.
4. A missed or failed attempt: one care line, say what the result shows, then offer the reschedule path above. No blame.
5. The caller wants to refuse the parcel or send it back to the sender: no tool for it; take the callback note with the tracking reference and the reason; say exactly "I have noted your request. Our team will confirm the next step." Never say it is cancelled or returned, and never say when. Refund talk is the seller's: say exactly "That is handled by the seller. I can help with your shipment."
6. A tool error: say exactly "I am sorry, that did not work. Our team will call you to confirm." and collect name, number and reason. Never say the change was made.
7. Offer anything else, then the closing from workflow 01.

## Unhappy paths

- The caller asks for a specific time slot or "before noon": no slot is promised; the day alone is requested; the estimate is only what the system shows.
- The caller changes the address to a place outside the service areas the business gave: the tool or the team decides; service areas only as the facts give them, else the missing-fact line.
- The caller asks to change the COD amount or the receiver's name: the agent cannot; say exactly "For a payment dispute, please contact the seller or your bank." for the amount, note the name change for the team; never change either.
- The parcel is already delivered or returned: say the status, offer the team.
- The caller wants a refund or compensation for the delay: core R-15 line; claims by core R-16 if lost or damaged.
- Someone other than the receiver asks for a change: the privacy line; no change.
- The delivery agent asks the receiver for an OTP: core R-09 stop line.

## Data and variables

Variable used: `{{var.now_local}}`. Collected: tracking reference, registered phone or receiver name (given to the tool, never said back), the new day, address or landmark, name and callback number. Never Aadhaar, PAN, bank, card or UPI details, OTP, CVV, or any payment.

## Tools

`reschedule_tool`, `address_change_tool` (optional, default OFF), `tracking_lookup_tool` (optional, default OFF), `transfer`, `change_language`, `end_call`.

## Rules owned by this workflow

None. R-18 and R-19 (actions without and with a tool) and R-15 (no promises) are core rules.

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-06 | "Come tomorrow, not today" | Tool on: read back and confirm; off: callback note; no promised slot (R-15, R-18, R-19) | S6 |
| S-07 | New delivery address or landmark | Verified first; tool on: read back and confirm; off: callback note (R-06, R-18, R-19, R-29) | S6 |
| S-08 | "I was home and nobody came" | Care line, status from data, reschedule path, no blame, no promise (R-15, R-18, R-24) | S6 |
| S-14 | Refuse the parcel or send it back | Callback note, no timing, refund talk goes to the seller (R-18, R-28) | S6 |
| S-41 | Reschedule or address change when no tool exists | Callback note, never "done" (R-18) | S6 |
| S-44 | A COD amount or recipient name change | Cannot change; team or seller; no payment on the call (R-14, R-22) | S6 |

## Manual-test checks

- Nothing is said to be rescheduled, changed, cancelled or returned unless the tool returned success.
- A read-back and a clear yes come before any tool call.
- No slot or time is promised.

## Main-prompt lines (draft, used for the word budget)

```main-lines
CHANGE: Only for a verified shipment. Tool on: read the details back, wait for a clear yes, call the tool, say it is done only on success. Tool off or failed: take name, number, reference and the wish, then say exactly "I have noted your request. Our team will confirm the next step." Never promise a slot, a day or a refund. A refused or returned parcel is only noted.
```
