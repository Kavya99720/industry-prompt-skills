# Education grill-me

Date: 2026-10-14. Interview: 9 questions in the main chat (asked two at a time), then the owner's changes after the summary. Every answer below was chosen by the owner; "recommended" means the owner picked the option the interviewer suggested. Nothing here is a design: the brief and skill are the next steps.

References used: docs/DECISIONS.md (entry 108 for the no-evals plan, 109 to 115 for real estate and retail), docs/shared/.

## Answers

| # | Topic | Owner's answer |
|---|---|---|
| 1 | Businesses | All four main types: school (K-12), college or university, coaching or tuition centre, online course or edtech. One skill; the business type decides the workflows |
| 2 | Preschool or daycare | Included as a school variant (younger-child notes). Owner's change: it never confirms who may pick up a child and never changes pickup or authorised-person details by phone; the request is noted for staff |
| 3 | Callers | Parents and guardians, students, applicants |
| 4 | Channel | Voice only in v1 |
| 5 | Inbound scenarios | Admissions enquiry, fees and payment schedule, courses and batches, timings and location, documents, exam and results questions, transport, hostel, scholarship, complaints |
| 6 | Outbound scenarios | Admission follow-up, fee reminder, demo class or counselling booking, event or PTM reminder |
| 7 | Verification and student data | Per the business's rules; the default is no sharing on a call. Marks, attendance, fees, results and contact details of a student are shared only with a verified parent or guardian, or the student, as the business's rules say |
| 8 | Minor caller | Collect no personal details and ask for a parent or guardian. General information only (timings, location) |
| 9 | Fees | Published fee structure and schedule only. No dues, no payment on the call, never card, UPI or OTP. A payment link only if the business approved it |
| 10 | Child safety | An emergency. Owner's change: a child in immediate danger gets exactly "Call 1 1 2 right now." first, then Childline "1 0 9 8". Not immediate: Childline 1 0 9 8. Never investigate, never question the caller about the accused, never promise action |
| 11 | Self-harm and exam stress | Tele-MANAS 1 4 4 1 6 first, and 1 1 2 if there is immediate danger; transfer if a target exists; no counselling or advice |
| 12 | Outbound calls | Parent, guardian or applicant who gave the number; AI disclosure first, recording line before the question only if calls are recorded; stop on request; no pressure. Owner's change: a fee reminder confirms the right parent or guardian by name before any fee or due is mentioned; if someone else answers, nothing is revealed and a callback is offered; no threats, shaming or consequences ("your child will be stopped from exams") |
| 13 | Guidance and promises | Courses and eligibility are described as published. Never recommend a course. Never promise admission, a seat, results, a rank or a job. Counselling booking is offered |
| 14 | Payment links | Owner's change: only a business-approved link, only when link sending is on, never read aloud, never said to be "sent" before the tool confirms |
| 15 | Ragging, harassment, bullying | Owner's change: high priority; routed to the business's grievance or anti-ragging contact if given, else the main target; never investigated |
| 16 | Scams | Fake-admission and fee-scam warning; no Aadhaar, PAN or bank details |
| 17 | Tools | Booking (demo class or counselling), transfer, callback, send link |
| 18 | Nobody available | Offer a callback booking or a link, take name and reason; never promise a time the business has not set |
| 19 | Intake | Required: business type (school or preschool, college, coaching, edtech), call direction, name and campus or branch, address, phone, office hours, assistant name and gender, languages and start language, transfer targets (admissions, accounts or fees, transport, counsellor, grievance) or callback only. Optional: courses, classes and batches; published fee structure and schedule; admission process and dates; eligibility as published; documents list; transport routes; hostel; scholarships; student-data sharing rule (default none on call); tools on or off (booking, send link, callback); approved links; confirmation channels; calls recorded; outbound purposes; grievance or anti-ragging contact; special rules |
| 20 | Brainstorm | Run the brainstorm skill as a cross-check; save brainstorm.md and add only what is missing |
| 21 | Shared rules | All shared rules apply: interactive intake with a summary, real values printed (option B), English first in Supported with the business's start language, helpline digits in Latin digits, required safety blocks word for word, "I'll connect you to our team." inline in every transfer only when a target exists, the customer's channels exactly as given, outbound welcome with AI disclosure and the recording line before the question only if recorded, no rule IDs, plain-word notes |
| 22 | Evals | None for this industry (DECISIONS 108). Six manual test profiles instead |
