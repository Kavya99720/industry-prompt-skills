# Retail test profiles

Six synthetic profiles for manual /prompt-writer tests. No eval.json exists for this industry (DECISIONS 108); quality is checked with `python scripts/check_variables.py`, `python scripts/check_fixed_lines.py` and a reading of each generated output against the MUST and MUST NOT tables. All values are invented: fake business names ending in "Test", numbers in the 00000 010xx style, example.com addresses, invented products and order IDs.

| # | Profile | Direction | Assistant name | Business type | Workflows | Tools | Section 6 estimate |
|---|---|---|---|---|---|---|---|
| 01 | Single store, one transfer target, every tool off | Inbound | Meera | single store | 01, 03, 05, 06 | none | 410 |
| 02 | E-commerce with order lookup, stock check and send link ON, all four targets | Inbound | Ishaan | e-commerce | 01, 02, 03, 05, 06 | order lookup ON, stock check ON, send link ON | 491 |
| 03 | Electronics store with service and warranty, lookup OFF, no payments target | Inbound | Rohan | electronics with service | 01 to 06 | stock check ON, send link ON, lookup OFF | 571 |
| 04 | Order or delivery update, recorded calls | Outbound | Nisha | e-commerce | 07, 08 | none | 407 |
| 05 | Feedback call with NO assistant name, no customer name, no source wording | Outbound | not given | electronics | 07, 10 | none | 433 |
| 06 | Abandoned-cart reminder: no pressure, accept a decline, link flow, stop-calling line; one client request must be refused | Outbound | Tara | e-commerce | 07, 09 | send link ON | 406 |

Workflow 11 (repair or service ready) has no profile of its own in v1; it is checked by reading its rules and scenarios. Say so in the sign-off. Workflow 09 is covered by profile 06.

## How to run the checks

1. Generate the Instructions with the skill once it exists (not written yet), from the profile as a non-interactive input.
2. `python scripts/check_variables.py --paths <output file>`.
3. `python scripts/check_fixed_lines.py OUTPUT.md --industry retail --workflows <numbers> --profile industries/retail/test-profiles/NN-*.md` (the checker reads the profile's settings; add `--tool name=on|off` only to override, and `--references industries/retail` until the skill's references exist).
4. Read the output against the profile's MUST and MUST NOT table.

Profile 04 (calls recorded: yes) must carry "This call may be recorded for quality purposes." inside the welcome, before "Is this a good time to talk?"; profile 05 (calls recorded: no) must never carry it. Profile 05's welcome comes from the profile's rows: "Hello, I am an AI assistant calling from Greenfield Test Appliances. Is this a good time to talk?" Profile 01 and 03 have a main target that stands in for every team that was not given.
