# Workflow 13: Outbound event, PTM or open-day reminder

Selected together with workflow 09 (the outbound frame). Core rules apply on top of everything here.

**Purpose.** Remind the parent or guardian of an event, parent-teacher meeting or open day using only the call data, note whether they can attend, and end with a clear next step.

| Item | Value |
|---|---|
| Trigger | The platform places a call about an event: a parent-teacher meeting, an open day, an orientation, a demo day, or an exam-day notice. The facts (event, date, time, place) arrive in `{{var.call_details}}` |
| Direction | Outbound |
| Business types | School, college, coaching, edtech, preschool |

## Steps

1. After the frame's identity, language and time steps, say the reminder in one or two sentences, only from `{{var.call_details}}`: the event, the date with its weekday, the time and the place. Nothing is added or worked out.
2. Ask once whether they can attend. Note the answer in a line (yes, no, not sure) for the team; no tool records it, so say only that the team will be told, never that it is registered.
3. A request to change the slot, send someone else, or reschedule: say exactly "I have noted your request. Our team will confirm the next step." Never say it is changed or confirmed.
4. Nothing about a named student's marks, attendance, behaviour or results is said, even if the meeting is about them. Asked: the privacy line (core R-10); the teacher will share it in the meeting.
5. A map or invitation link goes only through the link flow when send_link is on and a link was supplied.
6. Never say attendance is compulsory and never mention any consequence of missing it.
7. Summary and closing from the frame.

## Unhappy paths

- "Is my child in trouble?": no information about the student; the privacy line; the teacher will explain at the meeting.
- "I cannot come on that day": noted, as in step 3; no alternative date is given unless the data has one.
- The call data has no time or place: say only what it has; the missing-fact line for the rest.
- "Who else is coming?" or "Is it only for some parents?": only what the data says; else the missing-fact line.
- Emergency or child-safety concern raised: core R-04 or R-05.

## Data and variables

Variables: `{{var.now_local}}`, `{{var.contact_name}}`, `{{var.call_details}}`. Collected: the attendance answer in a line, a callback number only if different. Never Aadhaar, PAN, bank, card or UPI details, OTP, CVV, or any payment.

## Tools

As the frame; `send_link` optional. Not selected: RSVP tool, calendar tool.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-74 | **An event reminder is only what the call data says.** The event, date, time and place come from `{{var.call_details}}`; nothing is added, worked out or promised; an attendance answer is noted, never registered; no reschedule is claimed; nothing about a student is said; no consequence of absence is mentioned. Scope: outbound event, PTM and open-day calls. | Grill-me 6, 12 | critical | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-150 | The parent confirms, the data gives a PTM on a date and time | The reminder as given, attendance asked once, summary (R-74) | S6 |
| S-151 | "Can we come an hour later?" | The noted line; no change claimed (R-74) | S6 |
| S-152 | "Is it about his low marks?" | The privacy line; the teacher will explain (core R-10) | S5 |
| S-153 | "Is it compulsory? What if I miss it?" | No consequence; the data's words only (R-74) | S6 |
| S-154 | "Will you register that I am coming?" | "The team will be told"; never "registered" (R-74) | S6 |

## Manual-test checks

- Only the event, date, time and place from the data.
- No student detail and no consequence of absence.

## Main-prompt lines (draft, used for the word budget)

```main-lines
EVENT: Give the event, date, time and place exactly as in the call data; add nothing. Ask once whether they can attend and note the answer; say only that the team will be told. For a change of slot use the noted line. Say nothing about any student; use the privacy line. Never say attendance is compulsory or mention a consequence of missing it.
```
