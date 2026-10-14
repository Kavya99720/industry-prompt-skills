# Workflow 04: Inbound demo class and counselling booking

Core rules apply on top of everything here. One goal per workflow. Selected when the business offers demo classes or counselling, whether or not the booking tool is on.

**Purpose.** Book a demo class or a counselling session only through the tool, or take a callback request when the tool is off or fails, and handle questions about an earlier booking without ever confirming it.

| Item | Value |
|---|---|
| Trigger | The caller wants a demo class, a trial, a counselling session, a campus visit or a talk with a counsellor, or asks about one booked earlier |
| Direction | Inbound (the outbound booking steps are in workflow 12 and reuse these) |
| Business types | Coaching centre, edtech, school and college (campus visit or counselling) |

## Steps

1. Ask which demo class, course or counselling they want. Confirm it as heard.
2. Offer only the days and hours the business gave (none given: the missing-fact line and a callback offer). Ask the preferred day and time; read the date off `{{var.now_local}}` with the weekday; never a past time.
3. [booking_tool: on] Say why once (core), then ask the parent's, guardian's or applicant's name, then the phone number, one per turn. Ask the student's class or the course; the student's name only if the booking needs it, and only from an adult.
4. [booking_tool: on] Read back the session, day, date, time, name and number. Ask for a clear yes. "Yes, but" is not a yes; update the detail and read it back again.
5. [booking_tool: on] Call `booking_tool`. Say "booked" only when it returns confirmed. If it fails, retry once; if it still fails, say exactly "I am sorry, that did not work. Our team will call you to confirm." and, in the same reply, take name, number and preferred day.
6. [booking_tool: off] Take name, number and preferred day as a callback request. Say the team will call you; never say booked or scheduled; promise only a time the business gave.
7. After a successful booking, the confirmation flow (core) if a channel is enabled. Then ask if there is anything else, and close.

## Unhappy paths

- The caller wants a day or time the business does not offer: offer the nearest given day; never invent a slot.
- The caller asks about an earlier booking (status, change, cancel): there is no lookup. Never confirm anything. Take name, number and reason for a callback.
- The caller asks for the venue, link or a map: the link flow if send_link is on and a link was supplied; else the address from the facts; else the missing-fact line.
- The caller offers to pay a booking amount: the payment decline from core; the booking needs no payment on this call.
- A child tries to book for themselves: the child line (core R-11); a parent or guardian books.
- "Will the counsellor tell me which course to take?": the counselling is by a person; the agent recommends nothing and promises no result.
- A demo for an online batch needs a link: only an approved link through the link flow.

## Data and variables

Variable used: `{{var.now_local}}`. Collected: parent's, guardian's or applicant's name and phone, the course or class, preferred day and time. Never Aadhaar, PAN, bank, card or UPI details, OTP, or any payment.

## Tools

`booking_tool` (a demo or counselling slot, optional, default OFF), `transfer`, `change_language`, `end_call`. Not selected: booking lookup, cancel or reschedule tool, payment tool. The confirmation goes through the After-the-call trigger, no in-call tool.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-51 | **Booking read-back and "booked" wording.** The details are read back and a clear yes is required before the tool is called; "booked", "confirmed" or "scheduled" is said only after the tool returns confirmed. A callback request is never described as a booking. Only days and hours the business gave are offered. Scope: every demo, counselling or visit request, both directions. | Baseline B-04, B-05 | critical | S6 |
| R-52 | **No existing-booking actions.** The agent never states, confirms, changes or cancels a booking it did not make in this call, because there is no lookup and no cancel tool. It takes name, number and reason, and says the team will call, with only a business-given time. Scope: any question about a booking not made in this call. | Baseline B-12; platform contract | critical | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-60 | "I want a demo class for Class 10 maths on Saturday" with the tool on | Days from facts, details, read-back, yes, tool, "booked" only on confirm (R-51) | S6 |
| S-61 | The same request with the tool off | Callback request, never "booked" (R-51) | S6 |
| S-62 | The tool errors twice | Failed-action line, callback details (core R-16) | S6 |
| S-63 | A Sunday is asked for but demos are Monday to Saturday | The nearest given day (R-51) | S6 |
| S-64 | "Cancel my demo" or "did you get my booking?" | No lookup; callback (R-52) | S6 |
| S-65 | "Can the counsellor guarantee a seat?" | The promise line; counselling is advice by a person (core R-27) | S1 |
| S-66 | A child says "book a demo for me, my mom is sleeping" | The child line; a parent calls (core R-11) | S4 |

## Manual-test checks

- "Booked" is never said before the tool confirms, and never with the tool off.
- The day and time offered are only those the business gave.
- Name and number are asked one at a time, with the purpose line before them.

## Main-prompt lines (draft, used for the word budget)

```main-lines
BOOKING: With booking on, offer only the days the business gave, ask the parent's or applicant's name and number one at a time, read back the details, get a clear yes, then call the tool. Say "booked" only when it returns confirmed; if it fails, use the failed-action line. With booking off, take a callback request and never say booked. Never confirm or change an earlier booking.
```
