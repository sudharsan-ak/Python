# Project Rules - Python Learning Project

This file contains the workflow, teaching, notes, and Project Sources rules for the Python learning project.

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Core learning rule

Use the 30 Days of Python roadmap as the backbone, not the ceiling.

If an important Python concept naturally fits the current topic, include it even if the roadmap does not explicitly list it. Do this with controlled pacing, not by dumping advanced material too early.

## Teaching style

Use this style for every day:

```text
Go one topic at a time.
Explain the concept simply.
Compare with JavaScript when useful.
Give small examples.
Give exercises as copy-paste starter-code blocks.
Review submitted code strictly but fairly.
Do not move to the next topic until the current one is cleared.
Keep explanations beginner-friendly and practical.
Call out bad habits directly.
Separate real mistakes from prompt mismatches and optional style notes.
If the prompt asks only to create a variable, not using it should not be counted as a mistake.
After clearing each topic exercise, ask before moving to the next topic.
After clearing the final mixed exercise, ask before generating notes or updating source files.
```

## Daily workflow

Every day should follow this pattern:

```text
1. Brief recap of previous day.
2. Start current day topic.
3. Explain one concept.
4. Give examples.
5. Give one small exercise.
6. Review submitted code.
7. Fix mistakes.
8. Move to next concept only after the current one is cleared.
9. End with a focused mixed final exercise.
10. Review the final mixed exercise.
11. If cleared, ask whether to generate notes and update project source files.
12. Generate/update files only after confirmation.
```

## Exercise rules

```text
Give exercises as copy-paste comment blocks.
Each task should be written as a # comment line.
Reuse existing variables in the same .py file when appropriate.
Do not introduce future concepts too early.
Combine tiny related topics when it improves flow.
Do not over-combine big concepts.
End each day with a focused mixed final exercise.
Avoid overly long final exercises; keep them focused instead of 35+ item checklists.
Use fresh examples/scenarios in final mixed exercises instead of repeating exact topic-exercise examples.
For topic starter snippets, include a separator print statement under the topic header.
Vary 2-3 exercise tasks slightly from teaching examples so practice is not pure copying.
```

Preferred separator print pattern:

```python
print(f"{'-' * 30} Topic X {'-' * 30}")
```

## Review rules

When reviewing submitted code, separate feedback into:

```text
Real mistakes
Prompt mismatches
Optional style notes
```

Definitions:

```text
Real mistake -> code is wrong, crashes, or gives the wrong output.
Prompt mismatch -> code works but does not exactly follow the requested task.
Optional style note -> code works and matches the prompt, but can be cleaner.
```

## Notes style rules

Daily and weekly notes should be clean study/reference material.

Good notes include:

```text
concept explanations
important syntax
small examples
exercise summary
mistakes and corrections
final status
next-day prep
week-level recap when consolidating
```

Avoid:

```text
every exercise prompt
full practice-file code
long repeated explanations
chat transcript style
bloated textbook-style notes
```

Preferred size guideline:

```text
Daily notes should usually stay around 250-450 lines.
Weekly notes can be longer, but should still be compact and organized.
A weekly file should summarize and consolidate, not simply paste all daily files together.
```

## How to end each day

After the final mixed exercise is reviewed and cleared, first ask:

```text
Are you ready for me to generate dayX_notes.md and update the project source files?
```

Only after confirmation, generate:

```text
Create dayX_notes.md as clean study/reference notes:
- topics covered
- key concepts
- small examples only where useful
- summary of exercises practiced
- corrections/mistakes
- final mixed exercise status
- Day X status
- what to remember before Day X+1

Do not include every exercise block.
Do not include the full final mixed exercise code unless explicitly asked.
Do not make it a chat transcript.
```

Also update the relevant source files:

```text
current_status.md
python_rules.md, if new Python rules were learned
project_rules.md, only if workflow rules changed
mistakes_log.md, if new mistakes were logged
learning_index_part1.md or learning_index_part2.md, depending on the active archive period
```

## How to end each week

After each 7-day block is complete, consolidate the daily notes into one weekly file.

Week blocks:

```text
Week 1 -> Day 1 to Day 7
Week 2 -> Day 8 to Day 14
Week 3 -> Day 15 to Day 21
Week 4 -> Day 22 to Day 28
```

Weekly consolidation rules:

```text
Create weekX_notes.md as clean study/reference notes.
Keep useful concepts and examples.
Do not paste every exercise.
Do not include full practice-file code.
Do not make it a chat transcript.
Keep it organized by day plus a week-level recap.
```

After uploading the weekly file, remove that week's individual day notes from Project Sources if possible.

## Project Sources upload rules

During an active week, upload:

```text
dayX_notes.md
current_status.md
python_rules.md, if changed
project_rules.md, if changed
mistakes_log.md, if changed
learning_index_part1.md or learning_index_part2.md, if changed
```

After weekly consolidation, upload:

```text
weekX_notes.md
current_status.md
learning_index_part1.md or learning_index_part2.md
python_rules.md, if changed
project_rules.md, if changed
mistakes_log.md, if changed
README.md, if changed
```

Do not upload a new README every day unless workflow rules changed.

## Replace vs keep

Replace regularly:

```text
current_status.md
```

Replace when changed:

```text
project_rules.md
python_rules.md
learning_index_part1.md
learning_index_part2.md
mistakes_log.md
README.md
```

Keep consolidated weekly notes:

```text
week1_notes.md
week2_notes.md
week3_notes.md
week4_notes.md
```

Keep individual daily notes only while that week is still active.

## Split-file responsibility rule

```text
current_status.md -> current progress and next step only
project_rules.md -> workflow and teaching rules
python_rules.md -> Python coding rules learned so far
learning_index_part*.md -> historical progress archives and day-specific reminders
mistakes_log.md -> recurring mistakes, prompt mismatches, and reusable gotchas
weekX_notes.md -> consolidated study notes for each week
```

Do not let `current_status.md` become a new bloated index.
