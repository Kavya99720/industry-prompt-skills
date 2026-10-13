**Assumptions and defaults used**
- No languages were named at intake, so the 11 platform languages stay in section 3 and the call starts in English (default).
- No extra emergency signs were given, so only the default compact list is in section 1.
- No flag for minors calling alone was given, so the default applies: a minor is not treated as able to call alone, and a parent or guardian is asked for.
- No package or offer was given, so no offer line was added to section 1.
- No services, beds or years of service were given; those facts are left out of the Business facts block, and a caller who asks gets "Our team will confirm that for you."
- Booking style (time slots) was given but is not used, since Booking (workflow 02) was not selected; the standalone NEW TIME lines from workflow 03 are used for the new day and time instead.
- No After-the-call trigger channel was given, so the confirmation/send flow is skipped entirely (there is no booking workflow here either).
- The roster (4 doctors, Doctor A to Doctor D) is set on the platform's Doctors config and is never printed in the Instructions.

**Refused or adapted client requests**
- none

**Open questions**
- Whether the platform actually passes {{var.patient_name}} and {{var.appointment_details}} on this outbound call (marked unconfirmed in the platform's variable list).
- Whether the platform detects voicemail or no answer, and whether a do-not-call tool exists; until confirmed, the agent only says the fixed lines in R-45 and R-73.
- The outbound closing line ("Thank you for your time. Have a good day.") is a proposal pending sign-off.
- The default emergency signs list in section 1 needs review by the client's clinical team.
- Start language was not given; English was used as the default — confirm if a different start language is wanted.

**Word counts**
- Welcome: 16. Section 1: 708. Section 2: 233. Section 3: 176. Section 4: 151. Section 5: 524.
- Section 6: 407 words. Roster: 4 doctors x 23 = 92. Allowance: 615 - 92 = 523. Status: within budget (116 words below allowance).

**Fill these in the platform**
| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | Kiran | Voice settings |
| Agent gender | Male | Voice settings |
| Start language | Not provided (English used as default) | Voice settings |
| Roster | 4 doctors (Doctor A to Doctor D) | Doctors |
| Transfer numbers | Not provided | Transfer/escalation setup |
| After-the-call trigger channels | Not provided (flow skipped) | After-the-call trigger |

If your hours, phone or address change, regenerate these Instructions.
