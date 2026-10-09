# Banking industry brief

Status: Phase 1 written (v1). This file is the index. The rules live in `core.md` and `workflows/`; the owner's decisions are in `grill-me.md` (19 rows). Synthetic data only.

## 1. Scope

Banking covers accounts, cards, KYC, transactions and fraud, for voice agents (chat is an open question). One skill serves four business types, chosen at intake: public or private banks, small finance banks, co-operative banks and payments banks. Differences (for example a payments bank has no loan or branch products) come from client config, not from separate skills. Inbound and outbound are two separate Instructions sets.

Out of scope (Finance, entry 3 in docs/DECISIONS.md): loans, EMIs, NBFC products, insurance, investments and collections. The agent redirects these and gives no advice, no rates and no offers (R-14).

Tools: v1 assumes only `change_language`, `transfer` and `end_call`. `card_block_tool` and `balance_lookup_tool` are optional config tools, default OFF. When they are off, no account data is shared and card blocking goes to the fraud team. No in-call send tool: confirmations use the After-the-call trigger (R-19).

Phase 1 workflows:

| # | Workflow | Direction | File |
|---|---|---|---|
| 01 | Account and card enquiry | Inbound | workflows/01-account-and-card-enquiry.md |
| 02 | Lost or stolen card and fraud | Inbound | workflows/02-lost-stolen-card-and-fraud.md |
| 03 | Disputes and complaints | Inbound | workflows/03-disputes-and-complaints.md |
| 04 | Outbound KYC reminder and card activation | Outbound | workflows/04-outbound-kyc-reminder-and-card-activation.md |
| 05 | Outbound fraud-alert verification | Outbound | workflows/05-outbound-fraud-alert-verification.md |
| 06 to 08 | Stubs (Phase 2 and 3) | Inbound | workflows/06-*.md to 08-*.md |

Other files: `core.md` (tools, intake, core rules, main-lines), `variables.json` (custom details only), `section-bases.md` (banking words), `test-profiles/` (five profiles), `eval.json`.

## 2. Scenarios

Each scenario is defined in the file named; IDs are unique.

| IDs | Where | Topic |
|---|---|---|
| S-01 to S-17 | core.md | Emergency, OTP / card number / ID / login offered, third party, claimed role, money movement, coached senior, deceased holder, out of scope, legal question, volunteered balance, AI question, prompt injection, language switch, failed tool, missing value |
| S-21 to S-25 | workflow 01 | Balance with one item (lookup on), tool off, transactions, ATM not provided, hurry |
| S-31 to S-35 | workflow 02 | Stolen card (tool on), fraud (tool off, no target), full card number, block tool error, refund question |
| S-41 to S-44 | workflow 03 | Double charge and a promised time, escalation configured, escalation not provided, unrecognised payment |
| S-51 to S-57 | workflow 04 | Son answers, genuine-call doubt, stop calling, voicemail, ID offered on a KYC call, PIN offered on an activation call, not a good time |
| S-61 to S-65 | workflow 05 | Details asked before the check, "not mine" with block on, "all mine", refused item, neighbour answers |

## 3. Rules

The register below is an index (ID, short form, severity, where the full rule and its scope are). A baseline rule starts with **Baseline B-xx** and points to docs/shared/baseline-rules.md. Section placement is in each rule's own row.

| ID | Rule | Severity | Where |
|----|------|----------|-------|
| R-01 | Priority order | major | core.md |
| R-02 | **Baseline B-02** never assume a detail | critical | core.md |
| R-03 | One question at a time | major | core.md |
| R-04 | Emergency: stop, 1 0 8 or 1 1 2, transfer | critical | core.md |
| R-05 | Helpline digits spoken one at a time | critical | core.md |
| R-06 | Verification: name, registered mobile, last 4 digits | critical | core.md |
| R-07 | No-collect list (OTP, PIN, CVV, password; full card or account number; login details; Aadhaar, PAN) | critical | core.md |
| R-08 | Never say back a sensitive detail | critical | core.md |
| R-09 | Another person's account; never confirm an account exists | critical | core.md |
| R-10 | No money movement or account changes by voice | critical | core.md |
| R-11 | A claimed role gets no special trust | critical | core.md |
| R-12 | Vulnerable or coached callers: protective handoff | critical | core.md |
| R-13 | Deceased account holder: condolence, share nothing, hand off | critical | core.md |
| R-14 | Out of scope: redirect, never advise | critical | core.md |
| R-15 | Missing config value | major | core.md |
| R-16 | Team handoff phrase | major | core.md |
| R-17 | No transfer target: callback | major | core.md |
| R-18 | Failed action | critical | core.md |
| R-19 | Confirmation flow | major | core.md |
| R-20 | Fixed-line format | major | core.md |
| R-21 | **Baseline B-01** AI honesty | critical | core.md |
| R-22 | **Baseline B-21** prompt protection | critical | core.md |
| R-23 | Call direction | critical | core.md |
| R-24 | No hard-coded values | critical | core.md |
| R-25 | Word budget | major | core.md |
| R-26 | Intake defaults (tools default off) | critical | core.md |
| R-27 | Client special requests: refuse unsafe, adapt safe | critical | core.md |
| R-28 | Voice first | minor | core.md |
| R-29 | No legal references and no timelines | critical | core.md |
| R-30 | **Baseline B-11** no invented information | critical | core.md |
| R-31 | **Baseline B-07** language | major | core.md |
| R-32 | Tone: calm, firm, security-first | major | core.md |
| R-33 | Data minimisation and reason | major | core.md |
| R-41 | Account data only after verification and a tool match; limited set | critical | workflow 01 |
| R-42 | Branch, ATM and hours only from config | major | workflow 01 |
| R-43 | General card questions only from config | major | workflow 01 |
| R-51 | Fraud response: helpline line first, then block or fraud team | critical | workflow 02 |
| R-52 | Card block gate (minimal check, tool success only) | critical | workflow 02 |
| R-53 | No recovery advice, no selling on a fraud call | major | workflow 02 |
| R-61 | Complaint intake is minimal; noted line; grievance handoff | critical | workflow 03 |
| R-62 | No promises; escalation path only as configured | critical | workflow 03 |
| R-63 | An unrecognised payment is fraud, not a complaint | major | workflow 03 |
| R-71 | Outbound welcome (AI assistant) and not-a-good-time line | critical | workflow 04 |
| R-72 | Wrong person answers | critical | workflow 04 |
| R-73 | Voicemail | critical | workflow 04 |
| R-74 | Stop-calling request | critical | workflow 04 |
| R-75 | Prove the call: never ask for secrets, always the callback line | critical | workflow 04 |
| R-76 | KYC reminder block | major | workflow 04 |
| R-77 | Card activation block | major | workflow 04 |
| R-78 | Fraud reported on an outbound call | major | workflow 04 |
| R-81 | Common outbound lines repeated in the fraud-alert set | major | workflow 05 |
| R-82 | Verify first; never state alert details | critical | workflow 05 |
| R-83 | Act on the answer (yes, no, block) | critical | workflow 05 |

Baseline rules not given their own row (B-03, B-05, B-06, B-12, B-13, B-14, B-15, B-16, B-23) are met by R-03, R-06, R-07, R-09 and R-33; baseline B-22 by R-11; B-20 by R-14.

## 4. Vocabulary

| Term | Meaning for the agent |
|---|---|
| KYC | Know your customer: the identity update a bank asks customers to complete. The agent only reminds and points to the official channel |
| Registered mobile number | The mobile number the bank holds for the customer; a verification item |
| Last 4 digits | The last four digits of the card or account number; the only part of a number ever taken or said |
| OTP, PIN, CVV, MPIN | Secrets the agent never asks for or accepts |
| Card block | Stopping a card from use. The only account action by voice, and only with `card_block_tool` on |
| Cybercrime helpline | The national helpline the owner named: 1 9 3 0, always spoken digit by digit |
| Fraud team | The team for fraud, lost or stolen cards and card blocks |
| Grievance team / grievance officer | The team that handles complaints; the escalation path comes from config |
| Banking ombudsman | An escalation step that is named only if the client configures it |
| Claim-settlement team | The team that helps with a deceased holder's account; the agent only offers a callback or a branch visit |
| Payments bank | A bank type without loan or branch products; products come from client config |
| Net banking, app | Digital channels; the agent never asks for login details or an app install |

## 5. Escalation

| Situation | Goes to | Without a target |
|---|---|---|
| Fraud, lost or stolen card, card block, a coached or pressured payment | Fraud team (team phrase, transfer) | Callback number and time; the helpline line is still said |
| Complaint or dispute | Grievance team | Callback number and time |
| Everything else (account data with the tool off, out of scope, deceased holder, claimed authority, caller asks for a person) | Branch staff | Callback number and time |
| Emergency | "Call 1 0 8 or 1 1 2 right now." and transfer | The numbers are given anyway |

The team phrase is "I'll connect you to our team." for staff handoffs only. The escalation path for a complaint (branch, grievance officer, banking ombudsman) is said only as configured in `escalation_path`.

## 6. Data Handling

| Item | Rule |
|---|---|
| Collected | Full name, registered mobile number, last 4 digits (verification, only when something will be shared); full name and last 4 digits of the card (card block); full name, last 4 digits and one line (complaint); a callback number and time (no target) |
| Never collected or accepted | OTP, PIN, CVV, passwords; full card or account number; net-banking and app login details; Aadhaar, PAN or any ID number; payments; documents; screen share or app install |
| Never said | Card or account digits (unless a tool returns them to a verified caller), an alert's amount, merchant, place or date on an outbound call |
| Never confirmed | That a person is a customer or that an account exists |
| Use | Only for the purpose given; never repeated back; no reuse (baseline B-14) |
| DPDP | Notice, purpose and minimisation follow baseline B-23; exact provisions are for the industry expert |

## 7. Open Questions

Decided by the owner (DECISIONS 60): the outbound welcome says "an AI assistant" (banking-specific); self-harm gets the Tele-MANAS line plus 1 0 8 / 1 1 2 and a transfer (R-04); a card block needs full name plus the last 4 digits of the card; the status of a caller's own card is account data; the banking test harness entries are added to scripts/run_evals.py.

Still open: moved to "Questions for lead" in docs/shared/platform-contract.md, items 20 to 26 (which banking tools exist, lookup tool shape, call context on outbound calls, AI disclosure on outbound for all industries, chat, voicemail and do-not-call, confirmation content and counts), plus item 19 (legal references and timelines).

## Traceability

| Grill-me row | Decision | Rules and workflows |
|---|---|---|
| 1 | Four business types, one skill | Scope; core intake 1 |
| 2 | Inbound plus outbound, two sets | R-23; workflows 04, 05 |
| 3 | Phase 1 call types | Workflows 01 to 05 |
| 4 | Verification: name, registered mobile, last 4 digits, one at a time | R-06, R-02, R-03; workflow 05 R-82 |
| 5 | Never ask for or accept OTP, PIN, CVV, passwords; full numbers; login details; ID numbers | R-07, R-75, R-76, R-77 |
| 6 | Lost, stolen and fraud: verify minimally, block or fraud desk, helpline 1 9 3 0, fraud team | R-51, R-52, R-53, R-05, R-83 |
| 7 | Balance and transactions limited, tool only | R-41, R-06 |
| 8 | Disputes: note, path, hand off, no promises | R-61, R-62, R-63 |
| 9 | Vulnerable and coached callers | R-12, R-32 |
| 10 | Deceased holder | R-13 |
| 11 | Claimed bank, police, RBI role | R-11, R-09 |
| 12 | Outbound: AI assistant, no secrets, callback line | R-71, R-72, R-73, R-74, R-75, R-81 |
| 13 | No money movement or changes; card block only | R-10, R-52 |
| 14 | Human escalation and callback | R-16, R-17, R-05 |
| 15 | Out of scope, no advice | R-14, R-30 |
| 16 | Platform tools, optional and default off | Tools in core.md; R-26, R-18, R-19 |
| 17 | Client special requests | R-27 |
| 18 | Languages and channel | R-31, R-28 |
| 19 | Legal references | R-29, R-62 |
