# HR workflows

Core rules (industries/hr/core.md) apply to every workflow. Inbound and outbound are separate Instructions sets. Word counts are the whitespace-separated words of each `main-lines` block (section 6 only; sections 1 to 5 do not count). The total for any selection must stay under 595; the generated section 6 is shorter than these drafts because a main line that only repeats a section 1 or 5 rule is dropped or cut to its trigger.

| # | Workflow | Direction | Business types | Main-lines words |
|---|---|---|---|---|
| core | Core block (UNDERSTAND, HANDOFF with routing) | both | all | 140 |
| 01 | Inbound employee requests: policy, personal data, leave (owns the inbound closing) | Inbound | all | 111 |
| 02 | Inbound payroll, resignation and exit | Inbound | all (in-house and payroll providers most) | 83 |
| 03 | Inbound candidates and hiring | Inbound | all (staffing most) | 128 |
| 04 | Inbound new joiners and onboarding | Inbound | all | 38 |
| 05 | Inbound harassment, ethics reports and distress | Inbound | all | 81 |
| 06 | Inbound managers, staffing workers and client companies, background verification (lighter set; owns the background-verification rule) | Inbound | staffing, payroll provider, training or verification vendor; managers of in-house | 80 |
| 07 | Outbound frame (identity, voicemail, stop, source, summary; owns every outbound-only fixed line) | Outbound | all | 247 |
| 08 | Outbound interview reminder | Outbound | all | 60 |
| 09 | Outbound document follow-up and onboarding nudge (owns the document rule) | Outbound | all | 63 |

## Default selections

| Business type and direction | Workflows | Section 6 estimate (words) |
|---|---|---|
| In-house HR, inbound (tools on or off) | 01, 02, 03, 04, 05 | 140 + 111 + 83 + 128 + 38 + 81 = 581 |
| Staffing or recruitment agency, inbound | 01, 03, 05, 06 | 140 + 111 + 128 + 81 + 80 = 540 |
| HR outsourcing or payroll provider, inbound | 01, 02, 05, 06 | 140 + 111 + 83 + 81 + 80 = 495 |
| Training or background-verification vendor, inbound | 01, 04, 05, 06 | 140 + 111 + 38 + 81 + 80 = 450 |
| Outbound interview reminder | 07, 08 | 140 + 247 + 60 = 447 |
| Outbound document follow-up or onboarding nudge | 07, 09 | 140 + 247 + 63 = 450 |

Workflow 01 and 05 are in every inbound set (the closing line and the safety steps). A business that wants managers handled in an in-house set adds 06 only if the budget allows; the core rules already refuse a manager's request for someone else's data or a decision. Chat is a later option and a confirmation or link flow is not part of v1 (an open item in the draft notes).

## Fixed-line check

`python scripts/check_fixed_lines.py OUTPUT.md --industry hr --references industries/hr --workflows ... --profile industries/hr/test-profiles/NN-*.md` reads every `say exactly` line of core.md and the selected workflows (once the skill's references are built, use `.claude/skills/hr-prompt-writer/references` instead). Use the profile of the output: it supplies the tool settings, the recording setting, the transfer targets and the contact-source wording.
