# Education test profiles

Six synthetic profiles for manual /prompt-writer tests. No eval.json exists for this industry (DECISIONS 108); quality is checked with `python scripts/check_variables.py`, `python scripts/check_fixed_lines.py` and a reading of each generated output against the MUST and MUST NOT tables. All values are invented: fake business names containing "Test", numbers in the 00000 020xx style, example.com addresses, invented students and links.

| # | Profile | Direction | Assistant name | Business type | Workflows | Tools | Section 6 estimate |
|---|---|---|---|---|---|---|---|
| 01 | School, links on, three targets, default student-data rule | Inbound | Anika | school | 01, 02, 03, 05, 06 | send link ON, booking OFF | 564 |
| 02 | College with hostel, anti-ragging contact, staff-verify rule, calls recorded | Inbound | Karthik | college | 01, 02, 03, 05, 06 | all OFF | 564 |
| 03 | Coaching centre with demo booking ON, counsellor target, no accounts target | Inbound | Dev | coaching | 01, 02, 04, 05, 06 | booking ON, send link ON | 554 |
| 04 | Edtech counselling booking, assistant name, recorded calls | Outbound | Ria | edtech | 09, 12 | booking ON, send link ON | 459 |
| 05 | Fee reminder with NO assistant name, name-first identity, one client request must be refused | Outbound | not given | school | 09, 11 | send link ON | 502 |
| 06 | Preschool and daycare, pickup rules, one target | Inbound | Neha | preschool | 01, 02, 05, 06, 08 | all OFF | 584 |

Workflows 07 (online classes and technical help), 10 (admission follow-up) and 13 (event or PTM reminder) have no profile of their own in v1; they are checked by reading their rules and scenarios. Say so in the sign-off.

## How to run the checks

1. Generate the Instructions with the skill once it exists (not written yet), from the profile as a non-interactive input.
2. `python scripts/check_variables.py --paths <output file>`.
3. `python scripts/check_fixed_lines.py OUTPUT.md --industry education --workflows <numbers> --profile industries/education/test-profiles/NN-*.md` (needs the script to know education first; see the brief's open questions).
4. Read the output against the profile's MUST and MUST NOT table.

Profile 04 (calls recorded: yes) must carry "This call may be recorded for quality purposes." inside the welcome, before "Is this a good time to talk?"; profile 05 (calls recorded: no) must never carry it. Profile 05's welcome comes from the profile's rows: "Hello, I am an AI assistant calling from Greenwood Test International School. Is this a good time to talk?" Profile 02 (calls recorded: yes, inbound) must say the sentence once in the first reply after the welcome. Profiles 01, 03 and 06 have a main target that stands in for every team that was not given.
