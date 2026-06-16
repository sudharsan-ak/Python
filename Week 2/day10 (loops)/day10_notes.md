# Day 10 Notes - Loops

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 10 focused on repeating work in Python with `for`, `while`, `range()`, dictionary loops, `enumerate()`, `break`, `continue`, loop `else`, and nested loops.

Core idea:

```text
Conditionals decide whether code runs.
Loops decide how many times code runs.
```

---

# 1. `for` loops

A `for` loop runs once for each item in a sequence.

```python
languages = ["JavaScript", "Python", "React"]

for language in languages:
    print(language)
```

Mental model:

```text
languages -> full collection
language  -> one item during the current loop run
```

Use plural names for collections and singular names for one item.

```python
for skill in skills:
    print(skill)
```

Avoid confusing names like:

```python
for skills in skills:
    print(skills)
```

Strings can also be looped through character by character.

```python
for letter in "Python":
    print(letter)
```

Loops can contain conditionals.

```python
for language in languages:
    if language == "Python":
        print("Python is part of my learning path")
    else:
        print(f"{language} is part of my tech stack")
```

JavaScript comparison:

```text
JavaScript -> for (const skill of skills) { ... }
Python     -> for skill in skills:
```

---

# 2. `range()`

`range()` creates numbers for a loop.

```python
for number in range(5):
    print(number)
```

This prints `0` through `4`.

Important rule:

```text
range() includes the start value and excludes the stop value.
```

Common patterns:

```python
range(5)          # 0, 1, 2, 3, 4
range(1, 6)       # 1, 2, 3, 4, 5
range(2, 11, 2)   # 2, 4, 6, 8, 10
range(5, 0, -1)   # 5, 4, 3, 2, 1
```

If counting backward, the step must be negative.

JavaScript-style counter loop:

```javascript
for (let i = 0; i < nums.length; i++) {
  console.log(nums[i]);
}
```

Python equivalent:

```python
for i in range(len(nums)):
    print(nums[i])
```

Use `range(len(...))` only when indexes are actually needed.

---

# 3. `enumerate()`

Use `enumerate()` when both the index and item are needed.

```python
topics = ["Dictionaries", "Conditionals", "Loops"]

for index, topic in enumerate(topics):
    print(f"{index}: {topic}")
```

Use `start=1` for human-friendly numbering.

```python
for index, topic in enumerate(topics, start=1):
    print(f"{index}. {topic}")
```

Comparison:

```text
dict.items()      -> key + value
enumerate(list)   -> generated index + item
```

Rule:

```text
Need only item?              for item in items
Need index + item?           for index, item in enumerate(items)
Need only/manual index use?  for index in range(len(items))
```

Prefer `enumerate()` over `range(len(...))` when both index and value are needed.

---

# 4. Dictionary loops

By default, looping over a dictionary gives keys.

```python
for key in developer_profile:
    print(key)
```

Changing the variable name does not change behavior.

```python
for value in developer_profile:
    print(value)  # still keys, not values
```

Use `.values()` for values.

```python
for value in developer_profile.values():
    print(value)
```

Use `.items()` for key-value pairs.

```python
for key, value in developer_profile.items():
    print(f"{key}: {value}")
```

JavaScript comparison:

```text
JavaScript -> Object.entries(profile)
Python     -> profile.items()
```

Key rule:

```text
The object after `in` controls what Python loops through.
The variable name after `for` does not control loop behavior.
```

---

# 5. `while` loops

A `while` loop runs as long as a condition is true.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Important parts:

```text
starting value
condition
update that eventually makes the condition false
```

Without an update, the loop may become infinite.

```python
count = 1

while count <= 5:
    print(count)  # bad: count never changes
```

Simple guide:

```text
for loop   -> known collection or count
while loop -> repeat while condition is true
```

Do not overuse `while`. If there is a list, string, dictionary, or `range()`, a `for` loop is usually cleaner.

---

# 6. `break` and `continue`

`break` stops the whole loop immediately.

```python
for language in languages:
    if language == "Python":
        print("Found Python")
        break
    print(language)
```

`continue` skips the current loop run and moves to the next one.

```python
for tool in tools:
    if tool == "Postman":
        continue
    print(tool)
```

Comparison:

```text
break    -> stop the whole loop
continue -> skip this run and keep looping
```

Be careful with `continue` inside `while` loops. If `continue` skips the counter update, the loop can become infinite.

```python
count = 1

while count <= 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1
```

Rule:

```text
In while loops, update the counter before continue if continue would skip the normal update.
```

---

# 7. Loop `else`

Loop `else` means:

```text
Run this only if the loop finished normally without hitting break.
```

```python
languages = ["JavaScript", "TypeScript", "React"]

for language in languages:
    if language == "Python":
        print("Python found")
        break
else:
    print("Python not found")
```

Key takeaway:

```text
Loop completed normally -> else runs
Loop stopped by break   -> else does not run
```

This works with both `for` and `while` loops.

---

# 8. Nested loops

A nested loop is a loop inside another loop.

```python
frontend_skills = ["HTML", "CSS"]
backend_skills = ["Node.js", "Python"]

for frontend_skill in frontend_skills:
    for backend_skill in backend_skills:
        print(f"{frontend_skill} + {backend_skill}")
```

Mental model:

```text
For each outer item,
    run the full inner loop.
```

Nested loops multiply work.

```text
outer items x inner items = total loop runs
```

Common dictionary + list nested loop:

```python
for day, topics in weekly_plan.items():
    print(f"{day}:")
    for topic in topics:
        print(f"- {topic}")
```

Good naming matters:

```text
day    -> one dictionary key
topics -> list of topics for that day
topic  -> one topic from that list
```

Avoid reusing the same loop variable name in nested loops.

---

# What was practiced

```text
looping through lists and strings
conditionals inside loops
range(stop), range(start, stop), range(start, stop, step)
counting forward and backward
range(len(...)) for index-based access
enumerate() for index + value loops
enumerate(..., start=1) for human-friendly numbering
dictionary keys, values, and items
while loops with counters
avoiding infinite loops
break and continue
continue safely inside while loops
loop else with for and while
nested loops with lists, ranges, and dictionaries
```

---

# Mistakes, prompt mismatches, and corrections

| Issue | Correction / Clarification |
|---|---|
| Asked whether `for value in profile:` loops through values | No. Dictionaries loop through keys by default. Use `.values()` for values. |
| Used plural loop variable names like `keys` and `values` | Code worked, but singular names like `key` and `value` are clearer. |
| Misleading output label like `Range 0 to 4` for a loop that printed 1 to 5 | Labels should match the actual output. |
| Initial terminal run missed `Practice round 3` | Pasted code was correct; rerunning after saving confirmed the output. |
| Repeated generic labels like `---Numbers---` | More specific labels make longer terminal output easier to scan. |
| Used `print(day + ":")` | Valid, but `print(f"{day}:")` is more consistent with f-string style. |
| Initially skipped `enumerate()` during loops | Fixed as a Day 10 addendum. Use `enumerate()` when both index and item are needed. |

---

# Final mixed exercise summary

Final scenario:

```text
Python bootcamp progress tracker
```

Practiced:

```text
for loop over a list
range()
dictionary .items()
conditionals inside loops
continue
for loop else
while loop
break
while loop else
nested loop through dictionary values
```

Final result:

```text
Cleared
```

---

# Day 10 key takeaways

```text
Use for loops to repeat work over known items.
Use while loops when repeating while a condition is true.
Use clear singular/plural naming in loops.
Dictionaries loop through keys by default.
Use .values() for dictionary values.
Use .items() for dictionary key-value pairs.
The object after in controls loop behavior.
The variable name after for does not control loop behavior.
range() excludes the stop value.
Use range(len(list_name)) only when indexes are needed.
Use enumerate(list_name) when both index and item are needed.
Use enumerate(list_name, start=1) for human-friendly numbering.
Prefer enumerate() over range(len(...)) when you need both index and value.
Every while loop needs a condition that can eventually become false.
break stops the whole loop.
continue skips the current loop run.
Be careful with continue in while loops because it can skip the counter update.
Loop else runs only when the loop finishes without break.
Nested loops run the inner loop fully for each outer loop item.
Nested loops multiply work, so use them carefully.
```

---
