**Assumptions and defaults used**
- Workflow: only 01 Enquiry selected, per the client's config (R-78: no timed booking at a token/walk-in clinic, so no workflow 02).
- Welcome template: Standard inbound default used; the client may change it to Warm or Brief in the platform.
- Languages: `{{var.default_language}}` set to Hindi per the client's "Hindi start" instruction; the other 10 platform languages remain available on mid-call switch (core default).
- Roster: 1 doctor confirmed by the client (Doctor A, General Physician); word budget calculated on that count.
- `{{var.confirmation_channels}}` not given by the client, so the confirmation flow (R-18) is omitted entirely, per the skill's rule to skip it when unset — there is also no booking action in this workflow for it to follow.
- `{{var.minors_may_book_alone}}` defaulted to false (not addressed by the client).
- `{{var.emergency_signs_extra}}` left empty (not addressed by the client); the compact default emergency list is used as-is.
- Agent name and gender: not given by the client; left as `{{var.agent_name}}` / `{{var.agent_gender}}` for the client to set in Voice settings.
- R-79 (admission/ward questions) omitted from section 6: this is a single-doctor OPD clinic with no inpatient wards described, so the scenario does not apply; flagged as an open item below in case that changes.

**Refused or adapted client requests**
- None refused. "Never promise a time the patient will be seen" was already required by core rule R-35/R-78 and workflow 01's TOKENS line — applied as given, not an adaptation.
- Emergency line adapted (not refused) because `{{var.emergency_department}}` = no: per R-09 it reads "we do not have an emergency department, call 1 0 8 or 1 1 2, or go to the nearest hospital" instead of naming an in-house emergency department.

**Open questions**
- Confirm the default emergency signs list with the client's clinical team (standing item, R-09).
- Confirm whether this clinic ever handles admission/ward questions; if so, R-79 needs adding back in a later run.
- Confirm `{{var.business_phone}}` and `{{var.clinic_address}}` values in the platform; neither was given in this profile.

**Word counts**
- Welcome: 16. Section 1: 372. Section 2: 129. Section 3: 123. Section 4: 100. Section 5: 227.
- Section 6: 172 words. Roster: 1 doctor x 23 = 23. Allowance: 615 - 23 = 592. Status: within budget (420 words under allowance, well past the 20-word margin).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | Hindi | Voice settings |
| `{{var.business_hours}}` | OPD morning and evening (exact hours not provided) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.business_info}}` | token system explanation (text not provided) | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (default false) | Your business, Add a detail |
| `{{var.roster}}` | Doctor A, General Physician, fee not provided | Doctors |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
