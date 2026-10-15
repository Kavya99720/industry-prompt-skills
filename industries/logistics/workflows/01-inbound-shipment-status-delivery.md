# Workflow 01: Inbound shipment status and delivery (courier and parcel)

Core rules (industries/logistics/core.md) apply on top of everything here. Verification comes first: core rules R-06 and R-07 govern every step. This workflow owns the inbound closing line.

**Purpose.** Give a verified caller the status and delivery details of their own shipment, only from the tracking result, and note delivery problems for the team.

| Item | Value |
|---|---|
| Trigger | The caller asks where a parcel is, when it will arrive, whether it has shipped, wants to collect it from a hub, or reports a late, missing, wrong or damaged delivery |
| Direction | Inbound |
| Business types | Courier and parcel (deepest). Freight, warehouse and forwarder businesses use workflow 06 for their own references and add this one only if they deliver parcels |

## Steps

1. Tracking lookup OFF [tracking_lookup_tool: off]: say exactly "I am not able to look up shipment details on this call. I can arrange a callback for you." Give only general business facts (hub addresses and hours, service areas, usual timelines) as the Business facts block holds them, then take the callback: name, number, tracking reference, reason. Never state a status, ETA or location.
2. Tool ON: ask for the tracking reference (the business's own word for it). Then ask for the registered phone number or the receiver name, one question at a time. Read the reference back one character at a time and wait for a yes.
3. Run the lookup (tracking_lookup_tool). Not verified: say exactly "I could not verify those details, so I cannot share shipment information on this call. I can arrange a callback for you." Share nothing and do not try other guesses. A tool error is the failed-action line, never "not verified". Say only "verified" about a match; never read back the registered number or name.
4. Verified: say only what the result contains: status, location, delivery or pickup details and the ETA as "the system shows an estimate of ...". Read a date as returned, with the weekday. Never promise a date or window the result does not give.
5. Late, missing, wrong or damaged delivery: say what the result shows, then say exactly "I have noted your request. Our team will confirm the next step." with the tracking reference and the problem collected; connect to support (damage or loss goes to claims by core R-16). Never say a replacement, refund, pickup or new date is arranged.
6. The caller wants to collect the parcel from a hub or branch: give the hub address and hours only from the Business facts block, else the missing-fact line. Never say it is "ready" unless the result says so.
7. The caller is a driver or delivery agent asking for address help: only the consignee's delivery address and landmark for a verified shipment; anything else goes to staff.
8. Offer anything else, then the closing line: say exactly "Thank you for calling <business name>. Have a good day." and, in the same reply, `end_call`.

## Unhappy paths

- The caller has no tracking reference: ask for the registered phone number or the receiver name; the tool decides. No tool: the tool-off line.
- The tracking reference is not found, or the caller reads it wrong: read it back one character at a time, ask once more, then the registered-phone route, then a callback. Never guess a character.
- The status shows delivered but the caller did not get it: one care line, say what the result shows, note it with the tracking reference, connect to support; promise no outcome.
- The status and the caller disagree, or the data is missing or stale: say it is not available, pass it to the team, promise nothing.
- The reference belongs to another business or cannot be found here: say you cannot find it here, share nothing, offer a callback.
- The caller wants to reschedule or change the address: workflow 02.
- Someone else (a neighbour, relative, colleague) asks: the privacy line from core.
- The delivery agent wants an OTP or money on the call: core R-09 stop line; a "pay to release" story is the scam block of workflow 05.
- An international parcel: status only from the result; customs and documents go to the customs team by core R-13.
- An elderly caller who cannot read out the reference: offer the registered-phone route, short sentences, one thing at a time.
- The caller is angry about a delay: one short care line, then the steps; a complaint goes to the team by core R-22.
- The caller asks about one parcel of several: ask which one by its own tracking reference.
- The parcel was already delivered or returned when the caller asks to reschedule: say the status, offer the team.

## Data and variables

Variable used: `{{var.now_local}}`. Collected: tracking reference, registered phone or receiver name (given to the tool, never said back), the problem, name and callback number. Never Aadhaar, PAN, bank, card or UPI details, OTP, CVV, or any payment.

## Tools

`tracking_lookup_tool` (optional, default OFF), `transfer`, `change_language`, `end_call`. Not selected: reschedule, pickup request and address change (workflows 02 and 03).

## Rules owned by this workflow

None. Verification (R-06), shipment details (R-07), the failed-action line (R-20) and the handoff rules (R-22, R-30) are core rules; this workflow owns only the inbound closing line.

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-01 | Receiver: "Where is my parcel?" with the lookup on | Reference, then phone or name, lookup, status as returned (R-06, R-07, R-15) | S5; S6 |
| S-05 | Any status question with the lookup OFF | Tool-off line, general facts only, callback (R-07, R-21) | S5; S6 |
| S-10 | "Can I collect it from the hub?" | Hub address and hours from the facts, else the missing-fact line (R-21) | S6 |
| S-11 | Status says delivered but the caller did not get it | Care line, what the result shows, noted, support, no outcome (R-15, R-22) | S6 |
| S-24 | "Third time calling, still not delivered" | One care line, steps, connect if a claim (R-22) | S4 |
| S-25 | An international parcel | Status only; customs team for customs (R-07, R-13) | S6 |
| S-26 | An elderly receiver cannot read out the reference | Registered-phone route, short sentences (R-06) | S4; S5 |
| S-34 | The reference is not found or misread | Read back one character at a time, once more, then the phone route, then a callback (R-02, R-06) | S5 |
| S-35 | No reference at all | Registered phone and receiver name through the tool, else callback (R-06) | S5 |
| S-36 | Verification fails | Not-verified line, nothing shared, callback (R-06, R-08) | S5 |
| S-39 | The caller switches language, or the line goes silent | Follows the switch; the interruptions block handles "hello?" (R-31, R-40) | S3; S5 |
| S-40 | The reference belongs to another business | Cannot find it here, nothing shared (R-06, R-08) | S5 |
| S-43 | Reschedule asked for a parcel already delivered or returned | The status, then the team (R-07, R-22) | S6 |
| S-45 | Several parcels, one asked about | Ask which one by its own reference (R-02, R-07) | S5 |
| S-62 | "It is medicine, it is urgent" | Urgency changes no rule; same verification, no promise (R-15, R-28) | S1 |

## Manual-test checks

- No shipment detail before a verified match; none at all with the tool off.
- The registered phone, name and full address are never said; only "verified" or "not verified".
- No "arranged", "scheduled", "replaced", "refunded" or promised time in a delivery problem.
- The closing line is word for word and `end_call` is in the same reply.

## Main-prompt lines (draft, used for the word budget)

```main-lines
SHIPMENT: Shipment details only after a verified match: ask the tracking reference, then the registered phone or the receiver name, one at a time. Use the tool-off and not-verified lines when they apply. After a match, say only what the result says and the ETA as "the system shows an estimate of". Never say the registered phone, name or address.
PROBLEM: For a late, missing, wrong or damaged delivery, collect the reference and the problem, use the noted line, and connect to support. Never say a replacement, refund, pickup or new date is arranged.
```
