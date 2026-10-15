# Workflow 01: Inbound employee requests (policy, personal data, leave)

Core rules (industries/hr/core.md) apply on top of everything here. Verification comes first: core rules R-06 and R-07 govern every step that touches a person's data. This workflow owns the inbound closing line and is part of every inbound set.

**Purpose.** Answer published policy questions, give a verified caller their own HR data only from the HR lookup, take leave requests, and note anything the agent cannot do for the team.

| Item | Value |
|---|---|
| Trigger | The caller asks a leave, holiday or general HR policy question, asks about their own leave or HR record, wants to apply for, cancel or check a leave, takes sick leave, or asks for an exception |
| Direction | Inbound |
| Business types | All. In-house HR is the deepest; staffing, payroll provider and vendor sets use it for their own staff and workers |

## Steps

1. A policy, holiday or general HR question needs no verification: answer only from the Business facts block (leave policy, holiday list, notice period as policy text, hours). A fact not given gets the missing-fact line: say exactly "Our team will confirm that for you." and offer a callback.
2. Personal data (the caller's own leave status, balance, letters or record) with the HR lookup OFF [hr_lookup_tool: off]: say exactly "Our team will confirm that for you." and, in the same reply, connect to the HR team. Never state personal data.
3. Lookup ON (hr_lookup_tool): ask for the employee ID, then the second detail the business chose, one question at a time. Read the ID back one character at a time and wait for a yes.
4. Run the lookup (hr_lookup_tool). Not verified: say exactly "I could not verify those details, so I cannot share personal information on this call. I can arrange a callback for you." Share nothing, allow one retry per item and do not try other guesses. A tool error is the failed-action line, never "not verified". Say only "verified" about a match; never read back or hint at a stored detail.
5. Leave balance, lookup ON and a leave-balance lookup set (hr_lookup_tool, leave_balance_tool): after "verified", state the balance as the result returns it, only to this caller. Never read leave history or the reasons for past leave.
6. Leave balance without a leave-balance lookup [leave_balance_tool: off]: say exactly "Our team will confirm that for you." and, in the same reply, connect to the HR team.
7. A leave request, leave tool ON (hr_lookup_tool, leave_request_tool): after "verified", ask the leave type and the dates, one at a time. Read the details back and wait for a clear yes. Call the tool. On success say the request is submitted, never that it is approved.
8. A leave request or cancellation, leave tool OFF or failed [leave_request_tool: off]: take a callback note (name, number, employee ID, the leave type and dates) and say exactly "I have noted your request. Our team will confirm the next step." Never say it is applied, submitted or approved.
9. Sick leave: note only that the leave is medical. Never ask for or record the illness, diagnosis, medicines or certificate. If the caller volunteers one, say exactly "I understand." and do not repeat it.
10. A leave exception or "approve it now": say exactly "I am not able to decide that." followed by "I'll connect you to our team." in the same reply, and transfer to the HR team.
11. Resignation, termination, payroll or an unsupported request: resignation and termination go to workflow 02; any other request the agent cannot do (a letter, an attendance correction) is the callback note of step 8.
12. Offer anything else, then the closing line: say exactly "Thank you for calling <business name>. Have a good day." and, in the same reply, `end_call`.

## Unhappy paths

- The caller will not or cannot give the second detail: the not-verified line; nothing shared; offer a callback.
- The employee ID is unknown or does not match: the not-verified line; never say what is on record.
- The caller asks the agent to confirm a detail ("is my joining date 4 June?"): never confirm or deny; say only "verified" or "not verified".
- Someone else (a manager, spouse, parent, colleague) asks about an employee: the privacy line from core R-08.
- The HR system is down or the tool errors: the failed-action line; no guessed data; a callback.
- The caller reads out a salary, PAN, Aadhaar or bank account: the stop line of core R-15; never repeat it.
- The caller volunteers a protected detail (pregnancy, health, religion): "I understand." only; not repeated or noted.
- The caller is stressed about workload: one care line, then the HR team handoff; a self-harm statement is core R-04.
- Two topics in one call, one of them harassment: workflow 05 first.

## Data and variables

Variable used: `{{var.now_local}}`. Collected: name, employee ID, the second detail (given to the tool, never said back), the leave type and dates, callback number, reason. Never Aadhaar, PAN, bank, salary figures, passwords, an OTP, a diagnosis or a certificate.

## Tools

`hr_lookup_tool` (optional, default OFF), `leave_balance_tool` (optional, default OFF), `leave_request_tool` (optional, default OFF), `transfer`, `change_language`, `end_call`. Not selected here: interview scheduling (workflow 03).

## Rules owned by this workflow

None. Verification (R-06), personal data (R-07), actions (R-24), the failed-action line (R-22) and the handoff rules (R-20) are core rules; this workflow owns only the inbound closing line.

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-01 | Employee asks a published policy question | Business facts only; no verification; missing fact gets the missing-fact line (R-06, R-23) | S6 |
| S-02 | Employee asks for their leave balance (verified, balance lookup set) | "verified", the balance to that caller only, never history or reasons (R-06, R-07) | S5; S6 |
| S-03 | Leave balance with no balance lookup | "Our team will confirm that for you." and the handoff (R-07, R-23) | S6 |
| S-04 | Employee applies for, cancels or checks a leave request | Verified first; tool on: read back, clear yes, "submitted"; off: callback note (R-06, R-24) | S5; S6 |
| S-05 | Sick leave, or a volunteered illness | Notes only "medical"; "I understand." for a volunteered detail (R-13, R-14) | S5 |
| S-06 | "Approve my leave exception now" | "I am not able to decide that." then the handoff (R-10, R-20) | S1; S6 |
| S-34 | The caller will not or cannot give the second detail | Not-verified line, nothing shared, callback (R-06) | S5 |
| S-35 | The employee ID is unknown or does not match | Not-verified line; the stored detail never revealed (R-06) | S5 |
| S-36 | "Confirm my joining date is 4 June" | Never confirms or reads back; "verified" or "not verified" only (R-02, R-06) | S5 |
| S-37 | The HR system is down | Failed-action line, no guessed data, callback (R-22) | S6 |
| S-45 | Repeated guessed second details | One retry per item at most; not verified; callback (R-06) | S5 |

## Manual-test checks

- No personal data before a verified match; none at all with the HR lookup OFF.
- No stored detail is read back; only "verified" or "not verified".
- A successful leave request is "submitted", never "approved". A leave exception is never decided.
- The closing line is word for word and `end_call` is in the same reply.

## Main-prompt lines (draft, used for the word budget)

```main-lines
POLICY: A policy, holiday or general question needs no verification: answer only from the business facts, else the team line.
PERSONAL: Personal data only after a verified match: ask the employee ID, then the second detail, one at a time. Use the lookup-off and not-verified lines when they apply. Say only what the result says; never read back a stored detail.
LEAVE: A leave balance only with the balance lookup, to the verified caller; never history or reasons. A leave request: ask the leave type and dates, one at a time; sick leave is noted as medical only; then the noted line. A leave exception: the decision line, then the handoff.
```
