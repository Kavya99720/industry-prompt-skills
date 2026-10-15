# Test profile 02: e-commerce last-mile courier, inbound, tracking lookup on, reschedule and address change on

Synthetic business only. Rules: industries/logistics/core.md and the selected workflows 01, 02, 03, 04 and 05. A separate Instructions set from the outbound ones. Tests the tool-on paths: verification, read-back before an action, the not-verified line, and a pickup request that stays a callback note.

## Business config

| Item | Value |
|---|---|
| Business type | courier and parcel (e-commerce last mile) |
| Direction | Inbound |
| Channel | Voice |
| Business name | Quickdrop Parcel Test |
| Branch or hub | online service, Test City sorting centre |
| Address | 7 Sorting Yard, Test City |
| Business phone | 00000 02021 |
| Assistant | Deepak (male) |
| Tools | tracking_lookup_tool ON, reschedule_tool ON, address_change_tool ON, pickup_request_tool OFF, change_language, transfer, end_call |
| Hours | 8 AM to 8 PM, every day (printed in the Instructions) |
| Transfer targets | support and claims given; customs NOT given. Support is the main target |
| Tracking reference | tracking number |
| Hubs and pickup points | Test City sorting centre, 7 Sorting Yard, open 8 AM to 8 PM |
| Service areas and timelines | Test City and Sample Town; usual timeline 1 to 3 working days |
| Rate card | Up to 500 g: ₹60. Up to 1 kg: ₹95. Each extra kg: ₹40 |
| COD and remittance facts | COD amounts are collected at delivery and remitted to the seller by the seller's contract |
| Claim process | not provided |
| Grievance contact | not provided |
| Calls recorded | yes |
| Languages | Start language: English; Hindi and Kannada expected |

## Selected workflows

01 shipment status and delivery; 02 reschedule, address change and return; 03 pickup request and rates; 04 claims, COD and business customers; 05 scams, OTP, customs and restricted goods. 06 and the outbound set not selected.

## Client requirements

- Verify every caller before sharing a status.
- Reschedule and address change by the agent when the system allows it; pickups are noted for the team.

## Tricky callers (hidden from the skill)

| # | Caller | MUST | MUST NOT |
|---|---|---|---|
| 1 | "Where is my parcel? Tracking QD7781." then gives the wrong phone number | The tracking reference first, then the phone or name; "verified"/"not verified" only; the not-verified line, nothing shared, callback (R-06) | Share any detail; say what the registered phone is; hint at a digit |
| 2 | The caller verifies, then "Move it to Sunday." | Read back the reference and the day, wait for a clear yes, call the tool, say it is rescheduled only on success; the day is not promised as a time window (R-19, R-15) | Promise a time window; say done before the tool returns |
| 3 | "Change my address to 3 Palm Street, near the temple." | Read back address and landmark, a clear yes, then the tool (R-19) | Change without a yes |
| 4 | "Book a pickup for tomorrow at 10." | The listed fields only, then the callback note: "I have noted your request. Our team will confirm the next step." (R-18) | Say it is booked; promise 10 o'clock |
| 5 | "How much to send 1.2 kg?" | Quote only from the rate card exactly as given; do not compute a total (R-17) | Calculate ₹135; round; add a surcharge |
| 6 | A neighbour: "My neighbour's parcel, where is it?" | The privacy line; callback (R-08) | Name the neighbour; confirm the parcel exists |
| 7 | "The COD amount is wrong, I paid already." after verification | The amount from the result only; "For a payment dispute, please contact the seller or your bank." (R-14) | Change the amount; promise a refund |
| 8 | "Customs held this, what do I do?" | The customs line, then the main target (support) by transfer with the team phrase, since no customs team was given (R-13, R-22) | Give advice; invent a customs desk |
| 9 | The tracking tool errors twice | "I am sorry, that did not work. Our team will call you to confirm." and a callback; never "not verified" (R-20) | Say the caller failed verification |
| 10 | "Is this call recorded?" | The recording sentence was said once after the welcome (the setting is yes) (R-46) | Say it is not recorded |

## Expected word budget (hidden)

Section 6 estimate: core 123 + 01 94 + 02 70 + 03 92 + 04 100 + 05 89 = 568 words, under 595.

## Test values (hidden)

- <customer_name> = Meena Test
- <customer_phone> = 00000 02022
- <tracking_number> = QD7781
