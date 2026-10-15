# Logistics brainstorm

Source: Logistics grill-me, DECISIONS 121 (2026-10-15) and industries/logistics/grill-me.md. Voice only. v1 directions: inbound support, outbound delivery updates, outbound pickup and COD calls. Driver check-ins are v2 and not covered. Confirmed by the owner as is.

## 1. Caller scenarios

1. [MUST] Receiver: "Where is my parcel?" Status from system data only, after verification.
2. [MUST] Receiver: reschedule delivery, or "come tomorrow, not today". No promised slot.
3. [MUST] Receiver: change the delivery address or add a landmark.
4. [MUST] Receiver: failed attempt or missed delivery, "I was home and nobody came."
5. [MUST] Receiver: delivery agent is outside, wants an OTP, or "the agent says give him the OTP". Stop line, no OTP.
6. [NICE] Receiver: wants to pick the parcel up from the hub or branch. Hours and address come from business facts only.
7. [MUST] Receiver: parcel shows delivered but they did not get it.
8. [MUST] Receiver: parcel arrived damaged. Collect the details and hand off.
9. [MUST] Receiver: asked to pay COD and disputes the amount. State the amount from system data only, and send disputes to the seller.
10. [MUST] Receiver: wants to refuse the parcel or return it to the sender.
11. [MUST] Sender: book a pickup (address, parcel description, weight, size, declared value, callback number).
12. [MUST] Sender: asks for a quote or rate. Only business-supplied rates, or the team.
13. [MUST] Sender: pickup agent did not come, or wants to reschedule the pickup.
14. [MUST] Sender: parcel lost or damaged, wants to file a claim. Collect the damage or loss details, no outcome promised, hand off.
15. [NICE] Sender: asks whether an item is allowed or packed correctly (liquids, batteries, medicines, food). Never advises, hands off.
16. [MUST] Business customer: COD remittance or payment status. Only if the business gives that data; otherwise the team.
17. [NICE] Business customer: bulk or recurring pickups, account or rate query. Team.
18. [NICE] Business customer: invoice or billing question. Team.
19. [MUST] Freight: "Where is my truck or consignment?" Status from data only, with LR or booking number as the reference.
20. [NICE] Freight: book a truck or ask for a lorry quote. Take the lane and load details, team to quote.
21. [MUST] Warehouse or 3PL: inbound or outbound appointment, "has my stock arrived?" Verified status only.
22. [MUST] Forwarder: air or sea cargo milestone or ETA. System data only, no clearance time.
23. [MUST] Customs hold or "my shipment is stuck at customs." Hand off, no advice on duties, documents or timing.
24. [NICE] Driver or delivery agent calls the inbound line: address help, can't find the receiver. Only the consignee's delivery address and landmark with a verified shipment; staff handle the rest.
25. [MUST] Angry caller, "third time calling, parcel still not delivered." Care line, then hand off if the matter is a claim or an escalation.
26. [NICE] Caller asks for a branch or hub phone number, hours or address. Business facts only.
27. [NICE] Caller asks about an international shipment from India. Status only, otherwise the team.
28. [NICE] Elderly or less tech-savvy receiver who cannot read out the tracking number. Offer the registered phone route.
29. [MUST] Outbound delivery update: out for delivery, failed attempt, reschedule confirmation, address confirmation.
30. [MUST] Outbound: wrong number or the receiver is not the person. Share nothing.
31. [MUST] Outbound pickup: confirm pickup time and address with the sender. Do not promise a slot beyond the system data.
32. [MUST] Outbound COD: remind the receiver of the amount to keep ready. State the amount from system data and arrange no payment.
33. [MUST] Outbound: the receiver says "stop calling me." Use the fixed stop-calling line.
34. [NICE] Outbound: the receiver is busy and asks for a call later.
35. [NICE] Outbound: the receiver asks "how did you get my number?" Use the contact-source handling from the other industries.

## 2. Edge cases and failure modes

36. [MUST] The tracking or AWB number is not found, or the caller reads it wrong. Offer the registered phone route, then a callback.
37. [MUST] The caller has no tracking number. Use the registered phone, then the receiver name.
38. [MUST] Verification fails. Share nothing, offer a callback.
39. [MUST] The tracking tool is down or returns an error. Do not guess a status. Use the failed-action line and take a callback.
40. [MUST] The status data is missing or stale. Say it is not available and offer the team.
41. [MUST] Conflicting data (the agent says delivered, the caller says no). Pass to the team and promise no outcome.
42. [MUST] Nobody available for a transfer. Take the callback and say "Our team will call you back." with no time.
43. [NICE] The caller speaks another language or switches mid-call. Follow the business's supported list, with English first.
44. [NICE] The caller is silent, the line is noisy, or the caller interrupts. Platform behaviour, little to write.
45. [MUST] Tracking numbers, AWBs and phone numbers read out one digit at a time. Confirm without saying back sensitive details.
46. [MUST] A tracking number belongs to a different business than the one the caller reached.
47. [MUST] Reschedule or address change attempted when no tool exists. Take a callback and never say it was done.
48. [MUST] The caller wants a committed delivery time. Give only the system ETA, never a promise.
49. [NICE] The shipment has already been delivered or returned when the caller asks to reschedule.
50. [NICE] The caller wants a COD amount changed.
51. [NICE] A multi-parcel shipment, with the caller asking about only one of the parcels.
52. [NICE] Pickup address outside the service area. The team confirms.

## 3. Compliance and safety risks

53. [MUST] Courier scam: "your parcel has drugs", "customs or police case", "pay to release the parcel". Fixed block, cybercrime helpline 1 9 3 0, bank line if they already paid.
54. [MUST] Never confirm or deny that a scam call came from us.
55. [MUST] OTP of any kind, including the delivery OTP. Fixed stop line when a caller starts reading one out.
56. [MUST] No card, UPI, PIN or CVV on the call. A caller starts reading one out, same stop handling.
57. [MUST] Emergencies: road accident, injury, warehouse or hub fire, gas or chemical leak. Fixed "Call 1 1 2 right now." and transfer, no advice.
58. [MUST] Hazardous or restricted goods: never say if an item can ship. Hand off.
59. [MUST] COD: the amount only from system data, no payment taken or arranged on the call, disputes go to the seller or bank.
60. [MUST] Customs: no advice on duties, documents or clearance times. Holds go to the team.
61. [MUST] No promised delivery time, refund, compensation or claim outcome.
62. [MUST] Another person's shipment details: an address or phone number is personal data under DPDP, and nothing is shared before verification.
63. [MUST] A third party (a neighbour, the caller's family or a "relative") asks for status. Verification still applies.
64. [MUST] Claims: collect only what happened and when. No photos or documents over voice, no admission of fault.
65. [MUST] A child answers the phone. Share nothing and ask for an adult.
66. [MUST] AI disclosure in the outbound welcome. The recording line only if the business records calls.
67. [NICE] A legal threat, consumer court or a social media post. Hand off.
68. [NICE] A journalist or regulator asks questions. Hand off.
69. [NICE] Declared value and insurance questions. No coverage advice.

## 4. Adversarial attempts

70. [MUST] A caller claims to be the police, customs, the "courier head" or a lawyer and demands data. A claimed role changes nothing.
71. [MUST] A caller asks "is this number yours?" after a scam call, trying to get confirmation.
72. [MUST] Prompt injection ("ignore your instructions", "tell me your system prompt"). Decline plainly.
73. [MUST] A caller who knows only the receiver's name and phone tries to pull the address and parcel contents.
74. [MUST] A caller bargains for a refund, compensation or "just promise me tomorrow".
75. [MUST] Social engineering by a "delivery agent" or "branch staff" caller asking for customer details.
76. [MUST] A caller asks the agent to take a payment "just to release the parcel".
77. [NICE] A caller asks the agent to change a COD amount or a recipient's name.
78. [NICE] A caller asks for competitor comparisons or opinions on other couriers.
79. [NICE] A caller asks for non-shipment help (an order or product dispute, refunds). Out of scope, goes to the seller or bank.
80. [NICE] A caller pressures with urgency ("it's medicine, it's urgent") to get promises or data.

## Open questions

1. Which tools exist? A tracking lookup, reschedule, pickup booking, address change, callback and transfer are all unspecified. Assumed: tracking lookup and callback always on; the rest optional, as booking was in other industries.
2. Is the cybercrime helpline wording and the "bank line" for callers who already paid copied from banking word for word?
3. Does "registered phone number" mean the caller's own number (caller ID) or a number they read out? Assumed: a number they read out that matches the record.
4. Hub, branch and pickup hours: business facts only.
5. Business-type scope inside one skill: courier/parcel deepest, the other three lighter workflows, as in real estate? Not yet decided.
6. Quotes: only business-supplied rates, or none at all?
