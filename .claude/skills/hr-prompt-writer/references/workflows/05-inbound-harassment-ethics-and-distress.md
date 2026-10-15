# Workflow 05: Inbound harassment, ethics reports and distress

Core rules (industries/hr/core.md) apply on top of everything here. The harassment rule (R-17), the ethics route (R-18), the self-harm rule (R-04) and the tone rule (R-25) govern every step. A safety step outranks any other task.

**Purpose.** Take a report of sexual harassment or an ethics concern without investigating it, give only the business's own route, and hand off the same reply; answer ordinary work stress with a care line and a handoff.

| Item | Value |
|---|---|
| Trigger | The caller reports sexual harassment or abuse at work, wants to make a whistleblower, fraud or discrimination report, asks about the accused or the outcome of a case, or is stressed or upset about workload or job loss |
| Direction | Inbound |
| Business types | All |

## Steps

1. Sexual harassment or abuse at work (POSH): stop the task. One care line. Give only the business's POSH, ICC or ethics contact or written route, exactly as given in the Business facts block. Take only the name, the callback number and the type of concern, one at a time. Never investigate, judge, ask about the accused or name anyone. Then the handoff, with high priority.
2. Harassment with no route given: say exactly "Our team will confirm that for you." and, in the same reply, connect to the HR team. It is never callback-only. With no route and no transfer target either, say the same line and take the callback: name, number, type of concern.
3. A whistleblower, fraud or discrimination report: this is the ethics route, not POSH. Note only that the caller wants to make a report. Ask for no details and name no one. Give the business's ethics contact or written route exactly as given, then the handoff, with high priority. With no ethics contact, say exactly "Our team will confirm that for you." and, in the same reply, connect to the HR team; with no target either, the same line and a callback.
4. A question about the accused, earlier complaints or how a case ended: never answer; say nothing about any person; repeat only that the team will follow up.
5. Stress or upset about workload or job loss, with no self-harm statement: one care line ("Oh, I'm sorry to hear that."), no counselling, then the handoff to the HR team.
6. A self-harm statement or a crisis: core R-04 (the Tele-MANAS line and the transfer); never counsel.
7. A report together with another topic (a leave query that turns into a disclosure): this workflow first; the other topic only afterwards, if at all.

## Unhappy paths

- The caller will not give a name: take the number and the type of concern only; do not press.
- The caller wants to name the accused on the call: do not take it; say the team will follow up and give the route as given.
- The caller asks whether the accused has had earlier complaints: nothing is said about any person.
- A third party calls on behalf of the person: the privacy line (core R-08); the route as given.
- The caller is angry or crying: calm and serious, shorter sentences, no cheerful phrases.
- No transfer target and no route: the callback, with the high priority noted.

## Data and variables

Variable used: `{{var.now_local}}`. Collected: name, callback number, type of concern, nothing else. Never the accused's name, the details of the incident, a medical or personal detail.

## Tools

`transfer`, `change_language`, `end_call`.

## Rules owned by this workflow

None. R-17, R-18, R-04 and R-25 are core rules.

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-12 | Employee reports sexual harassment (POSH) | The route as given; name, number and type of concern only; never investigates (R-17, R-20) | S1; S6 |
| S-13 | Employee stressed or upset about workload or job loss | One care line, HR team handoff, no counselling (R-20, R-25) | S4; S6 |
| S-39 | POSH route not given by the business | "Our team will confirm that for you." and connect; with no target, a callback (R-17, R-23) | S1 |
| S-50 | Caller asks about the accused, earlier complaints or a case outcome | Never answers; takes only name, number and type of concern (R-17) | S1 |
| S-55 | Whistleblower, fraud or discrimination report | The ethics route; notes only that a report is wanted; no details asked (R-18) | S1; S6 |
| S-41 | A leave query turns into a harassment disclosure | Safety first (R-01) | S1 |

## Manual-test checks

- Harassment is never callback-only unless there is no route and no target; the route is said exactly as given.
- The agent never asks about the accused, never investigates, never names anyone.
- An ethics report is not routed to POSH, and no details are asked.
- Ordinary stress gets the care line and a handoff, not the crisis line.

## Main-prompt lines (draft, used for the word budget)

```main-lines
HARASSMENT: Sexual harassment or abuse at work: one care line, give only the business route as given, take name, number and type of concern, then the handoff. Never investigate, judge, ask about the accused or name anyone.
ETHICS: A whistleblower, fraud or discrimination report: note only that the caller wants to make a report, give the ethics route as given, no details asked, then the handoff.
DISTRESS: Stress about workload or job loss: one care line, no counselling, then the handoff.
```
