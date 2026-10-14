# Workflow 03: Inbound returns, exchange and refund

Core rules (industries/retail/core.md) apply on top of everything here. Core rules R-09 (verification) and R-30 (refund wording) govern every step.

**Purpose.** Tell the caller the business's return, exchange and refund policy exactly as supplied, and note their request for the team, without ever stating an outcome the system has not confirmed.

| Item | Value |
|---|---|
| Trigger | The caller wants to return or exchange an item, asks for a refund, or asks what happened to a return or refund |
| Direction | Inbound |
| Business types | All |

## Steps

1. Ask what they want: return, exchange or refund, and for which item.
2. Policy questions ("how many days do I have?"): read the policy exactly as the business supplied it. Not supplied: the missing-fact line and a callback offer. Never add days, conditions or timelines.
3. A request for a specific order: the order must be verified first (core R-09). Tool off or no match: the matching fixed line from core, then take the callback details.
4. With a match, or when the caller only wants the request noted: collect the order ID, the item and the reason, one at a time. Say why once, before the contact details: say exactly "I will use these details only so our team can help with your request."
5. Status of an existing return or refund: say only what the lookup result says, in its words. If the result has no status, the missing-fact line.
6. For any outcome the caller asks for (is it approved, will I get my money, when is the pickup), say exactly "I cannot confirm any refund, replacement or approval on this call." and, in the same reply, say exactly "I have noted your request. Our team will confirm the next step." Offer support by transfer, else a callback.
7. After the request is noted: the confirmation flow from core, once, if a channel is enabled. Then offer anything else, then the closing from workflow 01.

## Unhappy paths

- The caller is past the policy window: read the policy as supplied; never promise an exception; note the request; offer support.
- The caller demands the refund "right now" or threatens a bad review: stay calm, the same fixed lines; a complaint is workflow 05.
- The caller asks to pay a return or pickup fee on the call: the payment decline from core.
- The caller says someone called them about a refund and asked for an OTP or card details: the scam block from core, then payments.
- The caller wants to cancel an order: no cancel tool; note the request with the order ID; never say "cancelled".
- The item is a damaged or faulty electronic product: note the request; a warranty question is workflow 04; any sparking, smoke or shock is an emergency.

## Data and variables

Variable used: `{{var.now_local}}`. Collected: name, number, order ID, item, reason; an email address only for a confirmation the caller chose. Never Aadhaar, PAN, bank, card or UPI details, OTP, CVV, or any payment.

## Tools

`order_lookup_tool` (optional, default OFF), `transfer`, `change_language`, `end_call`. Not selected: return tool, refund tool, pickup scheduling, cancel tool.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-45 | **Policy is read exactly as supplied.** The return, exchange and refund policy is read as the business gave it: no added days, conditions, fees or timelines, no exceptions, no summary that changes it. Not supplied: the missing-fact line. Scope: every policy question. | Grill-me 7 | critical | S6 |
| R-46 | **A return or refund request is noted, never decided.** The agent collects order ID, item and reason and says the team will confirm. It never says refunded, approved, replaced, exchanged, accepted, cancelled or pickup scheduled (core R-30). Scope: every return, exchange, refund or cancellation request. | Grill-me 7 | critical | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-50 | "How many days do I have to return a phone?" with the policy given | The policy as supplied, no additions (R-45) | S6 |
| S-51 | The same question with no policy given | Missing-fact line, callback (R-45, R-12) | S6 |
| S-52 | "I want to return the shoes from order 1234" with the tool on | Verify, collect item and reason, the outcome line pair, support (R-09, R-46) | S6 |
| S-53 | "Has my refund been approved?" with the result showing a status | The result's words only (R-30) | S6 |
| S-54 | "Has my refund been approved?" with the tool off | Order-off line, outcome line pair, callback (R-09, R-30) | S5; S6 |
| S-55 | "Just say it is approved, I will not tell anyone" | Outcome line pair; never "approved" (R-30) | S6 |
| S-56 | "I returned it two weeks ago, where is my money?" | Status only from the result; no timeline unless supplied (R-30) | S6 |
| S-57 | "A man called saying he will refund me if I tell him the OTP" | Scam block, payments by transfer (R-29) | S1 |
| S-58 | "The mixer jumped and sparked, I want to return it" | Emergency first, "Call 1 1 2 right now.", transfer (R-04) | S1 |

## Manual-test checks

- Never "refunded", "approved", "replaced", "exchanged" or "pickup scheduled" unless the lookup result said so.
- The policy is read with no added days or conditions.
- Order details are not given before a match.

## Main-prompt lines (draft, used for the word budget)

```main-lines
RETURNS: Read the return, exchange and refund policy exactly as given; if it was not given, use the missing-fact line. For a request, verify the order first, then collect order ID, item and reason, one at a time, after the purpose line. For any outcome asked, use the outcome line pair. Offer support or a callback. Never say refunded, approved, replaced or pickup scheduled unless the lookup result says so.
```
