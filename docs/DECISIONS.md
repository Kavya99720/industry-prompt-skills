# Decisions Log

1. **Healthcare grill-me** (2026-10-07)
   - **Businesses:** Clinics/OPDs, hospitals, diagnostic labs, telehealth providers.
   - **Callers and intent:** Patients (and family) booking, rescheduling or cancelling appointments; asking for information and status; raising symptoms or urgent concerns.
   - **Channel:** Voice and chat.
   - **Languages:** English baseline. The platform language tool handles 11 languages, so the prompt must not force English replies.
   - **Prohibited behavior:** No diagnosis or medical advice. No sharing records or reports without verification. No delaying emergencies. No fee, insurance or clinical commitments.
   - **Human escalation:**
     - Emergency symptoms: emergency services plus on-duty staff.
     - Clinical questions: nurse or doctor.
     - Complaints, billing disputes and angry callers: front desk or manager.
     - Caller asks for a human: hand off.
     - If no human is available (after hours or busy): never leave the caller stuck. Take a callback number and preferred time and say when to expect the call. For emergencies always give 108/112 regardless of staff availability. For self-harm statements share the Tele-MANAS helpline 14416 and connect to staff; if the caller says they are in immediate danger, give 108/112 first, then 14416.
   - **Data collection:**
     - Collect only the minimum needed to book: patient name, phone number, preferred doctor/department, date and time, and a one-line reason for visit (department level, no detailed medical history). Insurer name is allowed. Age is allowed for new patients.
     - To share or change an existing appointment, verify identity first (registered phone number plus name or date of birth).
     - Never collect Aadhaar, PAN, card/bank/UPI details, insurance policy numbers or full medical history over the call.
     - Tell the caller why the details are needed.
   - **Industry boundaries (out of scope):** Medicine orders and refills (pharmacy). Insurance claims and payments. Prescription and medication questions (route to nurse/doctor). Lab report contents (agent may say a report is ready, never interpret it). Medical loans and EMI questions (finance).
   - **Unspecified:** Insurance/payer handling beyond collecting the insurer name; telehealth-specific behaviour; business-type differences beyond the list above.
   - **Note (2026-10-07):** 108 was changed to 108/112, and the immediate-danger order was added, to match R-09 and R-10 in industries/healthcare/brief.md.

2. **Healthcare brainstorm amendments** (2026-10-07)
   - **Age:** age is NOT collected. This supersedes entry 1, which allowed age for new patients.
   - **Confirmation channel:** after booking, the caller chooses WhatsApp or email and the agent uses their choice. For WhatsApp it uses the calling number unless the caller gives a different WhatsApp number. For email it asks for the address. An email address or alternate WhatsApp number is collected only for sending the confirmation, and is read back to confirm. Confirmations contain only doctor, date and time, with no clinical details.
   - **AI disclosure:** the agent may use a persona name (e.g. Ritu) but must never claim to be human. If asked, it says it is an AI assistant.
   - **Telehealth:** the video consultation link is sent through the caller's chosen confirmation channel, with the same safety and verification rules as in-person.
   - **Business config:** fees, timings and the list of accepted insurers/TPAs come only from business config. If not provided, the agent says staff will confirm. The agent never confirms coverage, claims or amounts.
   - **Call recording:** out of scope for now.

3. **Industry scope boundaries** (2026-10-07)
   - **Healthcare:** hospital and clinic appointments, doctors, emergencies. Medicine orders, refills and prescriptions are out of scope and go to pharmacy.
   - **Pharmacy:** medicine orders, refills, prescriptions, delivery. No dosage advice.
   - **Banking:** accounts, cards, KYC, transactions, fraud.
   - **Finance:** loans/EMIs, NBFC, insurance, investments, collections.
   - **Not yet decided:** boundaries for retail, education, logistics, hr, real-estate and travel (set in each industry's grill-me).
   - **Repository layout:** industries/<slug>/ holds brief.md, eval.json and results/. Shared rules are in docs/shared/baseline-rules.md and the eval format is in docs/shared/eval-schema.md. The industry skill folder is .claude/skills/<slug>-prompt-writer/.
