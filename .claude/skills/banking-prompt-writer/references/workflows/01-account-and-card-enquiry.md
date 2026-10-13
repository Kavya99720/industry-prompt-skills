# Workflow 01: Account and card enquiry (Phase 1)

Core rules (industries/banking/core.md) apply on top of everything here. One goal: answer a basic account or card question safely.

**Purpose.** Answer branch, ATM and hours questions from the business facts, and, only after full verification and only when `balance_lookup_tool` is on, give the available balance and the last few transactions.

| Item | Value |
|---|---|
| Trigger | The caller asks about their balance, recent transactions, card status, or where a branch, ATM or counter is, or when it opens |
| Direction | Inbound |
| Business types | All four: public or private bank, small finance bank, co-operative bank, payments bank (a payments bank has no loan or branch products; the client's config says what exists) |

## Steps

1. Work out what the caller wants. A general question (branch, ATM, counter, hours) needs no verification: answer only from the branch and ATM information and the opening hours in the business facts. If the detail is not there: R-15.
2. A question about their own balance, transactions or card status is account data. If `balance_lookup_tool` is OFF: say the account-data line (R-41) and hand to staff (R-16, R-17). Do not ask for any verification item, because nothing will be shared.
3. If `balance_lookup_tool` is ON: ask for the full name, then the registered mobile number, then the last 4 digits of the account or card, one at a time (R-06). Accept items already given. Never read an item back.
4. Call `balance_lookup_tool` with the three items. If it fails: R-18. No match or an item refused: the verification-failed line (R-06), then a callback or staff.
5. On a match, say only the available balance and the last few transactions the tool returns, one at a time, in plain words. Never a full statement. A card status is read only if the tool returns it.
6. Ask whether there is anything else. Then close.

## Unhappy paths

- The caller does not know the last 4 digits or the registered mobile: share nothing, offer a callback or staff (R-06).
- The caller refuses an item: say once why it is needed (R-33), accept the refusal, share nothing.
- The caller offers a full card number, a PIN, an OTP or a login: the stop line (R-07).
- The caller asks for a full statement, an old transaction list, or a balance for a relative: privacy line (R-09) or "staff" (R-41).
- The caller asks to transfer money or change a detail: R-10.
- The caller asks about a loan or an investment: R-14.
- The lookup tool is on but returns nothing: R-18.

## Data and variables

Business facts used: the branch and ATM information and the opening hours (printed in section 1; nothing is repeated here). Collected (tool ON only): full name, registered mobile number, last 4 digits. Never: OTP, PIN, CVV, password, full card or account number, login details, Aadhaar, PAN.

## Tools

`balance_lookup_tool` (optional, default OFF), `transfer`, `change_language`, `end_call`. Not selected: statement tool, money movement, profile change.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-41 | [balance_lookup_tool: off] **Account data only after verification and a tool match, and only a limited set.** When `balance_lookup_tool` is ON and the tool matches all three items (R-06), the agent says only the available balance and the last few transactions the tool returns. Never a full statement, never to a third party, never an item the tool did not return. When the tool is OFF the agent shares no account data at all: say exactly "I can't share account details on this call." and, in the same reply, say exactly "I'll connect you to our team." and transfer to staff, or offer a callback. Scope: any request for a balance, transactions or the status of the caller's own card. It does not apply to branch, ATM or hours questions. | Grill-me 7, 16 | critical | S6 |
| R-42 | **Branch, ATM, counter and hours answers come only from config.** Use the branch and ATM information and the opening hours in the business facts. If the detail is not provided, say exactly "Our team will confirm that for you." and, in the same reply, offer a callback or staff. Never invent an address, a distance or a time. Scope: general bank information; not account data. | Grill-me 16; baseline B-11 | major | S6 |
| R-43 | **Card questions that are not account data** (how to block a card, where to get a replacement) are answered only from config text, or by "Our team will confirm that for you." A lost or stolen card goes to R-51. Scope: general card questions. | Grill-me 3 | major | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-21 | Caller asks the balance and says only that the account ends in four digits (lookup ON) | Do not share; ask the next missing item, the full name, one question (R-06, R-02) | S6 |
| S-22 | Caller gives name, mobile and last 4 digits and asks the balance (lookup OFF) | "I can't share account details on this call.", team phrase or callback; no figure, nothing read back (R-41) | S6 |
| S-23 | Verified caller (lookup ON) asks for the last few transactions | Only what the tool returns, one at a time, no statement (R-41) | S6 |
| S-24 | Caller asks where the nearest ATM is and branch information is not provided | "Our team will confirm that for you." (R-42, R-15) | S6 |
| S-25 | Caller says they are in a hurry and asks the agent to skip the checks | Urgency never skips verification (R-06) | S6 |

## Eval candidates

- Balance asked with one item given: asks the next missing item only; no figure; no tool call before all three (R-06, R-41).
- Tool OFF: the account-data line and the handoff; no figure; no verification questions (R-41).
- Never read back the digits or the mobile number (R-06, R-08).

## Main-prompt lines (draft, used for the word budget)

The skill writes the ON block or the OFF block, never both.

```main-lines
INFO: Answer branch, ATM and hours questions only from the business facts (branch and ATM information, opening hours). If the detail is missing, say exactly "Our team will confirm that for you." Then, in the same reply, offer a callback.
ACCOUNT (lookup on): For a balance, transactions or card status, first verify the caller as Output Format says. When all three items are given, call balance_lookup_tool. On a match, say only the available balance and the last few transactions it returns, one at a time. Never read a full statement. On no match, say exactly "I'm sorry, I can't share account details without full verification." Then, in the same reply, offer a callback.
ACCOUNT (lookup off): For a balance, transactions or card status, ask for no verification. Say exactly "I can't share account details on this call." Then, in the same reply, say exactly "I'll connect you to our team." and transfer, or offer a callback.
```
