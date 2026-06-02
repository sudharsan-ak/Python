# Day 15 Notes - Python Type Errors

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 15 focused on understanding Python type-related errors and fixing the real cause instead of randomly changing code until it runs.

Core idea:

```text
A TypeError usually means Python understands the operation, but the value types do not work together.
```

Example:

```python
age = 30
message = "Age: " + age      # TypeError: str + int
```

Better for display:

```python
message = f"Age: {age}"
```

---

# 1. TypeError basics and tracebacks

A `TypeError` happens when an operation is used with the wrong type of value.

Example:

```python
"Python" + 3
```

Python can concatenate `str + str`, but not `str + int`.

A traceback is Python's crash report. Read it in this order:

```text
1. Error type
2. Error message
3. Exact line that crashed
```

Example message:

```text
TypeError: can only concatenate str (not "int") to str
```

Meaning:

```text
Python was trying to concatenate strings, but one value was an integer.
```

Debugging rule:

```text
Do not panic when you see red text.
Find the error type, crashed line, and bad value type first.
```

---

# 2. Common unsupported operations

## String + number

Wrong:

```python
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

Rule:

```text
Display goal -> use f-string or str()
Math goal    -> use int() or float()
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

# 3. List, string, and dictionary misuse

Access pattern depends on the type:

| Type | Access pattern | Example |
|---|---|---|
| `list` | numeric index | `skills[0]` |
| `str` | numeric index or slice | `language[0]`, `language[:3]` |
| `dict` | key | `profile["name"]` |
| list of dicts | index first, then key | `students[0]["name"]` |

Common mistakes:

```python
skills["first"]      # wrong: list index should be number
language["first"]    # wrong: string index should be number
profile("name")      # wrong: calls dictionary like a function
```

Correct:

```python
skills[0]
language[0]
profile["name"]
```

For a list of dictionaries:

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

Missing dictionary keys usually cause `KeyError`, not `TypeError`.

```python
course = {"name": "Python"}
course_day = course.get("day", "Not provided")
```

---

# 4. NoneType and function return mistakes

`None` means there is no useful value.

A function returns `None` by default if it has no `return`.

Wrong when you need a reusable value:

```python
def show_name():
    print("Sudharsan")

name = show_name()   # None
```

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

Some list methods mutate the original list and return `None`.

Wrong:

```python
sorted_scores = scores.sort()
updated_skills = skills.append("Node.js")
```

Correct:

```python
scores.sort()
skills.append("Node.js")
```

Use `sorted()` when you want a new sorted list:

```python
sorted_scores = sorted(scores)
```

Avoid calling methods on `None`:

```python
city = profile.get("city", "Not provided")
print(city.upper())
```

---

# 5. Step-by-step debugging process

Use this checklist:

```text
1. Read the last line of the traceback.
2. Find the exact line that crashed.
3. Identify the operation on that line.
4. Check the involved value types.
5. Decide the fix based on the real goal.
6. Rerun and verify the output.
```

Do not just force code to run. Fix the root cause.

Bad fix:

```python
score = "85"
bonus = 5
result = str(score) + str(bonus)   # "855"
```

Correct if the goal is math:

```python
result = int(score) + bonus        # 90
```

---

# 6. isinstance() basics

`isinstance()` checks whether a value belongs to a type.

```python
isinstance("90", str)  # True
isinstance(90, int)    # True
```

Useful when mixed data needs safe conversion:

```python
scores = [80, "90", 75, "85"]
cleaned_scores = []

for score in scores:
    if isinstance(score, str):
        cleaned_scores.append(int(score))
    else:
        cleaned_scores.append(score)
```

Use a normal loop when debugging clarity matters.

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

# Day 15 takeaways

```text
Read tracebacks before changing code.
Use type() when confused.
Use f-strings for display.
Use int() or float() for numeric math.
Lists and strings use numeric indexes.
Dictionaries use keys.
Use get("key", fallback) when a dictionary key may be missing.
Functions without return return None.
append() and sort() mutate the original list and return None.
Use sorted() when you need a new sorted list.
Use isinstance() for mixed data checks when needed.
Fix the root cause, not just the crashed line.
```

Exercise design correction:

```text
Final mixed exercises should use fresh real-world scenarios instead of repeatedly using student/course/Python-learning tracker scenarios.
```

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
Choose fixes based on intent: display, math, access, mutation, or fallback.
Remember that None often comes from missing return values or methods that mutate in place.
```
