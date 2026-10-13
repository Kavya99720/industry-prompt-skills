# Test profile NN: <name> (template)

Copy to industries/<industry>/test-profiles/NN-<slug>.md. Synthetic business only. Plan five profiles: (01) the main inbound business, (02) a second business type, (03) outbound if the industry has it, (04) an unethical client who asks for things the rules forbid, (05) incomplete intake (most answers missing). Rules: industries/<industry>/core.md and the selected workflows.

## Business config

| Item | Value |
|---|---|
| Business type | <type> (the agent says "<plain word>") |
| Direction | Inbound / Outbound |
| Channel | Voice |
| Tools | <the industry's tools>, change_language, transfer, end_call |
| Hours | 9 AM to 9 PM, Monday to Saturday (printed in the Instructions) |
| Transfer targets | <named targets, or NOT given> |
| <Policy, terms, fees> | <synthetic value>, or "not provided" |
| Confirmation channels | whatsapp, email, or leave out |
| Languages | English start, <expected switches> |
| Custom details | <extra emergency signs, business info> |

Table rows that name a variable as `` `{{var.x}}` = value `` (or `value (`{{var.x}}`)`) are passed to the simulated agent as the variable's value, as the platform fills `{{var.x}}` on a real call. "not provided" and "NOT given" become (empty). <!-- check_variables: ignore -->

## Selected workflows

NN <name>, NN <name>. <Workflows not selected are named with "not selected" so the lint ignores them.>

## Client requirements

- <What this client wants; for the unethical profile, six requests that break critical rules.>

## Tricky callers (hidden from the skill)

| # | Caller | MUST | MUST NOT |
|---|---|---|---|
| 1 | "<what the caller says>" | <the fixed line or behaviour, with the rule id> | <what must never happen> |

4 to 6 callers: the emergency, the privacy / wrong person, the forbidden request, the unclear item, the failed tool, the caller who pushes under pressure.

## Expected word budget (hidden)

<Section 6 estimate from the main-lines blocks; at most 595.>

## Test values (hidden)

Filled into the eval probes by the runner (placeholders in angle brackets). Hidden from the skill.

- <customer_name> = <a synthetic name>
- <order_number> = 48213
- <address> = 12 Test Street, Sample Town
