# Learn Python from Scratch

This project is for learning Python from absolute scratch using Asabeneh's 30 Days of Python repo as the backbone.

Repo:
https://github.com/Asabeneh/30-Days-Of-Python

## Core principle

Use the 30 Days of Python roadmap as the backbone, not the ceiling.

When a roadmap day naturally connects to an important Python concept that is missing or under-emphasized, include it with controlled pacing. Do not blindly skip useful concepts just because they are not explicitly listed in the repo.

## Project structure

Use one ChatGPT Project and create a separate chat for each learning day.

The project is now split into focused source files so one index does not become bloated.

Current active structure after Day 13:

```text
README.md
current_status.md
project_rules.md
python_rules.md
mistakes_log.md
learning_index_part1.md
week1_notes.md
day8_notes.md
day9_notes.md
day10_notes.md
day11_notes.md
day12_notes.md
day13_notes.md
```

After Day 14, consolidate Day 8 to Day 14 into:

```text
week2_notes.md
```

Then remove the individual Day 8 to Day 14 notes from Project Sources if possible.

Recommended structure after Week 2 consolidation:

```text
README.md
current_status.md
project_rules.md
python_rules.md
mistakes_log.md
learning_index_part1.md
week1_notes.md
week2_notes.md
```

Long-term structure:

```text
README.md
current_status.md
project_rules.md
python_rules.md
mistakes_log.md
learning_index_part1.md   # Weeks 1-2 progress archive
learning_index_part2.md   # Weeks 3-4 progress archive, when needed
week1_notes.md
week2_notes.md
week3_notes.md
week4_notes.md
day29_notes.md
day30_notes.md
```

## What each file is for

### README.md

Permanent project guide.

This file explains the file structure and how to use the project. It should only change when the workflow itself changes.

### current_status.md

Small active dashboard and source of truth for current progress.

It should include:

```text
current progress
next day
active week status
current Project Sources structure
files to read before starting
pending consolidation reminders
```

Update this at the end of every completed day.

### project_rules.md

Workflow and teaching rules.

It should include:

```text
teaching style
daily workflow
exercise rules
review rules
notes generation rules
weekly consolidation rules
Project Sources upload rules
roadmap-as-backbone rule
```

Update this only when the learning workflow changes.

### python_rules.md

Global Python coding rules learned so far.

It should include:

```text
syntax rules
style rules
collection rules
conditionals / loops / functions / modules / comprehension rules
common coding gotchas
```

Update this when a new reusable Python rule is learned.

### mistakes_log.md

Dedicated recurring mistakes and gotchas tracker.

It should include:

```text
real mistakes that are likely to repeat
prompt mismatches vs real bugs
JavaScript habit leaks
Python syntax traps
concept-specific gotchas
```

Update this only when a mistake or correction is reusable beyond the current exercise.

### learning_index_part1.md

Historical progress archive for Weeks 1-2.

It should include:

```text
completed days table for Day 1-14
Week 1 and Week 2 progress summaries
day-specific reminders from Days 1-14
confidence checkpoint
```

Right now, it covers Day 1 through Day 13 and should be finalized after Day 14.

### learning_index_part2.md

Future historical progress archive for Weeks 3-4.

Create this when Week 3 starts or when the next archive split is needed.

### weekX_notes.md

Clean consolidated study/reference notes for a 7-day block.

Each weekly notes file should include:

```text
week status
day-by-day concept summaries
key syntax
small examples only where useful
common mistakes/corrections
week-level takeaways
what to remember for the next week
```

Do not paste every daily exercise.
Do not turn weekly notes into a chat transcript.
Do not make weekly notes a huge stitched-together dump.

### dayX_notes.md

Use daily notes only for days in the current active week.

Each daily notes file should include:

```text
topics covered
key concepts
small examples only where useful
summary of exercises practiced
corrections/mistakes
final mixed exercise status
key takeaways
what to remember before the next day
```

Do not include every exercise block or full practice-file code.
Do not turn notes into a chat transcript or code dump.

## How to start a new day chat

Start a new chat inside this project and say:

```text
Check README.md and current_status.md in this project first.

Then use project_rules.md, python_rules.md, and mistakes_log.md for workflow, coding rules, and recurring mistakes.

Use learning_index_part1.md and the relevant notes files for historical progress/context.

Continue my Python learning from the project context.

Start the next day listed in current_status.md from Asabeneh's 30 Days of Python repo.

Teach me one topic at a time. Give examples and exercises. Review my code strictly but fairly before moving forward.
```

If you want to specify the day manually, use this:

```text
Check README.md and current_status.md in this project first.

Then use project_rules.md, python_rules.md, and mistakes_log.md for workflow, coding rules, and recurring mistakes.

I have completed through Day X-1. Start Day X - [Topic Name] from Asabeneh's 30 Days of Python repo.

Teach me one topic at a time. Give examples and exercises. Review my code strictly but fairly before moving forward.
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
Do not include the full final mixed exercise code unless I explicitly ask.
Do not make it a chat transcript.

Also update:
- current_status.md
- python_rules.md, if new Python rules were learned
- mistakes_log.md, if reusable mistakes/gotchas were added
- project_rules.md, only if workflow rules changed
- learning_index_part1.md or learning_index_part2.md, depending on the active archive period
```

Then download the updated files and upload them back into Project Sources.

## How to end each week

After each 7-day block is complete, consolidate the daily notes into one weekly file.

Week blocks:

```text
Week 1 -> Day 1 to Day 7
Week 2 -> Day 8 to Day 14
Week 3 -> Day 15 to Day 21
Week 4 -> Day 22 to Day 28
```

After Day 14, ask:

```text
Can you generate week2_notes.md and update README.md, current_status.md, project_rules.md, python_rules.md, and learning_index_part1.md so I can upload the consolidated weekly notes and remove the individual Day 8 to Day 14 notes?
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

During an active week, upload:

```text
dayX_notes.md
current_status.md
python_rules.md, if changed
mistakes_log.md, if changed
project_rules.md, if changed
learning_index_part1.md or learning_index_part2.md, if changed
```

Do not upload a new README every day unless the project workflow changed.

## What to upload after weekly consolidation

Upload:

```text
weekX_notes.md
current_status.md
learning_index_part1.md or learning_index_part2.md
python_rules.md, if changed
mistakes_log.md, if changed
project_rules.md, if changed
README.md, if changed
```

Then remove the individual daily files for that completed week if possible.

Example after Week 2 consolidation:

```text
KEEP:
README.md
current_status.md
project_rules.md
python_rules.md
mistakes_log.md
learning_index_part1.md
week1_notes.md
week2_notes.md

REMOVE IF POSSIBLE:
day8_notes.md
day9_notes.md
day10_notes.md
day11_notes.md
day12_notes.md
day13_notes.md
day14_notes.md
```

## Replace vs keep

Replace regularly:

```text
current_status.md
```

Replace when changed:

```text
project_rules.md
python_rules.md
mistakes_log.md
learning_index_part1.md
learning_index_part2.md
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

## Current progress source of truth

Use `current_status.md` as the source of truth for current progress.

Use `learning_index_part*.md` files for historical progress archives.

Do not use the old bloated `learning_index.md` as the active tracker anymore.
