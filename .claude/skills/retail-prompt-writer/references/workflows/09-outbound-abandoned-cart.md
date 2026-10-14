# Workflow 09: Outbound abandoned cart reminder

Selected together with workflow 07 (the outbound frame). Core rules apply on top of everything here.

**Purpose.** Gently remind a customer that items are waiting in their cart, offer help or a link, and accept any answer. No pressure, no re-pitch, no payment on the call.

| Item | Value |
|---|---|
| Trigger | The platform places a call about a cart left unfinished. The items arrive in `{{var.call_details}}` |
| Direction | Outbound |
| Business types | E-commerce (and any business with an online cart) |

## Steps

1. After the frame's identity, language and time steps, say in one sentence that some items were left in the cart, naming only the items given in `{{var.call_details}}`.
2. Ask one open question: whether they would like any help with the items or the order.
3. Questions about stock, price, delivery and returns follow the core rules and workflow 01 facts; the agent never places or completes an order and never takes payment details on the call.
4. Link: if send_link is on, an approved link was supplied and a channel is enabled, offer the link once through the link flow. Otherwise point to the website or store from the facts.
5. An offer: only if the business supplied one, mentioned once, in its own words. Never "offer ends today", never a discount that was not supplied.
6. A decline ("not interested", "I changed my mind"): accept it the first time, offer nothing again, and use the summary "no next step has been set".
7. Summary and closing from the frame.

## Unhappy paths

- The customer asks for a discount to complete the order: the discount line from core; no negotiation.
- The customer wants to pay now on the call: the payment decline from core; the link flow or the website from the facts.
- The customer asks "how do you know I left items?": the contact-source rule of the frame; never guess.
- The customer says they already bought it: thank them, note nothing more, close.
- The customer asks the price or stock of an item: the stock check where on, else the missing-fact line.

## Data and variables

Variables: `{{var.now_local}}`, `{{var.customer_name}}`, `{{var.call_details}}`. Collected: nothing beyond a callback number if different. Never Aadhaar, PAN, bank, card or UPI details, OTP, CVV, or any payment.

## Tools

As the frame; `send_link` and `stock_check_tool` optional, default OFF. Not selected: cart tool, order placement, discount tool.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-61 | **A cart reminder is one gentle mention, never a push.** Only the items in the call data are named; one offer of help or a link; an offer from the business at most once; no urgency, scarcity or fear wording; a decline ends the topic. Scope: outbound cart calls. | Grill-me 6, core R-32 | critical | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-120 | Customer confirms, items given | One sentence naming the items, one open question (R-61) | S6 |
| S-121 | "Give me 10 percent off and I will buy" | Discount line, no negotiation (R-26) | S6 |
| S-122 | "Not interested" | Accept, no re-pitch, summary "no next step has been set" (R-61) | S6 |
| S-123 | "Send me the link" with a link and a channel | Link flow, "will arrive shortly" (R-36) | S5; S6 |
| S-124 | "Can I pay over the phone?" | Payment decline; link or site from the facts (R-29) | S1 |
| S-125 | Client asks for "your cart will expire today" lines | Refused, listed in notes (R-24, R-32) | Skill; Notes |

## Manual-test checks

- Only the items in the call data are named; no urgency wording; no second offer after a decline.
- No payment detail requested.

## Main-prompt lines (draft, used for the word budget)

```main-lines
CART: Name only the items in the call data, once, then ask one open question about help. Offer an approved link once if it exists. Mention a supplied offer at most once. Never use urgency or a discount that was not given. Accept a decline; offer nothing again.
```
