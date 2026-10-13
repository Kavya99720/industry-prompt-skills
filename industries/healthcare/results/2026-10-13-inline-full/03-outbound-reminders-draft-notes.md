**Assumptions and defaults used**
- No language was named at intake, so the 11 platform languages stay in section 3 and the call starts in English (assumed default start language).
- No extra emergency signs were given, so only the default compact list is used.
- No services, beds or years-of-service detail was given; nothing was added to the business facts block.
- Minors may not book alone (default; not raised by the client).
- No After-the-call channel (SMS, WhatsApp or email) was chosen, so the confirmation/After-the-call flow is skipped entirely for this agent.
- Outbound closing line used is "Thank you for your time. Have a good day." (the standard outbound wording; still a proposal pending sign-off per the brief).

**Refused or adapted client requests**
- None. "Reminders only, no clinical talk, no sales" matches the Reminder workflow as written; no change was needed to honour it.
- The no-emergency-department line was adapted (not removed): it tells the caller to call 108 or 112 or go to the nearest hospital instead of naming an emergency department, since this clinic has none.

**Open questions**
- Confirm the start language for calls (defaulted to English here).
- Confirm whether `{{var.patient_name}}` and `{{var.appointment_details}}` are actually passed by the platform on outbound calls (unconfirmed platform variables).
- Confirm whether outbound calls must say "an AI assistant" up front, or whether the given welcome template is final as written.
- Confirm the outbound closing wording ("Thank you for your time. Have a good day.") with your team; it is marked a proposal in our rules.
- If you want SMS, WhatsApp or email confirmations sent after the call, tell us the channel(s) so that flow can be added.

**Word counts**
- Welcome: 16. Section 1: 756. Section 2: 222. Section 3: 176. Section 4: 149. Section 5: 618.
- Section 6: 407 words. Roster: 4 doctors x 23 = 92. Allowance: 615 - 92 = 523. Status: within budget (116 words of margin).

**Fill these in the platform**

| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | Kiran | Voice settings |
| Agent gender | Male | Voice settings |
| Start language | Not provided (defaulted to English) | Voice settings |
| Roster | Doctor A, Doctor B, Doctor C, Doctor D (names, specialties, fees and timings set here) | Doctors |
| Transfer numbers | Not provided | Transfer settings |
| After-the-call trigger channels | Not provided — flow skipped | After-the-call trigger |

If your hours, phone or address change, regenerate these Instructions.
