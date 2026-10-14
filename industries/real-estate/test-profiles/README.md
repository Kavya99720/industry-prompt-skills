# Real estate test profiles

Five synthetic profiles for manual /prompt-writer tests. No eval.json exists for this industry (DECISIONS 108); quality is checked with `python scripts/check_variables.py`, `python scripts/check_fixed_lines.py` and a reading of each generated output against the MUST and MUST NOT tables. All values are invented: fake business names, numbers in the 00000 010xx style, example.com addresses, invented project names, and RERA numbers of the form TEST/RERA/000x.

| # | Profile | Direction | Assistant name | Business type | Workflows | Tools | Section 6 estimate |
|---|---|---|---|---|---|---|---|
| 01 | Builder inbound | Inbound | Anaya | builder | 01, 02, 03, 04 | booking ON, send_link ON | 403 |
| 02 | Broker inbound (also carries six client requests that break rules) | Inbound | Ishaan | broker | 01, 02, 03, 04 | booking OFF, send_link OFF, no transfer target | 403 |
| 03 | Advisory firm, outbound consultation calls | Outbound | Nisha | advisory | 05 | booking ON, send_link ON | 395 |
| 04 | Outbound with NO assistant name, no lead name, no source, no tools | Outbound | not given | broker | 05 | booking OFF, send_link OFF, no transfer target | 395 |
| 05 | Rental inbound (lighter variant) | Inbound | Kabir | rental | 07, 02, 04 | booking ON, send_link OFF, email only | 325 |

## How to run the checks

1. Generate the Instructions with the skill once it exists (not written yet), from the profile as a non-interactive input.
2. `python scripts/check_variables.py --paths <output file>`.
3. `python scripts/check_fixed_lines.py OUTPUT.md --industry real-estate --workflows <numbers> --profile industries/real-estate/test-profiles/NN-*.md --tool booking_tool=on|off --tool calls_recorded=on|off --tool confirmation_channels=whatsapp|email|both` (omit the channels tool when none are set).
4. Read the output against the profile's MUST and MUST NOT table.

Profile 03 (calls recorded: yes) must carry "This call may be recorded for quality purposes." right after the welcome in the same turn; profile 04 (calls recorded: no) must never carry it. Profile 04's welcome comes from the profile's rows: "Hello, I am an AI assistant calling from Cedar Row Realty. Is this a good time to talk?" The shared fixed-line script builds an outbound welcome with the AI disclosure only for industries listed in AI_OUTBOUND_INDUSTRIES (banking today); real estate needs adding there (listed in the brief's open questions).
