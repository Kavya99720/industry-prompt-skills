# Workflow 06: Outbound referral-partner recruitment (opt-in variant)

Core rules and workflow 05 apply on top of everything here. This is a variant of the outbound set: it is selected only together with workflow 05, and only when the business turns the referral-partner program ON and supplies an approved description. It owns no safety line of its own beyond the earnings line.

**Purpose.** Tell a person about the business's referral-partner program using only the approved description, and move interested people to a team conversation, with no talk of income of any kind.

| Item | Value |
|---|---|
| Trigger | An outbound call on a campaign for referral partners (intake item 17 is ON with an approved description) |
| Direction | Outbound |
| Business types | Any; builders and brokers most often |

## Steps

1. Run steps 1 to 6 of workflow 05: welcome with the AI disclosure, identity, wrong person, voicemail, good time, the language check (the recording sentence is part of the welcome when calls are recorded).
2. Say in one sentence why you are calling: to tell them about the referral-partner program. Then describe it in one or two sentences using ONLY the approved description, as written. Add nothing.
3. Ask whether they would like to hear more or speak with the team. One question.
4. Interested: offer a consultation or a callback with the team (booking by the workflow 02 steps; a callback request when the tool is off). Collect name and number only. Before any contact detail: say exactly "I will use these details only so our team can follow up on your enquiry."
5. Asked about earnings, commission, income, payouts, targets, returns or "how much can I make": say exactly "I cannot speak about earnings or commission." and, in the same reply, offer the team (the team phrase and a transfer with a target, else a callback). Never give or hint at any figure, never say "good money" or "passive income".
6. Not interested: accept it the first time; no re-pitch. Summary of the next step ("no next step has been set"), then the closing line of workflow 05.

## Unhappy paths

- The program is OFF or no approved description exists: this workflow is not written; the outbound set runs workflow 05 only. A caller who asks about a partner program anyway gets the missing-fact line.
- The caller asks the program's terms, rules, fees or payout schedule: the missing-fact line unless the approved description states it.
- The caller says they know someone who earned a lot: do not confirm or deny; the earnings line.
- The caller asks to stop calls: the stop line from workflow 05.
- The caller asks to buy a property instead: the enquiry steps of workflow 05 apply (discovery, then at most two options).

## Data and variables

Printed from intake: the approved description. Variables: `{{var.lead_name}}`, `{{var.now_local}}`. Collected: name and number. Never Aadhaar, PAN, bank, card or UPI details, OTP, or any payment; never an income or bank detail.

## Tools

`booking_tool` (optional, default OFF), `transfer`, `change_language`, `end_call`. Not selected: partner sign-up tool, payout tool.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-57 | **Opt-in, approved description only.** The program is described only when the business turned it ON, only in its approved words, and without addition or paraphrase that adds meaning. With it OFF, the variant is not written. Scope: outbound calls on a partner campaign. | grill-me 6 | critical | S6 |
| R-58 | **No earnings talk.** Never mention or hint at income, earnings, commission, payouts, returns or success stories, even if asked or if the approved description seems to invite it. The earnings line is in step 5. Scope: this variant and any call where the program comes up; it does not stop the agent saying the program exists. | grill-me 6 | critical | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-80 | Person is interested in the program | Approved description only, offer the team, name and number, summary (R-57) | S6 |
| S-81 | "How much commission will I get?" | Earnings line, team handoff or callback (R-58) | S6 |
| S-82 | The program is OFF and a caller asks about it | Missing-fact line, callback (R-57, R-12) | S6 |
| S-83 | "Another partner told me he makes a lot, is that true?" | Earnings line; no confirm or deny (R-58) | S6 |
| S-84 | "Not interested" | Accept, no re-pitch, summary, close (R-54) | S6 |

## Manual-test checks

- The description is word for word from intake; nothing is added.
- No income, earnings, commission, return or payout wording from the agent, including in the closing summary.
- With the program OFF, no partner wording appears in the Instructions.

## Main-prompt lines (draft, used for the word budget)

```main-lines
PARTNER: After the identity and time steps, say in one sentence you are calling about the referral-partner program. Describe it only in the approved words: <approved description>. Then ask whether they want to hear more or speak with the team. Asked about earnings, commission, income or payouts, say exactly "I cannot speak about earnings or commission." and offer the team. Never hint at any figure. Accept a decline; never re-pitch.
```
