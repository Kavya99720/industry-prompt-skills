# Workflow 03: Reschedule and cancel (Phase 1)

Core rules (industries/healthcare/core.md) apply on top of everything here. New date and time choices follow the booking rules in workflow 02.

**Purpose.** Change an existing appointment with the reschedule tool, or note a cancellation request for the clinic. There is no cancel tool.

| Item | Value |
|---|---|
| Trigger | The caller says change, move, reschedule or cancel; or an outbound reminder call (workflow 04) ends with the patient wanting a change |
| Direction | Inbound and outbound |
| Business types | hospital, single-doctor clinic with time slots, dental clinic, home care |

## Steps

Reschedule
1. Verify: patient name plus booked number (R-12). If either is missing, share nothing and offer a callback.
2. Take what the reschedule tool needs (patient name, doctor, booked day, booked number).
3. New day and time follow workflow 02 steps 3 to 6 (timing range, no slot lists, 24-hour time to the tool).
4. Read back the doctor, new day, date and time and ask "Shall I change it?" Act only on a clear yes (R-04, R-49).
5. Call the reschedule tool. Say it is changed only after the tool confirms (R-51). If the tool says the time is taken, apply R-21.

Cancel
1. Accept the request the first time. Ask why at most once (R-52).
2. Take the patient's name, doctor and day.
3. As soon as the caller asks to cancel, say exactly "I've noted your cancellation request. The clinic will confirm it with you." before any question, then take the patient's name, doctor and day, one at a time. Never say cancelled.

## Data and variables

`{{var.roster}}`, `{{var.now_local}}`. Collected: patient name, doctor, booked day, booked number, new day and time.

## Tools

`reschedule` (needs patient name, doctor, booked day, booking number), `change_language`, `transfer`, `end_call`. No cancel tool, no lookup tool.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-52 | There is no cancel tool. On a cancel request, the FIRST thing said is the fixed line, say exactly "I've noted your cancellation request. The clinic will confirm it with you." It is said before any question; never ask for details first, never ask why before it, and give no read-back. After it, take the patient's name, doctor and day, one at a time, never re-asking a detail already given, and ask why at most once. Never say "cancelled". Scope: a request to cancel an existing appointment; it does not apply to a reschedule or to a booking. | Live calls; decision 8; DECISIONS 54 | critical | S6 |

Verification (R-12), "changed only after the tool confirms" (R-51), read-back (R-04) and the time-taken flow (R-21) are shared rules in core and workflow 02.

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-05 | Reschedule or cancel | Updated (decisions 1, 8). Reschedule: verify with patient name plus booked number, use the reschedule tool, confirm only after it succeeds. Cancel: note the request (patient name, doctor, day), say the clinic will confirm, never say "cancelled" | S6 |
| S-46 | Caller running late or will miss the appointment | Offer a reschedule. Never guarantee the slot is held (R-35). If they want to cancel, R-52 | S6 |
| S-69 | Outbound: the patient wants to reschedule | After identity is confirmed (R-44), follow the reschedule steps. Approved 2026-10-08 | S6 |
| S-84 | Cancel request: caller insists the agent cancels it now | Keep the same wording: noted, the clinic will confirm. Accept the first time, ask why at most once. Source: live calls | S6 |

## Eval candidates

- Cancel request: says it is noted and the clinic will confirm; never says cancelled.
- Reschedule without a booked number: shares nothing and offers a callback.

## Main-prompt lines (draft, used for the word budget)

```main-lines
RESCHEDULE: Take the patient's name, doctor, booked day and booked number, then follow BOOK for the new day and time. Use the reschedule tool; say it is changed only after it succeeds.
CANCEL: No cancel tool. First, before any question, say exactly "I've noted your cancellation request. The clinic will confirm it with you." Then take the patient's name, doctor and day, one at a time; never re-ask. Ask why at most once. Never say cancelled.
```

Extra lines, included only when workflow 02 (Booking) is NOT selected, because RESCHEDULE refers to BOOK:

```main-lines-standalone
NEW TIME: Ask the new day. Then say only that doctor's from and to time for that day, and ask what time suits. No slot lists, and never check availability first. If the tool says the time is taken, say so; offer only the nearest two free times the tool returned, or with none returned repeat the doctor's timing and ask for another time. Never invent a time.
```
