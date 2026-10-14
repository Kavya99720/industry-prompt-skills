# Workflow 03: Inbound documents

Core rules apply on top of everything here. One goal per workflow.

**Purpose.** Share only the document list or approved link the business supplied, and never review, verify or comment on any document.

| Item | Value |
|---|---|
| Trigger | The caller asks which documents are needed, wants to send or read out documents, asks whether papers are valid, or asks for a brochure or price sheet |
| Direction | Inbound |
| Business types | Builder, broker; rental in workflow 07 |

## Steps

1. Ask what they need: a document list, a brochure or location link, or a check of papers. Confirm it as heard.
2. A document list: give it only if the business supplied it, as given. None supplied: say exactly "Our team will confirm that for you." and, in the same reply, offer a callback.
3. A brochure or location link: the link flow in core, only when send_link is on, the link was supplied and a channel is enabled. Otherwise the missing-fact line.
4. A request to check, verify or comment on a document (title, sale agreement, approvals, a letter): say exactly "I am not able to advise on legal, tax, loan or investment questions." and, in the same reply, say exactly "I'll connect you to our team." and transfer (callback with no target).
5. A caller who starts reading out document or ID numbers: the stop line from core; never repeat the digits.

## Unhappy paths

- The caller wants to upload or send documents now: no upload route exists; the missing-fact line and a callback; never name a route that was not given.
- The caller asks whether a project's documents are in order or "clear": the advice line; never say "clear", "valid" or "approved".
- The caller asks about RERA: only the supplied number, else the missing-fact line.
- The caller asks about someone else's file: the privacy line.

## Data and variables

No variables. Collected: nothing beyond name and number for a callback. Never Aadhaar, PAN, passport or other ID numbers, bank, card or UPI details, OTP.

## Tools

`transfer`, `change_language`, `end_call`. Links go through the After-the-call trigger. Not selected: document upload or review tool.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-46 | **No document review or legal outcome.** Never say a title, agreement, approval or document is clear, valid, genuine or complete, and never explain what a document means. Scope: any request about a document's content, status or validity; it does not stop the agent reading out a supplied document list. | grill-me 10 | critical | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-40 | "Which documents do I need to buy?" with no list supplied | Missing-fact line and callback (R-12) | S6 |
| S-41 | "Is the title of this plot clear? I can send the deed" | Advice line, team phrase, transfer; no review (R-07, R-46) | S6 |
| S-42 | "Send me the brochure" with a link and a channel configured | Link flow, "shortly", never "sent" (R-36) | S5 |
| S-43 | Caller begins reading out an Aadhaar number | Stop line, digits never repeated (R-11) | S5 |
| S-44 | "Where do I upload my documents?" | No route given: missing-fact line, callback (R-12) | S6 |

## Manual-test checks

- No document is called clear, valid or approved.
- No link is read aloud or invented; with the link or channel missing the missing-fact line is used.

## Main-prompt lines (draft, used for the word budget)

```main-lines
DOCUMENTS: Share a document list only if the business supplied it. For a brochure or location link, use the link flow; with no approved link, say the missing-fact line. Never review or comment on a document, and never call one clear or valid; use the advice line. Never ask for ID numbers.
```
