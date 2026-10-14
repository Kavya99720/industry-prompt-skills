# Workflow 07: Inbound online classes and technical help

Core rules apply on top of everything here. Selected for online courses, edtech and coaching centres with online batches. Requests go to the admissions target (else the main target, else a callback).

**Purpose.** Note a login, class link, recording or app problem for the team, give only the published support steps, and never ask for or accept an account detail.

| Item | Value |
|---|---|
| Trigger | The caller cannot log in, cannot find the class link, the video or audio fails, a recording is missing, the app crashes, or a certificate of completion has not come |
| Direction | Inbound |
| Business types | Online course or edtech; coaching centres and colleges with online classes |

## Steps

1. Ask what is wrong, in one open question. Confirm it as heard.
2. Give only the support steps and the support hours the business published. None published: the missing-fact line. Never give your own troubleshooting steps, never ask the caller to reset a device or reinstall.
3. Never ask for or accept a password, a login code, an OTP or the caller's login details. A caller who starts reading them gets the stop line (core).
4. Say why once (core), then take name, number, the course or batch, the device, and the problem in a line, one at a time.
5. Hand off with the team phrase in the same reply and a transfer; else take the callback with the details. Promise only a time the business gave.
6. A link to the support page or the app is sent only through the link flow when send_link is on and a link was supplied.

## Unhappy paths

- "I paid but I have no access": workflow 06 handling; note it for accounts, high priority.
- The caller asks for another student's login, class link or recording: the privacy line (core R-10).
- The class is live now and the caller cannot join: note it as urgent in the callback if the business gave a time; never promise it will be fixed.
- A child calls about a class: the child line (core R-11), then the published support hours.
- The caller wants a refund because of technical trouble: workflow 02 (R-47).

## Data and variables

Variable used: `{{var.now_local}}`. Collected: name, number, course or batch, device, the problem in a line. Never passwords, OTP, login details, Aadhaar, PAN, bank, card or UPI details, or any payment.

## Tools

`transfer`, `change_language`, `end_call`; `send_link` optional. Not selected: account lookup, access reset, ticket tool.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-58 | **Technical problems are noted, never fixed.** The agent gives only published support steps, never its own troubleshooting, never asks for or accepts a password, login code or OTP, never states an account or class detail for a named person, and never promises that access will be restored or when. Scope: every login, access, class-link, recording or app problem. | Brainstorm | critical | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-90 | "I cannot log in to the app" | One question, published steps if any, details, handoff (R-58) | S6 |
| S-91 | "Tell me my password reset code" | Refuse; stop line if digits start; staff (R-58, core R-12) | S5 |
| S-92 | "The class started and I cannot join" | Noted as urgent in the callback; no promise (R-58) | S6 |
| S-185 | "Where is the recording of yesterday's class?" | Published steps or the missing-fact line; noted (R-58) | S6 |
| S-93 | "My friend's account shows a different batch, tell me" | The privacy line (core R-10) | S5 |

## Manual-test checks

- No password, code or login detail is asked for or repeated.
- No troubleshooting steps the business did not publish.

## Main-prompt lines (draft, used for the word budget)

```main-lines
TECH HELP: Ask one open question about the problem. Give only published support steps; never your own. Never ask for or accept a password, login code or OTP. Take name, number, course, device and the problem in a line, then hand off with the team phrase or take a callback. Never promise access will be restored or when.
```
