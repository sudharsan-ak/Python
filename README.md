# Learn Python from Scratch

This project is for learning Python from absolute scratch using Asabeneh's 30 Days of Python repo as the backbone.

Repo:
https://github.com/Asabeneh/30-Days-Of-Python

## Project structure

Use one ChatGPT Project and create a separate chat for each learning day.

To keep Project Sources clean, notes should be consolidated by week after each 7-day block.

Recommended long-term structure:

```text
README.md
learning_index.md
week1_notes.md      # Day 1 to Day 7
week2_notes.md      # Day 8 to Day 14, once complete
week3_notes.md      # Day 15 to Day 21, once complete
week4_notes.md      # Day 22 to Day 28, once complete
day29_notes.md
day30_notes.md
```

During an active week, keep individual daily notes for that week only.

Example after Day 8:

```text
README.md
learning_index.md
week1_notes.md
day8_notes.md
```

Example after Day 11:

```text
README.md
learning_index.md
week1_notes.md
day8_notes.md
day9_notes.md
day10_notes.md
day11_notes.md
```

After Day 14, consolidate Day 8 to Day 14 into:

```text
week2_notes.md
```

Then remove the individual Day 8 to Day 14 notes from Project Sources if possible.

## What each file is for

### README.md

Permanent project instructions.

This file should rarely change.

### learning_index.md

Short rolling progress tracker.

This should be updated at the end of every completed day.

It should include:

- days completed
- current next day
- important global rules
- recurring mistakes to watch for
- current source file structure

Do not put full lessons or long code blocks here.

Use `learning_index.md` as the source of truth for current progress.

### weekX_notes.md

Clean consolidated study/reference notes for a 7-day block.

Each weekly notes file should include:

- week status
- day-by-day concept summaries
- key syntax
- small examples only where useful
- common mistakes/corrections
- week-level takeaways
- what to remember for the next week

Do not paste every daily exercise.

Do not turn weekly notes into a chat transcript.

Do not make weekly notes a huge stitched-together dump.

### dayX_notes.md

Use daily notes only for days in the current active week.

Each daily notes file should include:

- topics covered
- key concepts
- small examples only where useful
- a short summary of exercises practiced
- corrections/mistakes
- final mixed exercise status
- key takeaways
- what to remember before the next day

Do not include every exercise block or full practice-file code.

Do not turn notes into a chat transcript or code dump.

## How to start a new day chat

Start a new chat inside this project and say:

```text
Check the README and learning_index.md in this project.

Continue my Python learning from the project context.

Start the next day listed in learning_index.md from Asabeneh's 30 Days of Python repo.

Teach me one topic at a time. Give examples and exercises. Review my code strictly but fairly before moving forward.
```

If you want to specify the day manually, use this:

```text
Check the README and learning_index.md in this project.

I have completed through Day X-1. Start Day X - [Topic Name] from Asabeneh's 30 Days of Python repo.

Teach me one topic at a time. Give examples and exercises. Review my code strictly but fairly before moving forward.
```

## How to end each day

After the final mixed exercise is reviewed and cleared, first ask:

```text
Are you ready for me to generate dayX_notes.md and update learning_index.md?
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
Do not include the full final mixed exercise code unless I explicitly ask.
Do not make it a chat transcript.

Also update learning_index.md:
- mark Day X as Cleared
- set Day X+1 as Next
- add any new global rules or recurring mistakes
- update current project source file list if needed
```

Then download both files and upload them back into Project Sources.

## How to end each week

After each 7-day block is complete, consolidate the daily notes into one weekly file.

Week blocks:

```text
Week 1 -> Day 1 to Day 7
Week 2 -> Day 8 to Day 14
Week 3 -> Day 15 to Day 21
Week 4 -> Day 22 to Day 28
```

Ask:

```text
Can you generate weekX_notes.md and update README.md and learning_index.md so I can upload the consolidated weekly notes and remove the individual day notes for that week?
```

Weekly consolidation rules:

```text
Create weekX_notes.md as clean study/reference notes.
Keep the useful concepts and examples.
Do not paste every exercise.
Do not include full practice-file code.
Do not make it a chat transcript.
Keep it organized by day plus a week-level recap.
```

After uploading the weekly file, remove that week's individual day notes from Project Sources if possible.

## What to upload into Project Sources after each day

Upload only these:

```text
dayX_notes.md
learning_index.md
```

Do not upload a new README every day.

During an active week, keep that week's individual day notes.

## What to upload after weekly consolidation

Upload:

```text
weekX_notes.md
learning_index.md
README.md
```

Then remove the individual daily files for that completed week if possible.

Example after Week 1 consolidation:

```text
KEEP:
README.md
learning_index.md
week1_notes.md
day8_notes.md

REMOVE IF POSSIBLE:
day1_notes.md
day2_notes.md
day3_notes.md
day4_notes.md
day5_notes.md
day6_notes.md
day7_notes.md
```

## Replace vs keep

Replace regularly:

```text
learning_index.md
```

Replace README only when project workflow rules change:

```text
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

## Teaching style

Use this style for every day:

- Go one topic at a time.
- Explain the concept simply.
- Compare with JavaScript when useful.
- Give small examples.
- Give exercises as copy-paste starter-code blocks.
- Review my code strictly but fairly.
- Do not move to the next topic until I clear the current one.
- Keep explanations beginner-friendly and practical.
- Call out bad habits directly.
- Separate real mistakes from optional style notes.
- If the prompt asks only to create a variable, not using it should not be counted as a mistake.
- After clearing each topic exercise, ask before moving to the next topic.
- After clearing the final mixed exercise, ask before generating notes or updating the learning index.

## Daily workflow

Every day should follow this pattern:

1. Brief recap of previous day
2. Start current day topic
3. Explain one concept
4. Give examples
5. Give one small exercise
6. Review my submitted code
7. Fix mistakes
8. Move to next concept only after clearing the current one
9. End with a focused mixed final exercise
10. Review the final mixed exercise
11. If cleared, ask whether to generate notes and update the learning index
12. Generate notes/index only after confirmation

## Coding rules for now

- Use `snake_case`.
- Use f-strings for output.
- Remember `input()` always returns a string.
- Convert before doing math.
- Use clear variable names.
- Do not hide calculated values inside misleading variable names.
- Prefer clarity over clever one-liners while learning.
- Label outputs when it helps readability.
- Use `type()` when confused about a value.
- Keep daily notes separate only during the active week.
- Consolidate completed weeks into weekly notes.

## Notes style rules

Daily and weekly notes should be clean study/reference material.

They should explain what was learned, but they should not re-create the full chat or practice files.

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

## Current progress source of truth

Use `learning_index.md` as the source of truth for current progress.

The README should not need daily edits.
