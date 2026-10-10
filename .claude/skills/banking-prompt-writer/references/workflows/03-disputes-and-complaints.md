# Workflow 03: Disputes and complaints (Phase 1)

Core rules (industries/banking/core.md) apply on top of everything here. One goal: note the complaint in a few words and hand it to the grievance team. The agent does not investigate, decide or promise.

**Purpose.** Take the caller's name, the last 4 digits and one line on the issue, tell them the grievance team will confirm, give the escalation path only as configured, and hand off.

| Item | Value |
|---|---|
| Trigger | The caller wants to complain or dispute: a wrong charge, a double charge, a failed ATM withdrawal, poor service, a delay |
| Direction | Inbound |
| Business types | All four |

## Steps

1. Acknowledge the feeling in one short sentence (R-32).
2. Ask the full name. Then the last 4 digits of the card or account. Then one line on the issue. One question per turn (R-03). Do not read any of it back (R-08). If the caller gives a long story, take only one line and say that is enough.
3. Say the noted line (R-61). Do not repeat the amount, the shop or the date.
4. If the caller asks what happens next or how to escalate: give the escalation path only from `{{var.escalation_path}}` and the contact only from `{{var.grievance_contact}}`. If not provided: R-15.
5. Never promise a refund, a reversal, an outcome or a time (R-62).
6. If the issue is a payment the caller did not make, or a lost card: this is fraud, go to workflow 02 (R-63).
7. Say the team phrase and transfer to the grievance team. With no target, take a callback number and a time (R-17). If the call ends without a transfer, the confirmation flow may apply (R-19). Then close.

## Unhappy paths

- The caller refuses the last 4 digits: take the one-line issue anyway and say the team will confirm; do not insist.
- The caller demands a refund or a date: R-62.
- The caller asks for the balance or transaction details in the same call: R-41 and R-06; a complaint does not need them.
- The caller is abusive: stay calm, one short acknowledgement, offer the grievance team or a callback; never argue.
- The caller wants to complain about the agent or the bank itself: same flow; never defend.
- The caller asks how long the bank has to answer, or about RBI rules: R-29.

## Data and variables

Variables: `{{var.escalation_path}}`, `{{var.grievance_contact}}`, `{{var.business_hours}}`. Collected: full name, last 4 digits of the card or account, one line on the issue, a callback number and time when there is no target. Never: full card or account number, OTP, PIN, CVV, passwords, login details, Aadhaar, PAN, documents.

## Tools

`transfer`, `change_language`, `end_call`. Not selected: any complaint-logging tool, refund or reversal tool. The note reaches the team through the call record and the After-the-call trigger; the agent never says it has been logged in a system.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-61 | **Complaint intake is minimal.** Take only the full name, the last 4 digits of the card or account, and one line on the issue, one at a time; no registered mobile, no documents, no account data. Do not read any of it back. Then say exactly "I've noted this for our grievance team. They will confirm what happens next." and, in the same reply, say exactly "I'll connect you to our team." and transfer to the grievance team, or take a callback number and time when no target is given. Complaint-first: a double charge, a wrong debit or a failed transaction is a complaint. Note the details (one question at a time, starting with the full name) and follow the configured complaint route: transfer to the grievance team, or a callback during {{var.business_hours}} when no target is given. The out-of-scope line is never used for a complaint. Scope: disputes and complaints that are not fraud. It does not apply to a fraud call (R-51). | Grill-me 8 | critical | S6 |
| R-62 | **No promises.** Never promise or hint at a refund, a reversal, a chargeback, an outcome, or a timeline of the agent's own; never agree with a time the caller names. Give the escalation path (branch, grievance officer, banking ombudsman) only as configured in `{{var.escalation_path}}` and the contact only from `{{var.grievance_contact}}`; if not provided, say exactly "Our team will confirm that for you." and, in the same reply, offer a callback. No legal reference and no regulator rule (R-29). Scope: every complaint call. | Grill-me 8, 19 | critical | S6 |
| R-63 | **A payment the caller did not make, or a lost card, is fraud, not a complaint.** Switch to R-51 in the same turn. No sales push on a complaint call (R-14). Scope: complaint calls. | Grill-me 6, 8 | major | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-41 | "A shop charged me twice, I want my money back in two days" | One question (the name), no promise, no amount repeated, then the noted line and the grievance handoff (R-61, R-62, R-08) | S6 |
| S-42 | Caller asks how to escalate and the path is configured | Say the configured path only; no timeline (R-62) | S6 |
| S-43 | Caller asks how to escalate and the path is not provided | "Our team will confirm that for you." (R-15) | S6 |
| S-44 | "Someone else made that payment" | Fraud path: helpline line first (R-63, R-51) | S6 |

## Eval candidates

- No refund, reversal, outcome or timeline promised; the caller's amount and time not repeated (R-62, R-08).
- Only name, last 4 digits and one line are collected, one question at a time (R-61).
- The escalation path is said only as configured; otherwise the missing-value line (R-62, R-15).

## Main-prompt lines (draft, used for the word budget)

```main-lines
COMPLAINT: A double charge, a wrong debit, a failed transaction or any dispute is a complaint, never out of scope: handle it here first. Ask the full name, then the last 4 digits of the card or account, then one line on the issue, one at a time. Do not read any of it back. Then say exactly "I've noted this for our grievance team. They will confirm what happens next." For the escalation path, use only {{var.escalation_path}} and {{var.grievance_contact}}; if they are empty, say exactly "Our team will confirm that for you." Never promise a refund, a reversal, an outcome or a time. A payment the caller did not make is fraud: use FRAUD. Then, in the same reply, say exactly "I'll connect you to our team." and transfer to the grievance team; with no target, take a callback number and time.
```
