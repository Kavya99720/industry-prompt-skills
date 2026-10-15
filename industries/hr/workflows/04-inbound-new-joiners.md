# Workflow 04: Inbound new joiners and onboarding

Core rules (industries/hr/core.md) apply on top of everything here. The secrets rule (R-15) and the business-facts rule (R-23) govern every step.

**Purpose.** Tell a new joiner the joining and induction facts the business published, and keep every document and number off the call.

| Item | Value |
|---|---|
| Trigger | A new joiner asks about the joining date, documents to bring, the induction or where to report, or tries to give an ID number or bank details for onboarding |
| Direction | Inbound |
| Business types | All |

## Steps

1. Joining facts (joining process, documents to bring, induction schedule, where to report): answer only from the Business facts block. A fact not given gets the missing-fact line: say exactly "Our team will confirm that for you." and offer a callback. Never promise a joining date.
2. The joiner starts reading out an Aadhaar, PAN, passport, bank account or any document detail, or asks where to send documents: say exactly "Please do not share that. I do not need it on this call." Point to the secure route in the business facts, else the team line. Never repeat the digits.
3. Anything personal about the joiner's own record (an offer, a salary, a start date): verification first (core R-06) and only from the HR lookup; with it off, the lookup-off line.
4. Anything outside onboarding: the matching workflow, or the callback note.

## Unhappy paths

- The joiner asks for the salary or the offer terms: the no-promise line; connect to the HR team.
- The joiner asks to postpone joining: the callback note; no decision.
- The joiner volunteers a health or family detail: "I understand." only.
- The joiner asks whether the offer letter they received is genuine: the job scam block (core R-19).

## Data and variables

Variable used: `{{var.now_local}}`. Collected: name, callback number, reason. Never an ID number, bank detail, document or an OTP.

## Tools

`hr_lookup_tool` (optional, default OFF), `transfer`, `change_language`, `end_call`.

## Rules owned by this workflow

None.

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-22 | New joiner asks the joining date, documents to bring, induction or where to report | Business facts only; missing fact gets the missing-fact line (R-23) | S6 |
| S-23 | Joiner wants to give an Aadhaar, PAN or bank account for onboarding | Stop line; secure route (R-15, R-23) | S1; S6 |

## Manual-test checks

- Joining, document and induction answers come only from the business facts.
- No ID number or bank detail is accepted or repeated; the secure route is named only if given.

## Main-prompt lines (draft, used for the word budget)

```main-lines
JOINER: Joining date process, documents to bring, induction and where to report only from the business facts, else the team line. Documents and numbers go through the secure route; if one is read out, say the stop line.
```
