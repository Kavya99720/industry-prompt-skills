**Assumptions and defaults used**
- emergency_signs_extra: not given, default empty — only the default emergency signs list is used.
- minors_may_book_alone: not given, default false — R-40 applies as written (parent or guardian asked to call back or join).
- Services/beds/years beyond the token-system explanation: not given, folded into {{var.business_info}} as a single custom detail; if it is empty the agent says the team will confirm.
- confirmation_channels: not given — no After-the-call confirmation flow is offered or written into section 5 (none applies, since this profile has no Booking workflow in any case).
- Doctor count taken as 1 (Doctor A, General Physician), as stated in the profile.
- Business word used throughout is "our clinic," matching the single-doctor clinic business type.

**Refused or adapted client requests**
- None of the client requirements conflicted with a critical rule. "Never promise a time the patient will be seen" is already required by R-35; "tell callers timings and how tokens work" is implemented via the TOKENS line and {{var.business_info}} — no adaptation needed, both requests were honoured directly.

**Open questions**
- Whether a confirmed token-status tool exists on the platform (open question 6 in platform-contract.md); until then the agent never estimates wait or token time.
- Whether {{var.business_info}} can hold the full token-system explanation as one block of text, or needs to be split into several custom details.

**Word counts**
- Welcome: 13. Section 1: 356. Section 2: 112. Section 3: 103. Section 4: 73. Section 5: 331.
- Section 6: 190 words. Roster: 1 doctor x 23 = 23. Allowance: 615 - 23 = 592. Status: within budget (190 is well below the allowance, 402 words under).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | Hindi (callers start in Hindi) | Voice settings |
| `{{var.business_hours}}` | OPD mornings and evenings (exact hours not provided) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | filled in automatically from Variables |
| `{{var.roster}}` | Doctor A, General Physician, fee as configured | Doctors |
| `{{var.business_info}}` | Explanation of the token system (exact wording not provided) | Your business, Add a detail |
| `{{var.emergency_department}}` | no | Your business, Add a detail |
