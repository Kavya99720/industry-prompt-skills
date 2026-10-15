# Logistics test profiles

Six synthetic profiles, courier and parcel deepest. Each is a business config, the selected workflows, client requirements, a hidden table of tricky callers (MUST and MUST NOT) and a hidden word-budget estimate. No eval (DECISIONS 108): quality is checked with check_variables.py, check_fixed_lines.py (using the profile) and a reading of each generated output against its tricky-caller table. All names, numbers and addresses are synthetic.

| # | Profile | Direction | Workflows | What it tests |
|---|---|---|---|---|
| 01 | Courier and parcel, every tool off | Inbound | 01, 02, 03, 04, 05 | No status, ETA or location without the lookup; callback notes; scam block; OTP; claims; customs; restricted goods; emergency |
| 02 | E-commerce last-mile courier, lookup on, reschedule and address change on, recorded | Inbound | 01, 02, 03, 04, 05 | Verification, read-back before an action, the not-verified line, the rate card without calculation, tool error |
| 03 | Freight forwarder and trucking, lookup on | Inbound | 06, 05, 04 | The lighter set, the business's own reference words, customs routing, claims |
| 04 | Outbound delivery update, assistant named, recorded | Outbound | 07, 08 | Welcome with disclosure and recording sentence before the question, wrong person, voicemail, stop request, source wording |
| 05 | Outbound pickup and COD call, no assistant name, not recorded, no source wording | Outbound | 07, 09 | The not-known source line, no payment on the call, COD amount from call data only |
| 06 | Warehouse and 3PL, no transfer target, rule-breaking client requests | Inbound | 06, 05 | Callback-only handling without the team phrase, refusal of unsafe client requests |

The checks read the profile's own settings (tools, recording, transfer targets, contact-source wording) through scripts/check_fixed_lines.py `--profile`.
