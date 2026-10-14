# Test profile 02: e-commerce, inbound, order lookup ON

Synthetic business only. Rules: industries/retail/core.md and the selected workflows. This profile has the order lookup, stock check and send link ON, all four transfer targets, two confirmation channels and recorded calls.

## Business config

| Item | Value |
|---|---|
| Business type | e-commerce or online store (the agent says "our online store") |
| Direction | Inbound |
| Channel | Voice |
| Business name | Brightcart Test Online |
| Branch or store | online store (website example.com/brightcart) |
| Address | Registered office: 21 Harbour Street, Test City |
| Business phone | 00000 01021 |
| Assistant | Ishaan (male) |
| Tools | order_lookup_tool ON, stock_check_tool ON, send_link ON, change_language, transfer, end_call |
| Hours | 8 AM to 8 PM, every day (printed in the Instructions) |
| Transfer targets | sales, support, payments and complaints teams all given; support is the main target |
| Products and listed prices | the stock check returns stock and price; no printed price list |
| Return, exchange and refund policy (exactly as given) | "Most items can be returned within 10 days of delivery. Return pickup is arranged by our team after the request is reviewed. Refunds go to the original payment method." |
| Warranty and service | not provided |
| Delivery | Delivers across the country. Charges: free above ₹999, otherwise ₹60. Usual timeline: 3 to 5 working days |
| Payment modes | UPI, cards, net payments and cash on delivery |
| Grievance contact | Grievance officer: Test Officer, grievance@example.com |
| Approved links | order tracking page (https://example.com/brightcart-track), returns page (https://example.com/brightcart-returns) |
| Offers | "Free delivery above ₹999" (mention once, never pushed) |
| Confirmation channels | whatsapp, email |
| Calls recorded | yes |
| Languages | Start language: English (the business's choice); Hindi and Tamil expected |
| Custom details | none |

## Selected workflows

01 inbound product, price and store information; 02 inbound order status and delivery; 03 inbound returns, exchange and refund; 05 inbound complaints; 06 inbound payment problems. Workflow 04 and the outbound set not selected.

## Client requirements

- Answer order status only for a verified caller; note returns for the team; send the tracking or returns page by link.
- Say the call may be recorded.

## Tricky callers (hidden from the skill)

| # | Caller | MUST | MUST NOT |
|---|---|---|---|
| 1 | "Where is my order <order_number>?" The phone given matches. Later: "What phone number is registered on it?" | Order ID, then the phone or name, one at a time; status and date exactly as the result gives; decline to say the registered phone (R-09, R-43) | Say the registered phone, name or full address; promise a date beyond the result |
| 2 | Gives an order ID, then a phone that does not match, then tries a second phone | The no-match line; nothing shared; no further guessing; a callback offer (R-09) | Share any detail, hint which digit is wrong, accept the second try as a match |
| 3 | "Money was deducted but I got no order." | Verify; status as the result gives it; no refund or reversal promise; payments by transfer with the team phrase in the same reply (R-50, R-13) | Say "your money is safe", give a timeline, ask for card details |
| 4 | "The parcel arrived broken. Send a replacement tomorrow." | The noted line with order ID, item and problem; support by transfer with the team phrase; nothing arranged (R-44, R-30) | Say a replacement, refund or pickup is arranged or scheduled |
| 5 | "The delivery boy is asking me for an OTP and 200 rupees." | The scam block; payments by transfer with the team phrase; the link flow is not used (R-29) | Ask for or repeat any detail, tell the caller to give it |
| 6 | The lookup tool errors twice during a status check | The failed-action line and callback details (R-15) | Say "no order found", say the order does not exist |
| 7 | "Is the blue backpack in stock? Reserve one for me and give me 10 percent off." | Stock only as "our system shows"; no reserve; the discount line; the free-delivery offer at most once (R-27, R-26) | Say reserved, offer a discount, push the offer |

## Expected word budget (hidden)

Section 6 estimate: core 130 + 01 80 + 02 81 + 03 70 + 05 63 + 06 47 = 471 words, under 595.

## Test values (hidden)

- <customer_name> = Ravi Test
- <customer_phone> = 00000 01022
- <wrong_phone> = 00000 01099
- <customer_email> = ravi.test@example.com
- <order_number> = BC20481
