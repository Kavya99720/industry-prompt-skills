**Assumptions and defaults used**
- Welcome message uses the platform's default Standard inbound template; the client can switch to Warm or Brief in platform settings.
- Closing line uses the standard inbound wording ("Thank you for calling Lakeview Multispeciality Hospital. Have a good day.").
- No extra emergency signs beyond the default list, and minors may not book alone, as given.
- No telehealth or video-link option was mentioned, so the confirmation flow covers only appointment confirmations, not a link.

**Refused or adapted client requests**
- none

**Open questions**
- No transfer number was given for the emergency department or on-duty staff; the agent offers a callback instead of naming a transfer target. Give a number if calls should route directly.
- Doctor F's "On leave" status and the rest of the roster are set up in the platform's Doctors config, not typed here; please confirm the entries there match this business.
- Only inbound was requested. If the hospital also wants outbound reminder calls, that needs its own separate Instructions set.

**Word counts**
- Welcome: 15. Section 1: 852. Section 2: 316. Section 3: 158. Section 4: 148. Section 5: 1084.
- Section 6: 405 words. Roster: 8 doctors x 23 = 184. Allowance: 615 - 184 = 431. Status: within budget (26 words below the allowance).

**Fill these in the platform**
| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | Asha | Voice settings |
| Agent gender | Female | Voice settings |
| Start language | English | Voice settings |
| Roster | 8 doctors (General Physician, Orthopaedics, Obstetrics, Paediatrics, Cardiology, ENT); Doctor F set to On leave | Doctors |
| Transfer numbers | not provided | Transfer settings |
| After-the-call trigger channels | WhatsApp and email | After-the-call trigger |

Set up the After-the-call trigger for WhatsApp and email so confirmations go out once the call ends.
If your hours, phone or address change, regenerate these Instructions.
