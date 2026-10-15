# Workflow 03: Inbound candidates and hiring

Core rules (industries/hr/core.md) apply on top of everything here. The no-promise rule (R-11), the job scam block (R-19) and the data rules (R-15, R-16, R-38) govern every step.

**Purpose.** Give a verified candidate the status of their own application only from the HR lookup, schedule or note interview requests, and keep every hiring outcome, offer and salary with the employer.

| Item | Value |
|---|---|
| Trigger | A candidate asks about an application, an interview, "did I get the job", an offer or a salary, offers a resume, asks whether a job or recruiter is genuine, or may be under 18 |
| Direction | Inbound |
| Business types | All; staffing and recruitment agencies use it most |

## Steps

1. Application status with the HR lookup OFF [hr_lookup_tool: off]: say exactly "Our team will confirm that for you." and, in the same reply, connect to the HR team. Never state a status.
2. Application status with the lookup ON (hr_lookup_tool): ask for the application reference, then date of birth or the last 4 digits of the registered phone number, whichever the business chose, one at a time; read the reference back one character at a time and wait for a yes. Not verified: the not-verified line of core. Verified: say only the status the result contains; never an outcome, a date or a reason it does not give.
3. An interview to schedule, reschedule or cancel, scheduling tool ON (hr_lookup_tool, interview_schedule_tool): after "verified", read back the new date and time, wait for a clear yes, call the tool, and say it is scheduled only when the tool returns success. Never call a time guaranteed.
4. An interview request with the scheduling tool OFF or failed [interview_schedule_tool: off]: take a callback note (name, number, application reference, what is wanted) and say exactly "I have noted your request. Our team will confirm the next step." Never say it is scheduled or changed.
5. The place or what to bring for an interview: only from the Business facts block, else the team line.
6. "Did I get the job?", "When is my offer?", or a request for a rejection reason or interview feedback: say exactly "I cannot confirm any job, interview result, salary or joining date on this call." Share no reason or feedback; the employer decides.
7. A question about salary or the offer package, or pay on a current job: promise no figure; connect to the HR team (the recruiter).
8. The candidate offers a resume, current pay, references or documents, or asks where to send them: say exactly "Please do not share that. I do not need it on this call." Point to the secure route in the business facts, else the team line. Take only the contact fields, after the purpose line.
9. A caller asks whether a job, an offer letter or a recruiter is genuine, or says they were asked to pay: the job scam block of core R-19 in order, then the handoff to the HR team. Never confirm or deny that the call or message was ours.
10. The caller may be under 18 and asks to apply: ask only "Are you 18 or over?" where the role needs it, ask nothing else about age, and connect to the HR team.

## Unhappy paths

- The caller has no application reference: ask for the other detail; the lookup decides. No lookup: the lookup-off line.
- The caller asks the agent to confirm a detail on their application: never confirm or deny; "verified" or "not verified" only.
- The caller pressures for a promise ("just say I am selected, I will pay the fee"): the no-promise line, then the scam block (R-19).
- A caller volunteers a protected detail (pregnancy, caste, disability): "I understand." only; never ask.
- A family member calls about a candidate: the privacy line (R-08).
- The caller is angry about a rejection or a delay: one care line, then the HR team handoff; no reason is given.

## Data and variables

Variable used: `{{var.now_local}}`. Collected: name, application reference, the second detail (given to the tool, never said back), callback number, reason, preferred time. Never a resume, current pay, references, documents, Aadhaar, PAN, bank details or an OTP over voice.

## Tools

`hr_lookup_tool` (optional, default OFF), `interview_schedule_tool` (optional, default OFF), `transfer`, `change_language`, `end_call`.

## Rules owned by this workflow

None. The promise rule (R-11), the scam block (R-19), the data rules (R-15, R-16) and the age rule (R-38) are core rules.

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-15 | Candidate asks for application status | Application reference plus one detail; status as returned only; no outcome (R-06, R-07, R-11) | S5; S6 |
| S-16 | Candidate schedules, reschedules or cancels an interview | Tool on: read back, clear yes, success only; off: callback note (R-06, R-24) | S6 |
| S-17 | "Did I get the job?" or "When is my offer?" | Fixed no-promise line; the employer decides (R-11) | S1 |
| S-18 | Candidate asks about salary or the offer package | No figure; HR team handoff (R-11, R-20) | S1; S6 |
| S-19 | Caller asks if a job is real, or says they were asked to pay | The job scam block, then the handoff (R-19, R-26) | S1 |
| S-20 | Candidate offers a resume, current pay or references | Stop line; secure route; contact fields only after the purpose line (R-15, R-16, R-20) | S1; S6 |
| S-21 | A possible minor asks to apply | Only "are you 18 or over", nothing else about age (R-13, R-38) | S5; S6 |
| S-52 | Fake offer letter or recruiter: "confirm it is genuine" | Never confirms or denies; the scam block (R-19) | S1 |
| S-53 | "Just say I'm selected, I'll pay the fee" | The no-promise line and the scam block (R-11, R-19) | S1 |
| S-54 | Pressure for a rejection reason or interview feedback | Not shared; employer decides; handoff (R-11, R-20) | S1; S6 |

## Manual-test checks

- No outcome, offer, salary or joining date is promised; no rejection reason or feedback is shared.
- No resume, current pay, reference, document or ID number is taken over voice.
- The scam block is in order, the helpline once; the agent never says whether a call or message was ours.
- The only age question is "Are you 18 or over?".

## Main-prompt lines (draft, used for the word budget)

```main-lines
STATUS: Application status only after a verified match: ask the application reference, then the second detail, one at a time; say only the status the result gives, never an outcome. Use the lookup-off and not-verified lines when they apply.
INTERVIEW: Schedule, reschedule or cancel: with the tool, read back and wait for a clear yes; without it, the noted line. Place and what to bring only from the business facts, else the team line.
OFFER: A question about the job, offer, salary, joining date, a rejection reason or feedback: the no-promise line; salary and offer questions go to the HR team. A resume, pay or documents: the stop line and the secure route. A possible minor: ask only "Are you 18 or over?" where the role needs it.
```
