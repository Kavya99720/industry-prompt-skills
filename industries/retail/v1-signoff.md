# Retail v1 sign-off

No eval.json and no eval runs (DECISIONS 108). Quality was checked with check_variables.py, check_fixed_lines.py and a reading of each generated output against its profile. All six test profiles were generated from the retail-prompt-writer skill's text and its references and saved in `sentence-tests/`.

## Results

| Profile | Direction | Saved output | check_variables | check_fixed_lines | Section 6 words |
|---|---|---|---|---|---|
| 01 single store inbound, every tool off | inbound | 01-single-store-inbound.md | 0 errors, 0 warnings | 20 required, 0 missing | 317 |
| 02 e-commerce inbound, order lookup on | inbound | 02-ecommerce-inbound-order-lookup.md | 0 errors, 0 warnings | 30 required, 0 missing | 437 |
| 03 electronics with service and warranty, lookup off | inbound | 03-electronics-service-inbound.md | 0 errors, 0 warnings | 24 required, 0 missing | 475 |
| 04 outbound order update, with name, recorded | outbound | 04-outbound-order-update-with-name.md | 0 errors, 0 warnings | 25 required, 0 missing | 355 |
| 05 outbound feedback, no assistant name | outbound | 05-outbound-feedback-no-assistant-name.md | 0 errors, 0 warnings | 24 required, 0 missing | 380 |
| 06 outbound abandoned cart, one rule-breaking client request | outbound | 06-outbound-abandoned-cart.md | 0 errors, 0 warnings | 28 required, 0 missing | 355 |

Section 6 is under the 595-word budget on every profile. The checker reads each profile's own settings (tools, recording, channels, transfer targets, contact-source wording). Profile 06's request for "cart will expire today" and "stock is running out" lines is refused and listed in its draft notes; its decline path ends with "no next step has been set". Profile 04 and 06 carry no recording sentence outside the welcome rules; profile 05 and 06 never say the call is recorded.

## What was not done

The tricky-caller tables of the profiles were not played as simulated calls. The checks read the Instructions text only; no safety case has been run as a conversation. The six outputs were written in the main session from the skill's text, with the profile's hidden caller tables already known, not in isolated runs, so the checks prove the fixed lines and the structure, not how a fresh run reads the profile. Workflow 11 (repair or service-ready update) has no profile of its own and was checked by reading its rules only. The owner has not reviewed the DPDP purpose line, the After-the-call message content, the outbound closing, the scam block or the bank line with the cybercrime helpline 1 9 3 0 beyond the approval in DECISIONS 114.

## Known items

Open platform questions stay as written in the brief: what the order lookup and stock check return (assumed: one lookup gives the match plus status, delivery, refund and warranty fields), whether customer_name and call_details are passed on outbound calls, voicemail detection and a do-not-call tool, and whether a return or refund can later be raised by a tool.

## Lock

Retail is added to `.claude/locked-industries.json`. Unlock only when the owner says "unlock retail".
