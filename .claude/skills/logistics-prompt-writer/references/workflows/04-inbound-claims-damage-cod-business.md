# Workflow 04: Inbound claims, damage, COD and business-customer queries

Core rules (industries/logistics/core.md) apply on top of everything here. R-14 (COD and payment), R-15 (no promises), R-16 (claims) and R-27 (insurance) govern every step.

**Purpose.** Note a loss or damage claim for the claims team without any outcome, handle COD questions from system data only, and route business-customer queries (remittance, invoices, accounts) to the team.

| Item | Value |
|---|---|
| Trigger | The caller reports a lost, damaged, short or wrong parcel, wants to claim, disputes a COD amount, or a business customer asks about COD remittance, an invoice or an account |
| Direction | Inbound |
| Business types | Courier and parcel (deepest); the same claim steps serve the other three types |

## Steps

1. Care first: one short line ("Oh, I'm sorry to hear that."), in a calm serious tone. No blame, no admission of fault.
2. Claim for loss or damage: say exactly "I will use these details only so our team can help with your shipment." before the first contact detail, then collect one at a time: the tracking reference, what happened (lost, damaged, short, wrong item), when it was noticed, name and callback number. No photos or documents over voice; if the caller offers them, say the team will tell them how to share. Never estimate a payout, say a claim will be approved, or say who is at fault.
3. Say exactly "I have noted the details for our team." and, in the same reply, connect to the claims team (else the main target) with the team phrase. With no target, take the callback and say the callback line. Claims are high priority.
4. COD amount questions: the amount is stated only from the tracking result after verification (workflow 01 steps 2 and 3). A wrong amount, a refund of the COD or a payment dispute: say exactly "For a payment dispute, please contact the seller or your bank." The agent never changes a COD amount and never takes or arranges a payment: say exactly "I cannot take or arrange any payment on this call." when asked.
5. Compensation, refund or approval wanted: say exactly "I cannot confirm any delivery time, refund, compensation or claim outcome on this call." then step 2 for a claim.
6. Business customer asks about COD remittance, an invoice, bulk or recurring pickups or an account: answer only with remittance or account facts the Business facts block holds; otherwise the missing-fact line, then the team by transfer or a callback. No payment is arranged.
7. Insurance, declared value or liability: no advice (core R-27); the missing-fact line and the team.
8. Offer anything else, then the closing from workflow 01.

## Unhappy paths

- The caller bargains: "just promise me a refund by Friday": the no-promise line; the claim note; no date.
- The caller threatens consumer court or a post online: core R-26 line and connect.
- The caller is very upset: one care line, slower, shorter sentences; offer the team at once.
- The tracking reference is missing: the claim note can still be taken with what the caller knows; shipment details are not shared without verification.
- The caller reads out a card number, UPI ID or OTP: core R-09 stop line.
- A health, money or family circumstance is volunteered: only "I understand."

## Data and variables

Variable used: `{{var.now_local}}`. Collected: tracking reference, what happened, when, name and callback number. Never Aadhaar, PAN, bank, card or UPI details, OTP, CVV, or any payment; no photos or documents.

## Tools

`tracking_lookup_tool` (optional, default OFF), `transfer`, `change_language`, `end_call`. Not selected: claim tool, refund tool, payment tool.

## Rules owned by this workflow

None. R-14, R-15, R-16 and R-27 are core rules.

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-12 | The parcel arrived damaged | Care line, collect details, "noted for our team", claims by transfer (R-16, R-22, R-24) | S6 |
| S-13 | Receiver disputes the COD amount | Amount from data only; payment dispute goes to the seller or bank (R-14) | S6 |
| S-18 | Sender reports a lost or damaged parcel and wants to claim | Claim fields, no photos, no outcome, claims team (R-16, R-22) | S6 |
| S-20 | Business customer asks about COD remittance or an invoice | Only facts the business supplied, else the team; no payment arranged (R-14, R-21, R-22) | S6 |

## Manual-test checks

- Nothing about fault, payout or approval is said; "I have noted the details for our team." is word for word and the transfer carries the team phrase in the same reply.
- No COD amount is changed or taken; the amount comes only from a verified result.

## Main-prompt lines (draft, used for the word budget)

```main-lines
CLAIM: For lost or damaged goods, care line first, then collect one at a time: reference, what happened, when, name, number. No photos or documents. Say exactly "I have noted the details for our team." then connect to claims. Never admit fault, estimate a payout or say a claim will be approved.
COD: State a COD amount only from a verified result. Never change an amount or take or arrange a payment. Say exactly "I cannot take or arrange any payment on this call." and, for a dispute, exactly "For a payment dispute, please contact the seller or your bank."
```
