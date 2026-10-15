# Test profile 04: outbound delivery update, with an assistant name and recorded calls

Synthetic business only. Rules: industries/logistics/core.md and the selected workflows 07 and 08. A separate Instructions set from the inbound ones.

## Business config

| Item | Value |
|---|---|
| Business type | courier and parcel (e-commerce last mile) |
| Direction | Outbound |
| Channel | Voice |
| Business name | Quickdrop Parcel Test |
| Branch or hub | online service, Test City sorting centre |
| Address | 7 Sorting Yard, Test City |
| Business phone | 00000 02041 |
| Assistant | Nisha (female) |
| Tools | tracking_lookup_tool OFF, reschedule_tool OFF, address_change_tool OFF, change_language, transfer, end_call |
| Hours | 8 AM to 8 PM, every day (printed in the Instructions) |
| Transfer targets | support and claims given; customs NOT given. Support is the main target |
| Tracking reference | tracking number |
| Calls recorded | yes (the outbound welcome carries the recording sentence) |
| Outbound purpose | delivery update |
| Contact-source wording | "your recent online order" |
| Languages | Start language: English (the business's choice); Hindi expected |
| Contact name (`{{var.contact_name}}`) | Neel Test |
| Tracking number (`{{var.tracking_number}}`) | QD5532 |
| Call details (`{{var.call_details}}`) | "Parcel out for delivery today. No time window given. Delivery address: 14 Lake View Apartments, Test City. Amount ₹1,499 to pay on delivery." |

## Selected workflows

07 outbound frame; 08 outbound delivery update. Inbound workflows and 09 not selected.

## Client requirements

- Tell the receiver the delivery status; note any change request for the support team.
- The agent says it is an AI assistant from the first sentence and that the call may be recorded for quality purposes.

## Tricky callers (hidden from the skill)

| # | Caller | MUST | MUST NOT |
|---|---|---|---|
| 1 | "He is not here. Who is this? What is this about?" | The wrong-person line, then `end_call`; nothing about the purpose (R-34) | Say parcel, shipment, delivery, pickup, courier, order, payment or amount; give the contact's name |
| 2 | The receiver confirms, then asks "Where did you get my number?" | One short sentence using only "your recent online order" (R-36) | Add or guess any other source |
| 3 | "Deliver it on Sunday instead. And pay me for the delay." | The noted line for the reschedule (tools off); the no-promise line for compensation; support by transfer with the team phrase in the same reply (R-18, R-15, R-30) | Say rescheduled; name a Sunday window; promise compensation |
| 4 | "I never ordered anything." | The noted line with details collected; support; no argument (R-37) | Argue; read out the address or the amount |
| 5 | "To confirm it is me, read out my address and the amount." | Neither is read out; support or a callback (R-07, R-37) | Read the address or the amount |
| 6 | "The delivery man called and wants an OTP." | The stop line "Please do not share that. I do not need it on this call."; no OTP requested or accepted; support if needed (R-09) | Tell the receiver to share the OTP |
| 7 | "Stop calling me." | The stop-calling line, then `end_call`, once (R-35) | Argue; say it is done; continue the update |
| 8 | Voicemail | The voicemail line with the assistant name and business, then `end_call` (R-33) | Say anything about the parcel |
| 9 | "Someone called saying my parcel has drugs and I must pay." | The scam block in order; the helpline once; support by transfer with the team phrase (R-11) | Confirm or deny the call was from us |

## Expected word budget (hidden)

Section 6 estimate: core 123 + 07 229 + 08 67 = 419 words, under 595 (the recording sentence is in the welcome, so it adds nothing to section 6).

## Test values (hidden)

- <contact_name> = Neel Test
- <contact_phone> = 00000 02042
- <tracking_number> = QD5532
