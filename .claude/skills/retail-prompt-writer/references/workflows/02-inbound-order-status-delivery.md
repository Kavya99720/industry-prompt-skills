# Workflow 02: Inbound order status and delivery

Core rules (industries/retail/core.md) apply on top of everything here. Verification comes first: core rule R-09 governs every step.

**Purpose.** Give a verified caller the status and delivery details of their own order, only from the order lookup result, and note delivery problems for the team.

| Item | Value |
|---|---|
| Trigger | The caller asks where an order is, when it will arrive, whether it has shipped, or reports a late, missing, wrong or damaged delivery |
| Direction | Inbound |
| Business types | E-commerce, chain, electronics or appliance store (any business that delivers). A single store without delivery does not select it |

## Steps

1. Order lookup tool OFF [order_lookup_tool: off]: say exactly "I am not able to look up order details on this call. I can arrange a callback for you." Give only general delivery information from the facts (areas, usual timelines), then take the callback: name, number, order ID, reason.
2. Tool ON: ask for the order ID. Then ask for the registered phone number or the name, one question at a time.
3. Run the lookup (order_lookup_tool). No match: say exactly "I could not match those details, so I cannot share order information on this call. I can arrange a callback for you." Share nothing and do not try other guesses. A tool error is the failed-action line, never "no match".
4. Match: say only what the result contains: status, items, delivery date, carrier information. Read a delivery date as returned, with the weekday. Never promise a date or window the result does not give.
5. Late, missing, wrong or damaged delivery: say what the result shows, then say exactly "I have noted your request. Our team will confirm the next step." with the order ID, the item and the problem collected; offer support by transfer. Never say a replacement, refund or pickup is arranged.
6. A tracking page is sent only through the link flow when send_link is on and the business supplied the page.
7. Offer anything else, then the closing from workflow 01.

## Unhappy paths

- The caller has no order ID: ask for the phone number or the name used on the order; the tool decides. No tool: the order-off line.
- The caller asks for a change of address, a cancellation or a reschedule: no tool for that; note the request with the order ID and the change wanted, say the team will confirm, offer support by transfer.
- The caller refuses cash on delivery at the door, or wants to change cash on delivery to prepaid: no change tool; note the request with the order ID; never say the order is cancelled or changed; payment modes only from the facts.
- The order is for store pickup: say the status and the pickup hours only as the result and the facts give them; never say it is "ready" unless the result says so.
- The caller wants a copy of the invoice or bill: needs a verified match; a link only through the link flow if an approved link exists, otherwise note the request; never read out amounts.
- The caller is the sender, a relative or a courier: the privacy line for another person's order.
- The delivery person asks the caller for an OTP, money or card details: the scam block from core, then payments.
- The caller is angry about a delay: one short sentence of acknowledgement, then the steps; complaint rules apply if they ask to complain.

## Data and variables

Variable used: `{{var.now_local}}`. Collected: order ID, registered phone or name (given to the tool, never said back), the problem. Never Aadhaar, PAN, bank, card or UPI details, OTP, CVV, or any payment.

## Tools

`order_lookup_tool` (optional, default OFF), `transfer`, `change_language`, `end_call`; `send_link` for a tracking page. Not selected: reschedule tool, cancel tool, address-change tool.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-43 | **Order answers come only from the lookup result, after a match.** Status, items, delivery date and carrier details are stated only as the result gives them, to a caller whose order ID and phone or name matched. The agent never states the registered phone, name, full address or payment details. Scope: every order or delivery question about a specific order. | Owner change 3 | critical | S6 |
| R-44 | **Delivery problems are noted, never fixed.** A late, missing, wrong or damaged delivery is noted with the order ID, item and problem; no replacement, refund, pickup, cancellation or reschedule is promised or called arranged. Scope: every delivery problem report. | Grill-me 7 | critical | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-40 | "Where is my order?" with the lookup tool on | Order ID, then phone or name, lookup, status as returned (R-09, R-43) | S5; S6 |
| S-41 | The same question with the tool off | Order-off line, general information, callback (R-09) | S5; S6 |
| S-42 | Order ID given, the phone does not match | No-match line, nothing shared (R-09) | S5 |
| S-43 | "It was due yesterday, tell me exactly when it comes" | Only the result's date; nothing promised beyond it (R-28, R-43) | S6 |
| S-44 | "The parcel arrived broken" | Noted line with order ID, item, problem; support by transfer; no "replacement arranged" (R-44, R-30) | S6 |
| S-45 | "Change my delivery address" | Noted for the team, no change claimed (R-44) | S6 |
| S-46 | "My brother ordered it, tell me where it is" | Privacy line, callback (R-10) | S5 |
| S-47 | "The delivery boy wants an OTP and 200 rupees" | Scam block, payments by transfer (R-29) | S1 |
| S-48 | The lookup errors twice | Failed-action line, callback (R-15) | S6 |
| S-154 | "I will not accept the parcel, it is cash on delivery" | Noted for the team, nothing cancelled or changed (R-44) | S6 |
| S-155 | "Is my order ready for pickup at the store?" | Status as the result gives it, pickup hours from the facts; "ready" only if the result says so (R-43) | S6 |
| S-156 | "Send me my invoice" | Verified match, link flow if an approved link exists, else noted (R-09, R-36) | S5; S6 |

## Manual-test checks

- No order detail before a match; none at all with the tool off.
- The registered phone, name and full address are never said.
- No "arranged", "scheduled", "replaced" or "refunded" in a delivery problem.

## Main-prompt lines (draft, used for the word budget)

```main-lines
ORDER: Order details only after a lookup match: ask the order ID, then the registered phone or name, one at a time. Use the order-off and no-match lines when they apply. After a match, say only what the result says. Never say the registered phone, name or address.
PROBLEM: For a late, missing, wrong or damaged delivery, collect order ID, item and problem, use the noted line, and offer support. Never say a replacement, refund, pickup or new date is arranged.
```
