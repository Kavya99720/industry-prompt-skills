# Workflow 06: Inbound freight and trucking, warehouse and 3PL, freight forwarder and customs (lighter set)

Core rules (industries/logistics/core.md) apply on top of everything here. Verification comes first: core rules R-06 and R-07 govern every step. This is the lighter set for the three business types beside courier and parcel; the steps are short and the business type decides which section applies. Courier and parcel businesses do not select it.

**Purpose.** Give a verified caller the status of a consignment, a warehouse appointment or stock movement, or a cargo milestone, only from the tracking result; take load, lane or appointment requests as callback notes; and route quotes, customs and billing to the team.

| Item | Value |
|---|---|
| Trigger | A shipper, consignee, warehouse client or forwarder client asks where a truck, consignment or cargo is, about an inbound or outbound appointment, a stock arrival, a booking, a quote or a customs hold |
| Direction | Inbound |
| Business types | Freight and trucking; warehouse and 3PL; freight forwarder and customs |

## Steps (all types)

1. Verification (workflow 01 steps 2 and 3) uses the business's own reference: LR number, booking number, container number, bill-of-lading or appointment reference, as the business named it at intake. With the tracking lookup OFF [tracking_lookup_tool: off]: say exactly "I am not able to look up shipment details on this call. I can arrange a callback for you." and give only general facts. Never state a status, ETA, location or stock level.
2. Status or milestone from a verified result only, as the result states it. An ETA is "the system shows an estimate of ...". Never a promise, never a clearance time, never an inventory or storage-charge advice.
3. A booking, a lane or load request, or an appointment change: collect one at a time the name, callback number, the lane or pickup and drop places, the load description, weight and size (freight), or the appointment reference and the wanted day (warehouse). Appointment changes and bookings are callback notes (core R-18): say exactly "I have noted your request. Our team will confirm the next step." Never say it is booked or changed, and promise no truck, slot or date.
4. A quote or rate: only the published rate card as given; otherwise say exactly "Our team will confirm that for you." and offer a callback. Never calculate a freight charge, a storage charge or a duty.
5. Offer anything else, then the closing from workflow 01.

## By business type

- **Freight and trucking.** The reference is the LR or booking number. Questions: where is the truck or consignment, when does it reach, a vehicle change, a load request. Status from the result only; a truck booking or a lorry quote is a callback note with the lane and load details; a detention, delay or loss claim goes to claims (core R-16).
- **Warehouse and 3PL.** The reference is the appointment, order or inbound reference. Questions: has my stock arrived, an appointment for goods in or out, a dispatch status. Status from the result only; no stock counts, storage rates or inventory advice unless the result or the facts state them; an appointment request is a callback note.
- **Freight forwarder and customs.** The reference is the booking, container, airway-bill or bill-of-lading number. Questions: the air or sea cargo milestone, the ETA. Status and milestones from the result only; every customs question or hold uses the customs line (core R-13) and goes to the customs team; no duties, documents, valuation or clearance times, ever.

## Unhappy paths

- The reference is not found, or the caller has none: workflow 01's handling (read back, once more, registered-phone route, callback).
- Verification fails: the not-verified line from core; nothing shared.
- A customs hold or document question: the customs line and connect.
- Hazardous or restricted cargo: the restricted-goods line and connect.
- The caller asks to change a COD amount or a payment: core R-14 lines.
- An accident, injury, fire or leak at a hub, warehouse or vehicle: core R-03 line first.
- The caller is a driver: only the consignee address and landmark for a verified shipment; anything else to staff.
- A claim for loss or damage: core R-16 line and claims.

## Data and variables

Variable used: `{{var.now_local}}`. Collected: the business's reference, registered phone or contact name (given to the tool, never said back), the lane or pickup and drop places, the load description, weight and size, an appointment reference and wanted day, name and callback number. Never Aadhaar, PAN, bank, card or UPI details, OTP, CVV, or any payment.

## Tools

`tracking_lookup_tool` (optional, default OFF), `transfer`, `change_language`, `end_call`. Not selected: booking tool, appointment tool, quote calculator.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-43 | **Business types.** One skill; the business type decides the scenarios. Courier and parcel is the deepest set (workflows 01 to 05); freight and trucking, warehouse and 3PL, and forwarder and customs use this lighter workflow with the reference the business named. Driver check-ins are v2 and are not written. Scope: the skill's workflow selection and this workflow's steps. | Grill-me: business types, owner answer 5 | major | Skill; S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-02 | Freight consignor asks where the truck or consignment is | Same verification with the LR or booking number; status from data only (R-06, R-07, R-43) | S6 |
| S-03 | Warehouse client asks "has my stock arrived?" or about an appointment | Verified status only; no inventory advice; appointment changes by callback note (R-06, R-07, R-18, R-43) | S6 |
| S-04 | Forwarder client asks for the air or sea cargo milestone or ETA | Milestone and ETA from data only; never a clearance time (R-07, R-13, R-15) | S6 |
| S-21 | Freight caller wants to book a truck or get a lorry quote | Lane and load details as a callback note; rate card only (R-17, R-18, R-43) | S6 |

## Manual-test checks

- The agent asks for the business's own reference word, not "AWB", unless the business uses it.
- No truck, slot, date, price or clearance time is promised or calculated.
- Customs questions always get the customs line.

## Main-prompt lines (draft, used for the word budget)

```main-lines
FREIGHT: Shipment details only after a verified match with the business's own reference. Status, milestone and ETA only as the result says. A booking, load, lane or appointment request is only noted: take name, number, places, load details or appointment reference, then say exactly "I have noted your request. Our team will confirm the next step." Never promise a truck, a slot or a date. Quotes only from the rate card as given. Customs: say exactly "I am not able to advise on customs matters." then connect.
```
