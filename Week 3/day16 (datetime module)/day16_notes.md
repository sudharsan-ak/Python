# Day 16 Notes - Python Date Time

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 16 focused on using Python's `datetime` module to create, read, format, parse, compare, and calculate with dates and times.

Core idea:

```text
Use datetime tools when your program needs real calendar dates, clock times, timestamps, deadlines, reminders, or durations.
```

---

# Topic 1 - datetime module and current date/time

## Import styles

Full module import:

```python
import datetime

current_datetime = datetime.datetime.now()
```

Specific class import:

```python
from datetime import datetime

current_datetime = datetime.now()
```

Important distinction:

```text
import datetime              -> datetime.datetime.now()
from datetime import datetime -> datetime.now()
```

Do not name a file `datetime.py`, because it can conflict with Python's built-in `datetime` module.

---

# Topic 2 - date, time, and datetime objects

## Core object types

```text
date      -> year, month, day only
time      -> hour, minute, second, microsecond only
datetime  -> date + time together
```

Examples:

```python
from datetime import date, time, datetime

delivery_date = date(2026, 6, 25)
delivery_time = time(15, 45)
delivery_datetime = datetime(2026, 6, 25, 15, 45)
```

## Extracting parts

```python
current_datetime = datetime.now()

current_datetime.year
current_datetime.month
current_datetime.day
current_datetime.hour
current_datetime.minute
current_datetime.second
```

These are attributes, not method calls.

```text
Correct: current_datetime.year
Wrong:   current_datetime.year()
```

## Getting date-only or time-only

```python
current_date_only = current_datetime.date()
current_time_only = current_datetime.time()
```

Remember:

```text
.year / .month / .day / .hour / .minute / .second -> attributes
.date() / .time()                                  -> methods
```

Optional helper introduced during discussion:

```python
datetime.combine(date_object, time_object)
```

It combines a separate `date` object and `time` object into one `datetime` object.

---

# Topic 3 - Formatting and parsing

## strftime() - object to string

Use `strftime()` when you already have a date/time object and want readable text.

```python
formatted = delivery_datetime.strftime("%B %d, %Y at %I:%M %p")
```

Example output:

```text
June 25, 2026 at 03:45 PM
```

## strptime() - string to datetime object

Use `strptime()` when date/time text needs to become a real `datetime` object.

```python
order_datetime = datetime.strptime("2026-07-04 18:30", "%Y-%m-%d %H:%M")
```

Core rule:

```text
strftime() -> datetime/date/time object to string
strptime() -> string to datetime object
```

## Common format codes

| Code | Meaning | Example |
|---|---|---|
| `%Y` | 4-digit year | `2026` |
| `%m` | month number | `06` |
| `%B` | full month name | `June` |
| `%b` | short month name | `Jun` |
| `%d` | day of month | `25` |
| `%H` | hour, 24-hour clock | `18` |
| `%I` | hour, 12-hour clock | `06` |
| `%M` | minute | `30` |
| `%S` | second | `00` |
| `%p` | AM/PM | `PM` |
| `%A` | full weekday name | `Thursday` |

Important correction from the final exercise:

```text
Use %H when the input hour is 24-hour style or has no AM/PM.
Use %I with %p when the input includes AM/PM.
```

Example:

```python
# Good for "2026-06-10 09:15" or "2026-06-10 18:15"
datetime.strptime(invoice_text, "%Y-%m-%d %H:%M")

# Good for "2026-06-10 09:15 AM"
datetime.strptime(invoice_text, "%Y-%m-%d %I:%M %p")
```

---

# Topic 4 - timedelta and date/time differences

## What timedelta means

A `timedelta` represents a duration.

```python
from datetime import datetime, timedelta

order_created = datetime(2026, 6, 20, 10, 30)
estimated_delivery = order_created + timedelta(days=5)
reminder = estimated_delivery - timedelta(days=1)
```

Core patterns:

```text
datetime + timedelta -> future datetime
datetime - timedelta -> past datetime
datetime - datetime  -> timedelta duration
date - date          -> timedelta duration
```

Example:

```python
delivery_duration = estimated_delivery - order_created

print(delivery_duration.days)
print(delivery_duration.total_seconds())
```

Important distinction:

```text
.days            -> whole day part
.seconds         -> leftover seconds after days are counted
.total_seconds() -> full duration converted to seconds
```

Use `total_seconds()` when you want the full duration in seconds.

## Plain time object warning

Do not subtract plain `time` objects directly for beginner date math.

```text
time(10, 30) only means 10:30 AM, not a full moment in time.
```

For duration calculations, use `datetime` objects so Python knows the actual date too.

---

# Topic 5 - Practical mini-scenarios

Topic 5 applied the Day 16 concepts in two small guided scenarios:

```text
Subscription renewal tracker
Appointment reminder
```

Practiced:

```text
fixed current datetime
datetime comparison
timedelta subtraction
strftime formatting
total_seconds()
```

This was intentionally kept smaller than the final mixed exercise.

---

# Final mixed exercise summary

Final scenario:

```text
Invoice due-date checker
```

Practiced:

```text
parsing invoice date text with strptime()
calculating due date with timedelta
calculating reminder date
checking overdue status with datetime comparison
formatting invoice dates with strftime()
printing a clean invoice summary
```

Final result:

```text
Day 16 final mixed exercise cleared.
```

---

# Mistakes and corrections from Day 16

```text
Do not mix datetime import styles unless there is a reason.
After import datetime, use datetime.datetime.now().
After from datetime import datetime, use datetime.now().
Do not name files datetime.py.
Use attributes like .year without parentheses.
Use methods like .date() and .time() with parentheses.
strftime() formats objects into strings.
strptime() parses strings into datetime objects.
The strptime() format must match the input string exactly.
Use %H for 24-hour input and %I with %p for AM/PM input.
Use timedelta for duration math.
Use total_seconds() for the full duration in seconds.
Do not subtract plain time objects directly when date context matters.
```

---

# Day 16 status

```text
Day 16 - Python Date Time: Cleared
Week 3 Day 2: Cleared
Next: Day 17 - Exception Handling
```

## What to remember before Day 17

```text
Read import style carefully before calling datetime methods.
Keep object-to-string and string-to-object conversion separate.
Use timedelta for date/time duration math.
When parsing dates, match the format string exactly to the input text.
For time differences, prefer datetime objects over plain time objects.
```
