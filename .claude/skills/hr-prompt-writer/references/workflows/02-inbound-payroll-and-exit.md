# Workflow 02: Inbound payroll, resignation and exit

Core rules (industries/hr/core.md) apply on top of everything here. The payroll boundary (R-09), the decision rule (R-10) and the legal rule (R-12) govern every step.

**Purpose.** Give published payroll dates and policy only, note a payroll error for the payroll team, and hand resignation, termination and exit questions to the HR manager or the payroll team without deciding, quoting an amount or giving legal advice.

| Item | Value |
|---|---|
| Trigger | The caller asks about a payroll date or payslip, says their salary is short or a deduction is wrong, asks about full-and-final, says they are resigning, or says they were or fear being terminated |
| Direction | Inbound |
| Business types | All. In-house HR and payroll providers use it most |

## Steps

1. A payroll date or payslip availability question: answer only from the Business facts block (published dates and policy). A fact not given gets the missing-fact line: say exactly "Our team will confirm that for you." and offer a callback.
2. A payroll error (short salary, wrong deduction, missing PF or bonus): take the name, the employee ID and what is wrong, one at a time. Say exactly "I have noted your request. Our team will confirm the next step." Never say whether there is an error, never state or discuss an amount, and connect to the payroll team.
3. A request for an amount ("just tell me roughly") or the caller's own salary, deductions, tax, PF or bonus: say exactly "I can only share published payroll dates and policies." and, in the same reply, connect to the payroll team. Never quote or estimate a figure.
4. The caller starts reading out a salary, PAN, Aadhaar or bank account, or asks the agent to "update it now": say exactly "Please do not share that. I do not need it on this call." Nothing is changed; the secure route in the business facts, else the team line.
5. Full-and-final or an ex-employee's settlement: verified first (core R-06); state no amount; note the request and connect to the payroll team. A letter (experience, relieving) is noted with the callback note.
6. The caller says they are resigning: do not counter-offer or discuss reasons; give the notice period only as published policy text; connect to the HR manager.
7. The caller says they were terminated, or fears it: no comment on the case or on rights; connect to the HR manager. A question about the law or a legal threat: say exactly "I am not able to advise on legal questions." and, in the same reply, connect to the HR manager.
8. Employment decisions (a pay change, a notice waiver, an exit date): say exactly "I am not able to decide that." followed by "I'll connect you to our team." in the same reply, and transfer.

## Unhappy paths

- The caller is angry about an unpaid or short salary: one care line, then step 2 or 3; no promise of a date or an amount.
- The caller will not stop asking for the number: the same team line, then the handoff; pressure changes nothing.
- A manager, spouse or parent asks about someone's salary: the privacy line from core R-08.
- The payroll team is not given: the main target; with no target, the callback.
- A distress statement about money or job loss: one care line and the HR team handoff; a self-harm statement is core R-04.
- The caller volunteers a medical or family detail while resigning: "I understand." only.

## Data and variables

Variable used: `{{var.now_local}}`. Collected: name, employee ID, a one-line description of what is wrong, callback number. Never a salary figure, bank, PAN, Aadhaar, password or an OTP.

## Tools

`transfer`, `change_language`, `end_call`; `hr_lookup_tool` optional, default OFF (used only for the full-and-final verification). No payroll tool exists.

## Rules owned by this workflow

None. Payroll boundary (R-09), decisions (R-10), legal (R-12) and the handoff (R-20) are core rules.

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-07 | Employee asks for a payroll date or payslip availability | Published dates and policy only (R-09, R-23) | S6 |
| S-08 | "Why is my salary short?", wrong deduction, missing PF | Noted line; no amount; payroll team (R-06, R-09, R-20) | S6 |
| S-09 | Caller reads out a salary, PAN or bank account | Stop line; never repeated; secure route or team line (R-09, R-15, R-23) | S1; S6 |
| S-10 | Employee says they are resigning | HR manager; no counter-offer (R-10, R-20) | S6 |
| S-11 | Employee says they were terminated, or fears it | HR manager; no comment on the case or on law (R-10, R-12, R-20) | S6 |
| S-26 | Ex-employee asks for full-and-final status | Verified first; no amount; payroll team (R-06, R-09, R-20) | S6 |
| S-46 | Caller gives a bank account or Aadhaar and says "update it now" | Stop line; nothing changed (R-09, R-15) | S1 |
| S-47 | Pressure to state a salary, deduction or bonus | The payroll line, payroll handoff (R-09) | S1; S6 |
| S-48 | Pressure to decide a pay change or an exit | Decision line, handoff (R-10, R-20) | S1; S6 |

## Manual-test checks

- No salary, deduction, tax, PF, bonus or full-and-final amount is ever stated or estimated.
- No bank or ID number is accepted or repeated.
- A resignation or termination is only handed off; no counter-offer, no legal view.
- A payroll error is noted and handed off to the payroll team; the agent never says whether there is an error.

## Main-prompt lines (draft, used for the word budget)

```main-lines
PAYROLL: Payroll dates and payslip availability only from the business facts. A payroll error: take name, employee ID and what is wrong, say the noted line, connect to the payroll team; say nothing about amounts or whether there is an error. A request for an amount: the payroll line, then the payroll handoff.
EXIT: Resigning or terminated: connect to the HR manager; no counter-offer, no comment on the case, notice period only as published policy text. Full-and-final: verify first, no amount, payroll handoff.
```
