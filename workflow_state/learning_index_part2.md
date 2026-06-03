# Learning Index Part 2 - Weeks 3 and 4

Historical progress archive for the Python learning project.

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Scope

```text
Part 2 covers Week 3 and Week 4.
Week 3: Day 15 to Day 21 - In progress
Week 4: Day 22 to Day 28 - Not started
Current completed through: Day 17
Next: Day 18 - Regular Expressions
```

This file is the active Weeks 3-4 archive. Keep it compact. Do not turn it into a notes dump.

---

## Completed days

| Day | Week day | Topic | Status | Notes file |
|---|---:|---|---|---|
| Day 15 | Week 3 Day 1 | Python Type Errors | Cleared | `day15_notes.md` |
| Day 16 | Week 3 Day 2 | Python Date Time | Cleared | `day16_notes.md` |
| Day 17 | Week 3 Day 3 | Exception Handling | Cleared | `day17_notes.md` |
| Day 18 | Week 3 Day 4 | Regular Expressions | Next | TBD |

---

## Week 3 status

```text
Week 3 - In progress
Completed: Day 15, Day 16, Day 17
Next: Day 18
```

Week 3 currently includes:

```text
Day 15 - Python Type Errors: Cleared
Day 16 - Python Date Time: Cleared
Day 17 - Exception Handling: Cleared
Day 18 - Regular Expressions: Next
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
extracting date-only and time-only parts
strftime formatting
strptime parsing
timedelta basics
adding/subtracting time
differences between dates/datetimes
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
After import datetime, use datetime.datetime.now().
After from datetime import datetime, use datetime.now().
Do not name files datetime.py.
Use strftime() to turn date/time objects into strings.
Use strptime() to turn strings into datetime objects.
The strptime() format string must match the input string exactly.
Use %H for 24-hour input and %I with %p for AM/PM input.
Use timedelta for duration math.
Use total_seconds() when the full duration in seconds is needed.
Avoid subtracting plain time objects directly when date context matters.
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
catching specific exceptions
reading exception messages with as error
multiple except blocks
else block for success-only logic
finally block for always-run logic
safe int and float conversion
fallback value pattern
safe date parsing with strptime()
.get() for optional dictionary fields
KeyError for required dictionary fields
IndexError for invalid list index access
practical exception handling patterns
focused real-world final mixed exercise
```

Final exercise scenario:

```text
Warehouse shipment intake checker
```

Key reminders:

```text
Catch specific exceptions instead of using bare except.
Keep try blocks focused on the risky operation.
Use else for success logic after a successful try block.
Use finally for code that must always run.
Use .get() for optional dictionary fields.
Use KeyError handling when a missing required field is an error path.
Use ValueError for failed conversion/parsing cases.
Use IndexError for invalid list indexes.
Use formatted output like :.2f for money values when exact display matters.
Do not overuse try / except when a simpler safe pattern is clearer.
```

---

## Day 18 - Regular Expressions

Status:

```text
Next
```

Expected focus:

```text
regular expression basics
Python re module
raw strings for regex patterns
re.search()
re.findall()
re.match() awareness
basic character classes and quantifiers
anchors
simple groups
re.sub()
practical validation/search examples
focused final mixed exercise
```

Day 18 should stay paced one topic at a time and should not become a giant regex-reference dump.

---

## Current confidence level

```text
Day 17 cleared.
Ready for Day 18 - Regular Expressions.
```
