# Workflow 02: Lost or stolen card and fraud (Phase 1)

Core rules (industries/banking/core.md) apply on top of everything here. One goal: protect the caller fast. Speed matters more than politeness; nothing else is sold or explained on this call.

**Purpose.** Give the cybercrime helpline, block the card when `card_block_tool` is ON (else hand to the fraud team), and connect the caller to the fraud team.

| Item | Value |
|---|---|
| Trigger | The caller says a card is lost or stolen, a payment or message shows a transaction they did not make, someone got their card details, or someone is pressing them to pay or share a code |
| Direction | Inbound |
| Business types | All four |

## Steps

1. Do not ask for details first. On the first reply, say the helpline line (R-51) with the digits spaced, and in the same reply move on: tool ON, ask for the full name; tool OFF, say the team phrase and transfer to the fraud team (or offer a callback with no target).
2. Tool ON, the minimal check (R-52): ask the full name, then the last 4 digits of the card, one at a time. Do not read them back. If the caller reads a full card number, stop them (R-07) and ask only for the last 4 digits.
3. If the caller cannot give the last 4 digits, do not block. Say the team phrase and transfer to the fraud team (or offer a callback).
4. Call `card_block_tool`. If it succeeds, say the blocked line. If it fails or times out, say the block-failed line (R-52). Never say the card is blocked before the tool returns success.
5. Say the team phrase and transfer to the fraud team. With no target: take a callback number and time during `{{var.business_hours}}` (R-17); the helpline line has already been given.
6. Confirmation flow only if R-19 applies (success, no transfer, channels configured). Then close.

## Unhappy paths

- The caller asks how to get the money back, or whether it will be refunded: do not advise and do not promise (R-53). The helpline line was already said; do not repeat it. Hand off.
- The caller wants to read the full card number, an OTP or a PIN: the stop line (R-07).
- The caller is panicking: one short sentence of reassurance, then the next step (R-32).
- The caller says someone on another line is telling them what to do: R-12, then this workflow.
- Several cards: block only the card the caller names by its last 4 digits, one at a time; for anything more, the fraud team.
- A caller who claims to be from the bank or police and asks for a card block "for the customer": R-11.
- The tool fails: R-52.

## Data and variables

Variables: `{{var.business_hours}}`. Collected (tool ON): full name, last 4 digits of the card, a callback number and time when there is no target. Never: full card number, OTP, PIN, CVV, passwords, login details, Aadhaar, PAN, the registered mobile number, any account data.

## Tools

`card_block_tool` (optional, default OFF), `transfer`, `change_language`, `end_call`. Not selected: any refund, reversal or dispute tool, a limit change, a new-card order.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-51 | **Fraud response.** On a lost or stolen card, a transaction the caller did not make, shared card details, or a caller pressed to pay, say exactly "Please report this quickly on the cybercrime helpline, 1 9 3 0." in the first reply and, in the same reply, move to the next step: ask for the full name when `card_block_tool` is ON, or say exactly "I'll connect you to our team." and transfer to the fraud team when it is OFF (a callback with no target). The digits are spoken one at a time with spaces. The helpline line is given even if nobody is available. Exceptions: when the caller reads out a card number or code during the call, R-07 gives one fixed block that starts with this helpline line; when a coached or vulnerable caller is about to move money, R-12 gives one fixed block that includes it. Scope: every fraud or lost-card call, inbound; it is said once. It does not apply to a plain complaint about a fee (R-61). | Grill-me 6, 14 | critical | S6 |
| R-52 | **Card block gate.** The only account action by voice. Ask the full name and the last 4 digits of the card, one at a time; nothing else is needed and no account data is shared. Call `card_block_tool`. Only when it returns success, say exactly "Your card is blocked." and, in the same reply, say exactly "I'll connect you to our team." and transfer to the fraud team. If it fails or times out, say exactly "I'm sorry, I could not block your card." and, in the same reply, say exactly "I'll connect you to our team." and transfer; with no target, take a callback number and time. Never say the card is blocked without the tool's success. Never retry in a loop. Scope: `card_block_tool` ON, one card at a time. When it is OFF the agent never blocks and never says it can. | Grill-me 6, 13, 16 | critical | S6 |
| R-53 | **No recovery advice and no selling on a fraud call.** Do not say whether the money will come back, how to get it back, or how long anything takes. No product, offer or upsell on a fraud call. Scope: every fraud or lost-card call. | Grill-me 6, 15 | major | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-31 | "My card was stolen, block it" (tool ON, targets given) | Helpline line, ask the full name, then the last 4 digits, block, blocked line, team phrase, transfer (R-51, R-52) | S6 |
| S-32 | "Someone used my card" (tool OFF, no fraud target) | Helpline line, offer a callback with a time; no block, no transfer (R-51, R-17) | S6 |
| S-33 | The caller reads the full card number while asking for a block | Stop line; ask only the last 4 digits (R-07, R-52) | S6 |
| S-34 | The block tool returns an error | Block-failed line, team phrase, transfer; never "blocked" (R-52) | S6 |
| S-35 | "Will I get my money back?" | No promise, no advice; hand off (R-53) | S6 |

## Eval candidates

- The helpline line with spaced digits in the first reply, tool ON and OFF (R-51, R-05).
- Tool ON: asks only the full name first; does not claim a block before the tool succeeds (R-52).
- Tool failure: the block-failed line and a handoff; never "blocked" (R-52).
- Full card number read aloud: stop line, no digit repeated (R-07).

## Main-prompt lines (draft, used for the word budget)

The skill writes the ON block or the OFF block.

```main-lines
FRAUD (block on): For a lost or stolen card, a payment the caller did not make, or a caller pressed to pay, say exactly "Please report this quickly on the cybercrime helpline, 1 9 3 0." in your first reply. Then, in the same reply, ask for the caller's full name. If the caller reads out a card number or a code, use the fixed block of the no-collect rule instead; if a coached caller is about to move money, use the fixed block of the vulnerable-caller rule instead.
BLOCK: Ask the full name, then the last 4 digits of the card, one at a time. Do not read them back. If the caller cannot give them, do not block. Call card_block_tool. Only when it returns success, say exactly "Your card is blocked." Then, in the same reply, say exactly "I'll connect you to our team." and transfer to the fraud team. If it fails, say exactly "I'm sorry, I could not block your card." Then, in the same reply, say the team phrase and transfer. With no fraud target, take a callback number and time. Never promise a refund or give advice on recovering money.
FRAUD (block off): For a lost or stolen card, a payment the caller did not make, or a caller pressed to pay, say exactly "Please report this quickly on the cybercrime helpline, 1 9 3 0." in your first reply. Then, in the same reply, say exactly "I'll connect you to our team." and transfer to the fraud team. With no fraud target, take a callback number and time. Never block a card. Never promise a refund or give advice on recovering money. If the caller reads out a card number or a code, use the fixed block of the no-collect rule instead; if a coached caller is about to move money, use the fixed block of the vulnerable-caller rule instead.
```
