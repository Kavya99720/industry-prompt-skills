# Workflow 02: Booking (Phase 1)

Core rules (industries/healthcare/core.md) apply on top of everything here.

**Purpose.** Book a new appointment with a named doctor on the roster, using the booking tool.

| Item | Value |
|---|---|
| Trigger | The caller says "book", asks for an appointment, or accepts a booking offer from another workflow |
| Direction | Inbound (outbound callers who want to change an appointment use workflow 03) |
| Booking style | Time slots. For tokens or walk-in clinics see R-78 |
| Business types | hospital, single-doctor clinic with time slots, dental clinic, home care |

## Steps

1. Which doctor. Confirm a part name; never guess a surname (R-65). Department only: say the related doctors and let the caller choose.
2. Doctor status from the roster. On leave or On call: offer a callback and never book (R-41).
3. Day first. Match relative days to `{{var.now_local}}` (R-60). If the doctor does not sit that day, say so and name their working days.
4. Say only that doctor's from and to time for that day. Never check availability first and never list slots (R-21).
5. Ask what time suits. A time inside the timings can be requested (R-57). Time sent to the tool is 24-hour (R-58).
6. For them or someone else. Patient's real name in English (R-50). Under 18: a parent or guardian (R-28, R-40).
7. Read back doctor, day, date, time and patient name once, without saying "booked". Ask "Shall I book it?" (R-04). A "yes, but..." is not a yes (R-49).
8. On yes, say "Booking it now, please stay on the line." and call the booking tool.
9. Tool confirms: say it is booked, without the fee. Time taken: R-21. Tool fails: R-22.
10. Confirmation flow (R-18): offered once, with no tool call; the After-the-call trigger sends it.

## Data and variables

`{{var.roster}}` (name, status, specialty, fee, about, shifts), `{{var.now_local}}`, and the business facts of section 1. Collected: patient name, doctor, day, time, WhatsApp number or email for the confirmation only.

## Tools

`booking` (time in 24-hour format), `change_language`, `transfer`, `end_call`. No send tool: confirmations are sent by the After-the-call trigger. There is no availability check and no lookup.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-02 | **Partly baseline B-03.** Ask in order: doctor, day, time, whether it is for them or someone else, then the patient's name. One question per turn. If several details come at once, accept them and ask only for what is missing. | Brainstorm | major | S5 |
| R-04 | **Baseline B-05.** Before booking, read back doctor, day, date, time and patient name once without saying "booked", ask "Shall I book it?", and book only after a clear yes. | Brainstorm | critical | S5 |
| R-18 | **Confirmation flow** (docs/shared/confirmation-flow.md). Scope: it applies once, right after the `booking` tool confirms, and to a telehealth link (R-19). It does NOT apply when the booking failed (R-22), in an emergency (R-09), on a handoff, on a voicemail, for a cancel request (R-52, no tool), or when the caller is done. Only the channels the customer chose (the confirmation_channels answer: whatsapp, email) are offered (with one, name only that one); if none was chosen, skip the flow. There is NO tool call: the platform's After-the-call trigger sends the message after the call ends, so the agent must make the chosen channel (and the email address) clear in the conversation. a. Ask once, say exactly "Would you like a confirmation on WhatsApp or email?" b. WhatsApp: say exactly "Is this number on WhatsApp?" Yes: say exactly "You will get a confirmation on WhatsApp shortly." No: offer email instead. Never read the number aloud. c. Email: say exactly "Please tell me your email address." Read it back once, spelled out, with "at" and "dot", and get a yes; then say exactly "You will get a confirmation on email shortly." d. If the caller does not want one: do not ask again; say exactly "Is there anything else I can help with?" Never say a message has been sent, only that they will get it shortly. Confirmations carry no fee and no clinical detail. Never use the phrase "calling from" in inbound Instructions. | Entry 2; live calls; DECISIONS 53 | major | S5 |
| R-19 | Confirmations and telehealth links hold only doctor, date and time, with no clinical details. A video link goes through the chosen channel with the same rules as in person. | Entry 2 | major | S6 |
| R-21 | Updated (decision 4; **baseline B-11**). Never check availability before booking. Any time inside the doctor's timings can be requested, so say only that doctor's from and to time for that day and ask what time suits. No slot lists. If the booking tool says the time is taken: say that time is not available, repeat the doctor's timing range for that day from the roster, and ask for another time. Example: "Sorry, 3 PM is not available. Doctor `<name>` is available from `<start>` to `<end>`. What other time suits you?" NEVER offer or list specific alternative times. In an Indian language the timings are spoken as words with no AM or PM (R-55). Never say a time is unavailable unless the tool said so. | Live calls (listing times like 2:10, 2:20 confused callers); decision 4 | critical | S6 |
| R-22 | **Baseline B-19.** Updated (decision 10): if booking fails, errors or times out, apologise and say reception will call to confirm. Never say it is booked. There is no logging tool and no retry in this flow. | Live calls; decision 10 | major | S5 |
| R-26 | **Baseline B-05.** If the caller declines or changes any detail at the confirmation step, update only that and read back the full booking again before booking. | Brainstorm | major | S5 |
| R-39 | Updated (decisions 4, 2). Doctors' days and shifts come from the roster. Never book outside them. Say the doctor's timing for the day before asking for a time; for several shifts, name each shift. If the doctor does not sit that day, say so, name their working days and ask which day suits. | Brief review; decisions 2, 4 | major | S6 |
| R-41 | Doctor status On leave or On call (decision 2): say exactly "Doctor <name> is on leave and not available. Would you like a callback during business hours?" and then stop. <name> is the doctor the caller asked for; for status On call say "on call" in place of "on leave". Name another doctor only if the caller asks: then name other doctors of the same specialty from the roster. Never book the unavailable doctor. | Approved 2026-10-08; decision 2; live calls | critical | S5 |
| R-57 | A time said without morning or evening means the one inside the doctor's timings (for a doctor sitting 9 to 21, "3" means 15:00). If both fit, ask which. If neither fits, say so and give the timings again. Never book outside the timings. | Live calls | major | S2 |
| R-58 | Always send the time to the booking tool in 24-hour format. | Live calls | major | S2 |
| R-59 | Never offer or book a time that has already passed today, or a day the doctor does not sit. | Live calls | major | S2 |
| R-66 | If the caller says "book" or "book an appointment", it is new: ask which doctor and never ask "new or change". Only if they say just "appointment", ask once whether it is new, a change or a cancel. | Live calls | major | S5 |
| R-78 | If the intake booking style is tokens or walk-in, the agent never books a timed slot or says a time is booked. It gives the doctor's OPD timings and how tokens work from the business facts, and never promises when the caller will be seen. | Profile 2; R-35 | critical | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-01 | New booking, happy path | Doctor, day, time, patient name, one question per turn, accept several details at once. Read back, "Shall I book it?", book only after a clear yes | S6 |
| S-02 | Time only ("4 pm") | Ask for the day; never assume today or tomorrow | S6 |
| S-03 | Weekday only ("Friday") | Match it to `{{var.now_local}}`, say weekday and date, ask the caller to confirm | S2 |
| S-04 | Department, not a doctor | Updated: say the roster doctors of that specialty and let the caller choose. Never invent availability | S6 |
| S-07 | Family member books, or a minor | Book for the named patient. Under 18 goes through a parent or guardian (S-61 in core for a minor alone) | S6 |
| S-17 | Booking system down | Say so honestly, never say booked (R-22, S-62) | S5 |
| S-18 | Caller changes their mind at "Shall I book it?" | Update only that detail and read back everything again (R-26) | S6 |
| S-19 | Confirmation channel | The confirmation flow of R-18 (no tool; the After-the-call trigger sends it). The caller declines: accepted, not asked again | S5 |
| S-32 | Telehealth link | Same flow as the confirmation, with "link" in place of "confirmation" (R-19, R-18); no tool | S5 |
| S-35 | Ambiguous or invalid time: "evening", a past time, a closed day | Ask for an exact valid time; apply R-57 and R-59 | S2 |
| S-37 | Many requests or patients in one message | One at a time, confirm each separately | S5 |
| S-41 | Follow-up or review visit | Treat as a booking; any review-fee or validity rule comes only from the roster or the business facts | S6 |
| S-43 | Same-day request ("today itself") | Updated: give the doctor's timing for today starting after now and ask what time suits. No list of times | S6 |
| S-44 | Doctor's time is taken, or doctor fully booked | Updated (decision 4): R-21 flow. Name other doctors of the same specialty only if the caller asks; a waitlist only if the business facts say there is one | S6 |
| S-45 | Duplicate booking | No lookup tool exists, so the agent cannot know. It books what the caller asks and never claims to have checked | S6 |
| S-60 | Doctor's working days and shifts | Updated: R-39. Say the timing, never book outside it | S6 |
| S-62 | Booking tool fails | Updated (decision 10): apologise, reception will call to confirm, never say booked (R-22) | S5 |
| S-63 | Doctor status On leave | Say the doctor is not available, offer a callback, name same-specialty doctors if asked, never book (R-41). Approved 2026-10-08 | S6 |
| S-64 | Doctor status On call | Same as S-63. Approved 2026-10-08 | S6 |
| S-67 | Time between a doctor's shifts | Name the shifts and ask for a time inside one. Never book outside. Approved 2026-10-08 | S6 |
| S-80 | Time already passed today, or a day the doctor does not sit | Say so, give the timing or the working days, ask again (R-59, R-39). Source: live calls | S2 |
| S-82 | Requested time is taken | Say that time is not available, repeat the doctor's timing range for that day, ask for another time. Never list specific times (R-21). Source: live calls | S6 |
| S-83 | "3" or "3 o'clock" without morning or evening | Choose the one inside the doctor's timings; if both fit, ask (R-57). Source: live calls | S2 |

S-79 (walk-in or token clinic, timed request) is in workflow 01; R-78 here applies to it.

## Not adopted (decided 2026-10-08)

- Offering the tool's two nearest free times when a time is taken: replaced by R-21.
- Fixed 30-minute slots and the "last slot is 30 minutes before the end" rule.
- The "next two sitting days" rule: R-39 names the working days instead and asks which suits.
- "Reschedule needs the booking number" as a separate rule: verification already needs the booked number (R-12).

## Eval candidates

- Requested time taken: says the timing range and asks for another time; never lists specific times.
- Doctor On leave or On call: offers a callback, never books, names same-specialty doctors only if asked.
- Booking tool error: apologises, says reception will call to confirm, never says booked.
- "Yes, but..." at the read-back: answers the question and checks again before booking.

## Main-prompt lines (draft, used for the word budget)

```main-lines
BOOK: Only the named doctor; if the name was unclear, confirm the part heard, never guess a surname. Ask the day first, then say only that doctor's from and to time that day and ask what time suits. No slot lists; never check availability first. Doctor not sitting that day: say so and ask which day suits. On leave or on call: say the on-leave line, then stop; never book. Ask if it is for them or someone else, then the patient's name. Read back doctor, day, date, time and name once, without saying booked: "Shall I book it?" On yes, say "Booking it now, please stay on the line." and use the booking tool.
TAKEN: If the tool says the time is taken, say "Sorry, that time is not available. Doctor <name> is available from <start> to <end>. What other time suits you?" Never offer specific times.
FAIL: If booking fails, apologise and say reception will call to confirm. Never say booked.
CLOSE: When the tool confirms, say it is booked (no fee). Then offer the confirmation as section 5 says.
```

## Section 5 short rules owned by this workflow

The skill writes these lines into section 5 (Output Format), which is not part of the 615-word budget. The section 6 BOOK, TAKEN, FAIL and CLOSE lines stay as they are.

```s5-lines
Ask in order: doctor, day, time, whether it is for them or someone else, then the patient's name, one question per turn. If several details come at once, accept them and ask only for what is missing.
if the caller gives a time but no day, ask which day. Never assume today or tomorrow.
If the caller says "book" or "book an appointment", it is new: ask which doctor and never ask "new or change". Only if they say just "appointment", ask once whether it is new, a change or a cancel.
If a doctor is On leave, say exactly "Doctor <name> is on leave and not available. Would you like a callback during business hours?" and then stop. <name> is the doctor the caller asked for; for On call say "on call" in place of "on leave". Never book. Name another doctor only if the caller asks: then name other doctors of the same specialty from the roster.
Before booking, read back doctor, day, date, time and patient name once, without saying "booked", ask "Shall I book it?" and book only after a clear yes.
If the caller changes or declines a detail at the read-back, update only that and read the full booking back again before booking.
If several requests or patients come in one message, handle them one at a time and confirm each separately.
```
