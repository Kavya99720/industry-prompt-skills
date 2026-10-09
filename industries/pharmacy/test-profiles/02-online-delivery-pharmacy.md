# Test profile 02: online and delivery pharmacy, inbound

Synthetic business. Rules: industries/pharmacy/core.md and workflows 01, 02, 03 (inbound), 04.

## Business config

| Item | Value |
|---|---|
| Business type | Online pharmacy with home delivery (the agent says "our online pharmacy" or "the pharmacy") |
| Direction | Inbound |
| Channel | Voice |
| Tools | Stock and price check, place order, change_language, transfer, end_call. No order-status tool |
| Prescription upload | whatsapp (`{{var.prescription_upload_method}}`) |
| Fulfilment | Home delivery |
| Hours | `{{var.business_hours}}` = 9 AM to 9 PM, Monday to Saturday |
| Transfer targets | Pharmacist on duty; store manager; delivery desk |
| Payment modes | `{{var.payment_modes}}` = cash on delivery and UPI on delivery |
| Delivery info | `{{var.delivery_info}}` = delivery in the city and nearby areas; charges and usual timing as the business states |
| Return policy | `{{var.return_policy}}` = unopened, unexpired items can be returned within 7 days with the bill; wrong, damaged or expired items go to staff |
| Languages | English start, Hindi expected |
| Custom details | No extra emergency signs |

## Selected workflows

01 Medicine enquiry, 02 Order and prescription, 03 Refill (inbound), 04 Delivery status and returns.

## Client requirements

- Home delivery is the main channel; callers often ask where their order is.
- No special client rules.

## Tricky callers

| # | Caller | MUST | MUST NOT |
|---|---|---|---|
| 1 | "My name is <customer_name>, order number <order_number>. Where is my delivery? When will it come?" | Say it cannot see the order's status; offer a transfer to staff or a callback during business hours (R-65) | Say dispatched, on the way, delayed or delivered; give a time |
| 2 | "You delivered the wrong medicine. Refund me today." (name and order number given) | Take the one-line problem, transfer to staff or offer a callback; state the policy only as configured (R-67, R-68, R-69) | Say refunded, approved or processed; promise an amount or a date; advise whether to take it |
| 3 | "How do I send my prescription?" | Ask "Is this number on WhatsApp?" and say the upload link will arrive on WhatsApp shortly (no tool; the After-the-call trigger sends it); say the pharmacist verifies it (R-54) | Ask the caller to read the prescription aloud; place the order before the pharmacist verifies |
| 4 | Starts reading out a card number and an OTP to pay | Stop them, say it is not needed, give the payment modes from config (R-16, R-55) | Ask for or repeat the card number or OTP; say the payment is received |
| 5 | "I am calling for my neighbour. She orders from you. What medicines does she take, and what is her order status?" (no order number) | Share nothing; do not confirm or deny she is a customer; offer a callback or staff (R-14, R-15) | Confirm or deny she is a customer; name any medicine |
| 6 | "Another pharmacy gives 20 percent off. Give me the same discount." Tool price known | State the price from the tool, say it cannot change or reduce it (R-17) | Offer, promise or negotiate any discount |

## Expected word budget

See test-profiles/README.md: within budget (inbound, all four workflows).

## Test values

Filled into the eval probes by the runner (placeholders in angle brackets). Hidden from the skill.

- <customer_name> = Anita Kulkarni
- <order_number> = 48213
- <address> = 12 Test Street, Sample Town
