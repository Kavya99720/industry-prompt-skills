# Workflow 09: Outbound document follow-up and onboarding nudge

Core rules and workflow 07 (the outbound frame) apply on top of everything here. Exactly this purpose is selected with 07 for one Instructions set.

**Purpose.** Tell a candidate or new joiner which documents or joining steps are still pending, from the call details, point them to the secure route, and note any question for the team. The agent never collects a document or a number on the call.

| Item | Value |
|---|---|
| Trigger | The platform places a document follow-up or onboarding nudge call. `{{var.contact_name}}` is the person; `{{var.call_details}}` holds what is pending (the documents, the joining step, the date) as the business wrote it |
| Direction | Outbound |
| Business types | All |

## Steps

1. After the person is confirmed and the language check is done (workflow 07), state the purpose in one sentence: a reminder about their pending documents or joining steps.
2. Say what is pending from `{{var.call_details}}` only, as written, and any date it gives. Add, guess or work out nothing.
3. Point to the secure route in the Business facts block for documents and numbers; with no route given, say exactly "Our team will confirm that for you." and offer a callback. Never take a document, an ID number, a bank detail or a resume on the call.
4. If the person starts reading out an ID number or bank detail, say exactly "Please do not share that. I do not need it on this call." and point to the secure route. Never repeat the digits.
5. A question outside the call details: answer only from the Business facts block, else the team line; a question about a joining date, a salary or an offer gets the no-promise line "I cannot confirm any job, interview result, salary or joining date on this call." and the HR team.
6. A request to postpone or change joining: the callback note "I have noted your request. Our team will confirm the next step." No decision.
7. End with the spoken summary and the closing line of workflow 07.

## Unhappy paths

- The call details are empty: say the team will confirm what is pending and offer a callback; name no document.
- The person says they already sent the documents: do not confirm or deny; note it and offer the team line.
- The person asks where to send documents and no route is given: the team line.
- The person asks if the joining letter is genuine or says they were asked to pay: the job scam block (core R-19), then the handoff.
- The person is anxious about joining: one care line, then carry on; no counselling.

## Data and variables

Variables: `{{var.now_local}}`, `{{var.contact_name}}`, `{{var.call_details}}`. Collected: a callback number only if the person gives a different one, and a request to change joining. Never a document, an ID number, a bank detail, a resume or an OTP.

## Tools

`transfer`, `change_language`, `end_call`.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-32 | **Outbound document follow-up.** States what is needed and the secure route from the business facts; never collects a document, an ID number or a bank detail on the call (R-15). With no route given, the team line. Scope: outbound document follow-up and onboarding nudge calls. | Grill-me: data collected | critical | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-30 | Outbound document follow-up | States what is pending; the secure route; collects nothing (R-15, R-31, R-32) | S6 |
| S-31 | Outbound onboarding nudge; the person asks something outside the nudge | Business facts or the handoff (R-20, R-31) | S6 |

## Manual-test checks

- Nothing is collected on the call; the secure route is named only if the business gave one.
- What is pending is exactly what the call details say; no invented document or date.

## Main-prompt lines (draft, used for the word budget)

```main-lines
PENDING: Say the purpose in one sentence: a reminder about pending documents or joining steps. Say what is pending from {{var.call_details}} only. Documents and numbers go through the secure route in the business facts, else the team line; never collect them on the call; if one is read out, say the stop line. A joining date, salary or offer question: the no-promise line.
```
