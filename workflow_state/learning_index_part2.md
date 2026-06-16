# Learning Index Part 2 - Weeks 3 and 4

Historical progress archive for the Python learning project.

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Scope

```text
Part 2 covers Week 3 and Week 4.
Week 3: Day 15 to Day 21 - In progress
Week 4: Day 22 to Day 28 - Not started
Current completed through: Day 20
Next: Day 21 - Classes and Objects
```

This file is the active Weeks 3-4 archive. Keep it compact. Do not turn it into a notes dump.

---

## Completed days

| Day | Week day | Topic | Status | Notes file |
|---|---:|---|---|---|
| Day 15 | Week 3 Day 1 | Python Type Errors | Cleared | `day15_notes.md` |
| Day 16 | Week 3 Day 2 | Python Date Time | Cleared | `day16_notes.md` |
| Day 17 | Week 3 Day 3 | Exception Handling | Cleared | `day17_notes.md` |
| Day 18 | Week 3 Day 4 | Regular Expressions | Cleared | `day18_notes.md` |
| Day 19 | Week 3 Day 5 | File Handling | Cleared | `day19_notes.md` |
| Day 20 | Week 3 Day 6 | Python Package Manager | Cleared | `day20_notes.md` |
| Day 21 | Week 3 Day 7 | Classes and Objects | Next | TBD |

---

## Week 3 status

```text
Week 3 - In progress
Completed: Day 15, Day 16, Day 17, Day 18, Day 19, Day 20
Next: Day 21
```

Week 3 currently includes:

```text
Day 15 - Python Type Errors: Cleared
Day 16 - Python Date Time: Cleared
Day 17 - Exception Handling: Cleared
Day 18 - Regular Expressions: Cleared
Day 19 - File Handling: Cleared
Day 20 - Python Package Manager: Cleared
Day 21 - Classes and Objects: Next
```

---

## Day 15 - Python Type Errors

Status:

```text
Cleared
```

Notes file:

```text
day15_notes.md
```

Covered:

```text
TypeError basics
traceback reading
unsupported operations between types
string + number issues
numeric string conversion
list/string/dictionary misuse
KeyError vs TypeError awareness
NoneType errors
missing return values
methods returning None
get() fallback usage
isinstance() basics
step-by-step debugging
focused real-world final mixed exercise
```

Final exercise scenario:

```text
Order checkout debugging
```

Key reminders:

```text
Read the traceback before changing code.
Find the exact crashed line.
Check the operation and the involved types.
Use f-strings for display.
Use int() or float() for numeric math.
Use list indexes for lists and keys for dictionaries.
Use get("key", fallback) when a key may be missing.
Remember that functions without return return None.
Remember that append() and sort() mutate in place and return None.
Use isinstance() when mixed data requires type checking.
```

---

## Day 16 - Python Date Time

Status:

```text
Cleared
```

Notes file:

```text
day16_notes.md
```

Covered:

```text
Python datetime module
current date and time
date objects
time objects
datetime objects
extracting datetime attributes
strftime formatting
strptime parsing
timedelta basics
date/time differences
basic datetime comparisons
practical mini-scenarios
focused real-world final mixed exercise
```

Final exercise scenario:

```text
Invoice due-date checker
```

Key reminders:

```text
Use the correct datetime import style.
Use strftime() to format objects into strings.
Use strptime() to parse strings into datetime objects.
Match the strptime() format string exactly to the input.
Use timedelta for duration math.
Use total_seconds() when full seconds are needed.
Avoid subtracting plain time objects directly.
```

---

## Day 17 - Exception Handling

Status:

```text
Cleared
```

Notes file:

```text
day17_notes.md
```

Covered:

```text
exception basics
try / except
specific exceptions
as error messages
else for success-only logic
finally for always-run logic
safe numeric conversion
safe date parsing
.get() for optional fields
KeyError for required fields
IndexError for invalid indexes
focused real-world final mixed exercise
```

Final exercise scenario:

```text
Warehouse shipment intake checker
```

Key reminders:

```text
Catch specific exceptions.
Keep try blocks focused.
Use else for success logic.
Use finally only when something must always run.
Use .get() for optional dictionary fields.
Use KeyError when a required field is missing.
Do not overuse try / except when simple checks are clearer.
```

---

## Day 18 - Regular Expressions

Status:

```text
Cleared
```

Notes file:

```text
day18_notes.md
```

Covered:

```text
regex basics
Python re module
raw strings
re.search()
match objects and .group()
re.findall()
re.match() awareness
character classes
quantifiers
anchors
groups and extraction
re.sub() cleanup/replacement
practical validation/search/extraction examples
compact regex addendum awareness
focused real-world final mixed exercise
```

Final exercise scenario:

```text
Event registration intake parser
```

Key reminders:

```text
Use raw strings for regex patterns.
Use search() for first match, findall() for all matches, and sub() for replacement.
Check a match exists before calling .group().
Use groups to extract part of a larger match.
Use anchors when validating the whole string.
Use \. to match a real dot.
Do not hardcode exact values when the goal is parsing.
Keep regex patterns small and readable.
```

---

## Day 19 - File Handling

Status:

```text
Cleared
```

Notes file:

```text
day19_notes.md
```

Covered:

```text
file handling basics
basic file path awareness
open() and with open(...)
file modes r, w, and a
reading full content with read()
reading line by line with a file loop
writing text files
appending text files
newline handling with `\n`
encoding="utf-8" awareness
FileNotFoundError handling
safe file handling habits
focused real-world final mixed exercise
```

Final exercise scenario:

```text
Support shift handoff log
```

Key reminders:

```text
Use with open(...) as the default pattern.
Use "r" to read existing files.
Use "w" only when replacing content is intended.
Use "a" when adding to existing content.
write() does not add newlines automatically.
Opening with "w" resets content once when the file is opened.
Multiple write() calls in the same open block keep adding from the current position.
Reading a missing file raises FileNotFoundError.
Use encoding="utf-8" as a good text-file habit.
```

---

## Day 20 - Python Package Manager

Status:

```text
Cleared
```

Notes file:

```text
day20_notes.md
```

Covered:

```text
package manager basics
pip awareness
package vs module distinction
installing external packages
importing installed packages
checking installed packages with pip list
showing package details with pip show
uninstall command awareness
requirements.txt purpose
exact version pins with ==
installing from requirements.txt
pip freeze awareness
virtual environment awareness
safe package management habits
focused final mixed exercise
```

Final exercise scenario:

```text
Project setup checklist for a small API helper project
```

Key reminders:

```text
pip installs packages from the terminal.
import uses installed packages inside Python code.
Use python -m pip for clearer environment targeting.
Use requirements.txt to list project dependencies.
Use package==version for exact version pins.
Do not blindly run pip freeze in a messy environment.
Do not uninstall packages that the current project still imports.
Use virtual environments to isolate packages for real projects.
```

---

## Day 21 - Classes and Objects

Status:

```text
Next
```

Expected focus:

```text
class basics
object/instance basics
attributes
methods
self
__init__ constructor basics
creating multiple objects from one class
instance data vs shared structure
simple real-world class examples
focused final mixed exercise
```

---

## Current confidence level

```text
Day 20 cleared.
Ready for Day 21 - Classes and Objects.
```
