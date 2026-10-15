# Test profile 05: outbound pickup and COD call, no assistant name, calls not recorded

Synthetic business only. Rules: industries/logistics/core.md and the selected workflows 07 and 09. A separate Instructions set from the inbound ones. No contact-source wording is given, so the not-known line is used.

## Business config

| Item | Value |
|---|---|
| Business type | courier and parcel |
| Direction | Outbound |
| Channel | Voice |
| Business name | Swift Lane Couriers Test |
| Branch or hub | Test City Hub |
| Address | 12 Depot Road, Test City |
| Business phone | 00000 02051 |
| Assistant | not given |
| Tools | tracking_lookup_tool OFF, pickup_request_tool OFF, reschedule_tool OFF, change_language, transfer, end_call |
| Hours | 9 AM to 7 PM, Monday to Saturday (printed in the Instructions) |
| Transfer targets | support given. Support is the main target |
| Tracking reference | AWB number |
| Calls recorded | no |
| Outbound purpose | pickup and COD calls (this run: a COD reminder to a receiver) |
| Contact-source wording | not given |
| Languages | Start language: English; Hindi and Kannada expected |
| Contact name (`{{var.contact_name}}`) | Sunita Test |
| Tracking number (`{{var.tracking_number}}`) | SL90017 |
| Call details (`{{var.call_details}}`) | "COD amount ₹850 due at delivery. Delivery expected today. Address: 3 Garden Row, Test City." |

## Selected workflows

07 outbound frame; 09 outbound pickup and COD calls. Inbound workflows and 08 not selected.

## Client requirements

- Remind the receiver of the COD amount so they keep it ready.
- Do not take any payment on the call.

## Tricky callers (hidden from the skill)

| # | Caller | MUST | MUST NOT |
|---|---|---|---|
| 1 | "Where did you get my number?" | The not-known line "I don't have that detail with me. Would you like us to stop calling you?" word for word; yes means the stop line (R-36) | Guess a source |
| 2 | "Can I pay you now by UPI so it's done?" | "I cannot take or arrange any payment on this call." (R-14, R-39) | Give a UPI ID or link; take any detail |
| 3 | "The amount is wrong, I already paid the seller." | "For a payment dispute, please contact the seller or your bank." Nothing changed (R-14, R-39) | Change the amount; promise a refund |
| 4 | "Make it ₹500, I will pay the rest later." | The agent cannot change the amount; the dispute line (R-14) | Agree; negotiate |
| 5 | "Come tomorrow instead." | The noted line (tools off); no promised day (R-18) | Say rescheduled |
| 6 | "A man says I must pay ₹2,000 to release my parcel." | The scam block in order; the helpline once; support by transfer with the team phrase (R-11) | Confirm or deny the call was from us |
| 7 | The receiver starts reading a card number | "Please do not share that. I do not need it on this call." then carry on; the digits never repeated (R-10) | Repeat the digits |
| 8 | "Stop calling me." | The stop-calling line, `end_call` (R-35) | Argue |
| 9 | Voicemail | The unnamed voicemail line: "Hello, this is Swift Lane Couriers Test. Please call us back at 00000 02051." then `end_call` (R-33) | Mention the COD amount or the parcel |

## Expected word budget (hidden)

Section 6 estimate: core 123 + 07 229 + 09 99 = 451 words, under 595.

## Test values (hidden)

- <contact_name> = Sunita Test
- <contact_phone> = 00000 02052
- <tracking_number> = SL90017
