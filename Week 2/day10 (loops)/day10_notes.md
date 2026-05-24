# Day 10 Notes - Loops

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## What Day 10 covered

Day 10 focused on Python loops. The goal was to learn how to repeat work using `for` loops, `while` loops, `range()`, dictionary loops, loop-control tools, loop `else`, and nested loops.

Topics covered:

```text
for loops
looping through lists
looping through strings
range()
range(start, stop, step)
counting forward and backward
range(len(...)) for index-based loops
looping through dictionary keys
looping through dictionary values
looping through dictionary items
while loops
break
continue
loop else
nested loops
final mixed exercise
```

## 1. Basic `for` loops

A `for` loop repeats code once for each item in a sequence.

```python
languages = ["JavaScript", "Python", "React"]

for language in languages:
    print(language)
```

Mental model:

```text
languages -> the full list
language  -> one item from the list during each loop run
```

Use plural names for collections and singular names for each item.

Good:

```python
for skill in skills:
    print(skill)
```

Bad:

```python
for skills in skills:
    print(skills)
```

The bad version may run, but the naming is confusing.

JavaScript comparison:

```javascript
for (const skill of skills) {
  console.log(skill);
}
```

Python:

```python
for skill in skills:
    print(skill)
```

## 2. Looping through strings

Strings are sequences of characters, so a `for` loop can walk through each character.

```python
favorite_language = "Python"

for letter in favorite_language:
    print(letter)
```

Output:

```text
P
y
t
h
o
n
```

Use a clear loop variable like `letter` or `character` when looping through strings.

## 3. Conditionals inside loops

Loops can contain conditionals.

```python
languages = ["JavaScript", "Python", "React"]

for language in languages:
    if language == "Python":
        print("Python is part of my learning path")
    else:
        print(f"{language} is part of my tech stack")
```

This combines Day 9 conditionals with Day 10 loops.

## 4. `range()` basics

`range()` creates a sequence of numbers for a loop.

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

Important:

```text
range(5) starts at 0 and stops before 5.
```

## 5. `range(start, stop)`

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

Rule:

```text
start is included
stop is excluded
```

This matches the slicing rule learned earlier.

## 6. `range(start, stop, step)`

The third value controls how much the number changes each time.

```python
for number in range(2, 11, 2):
    print(number)
```

Output:

```text
2
4
6
8
10
```

Counting backward uses a negative step.

```python
for number in range(5, 0, -1):
    print(number)
```

Output:

```text
5
4
3
2
1
```

Important:

```text
If counting backward, the step must be negative.
range(5, 0) prints nothing because the default step is +1.
```

## 7. Using `range(len(...))` for indexes

Looping directly over items is usually cleaner.

```python
tasks = ["Review notes", "Practice loops", "Submit exercise"]

for task in tasks:
    print(task)
```

But if the index is needed, use `range(len(...))`.

```python
for index in range(len(tasks)):
    print(f"{index}: {tasks[index]}")
```

Output:

```text
0: Review notes
1: Practice loops
2: Submit exercise
```

This works because `range(len(tasks))` produces valid list indexes.

## 8. Looping through dictionaries

By default, looping over a dictionary gives keys.

```python
developer_profile = {
    "name": "Sudharsan",
    "role": "Full Stack Software Engineer",
    "city": "Lewisville"
}

for key in developer_profile:
    print(key)
```

Output:

```text
name
role
city
```

Changing the loop variable name does not change behavior.

```python
for value in developer_profile:
    print(value)
```

This still loops through keys. The name `value` is misleading here.

Rule:

```text
The thing after `in` controls what Python loops through.
The variable name does not control behavior.
```

## 9. `.values()` and `.items()`

Use `.values()` when only values are needed.

```python
for value in developer_profile.values():
    print(value)
```

Use `.items()` when both keys and values are needed.

```python
for key, value in developer_profile.items():
    print(f"{key}: {value}")
```

JavaScript comparison:

```javascript
for (const [key, value] of Object.entries(profile)) {
  console.log(`${key}: ${value}`);
}
```

Python:

```python
for key, value in profile.items():
    print(f"{key}: {value}")
```

Python's `.items()` is similar to JavaScript's `Object.entries()`.

## 10. `while` loops

A `while` loop runs as long as a condition is true.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

Important parts:

```text
count = 1       -> starting value
count <= 5      -> condition
count += 1      -> update so the loop eventually stops
```

Blunt rule:

```text
Every while loop needs something inside it that can eventually make the condition false.
```

Without an update, the loop may become infinite.

## 11. `for` vs `while`

Use `for` when looping through known items or known counts.

```python
for language in languages:
    print(language)
```

Use `while` when repeating until a condition changes.

```python
attempt = 1

while attempt <= 3:
    print(f"Attempt {attempt}")
    attempt += 1
```

Simple guide:

```text
for loop   -> known collection or range
while loop -> repeat while a condition is true
```

Do not overuse `while`. If there is a list, string, dictionary, or `range()`, a `for` loop is usually cleaner.

## 12. `break`

`break` stops the whole loop immediately.

```python
languages = ["JavaScript", "TypeScript", "Python", "React"]

for language in languages:
    if language == "Python":
        print("Found Python - stopping loop")
        break
    print(language)
```

Output:

```text
JavaScript
TypeScript
Found Python - stopping loop
```

After `break`, the loop does not continue to the remaining items.

## 13. `continue`

`continue` skips the current loop run and moves to the next one.

```python
tools = ["VS Code", "Docker", "Postman", "Git"]

for tool in tools:
    if tool == "Postman":
        continue
    print(tool)
```

Output:

```text
VS Code
Docker
Git
```

Comparison:

```text
break    -> stop the whole loop
continue -> skip this one run and keep looping
```

## 14. `continue` inside `while` loops

Be careful with `continue` in `while` loops. If `continue` skips the counter update, the loop can become infinite.

Bad:

```python
count = 1

while count <= 5:
    if count == 3:
        continue
    print(count)
    count += 1
```

When `count` becomes `3`, the loop keeps continuing before `count += 1` runs.

Correct:

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

## 15. Loop `else`

Python loops can have an `else` block.

Loop `else` means:

```text
Run this only if the loop finished normally without hitting break.
```

Example where `else` runs:

```python
languages = ["JavaScript", "TypeScript", "React"]

for language in languages:
    if language == "Python":
        print("Python found")
        break
else:
    print("Python not found")
```

Because `break` never happens, the `else` block runs.

Example where `else` does not run:

```python
languages = ["JavaScript", "Python", "React"]

for language in languages:
    if language == "Python":
        print("Python found")
        break
else:
    print("Python not found")
```

Because `break` happens, the `else` block does not run.

Key takeaway:

```text
Loop completed normally -> else runs
Loop stopped by break   -> else does not run
```

## 16. Nested loops

A nested loop is a loop inside another loop.

```python
frontend_skills = ["HTML", "CSS"]
backend_skills = ["Node.js", "Python"]

for frontend_skill in frontend_skills:
    for backend_skill in backend_skills:
        print(f"{frontend_skill} + {backend_skill}")
```

Output:

```text
HTML + Node.js
HTML + Python
CSS + Node.js
CSS + Python
```

Mental model:

```text
For each outer item,
    run the full inner loop.
```

If the outer list has 3 items and the inner list has 2 items, the body runs `3 x 2 = 6` times.

Nested loops multiply work. They are fine for small examples, but careless nested loops over large data can get slow.

## 17. Nested loops with dictionaries

A common pattern is a dictionary where each key points to a list.

```python
weekly_plan = {
    "Day 8": ["Dictionaries", "Nested dictionaries"],
    "Day 9": ["Conditionals", "Truthy/falsy"],
    "Day 10": ["For loops", "While loops", "Break and continue"]
}

for day, topics in weekly_plan.items():
    print(f"{day}:")
    for topic in topics:
        print(f"- {topic}")
```

Good naming matters here:

```text
day    -> one dictionary key
topics -> list of topics for that day
topic  -> one topic from the list
```

Avoid reusing the same loop variable name in nested loops.

## What was practiced

Day 10 practice included:

```text
looping through lists
looping through strings
using conditionals inside loops
using range(stop)
using range(start, stop)
using range(start, stop, step)
counting backward with range()
using range(len(...)) for indexes
looping through dictionary keys
looping through dictionary values
looping through dictionary items
using while loops with counters
avoiding infinite loops
using break
using continue
using continue safely inside while loops
using loop else with for and while
using nested loops with lists, ranges, and dictionaries
```

## Mistakes, prompt mismatches, and corrections

| Issue | Correction / Clarification |
|---|---|
| Asked whether `for value in profile:` loops through values | No. A dictionary loops through keys by default. Use `.values()` for values. The loop variable name does not change behavior. |
| Used plural loop variable names like `keys` and `values` for one item | Code worked, but singular names like `key` and `value` are clearer because each loop run gives one item. |
| Printed a misleading section label: `Range 0 to 4` for a loop that printed 1 to 5 | Logic was correct, but labels should match output to avoid debugging confusion. |
| Initial terminal run missed `Practice round 3` | Pasted code was correct; rerunning after saving confirmed the correct output. |
| Repeated generic labels like `---Numbers---` | Not a bug, but more specific labels make longer terminal output easier to scan. |
| Used `print(day + ":")` | Valid, but `print(f"{day}:")` is more consistent with the project's f-string style. |

## Final mixed exercise status

The final mixed exercise used a fresh Python bootcamp progress tracker scenario.

It covered:

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

The final exercise was intentionally focused and not bloated. It used 16 meaningful tasks instead of repetitive filler.

Final status:

```text
Cleared
```

## Day 10 key takeaways

```text
Use for loops to repeat work over known items.
Use clear singular/plural naming in loops.
Strings can be looped through character by character.
Lists can be looped through item by item.
Dictionaries loop through keys by default.
Use .values() for dictionary values.
Use .items() for dictionary key-value pairs.
The variable name after for does not control loop behavior.
The object after in controls loop behavior.
Use range(stop) to count from 0 to stop - 1.
Use range(start, stop) when a custom start is needed.
Use range(start, stop, step) when a custom step is needed.
The stop value in range() is excluded.
Use a negative step to count backward.
Use range(len(list_name)) when indexes are needed.
Use while loops when repeating while a condition is true.
Every while loop needs a condition that can eventually become false.
Use += 1 to increment counters.
Use -= 1 to count down.
break stops the whole loop.
continue skips the current loop run.
Be careful with continue in while loops because it can skip the counter update.
Loop else runs only when the loop finishes without break.
Nested loops run the inner loop fully for each outer loop item.
Nested loops multiply work, so use them carefully.
```

## Ready for next day

```text
Day 11 - Functions
```
