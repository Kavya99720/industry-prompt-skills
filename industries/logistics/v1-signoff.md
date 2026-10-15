# Logistics v1 sign-off

No eval.json and no eval runs (DECISIONS 108). Quality was checked with check_variables.py, check_fixed_lines.py and a reading of each generated output against its profile. All six test profiles were generated from the logistics-prompt-writer skill's text and its references and saved in `sentence-tests/`. The outputs were composed in the main session with a generator script that follows the skill's rules; they are not independent model runs of the skill.

## Results

| Profile | Direction | Saved output | check_variables | check_fixed_lines | Section 6 words |
|---|---|---|---|---|---|
| 01 courier and parcel, every tool off | inbound | 01-courier-inbound-tools-off.md | 0 errors, 0 warnings | 26 required, 0 missing | 425 |
| 02 e-commerce courier, lookup, reschedule and address change on, recorded | inbound | 02-ecommerce-courier-inbound-lookup-on.md | 0 errors, 0 warnings | 27 required, 0 missing | 502 |
| 03 freight forwarder and trucking, lookup on (lighter set) | inbound | 03-freight-forwarder-inbound.md | 0 errors, 0 warnings | 25 required, 0 missing | 337 |
| 04 outbound delivery update, named, recorded | outbound | 04-outbound-delivery-update-named-recorded.md | 0 errors, 0 warnings | 27 required, 0 missing | 354 |
| 05 outbound pickup and COD call, no assistant name | outbound | 05-outbound-pickup-cod-no-assistant-name.md | 0 errors, 0 warnings | 27 required, 0 missing | 363 |
| 06 warehouse and 3PL, no transfer target, four rule-breaking client requests | inbound | 06-warehouse-inbound-client-requests-refused.md | 0 errors, 0 warnings | 22 required, 0 missing | 246 |

Section 6 is under the 595-word budget on every profile. The checker reads each profile's own settings (tools, recording, transfer targets, contact-source wording). Profile 06's four requests (a guaranteed delivery time, taking a storage fee by UPI on the call, saying a scam call was not from the business, giving a status from memory) are refused and listed in its draft notes. No output contains a rule ID, a slot left unfilled, or "calling from" in an inbound set; the words "booked", "rescheduled", "refunded", "cancelled", "approved" and "scheduled" appear only inside rules that forbid them.

## Manual tests done

- check_variables.py on industries/logistics (0 errors) and with --include-docs (the same 34 existing errors in docs as before, none new, leakage 0).
- check_fixed_lines.py on each of the six outputs with its own profile and workflows.
- build_skill_refs.py --check: the logistics references and the six other industries are in sync.
- pytest: all tests pass, including new tests for the logistics profile settings, the tool-gated verification lines, the scam block lines, the no-target path, and the goal, done condition and interruptions lines.
- Output 02 was read in full against its tricky-caller table (verification, the scam block order, the OTP stop line, the COD and payment lines, the claim line, the customs and restricted-goods lines, the emergency and self-harm lines). The other five were scanned with a script for rule IDs, unfilled slots, "calling from" in inbound sets, the banned outcome words and notes that name files or tools, and were checked by check_fixed_lines.py; they were not each read line by line.
- The thirteen new or adapted fixed lines were approved by the owner; the owner reviews them again in the hands-on test.

## What was not done

The tricky-caller tables of the profiles were not played as simulated calls. The checks read the Instructions text only; no safety case has been run as a conversation. The six outputs were written in the main session with the hidden caller tables known, not in an isolated skill run, so they test the references and the checker rather than the skill's behaviour under an unseen profile. A real hands-on test through /prompt-writer is still to be done by the owner.

## Known items

Open platform questions stay as written in the brief: what the tracking lookup returns and how it checks the registered phone or the receiver name (assumed: one lookup gives the match plus status, location, ETA and COD fields), whether `contact_name`, `tracking_number` and `call_details` are passed on outbound calls, voicemail detection and a do-not-call tool, and whether reschedule, pickup request and address change tools exist (all off by default). The confirmation and link flow is not in v1 and is listed as an open item in every draft note. Driver check-in calls are v2. The bank line is taken from retail and education because banking has no separate one. The recording line follows the other industries (a yes/no intake question; outbound, before "Is this a good time to talk?").

## Lock

Logistics is locked in `.claude/locked-industries.json`. Before locking, the OTP rule gained one sentence (never read out, repeat or resend any OTP, including the delivery OTP, even if the tracking result shows one; if asked, say it is sent only to the registered phone). References were rebuilt, pytest passed, and check_variables and check_fixed_lines passed on the six saved profiles and on outputs/swift-courier-test.md (a hands-on /prompt-writer test). Unlock only when the owner says "unlock logistics".
