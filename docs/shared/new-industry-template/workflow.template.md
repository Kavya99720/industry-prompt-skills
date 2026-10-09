# Workflow NN: <name> (template)

Copy to industries/<industry>/workflows/NN-<slug>.md. Core rules (industries/<industry>/core.md) apply on top of everything here. One goal per workflow. Write the happy path, then the unhappy paths, then the tools by purpose.

**Purpose.** <one sentence: the one thing this workflow does>

| Item | Value |
|---|---|
| Trigger | <what the caller says or does> |
| Direction | Inbound / Outbound / both (outbound is a separate Instructions set) |
| Business types | <which business types use it> |

## Steps

Short, numbered, speakable. One question per step. Say what data is collected and why.

1. <Ask the first item. Confirm it as heard.>
2. <Call the tool, named by purpose.> If it fails: R-15 (failed action), never say it worked.
3. <Gate: the condition that must hold before the main action; say what happens when it does not.>
4. <Read back the details and ask for a clear yes. A "yes, but..." is not a yes.>
5. <Main action. Say it is done only when the tool returns its result.>
6. <Confirmation flow (R-16) if the action succeeded.> Then close.

## Unhappy paths (write each as a step or a scenario)

- The caller does not know an item: <what the agent does>.
- The caller refuses to give a detail: say why it is needed once; accept a refusal.
- The tool fails or returns nothing: R-15.
- The caller asks for something out of scope: <handoff line, R-07>.
- Wrong person / unverified caller: R-09, R-10.

## Data and variables

Variables used (from docs/shared/variables.json or industries/<industry>/variables.json): `{{var.business_hours}}`, <...>. Collected: <item by item>; never <the no-collect items>.

## Tools

<tool> (<purpose>), `transfer`, `change_language`, `end_call`. Not selected: <list>.

## Rules owned by this workflow

Every rule states its scope. A fixed line is written as: say exactly "X" then, in the same reply, <action>.

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-xx | <rule>. Scope: <when it applies; when it does not>. | | | |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-xx | <caller says or does X> | <what the agent does, with the rule ids> | S6 |

## Eval candidates

- <the critical behaviours that need a check: the gate, the fixed line, the failure path>

## Main-prompt lines (draft, used for the word budget)

```main-lines
LABEL: <short imperative sentences, speakable, important rules first. Quote fixed lines with "say exactly".>
```

Count the words of every main-lines block (whitespace-separated). Report them in the workflows README table; the total for the largest profile must stay at 595 or less.
