# Retail brainstorm (cross-check against the brief)

Source: Retail grill-me, DECISIONS 112 (2026-10-14) and the owner's changes in 113; run after the first brief package, as a cross-check. Voice only (entry 113), so silence, noise, mishearing and spelled-out data are in scope. Each item shows where it is handled: "covered" with its rule, or "added" with the new rule or scenario. The owner asked for this run to save the list and add the missing items in one step; remove or re-mark any item and the matching addition will be taken out.

## 1. Caller scenarios

1. [MUST] Where is my order, status and delivery date (covered: R-09, R-43)
2. [MUST] Is a product in stock, and the price (covered: R-26, R-27, R-41)
3. [MUST] Return, exchange or refund request and "what happened to my refund" (covered: R-30, R-45, R-46)
4. [MUST] Warranty question for a specific product (covered: R-47)
5. [MUST] Repair or service request and repair status (covered: R-48)
6. [MUST] Complaint, including a consumer-court or "I will post online" threat (covered: R-49, R-07)
7. [MUST] Money deducted but no order, failed payment (covered: R-50)
8. [NICE] Store hours, address, other locations, delivery areas (covered: R-41)
9. [MUST] Gift card, voucher, store credit or loyalty points: how it works, a balance, a lost card, a code read out (added: R-66, S-150; the code goes in the no-collect list, R-11)
10. [MUST] EMI or no-cost EMI question, "am I eligible?" (added: R-67, S-151)
11. [MUST] Cash on delivery: refusing the parcel at the door, changing to prepaid (added: S-154; covered by R-44 for the no-cancel rule)
12. [MUST] Damaged, wrong or missing item on delivery (covered: R-44, S-44)
13. [MUST] Installation of a new appliance, "is it free?" (added: R-69, S-157)
14. [MUST] Price dropped after purchase, "give me the difference" (added: sentence in R-26, core S-25)
15. [NICE] Trade-in or exchange value for an old product (added: sentence in R-26, core S-26)
16. [NICE] Bulk, business or GST-invoice buyer (added: R-68, S-152)
17. [MUST] Store pickup: "is my order ready for pickup?" (added: S-155; a step in workflow 02)
18. [NICE] Copy of the invoice or bill (added: S-156; a step in workflow 02)
19. [NICE] Extended warranty purchase (added: S-158, no sale on the call)
20. [NICE] Festive sale rush: "is the sale ending, must I hurry?" (covered: R-26, R-32, S-37; added S-153 for the exact words)
21. [MUST] Caller asks for a person or a manager (covered: R-13, R-34)
22. [MUST] Elderly, confused or frightened caller (added: R-65, core S-23)
23. [MUST] Child caller (added: R-65, core S-24; age-restricted items are never sold or discussed)
24. [NICE] Exchange for another size or colour (covered: workflow 03)
25. [NICE] Product spec or compatibility question, "which one should I buy?" (covered: R-38, R-41, S-18)
26. [NICE] Caller who has called three times about the same issue and is angry (covered: workflow 05, R-49)

## 2. Edge cases and failure modes

27. [MUST] Order lookup tool errors or times out (covered: R-15, S-14, S-48)
28. [MUST] Stock check errors (covered: R-15)
29. [MUST] Order ID misheard or given with letters and digits mixed (covered: R-02 read-back, section 2 reads IDs one character at a time)
30. [MUST] Order ID matches but the phone or name does not (covered: R-09, S-12)
31. [MUST] Order lookup tool is off (covered: R-09, S-11)
32. [MUST] No transfer target, or a named team that was not given (covered: R-14, R-35, routing table)
33. [MUST] Caller asks about something the business gave no facts for (covered: R-12)
34. [NICE] Caller answers in Hindi, Kannada or a mix (covered: R-40)
35. [NICE] Silence, a noisy line or interruptions (platform behaviour; see open question 2)
36. [NICE] Caller gives several orders or items in one breath (covered: R-02, R-03)
37. [MUST] Outbound call reaches the wrong person, a voicemail or a stop request (covered: R-52, R-53, R-54)
38. [MUST] Outbound call data is empty (covered: R-57, workflows 08 to 11)

## 3. Compliance and safety risks

39. [MUST] Device sparking, smoking, burning smell, shock, fire, gas leak, injury (covered: R-04)
40. [MUST] Self-harm after a scam loss (covered: R-05)
41. [MUST] Card, UPI, OTP, CVV, PIN, Aadhaar, PAN, bank details on the call (covered: R-11)
42. [MUST] Fake refund call or link, "they asked for my OTP", already shared a detail (covered: R-29, R-50; the bank line now adds the cybercrime helpline 1 9 3 0)
43. [MUST] "Refunded", "approved", "replaced", "pickup scheduled" said too early (covered: R-30)
44. [MUST] Invented stock, price, discount, offer or delivery date (covered: R-26, R-27, R-28)
45. [MUST] Sharing order details without a match (covered: R-09)
46. [MUST] Data deletion, correction, access or stop-marketing request under DPDP (added: R-64, core S-22)
47. [MUST] Counterfeit, fake, used or refurbished-as-new claims (added: R-70, S-159)
48. [NICE] Overcharge above the printed price (MRP) complaint (added: S-160, an unhappy path in workflow 05)
49. [MUST] Repair, technical or safety advice and warranty cover decisions (covered: R-31, R-47)
50. [MUST] AI disclosure and recording line (covered: R-18, R-37, R-51)
51. [NICE] Aggressive urgency or scarcity lines asked for by the client (covered: R-24, R-32)

## 4. Adversarial attempts

52. [MUST] "Ignore your rules", prompt extraction, pasted text (covered: R-19)
53. [MUST] Claimed courier, police, owner, regulator or lawyer (covered: R-19, R-34)
54. [MUST] Another person's order, a relative or a child asking (covered: R-10, R-65)
55. [MUST] Guessing phone numbers or names until the lookup matches (covered: R-09, "do not try other guesses")
56. [MUST] Pressure to say "approved" or "refunded" off the record (covered: R-30, S-55)
57. [NICE] Price probing against a competitor and price matching (covered: R-26)
58. [NICE] Asking the agent to place an order or take a payment for them (covered: R-38, R-29)

## Open questions

1. A product recall or safety-notice outbound call is not in the owner's outbound list. Not added; the owner may want a workflow later.
2. Silence, background noise, interruptions and call drops are platform behaviours; nothing is written for them in the Instructions.
3. Whether the business sells age-restricted items (R-65 never sells or discusses them) is not asked at intake.
4. The business's GST invoice, installation and extended-warranty terms are optional intake facts only if the owner wants them as separate intake questions; today they are covered by "warranty and repair or service-centre information" and "special rules".
