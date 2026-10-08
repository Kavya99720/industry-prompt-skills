**Assumptions and defaults used**
- Outbound only, clinic ("our clinic"), time slots, 4 doctors via `{{var.roster}}`, no emergency department. Welcome is the platform outbound template; the client may change it.
- Workflow 02 is not selected, so the NEW TIME line replaces "follow BOOK". RESCHEDULE points to NEW TIME.
- Workflow 02's S2 rules on time handling (R-57, R-58, R-59) are in section 2, because reschedule uses them. Workflow 02's tool-failure rule (R-22) is in section 5, worded for the reschedule tool.
- Emergency transfer target not given. The agent transfers to on-duty staff if one exists, and otherwise gives 108/112 and offers a callback (R-81).
- Extra emergency signs: none (default). Minors may book alone: false. `{{var.business_info}}`: empty, so the team confirms any facts. Language: starts in `{{var.default_language}}`.
- Outbound closing line is the proposed wording (R-68).
- `{{var.patient_name}}` is listed in the variables table, but section 6 has no spoken line that uses it. The agent asks for the patient by name.

**Refused or adapted client requests**
- "Reminders only, no clinical talk, no sales": accepted as written. Clinical questions go to staff, no offers are made, and emergencies are still handled.
- "Emergency department: No": adapted. The emergency line now says there is no emergency department and gives 1 0 8 / 1 1 2. It is not removed (R-09, R-76).

**Open questions**
- Does the platform pass `{{var.patient_name}}` and `{{var.appointment_details}}` on outbound calls? Both are unconfirmed.
- Must outbound calls say "an AI assistant" up front?
- Does the platform support voicemail detection or a do-not-call tool?
- What is the transfer target for emergencies and staff handoff?
- The default emergency list needs review by the clinic's clinical team.

**Word counts**
- Welcome: 14. Sections 1 to 5: 1811 words combined; I could not run a per-section split here, so none is given.
- Section 6: 384 words (the roster placeholder is not counted). Roster: 4 doctors x 23 = 92. Allowance: 615 - 92 = 523. Status: within budget.
