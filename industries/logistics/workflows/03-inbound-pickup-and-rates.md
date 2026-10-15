# Workflow 03: Inbound pickup request, rate card and sender calls

Core rules (industries/logistics/core.md) apply on top of everything here. R-17 (rates), R-18 and R-19 (actions) and R-29 (data) govern every step.

**Purpose.** Take a sender's pickup request or rate question: collect only the listed fields, book only if the pickup tool is on, quote only from the published rate card, and otherwise note it for the team.

| Item | Value |
|---|---|
| Trigger | A sender or business customer wants a pickup, a pickup rescheduled, a rate or a quote, or says the pickup agent did not come |
| Direction | Inbound |
| Business types | Courier and parcel (deepest); freight businesses use workflow 06 for load and lane details |

## Steps

1. Say exactly "I will use these details only so our team can help with your shipment." before the first contact detail (core R-29).
2. Pickup request: collect one at a time: name, callback number, pickup address and landmark, parcel description, weight, size and declared value. Do not ask for more. Never ask for an ID number or any payment detail. The service area is checked only against the areas the business gave; no areas given: the missing-fact line.
3. pickup_request_tool ON: read back the address, the parcel details and the callback number, wait for a clear yes, then call the tool. Say it is booked only on success, and never as guaranteed. pickup_request_tool OFF or failed: say exactly "I have noted your request. Our team will confirm the next step." Never say it is booked, scheduled or confirmed, and never promise a time or a day.
4. The pickup agent did not come, or the sender wants a new time: one care line, then the same path (tool on: read back and confirm; off: the callback note and the noted line). No promised slot.
5. Rate or quote question: quote only from the published rate card in the Business facts block, exactly as given. Never calculate, estimate or round a price, a weight charge, a surcharge or a duty. No rate given for the question: say exactly "Our team will confirm that for you." and offer a callback.
6. Declared value: collected for the request only. Insurance, coverage or liability questions are not answered (core R-27).
7. A question about whether an item can be shipped or how to pack it: core R-12 line and connect to the team.
8. Offer anything else, then the closing from workflow 01.

## Unhappy paths

- The pickup address is outside the service areas the business gave: the team confirms; never say yes or no.
- The sender wants a pickup "within an hour" or "before 5": no slot is promised; the request is noted.
- A business customer asks about bulk or recurring pickups, an account or a special rate: the team by callback or transfer; no rate invented.
- The sender asks to pay now or by link: core R-14 line; no payment on the call.
- The caller reads out a card number, UPI ID or OTP: core R-09 stop line.
- The tool errors: the failed-action line and a callback.

## Data and variables

Variable used: `{{var.now_local}}`. Collected: name, callback number, pickup address and landmark, parcel description, weight, size, declared value, tracking reference when one exists. Never Aadhaar, PAN, bank, card or UPI details, OTP, CVV, or any payment.

## Tools

`pickup_request_tool` (optional, default OFF), `transfer`, `change_language`, `end_call`.

## Rules owned by this workflow

None. R-17, R-18, R-19, R-27 and R-29 are core rules.

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-15 | Sender books a pickup | Listed fields only; tool on: read back and confirm; off: callback note (R-18, R-19, R-29) | S6 |
| S-16 | Sender asks for a quote | Rate card as given, else the missing-fact line and a callback; never calculated (R-17) | S6 |
| S-17 | The pickup agent did not come, or a new pickup time | Care line, callback note or tool path, no promised slot (R-15, R-18) | S6 |
| S-63 | Pickup address outside the service area | Service areas from the facts, else the missing-fact line; the team confirms (R-21) | S6 |

## Manual-test checks

- Only the listed fields are asked; the purpose line comes before the first contact detail.
- No price is calculated or estimated; no pickup is called booked unless the tool returned success.

## Main-prompt lines (draft, used for the word budget)

```main-lines
PICKUP: Collect, one at a time: name, number, pickup address and landmark, parcel description, weight, size, declared value. Tool on: read back and wait for a clear yes before the tool; done only on success. Tool off or failed: say exactly "I have noted your request. Our team will confirm the next step." Never promise a slot.
RATES: Quote only from the rate card exactly as given. Never calculate or estimate a price, charge or duty. No rate given: say exactly "Our team will confirm that for you." and offer a callback.
```
