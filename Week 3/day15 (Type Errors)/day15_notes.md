# Day 15 Notes - Python Type Errors

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 15 focused on understanding and fixing Python type-related errors instead of randomly changing code until it runs.

Core idea:

```text
A TypeError usually means Python understands the operation, but the value types do not work together.
```

Example:

```python
age = 30
message = "Age: " + age
```

Python cannot concatenate `str + int` directly.

Better:

```python
message = f"Age: {age}"
```

---

# Topic 1 - TypeError basics and tracebacks

## What a TypeError means

A `TypeError` happens when an operation is used with the wrong type of value.

Common example:

```python
"Python" + 3
```

Python can concatenate strings with strings, but not strings with integers.

## Reading a traceback

A traceback is Python's crash report.

Read the most useful parts:

```text
1. Error type
2. Error message
3. Exact line that crashed
```

Example:

```text
TypeError: can only concatenate str (not "int") to str
```

This tells you Python was trying to concatenate strings, but one value was an integer.

Debugging rule:

```text
Do not panic when you see red text.
First find the error type, crashed line, and bad value type.
```

---

# Topic 2 - Unsupported operations between types

## String + number

Wrong:

```python
age = 30
message = "Age: " + age
```

Correct for display:

```python
message = f"Age: {age}"
```

or:

```python
message = "Age: " + str(age)
```

## Numeric string + number

Wrong:

```python
score = "85"
bonus = 5
final_score = score + bonus
```

Correct for math:

```python
final_score = int(score) + bonus
```

Important distinction:

```text
Display goal -> use f-string or str()
Math goal    -> convert numeric text with int() or float()
```

## List + non-list

Wrong:

```python
skills = ["Python", "React"]
updated_skills = skills + "Node.js"
```

Correct:

```python
updated_skills = skills + ["Node.js"]
```

or mutate the original list:

```python
skills.append("Node.js")
```

---

# Topic 3 - List, string, and dictionary misuse

## Access pattern depends on type

```text
list -> numeric index
str  -> numeric index or slice
dict -> key
```

Examples:

```python
skills = ["Python", "React"]
print(skills[0])

language = "Python"
print(language[0])

profile = {"name": "Sudharsan"}
print(profile["name"])
```

Wrong list access:

```python
skills["first"]
```

Wrong dictionary call:

```python
profile("name")
```

Correct dictionary access:

```python
profile["name"]
```

## List of dictionaries

```python
students = [
    {"name": "Sudharsan", "score": 90},
    {"name": "Alex", "score": 85}
]

first_name = students[0]["name"]
```

Read it as:

```text
students[0]         -> first dictionary
students[0]["name"] -> name inside that dictionary
```

## KeyError vs TypeError

Missing dictionary key usually causes `KeyError`, not `TypeError`.

```python
course = {"name": "Python"}
course["day"]
```

Safer:

```python
course_day = course.get("day", "Not provided")
```

---

# Topic 4 - NoneType and function return mistakes

## Functions return None by default

Wrong when you need a reusable value:

```python
def show_name():
    print("Sudharsan")

name = show_name()
```

`name` becomes `None` because the function printed but did not return.

Correct:

```python
def get_name():
    return "Sudharsan"

name = get_name()
```

Rule:

```text
print() is for humans.
return is for the program.
```

## Methods that return None

Some methods mutate the original object and return `None`.

Examples:

```python
scores.sort()
skills.append("Node.js")
```

Wrong:

```python
sorted_scores = scores.sort()
updated_skills = skills.append("Node.js")
```

Correct:

```python
scores.sort()
print(scores)

skills.append("Node.js")
print(skills)
```

Use `sorted()` when you want a new sorted list:

```python
sorted_scores = sorted(scores)
```

## NoneType method errors

Wrong:

```python
city = None
city.upper()
```

This fails because `None` is not a string.

Safer dictionary fallback:

```python
city = profile.get("city", "Not provided")
print(city.upper())
```

---

# Topic 5 - Debugging type errors step by step

Use this process:

```text
1. Read the last line of the traceback.
2. Find the exact line that crashed.
3. Identify the operation on that line.
4. Check the types of the values involved.
5. Decide the fix based on the real goal.
6. Rerun and verify the output.
```

Do not just force code to run. Fix the root cause.

Bad fix:

```python
score = "85"
bonus = 5
result = str(score) + str(bonus)  # "855"
```

Correct if the goal is math:

```python
result = int(score) + bonus  # 90
```

## isinstance()

`isinstance()` checks whether a value belongs to a type.

```python
isinstance("90", str)  # True
isinstance(90, int)    # True
```

Useful for mixed data:

```python
scores = [80, "90", 75, "85"]

cleaned_scores = []
for score in scores:
    if isinstance(score, str):
        cleaned_scores.append(int(score))
    else:
        cleaned_scores.append(score)
```

Compact version:

```python
cleaned_scores = [int(score) if isinstance(score, str) else score for score in scores]
```

Use the loop version when debugging clarity matters.

---

# Final mixed exercise summary

Final scenario:

```text
Order checkout debugging
```

Practiced:

```text
string + number display fixes
numeric string conversion
wrong list access
wrong dictionary access
missing dictionary keys
missing return values
methods returning None
mixed-type lists
nested dictionary access
safe fallback values
clean f-string summaries
```

Final result:

```text
Day 15 final mixed exercise cleared.
```

---

# Mistakes and corrections from Day 15

## Important corrections

```text
Do not assign .append() or .sort() expecting a new list.
Do not call .upper() on a value that may be None.
Use get("key", fallback) when a dictionary key may be missing.
Use f-strings for display instead of messy string concatenation.
Use int() or float() when the goal is numeric math.
For nested data, access the outer structure first, then the inner value.
```

## Exercise design correction

Final exercises should use fresh real-world scenarios when possible. Repeating student/course/Python-learning tracker scenarios makes practice feel artificial and repetitive.

This rule has been added to `project_rules.md`.

---

# Day 15 status

```text
Day 15 - Python Type Errors: Cleared
Week 3 Day 1: Cleared
Next: Day 16 - Python Date Time
```

## What to remember before Day 16

```text
Read tracebacks carefully.
Check the exact crashed line.
Use type() when confused.
Choose fixes based on intent: display, math, access, mutation, or fallback.
Remember that None often comes from missing return values or methods that mutate in place.
```
