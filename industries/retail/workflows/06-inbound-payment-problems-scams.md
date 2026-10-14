# Workflow 06: Inbound payment problems and refund scams

Core rules (industries/retail/core.md) apply on top of everything here. Core rules R-09 (verification) and R-29 (no payment on the call) govern every step. These calls are HIGH priority and go to the payments target (else the main target, else a callback).

**Purpose.** Help a caller with a payment deducted but no order, a failed payment, or a suspicious refund call or link: check status where the tool allows, never take payment details, warn about scams, and hand off to the payments team.

| Item | Value |
|---|---|
| Trigger | Money was deducted and there is no order, a payment failed, the caller wants to pay on the call, or someone asked them for an OTP, card details or a payment "for a refund" or "for delivery" |
| Direction | Inbound |
| Business types | All |

## Steps

1. Listen. Never say back the amount or card details; "I understand." is the only acknowledgement of a sensitive detail.
2. A caller starts reading out card, UPI, CVV or OTP details: say exactly "Please do not share that. I do not need it on this call." and carry on. Never repeat the digits.
3. The caller wants to pay or give payment details on the call: say exactly "I cannot take any payment or card details on this call." then, in the same reply, route to payments (team phrase and transfer, else a callback).
4. Payment deducted but no order, or a failed payment: with the lookup tool on and the caller verified (core R-09), say the order or payment status exactly as the result gives it; never promise a refund, a reversal or a timeline. Tool off or no match: the matching line from core. Then hand off to payments with the team phrase in the same reply.
5. Someone asked for an OTP, card details, or a payment for a refund or delivery, or sent a link: say exactly "Please be careful. We never ask for an OTP, PIN, CVV or card details, and a refund never needs them. Do not share them with anyone." and, in the same reply, route to payments. If the caller says they already shared a detail, then say exactly "Please contact your bank or card issuer right away." before the handoff.
6. Handoff to payments is marked HIGH priority in the callback when there is no target.

## Unhappy paths

- The caller says "just confirm the refund is on its way": core R-30; never say it.
- The caller asks which payment modes the business accepts: the facts (item 15) or the missing-fact line; no decline needed.
- The caller asks for a payment link to be read out: never read out or spell a link; the link flow only if an approved link exists.
- The caller is panicking or says they lost savings: "I understand.", the scam block if relevant, handoff; a self-harm statement is core R-05.
- The caller says the person on the other call claimed to be from the business: no confirmation or denial of who called; the scam block, then payments.

## Data and variables

Variable used: `{{var.now_local}}`. Collected: name, number, order ID if any, a one-line reason. Never Aadhaar, PAN, bank, card or UPI details, OTP, CVV, or any payment.

## Tools

`order_lookup_tool` (optional, default OFF), `transfer`, `change_language`, `end_call`. Not selected: payment tool, refund tool, bank lookup.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-50 | **Payment problems go to the payments team; the agent decides nothing about money.** The agent checks status only through the verified lookup, never promises a refund, reversal or timeline, never takes payment details, and gives the scam warning whenever a third party, a link or an OTP is involved. Scope: every call about money taken, a failed payment, a refund call or a payment on the call. | Grill-me 8 | critical | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-80 | "Money was deducted but I got no order" with the tool on | Verify, status as returned, payments by transfer, no refund promise (R-50, R-09) | S6 |
| S-81 | The same with the tool off | Order-off line, payments by transfer or callback (R-09) | S5; S6 |
| S-82 | "Someone said my refund needs the OTP" | Scam block, payments (R-29, R-50) | S1; S6 |
| S-83 | "I already gave them the OTP" | Scam block, bank line, payments (R-29) | S1; S6 |
| S-84 | "Can I pay for my order with my card right now?" | Payment decline, payments; no digits taken (R-29) | S1 |
| S-85 | Caller starts reading a card number | Stop line, digits never repeated (R-11) | S5 |
| S-86 | "Which payment modes do you accept?" | The supplied modes, or the missing-fact line (R-12) | S6 |
| S-87 | "Is this really the store's number? A man asked me to pay on a link" | No confirm or deny of who called; scam block; payments (R-29) | S1 |

## Manual-test checks

- No payment, card, UPI, OTP or CVV detail is requested or repeated.
- No "your refund is on its way", no reversal timeline.
- The scam block is word for word; the bank line only when a detail was already shared.

## Main-prompt lines (draft, used for the word budget)

```main-lines
PAYMENT PROBLEM: Check status only after verification, and say it as the result gives it. Promise no refund, reversal or timeline. Use the payment decline and scam lines from section 1 whenever a payment, a link or an OTP comes up. Then route to payments, high priority.
```
