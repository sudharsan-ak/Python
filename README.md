# Learn Python from Scratch

This project is for learning Python from scratch using Asabeneh's 30 Days of Python as the backbone.

Repo:
https://github.com/Asabeneh/30-Days-Of-Python

## Core principle

Use the roadmap as the backbone, not the ceiling.

When a roadmap day naturally connects to an important Python concept that is missing or under-emphasized, include it with controlled pacing instead of blindly skipping it.

## Source of truth

```text
current_status.md
```

Use `current_status.md` for:

```text
current progress
next day
active week status
files to read before starting
pending cleanup or consolidation reminders
```

## File map

```text
README.md                  -> lightweight project map
current_status.md          -> active progress source of truth
project_rules.md           -> workflow, teaching, review, notes, and upload rules
python_rules.md            -> Python coding rules learned so far
mistakes_log.md            -> recurring mistakes, prompt mismatches, and gotchas
learning_index_part*.md    -> historical progress archives
weekX_notes.md             -> consolidated weekly study notes
dayX_notes.md              -> active-week daily notes only
```

## New chat startup prompt

Use this pattern when starting a new learning chat:

```text
Check README.md and current_status.md first.

Then read the files listed in current_status.md.

Continue my Python learning from the project context.

Start from the next day listed in current_status.md.

Before starting anything, confirm the current status, summarize what the day is expected to cover, and wait for me to tell you what to do.

Do not automatically start Topic 1.
```

Add any day-specific instruction after that prompt only when needed.

## Maintenance rule

Keep this README small.

Do not put workflow details, coding rules, mistakes, daily notes instructions, or upload/consolidation rules here. Those belong in the dedicated files listed above.
