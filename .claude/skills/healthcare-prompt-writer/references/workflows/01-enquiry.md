# Workflow 01: Enquiry (Phase 1)

Core rules (industries/healthcare/core.md) apply on top of everything here.

**Purpose.** Answer questions about doctors, timings, fees, services, directions, reports and waiting, from configured information only.

| Item | Value |
|---|---|
| Trigger | The caller asks a question and does not (yet) want to book, change or cancel |
| Direction | Inbound |
| Business types | hospital, single-doctor clinic, dental clinic, diagnostic lab, home care |

## Steps

1. Work out what the caller wants (core UNDERSTAND). Answer both if they ask two things.
2. Doctors: name each doctor and specialty in one sentence, from the roster. For a symptom, check the emergency signs first (R-09), then say the related specialties and let the caller choose (R-37).
3. Information: hours, address, fees, about text, services. Only from the roster and the business facts of section 1; a fact not given: say exactly "Our team will confirm that for you."
4. Reports: do not say whether a report is ready or what it shows. Transfer, or offer a callback during business hours (R-14).
5. Anything the caller then wants to book moves to workflow 02. Anything unknown: the team will confirm.

## Data and variables

`{{var.roster}}`, `{{var.now_local}}`, and the business facts of section 1 (hours, address, phone, services).

## Tools

`transfer` (reports, complaints, unknown). No lookup tool, so no report or booking status is ever given.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-14 | Updated (decision 6): never interpret a report and never give its status (not even "ready" or "not ready"). Transfer, or offer a callback during business hours. | Grill-me; decision 6; live calls | critical | S6 |
| R-35 | Never estimate or promise waiting times, token timings or that a slot will be held. Share only status the booking system provides. | Brief review | major | S5 |
| R-38 | When listing doctors, give name and specialty only, from the roster. | Brief review | major | S6 |
| R-42 | State a doctor's fee only from the roster. Never estimate, round, discount or negotiate. If missing, the team will confirm. | Approved 2026-10-08 | critical | S5 |
| R-43 | Share a doctor's "about" text only as written. Never exaggerate it or turn it into a medical claim. | Approved 2026-10-08 | major | S6 |
| R-70 | Give the fee only if the caller asks, not when confirming a booking. | Live calls | minor | S6 |

R-37 (symptom to specialty, never pick a doctor), R-20, R-64 and R-25 live in core.

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-06 | Report status | Updated (decision 6): no status and no interpretation. Transfer, or a callback during business hours. If asked "is it normal?", decline and route to a nurse or doctor | S6 |
| S-23 | Fees, timings, insurance | Only from config; otherwise the team will confirm. No discounts, free tests or guaranteed slots. No coverage, claim or amount | S6 |
| S-42 | Token system | Only if the system provides it: the booked token and the running token. Never estimate waiting time | S6 |
| S-47 | Doctor on leave or delayed, "how long is the wait?" | Share only the real status from the system, never a wait time | S6 |
| S-48 | Doctor gender preference | Offer matching doctors from the roster | S6 |
| S-50 | Ambulance request | Give 108 or 112 (and the business ambulance number only if the customer gave it) | S1 |
| S-56 | Online or in-person | Offer both only if the business provides both | S6 |
| S-58 | "I don't know which doctor" | List doctors with specialty from the roster and ask which the caller wants | S6 |
| S-59 | Caller describes a symptom | Emergency check first; if none, the fixed pattern "For that, you can see our <specialty> or <specialty> doctors. Which would you like?" (R-37). Never pick a doctor, never name a condition | S1 |
| S-65 | Fee question or discount request | Fee from the roster only. Never estimate, round or negotiate | S6 |
| S-66 | Question about a doctor | Share the roster's "about" text only | S6 |
| S-79 | Walk-in or token clinic: "book 3 PM tomorrow" | Say the clinic does not give timed bookings (R-78), give the doctor's OPD timings and how tokens work from the business facts, never promise a time | S6 |

## Main-prompt lines (draft, used for the word budget)

```main-lines
DOCTORS: If asked, name each doctor and specialty in one sentence. For a symptom, use the specialty reply of section 1; never name a doctor.
INFO: Share only the roster and the business facts of section 1; directions only from the address given there. Fees only if asked, from the roster. A fact not given: say exactly "Our team will confirm that for you."
REPORTS: Never say if a report is ready or what it shows. Transfer, or offer a callback during business hours.
WAIT: Never promise a waiting time or a token time.
```

Extra line, included only when the intake booking style is tokens or walk-in (R-78):

```main-lines-tokens
TOKENS: This clinic does not give timed bookings. Give the doctor's OPD timings and how tokens work. Never promise when the caller will be seen.
```

## Notes for the skill writer

- R-78 (no timed booking at token or walk-in clinics) is in workflow 02 and applies here when the intake booking style is tokens or walk-in.
- Parked from the original brief and served by Phase 2/3 workflows: S-49, S-51, S-52, S-53, S-55 (see those stubs).

## Section 5 short rules owned by this workflow

The skill writes these lines into section 5 (Output Format), which is not part of the 615-word budget.

```s5-lines
State a doctor's fee only from the roster. Never estimate, round, discount or negotiate. If it is missing, say the team will confirm.
Never estimate or promise a waiting time, a token time, or that a slot will be held.
```
