# Logistics grill-me

Date: 2026-10-15. Interview: 4 rounds of two questions in the main chat, then the owner's changes after the summary. Every answer below was chosen or confirmed by the owner. Nothing here is a design: the brief and skill are not started.

## Answers

| # | Topic | Owner's answer |
|---|---|---|
| 1 | Business types | All four: courier/parcel, freight/trucking, warehouse/3PL, freight forwarder/customs. One skill; the business type decides the scenarios |
| 2 | Callers | Receivers/consignees, senders/shippers, drivers/delivery agents (inbound callers), business customers |
| 3 | Directions (v1) | Inbound support, outbound delivery updates, outbound pickup and COD calls. Separate Instructions sets. Driver check-ins are v2 (internal staff calls, not customers) |
| 4 | Channel | Voice only in v1 |
| 5 | Languages | English always first; the other languages are chosen by the business (for example Hindi, Kannada, Tamil), same as other industries. Nothing hardcoded |
| 6 | Outbound disclosure | AI disclosure in the welcome; the recording line only if the business records calls, same as other industries |
| 7 | Verification | Tracking or AWB number plus the registered phone number or receiver name before any shipment detail |
| 8 | OTP | Never ask for or accept an OTP of any kind on the call, including the delivery OTP. If a caller starts reading one out, stop them with a fixed line |
| 9 | Promises | No promised delivery time, refund, compensation or claim outcome. ETAs and claim status only from system data |
| 10 | Restricted goods | No advice on whether a dangerous, restricted or prohibited item can ship; hand off to the team |
| 11 | Payment details | Never take card, UPI or PIN details on the call |
| 12 | COD | State the COD amount only from system data. Never take or arrange payment on the call. Payment disputes go back to the seller or bank |
| 13 | Customs | Never advise on duties, documents or clearance times. Customs holds go to the team |
| 14 | Courier scam block | Fake calls such as "your parcel has drugs", "customs or police case", "pay to release the parcel". The agent says we never ask for payment, OTP or details to release a parcel, never confirms or denies the call was from us, and gives the cybercrime helpline 1 9 3 0. If they already paid or shared details, add the bank line. Fixed wording, copied word for word like banking |
| 15 | Emergency block | Road accident, injury, fire at a warehouse or hub, gas or chemical leak. Say "Call 1 1 2 right now." and transfer. No advice |
| 16 | Escalation | Claims, damage, safety, angry callers, hazardous goods, customs holds. "I'll connect you to our team." in the same reply as every transfer |
| 17 | Nobody available | Take a callback (name, number, reason). Say "Our team will call you back." Never promise a time |
| 18 | Data collected | Tracking/AWB number, name, callback number; pickup/delivery address and landmark; parcel description, weight, size and declared value; damage or loss details for a claim (no photos or documents over voice) |
| 19 | Out of scope | The shipment only. Order, product and payment disputes go to the seller or bank |
| 20 | Evals | None (DECISIONS 108). Quality: check_variables, check_fixed_lines, manual /prompt-writer tests on test profiles |
