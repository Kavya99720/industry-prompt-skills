# HR v1 sign-off (DRAFT, not locked)

No eval.json and no eval runs (DECISIONS 108). Quality was checked with check_variables.py, check_fixed_lines.py, compact_coverage.py and a reading of the generated outputs against their profiles. All six test profiles were generated from the hr-prompt-writer skill's text and its references and saved in `sentence-tests/`. The outputs were composed in the main session with a generator script that follows the skill's rules; they are not independent model runs of the skill, and they were composed with the hidden caller tables known.

## Results

| Profile | Direction | Saved output | check_variables | check_fixed_lines | Section 6 words |
|---|---|---|---|---|---|
| 01 in-house HR, every setting on, recorded, POSH and ethics routes | inbound | 01-in-house-hr-inbound-all-tools-on.md | 0 errors, 0 warnings | 23 required, 0 missing | 404 |
| 02 in-house HR, every setting off, one HR team target, no ethics contact | inbound | 02-in-house-hr-inbound-all-tools-off.md | 0 errors, 0 warnings | 21 required, 0 missing | 306 |
| 03 staffing agency, HR lookup on, three unsafe client requests refused | inbound | 03-staffing-agency-inbound-lookup-on.md | 0 errors, 0 warnings | 22 required, 0 missing | 328 |
| 04 payroll provider, no assistant name, recorded, balance lookup on | inbound | 04-payroll-provider-inbound-no-assistant-name.md | 0 errors, 0 warnings | 23 required, 0 missing | 265 |
| 05 training and verification vendor, no POSH route, no ethics contact, no transfer target, two requests refused | inbound | 05-verification-vendor-inbound-no-route-no-target.md | 0 errors, 0 warnings | 20 required, 0 missing | 191 |
| 06 outbound interview reminder, named, recorded, scheduling on | outbound | 06-outbound-interview-reminder-named-recorded.md | 0 errors, 0 warnings | 24 required, 0 missing | 297 |

Section 6 is under the 595-word budget on every profile. The checker reads each profile's own settings (tools, recording, transfer targets, contact-source wording). No output contains a rule ID, a slot left unfilled, "calling from" in an inbound set, or a draft note that names a file, a workflow or a tool. The words "approved", "booked", "scheduled", "submitted" and "terminated" appear only inside rules that forbid them or as a caller's state.

## Manual tests done

- check_variables.py on the whole repo (0 errors, leakage 0 hits not allowed) and on each saved output.
- check_fixed_lines.py on each of the six outputs with its own profile and workflows; a removed bank line is reported as missing (negative test).
- compact_coverage.py: every rule of core.md and the workflows is present in the saved outputs or listed as not applicable (3 rules: the document follow-up workflow has no saved profile; the business-type and tool-list rules are skill-level).
- build_skill_refs.py --check: the HR references and the other seven industries are in sync.
- pytest: all tests pass, including new tests for the HR profile settings, the tool-gated verification lines, the job scam block and safety lines, the no-target path and the outbound welcome.
- Output 01 was read in full. The other five were scanned with a script for rule IDs, unfilled slots, "calling from" in inbound sets, outcome words and notes that name files or tools, and spot-read (handoff, harassment and ethics lines, section 6 of the outbound and no-target sets); they were not each read line by line.

## What was not done

The tricky-caller tables of the profiles were not played as simulated calls; no safety case has been run as a conversation. The outputs test the references and the checker, not the skill's behaviour under an unseen profile. A real hands-on test through /prompt-writer is still to be done by the owner. Workflow 09 (outbound document follow-up and onboarding nudge) has no saved profile. The brief's NICE items are not in v1.

## Known items

- Section 1 is about 1,100 to 1,200 words in the inbound sets (no limit is set since DECISIONS 125 addendum).
- The HR goal line is "Your goal: help the caller with leave, payroll dates, an application or joining, using only system data and the business facts." (DECISIONS 133). The saved outputs of all eight industries had the handoff clause removed from their goal line by text replacement, not regenerated.
- Open platform questions: what the HR lookup returns and how it checks the second detail; whether `contact_name` and `call_details` are passed on outbound calls; voicemail detection and a do-not-call tool.
- The confirmation and link flow is not in v1. Chat is later.
- The payroll amount line "I can only share published payroll dates and policies." was added to core, workflow 02 and the six saved outputs by text replacement (DECISIONS 133).
- A new rule R-39 (call recording) and R-40 (source of the number) were added beyond the brief's 38 rules, as in logistics.

## Lock

Not locked. Lock only when the owner says so.
