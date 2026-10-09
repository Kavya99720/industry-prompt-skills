# Healthcare v1 sign-off

Date: 2026-10-09. Base: full run 7 (industries/healthcare/results/2026-10-08-run7-full.json), 59 of 59 after the HLT-E22 re-grade (DECISIONS 39 and 40).

Changes since run 7 (DECISIONS 53 to 56): confirmation flow via the After-the-call trigger (no in-call tool), wrong-person line, full seven-item no-collect list, cancel line first, fixed symptom reply and fixed stop-calling line, INSTRUCTIONS marker in the output format. Eval unchanged.

Targeted checks after those changes:
- conf1 (confirmation, booking, closing and safety cases): 42 of 45; the three failures were fixed afterwards.
- conf2: 27 of 29; E09 and E21 fixed afterwards.
- conf3, profiles 01 to 04: 27 of 27, including E09, E21, E17, E18 and E25. Profile 05 was a harness artifact (empty Instructions from a mis-split).
- conf4, profile 05 rerun with the line-anchored split: 2 of 2 (E07 emergency, E25 no-collect), no harness errors.

Finish line: every healthcare safety case passes on every profile it runs on (E09 counts as safety). Met. No full 5-profile run was made after the changes; the status table still shows run 7 (59/59).

Open for v1.1: a full healthcare run after all of the above, and the questions for lead in docs/shared/platform-contract.md (After-the-call trigger inputs, voicemail, do-not-call, outbound AI disclosure).
