# Healthcare vocabulary and config fields

Source: industries/healthcare/brief.md (section 4 and the config references in R-xx).

## Config fields

Use these placeholders in the skill and in templates. Fill them from the customer's requirements. If a value is missing, use the default shown. A default of "none" means the prompt must say the agent treats it as unknown and tells the caller staff will confirm.

| Placeholder | Meaning | Default when missing |
|---|---|---|
| `{{var.company_name}}` | Name of the hospital, clinic or lab | none (required; ask the customer) |
| `{{var.agent_name}}` | Name the agent uses for itself | none. The brief says "a default if none" but names none, so the prompt introduces the agent as "the AI assistant of {{var.company_name}}" with no personal name |
| `{{languages}}` | Languages the agent should expect | English baseline. The prompt never forces English; it follows the caller's language |
| `{{var.roster}}` | Doctors with specialty, working days and shifts (e.g. Mon/Wed/Fri, morning 9 AM-1 PM) | none. The agent uses only what the booking system returns |
| `{{emergency_signs}}` | Emergency signs list | The 12-item default list in compliance.md under R-09 |
| `{{var.minors_may_book_alone}}` | Whether a patient under 18 may book alone | `false` |
| `{{transfer_target}}` | Who receives transfers | "on-duty staff" |
| `{{ambulance_number}}` | The hospital's own ambulance number | none. The agent gives 108/112 only |
| `{{fees}}`, `{{timings}}`, `{{prep_instructions}}`, `{{accepted_insurers}}` | Business facts the agent may state | none. The agent says staff will confirm |
| `{{departments}}`, `{{service_area}}`, `{{visiting_hours}}`, `{{discharge_time}}`, `{{payment_modes}}`, `{{packages}}` | Other business facts | none. The agent says staff will confirm |
| `{{confirmation_channels}}` | Channels for confirmations and links | WhatsApp or email, as the caller chooses |
| `{{token_system}}` | Whether the clinic issues queue tokens | `false` |
| `{{waitlist}}` | Whether the business has a waitlist | `false` |
| `{{consultation_modes}}` | In-person, online, or both | in-person |

## Numbers
- **108 / 112**: India's emergency ambulance number and national emergency number. Given for emergencies.
- **Tele-MANAS 14416**: India's national tele-mental-health helpline. Given for self-harm statements.

## Terms
- **OPD** (outpatient department): visits where the patient is not admitted. Do not call it "admission".
- **Appointment slot**: a specific doctor, date and time the system confirms. Do not say "available" unless the system says so.
- **Shift**: a doctor's working window on a working day. Booking is only within shifts.
- **Specialty**: the doctor's field (e.g. General Medicine, ENT). Suggest a specialty, never a condition.
- **Registered phone number**: the number on the patient's record, used to verify identity. It is not necessarily the calling number.
- **TPA** (third-party administrator): handles insurance claims for insurers. Name accepted insurers/TPAs only from config.
- **Token**: a queue number issued at booking. The running token is the number being served now. State only what the system provides.
- **Follow-up (review) visit**: a repeat visit to the same doctor for the same issue. Fee and validity come only from config.
- **Emergency signs list**: the symptoms that trigger the emergency response (R-09). It lives in config. The hospital's clinical team reviews it.
- **Report ready**: the report is available for collection. It says nothing about the result.
- **Telehealth / video consultation link**: sent through the chosen confirmation channel, after the same checks as in-person.
- **Business config**: everything above. Anything not in config is unknown to the agent.
- **DPDP**: India's Digital Personal Data Protection Act, 2023.
