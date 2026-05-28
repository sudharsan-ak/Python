# Week 2 Notes - Core Control Flow and Data Handling

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## What Week 2 covered

Week 2 moved from basic collections into real Python control flow, reusable logic, modules, comprehensions, and higher order functions.

Completed topics:

```text
Day 8 - Dictionaries
Day 9 - Conditionals
Day 10 - Loops
Day 11 - Functions
Day 12 - Modules
Day 13 - Comprehensions
Day 14 - Higher Order Functions
```

Main foundation built:

```text
key-value data
branching logic
iteration
function design
module imports
comprehension patterns
lambda and callbacks
map/filter/reduce
sorting with key functions
```

---

# Day 8 - Dictionaries

## Main goal

Day 8 focused on dictionaries: Python's key-value collection type.

```python
profile = {
    "first_name": "Sudharsan",
    "last_name": "Srinivasan",
    "city": "Lewisville"
}
```

Use a dictionary when values need meaningful labels.

## Core patterns

Access existing keys with square brackets:

```python
profile["first_name"]
```

Use `get()` when a key may be missing:

```python
profile.get("country", "Not provided")
```

Add or update values:

```python
profile["city"] = "Dallas"
profile.update({"country": "USA", "language": "Python"})
```

Remove values:

```python
removed_language = profile.pop("language")
removed_state = profile.pop("state", "Not found")
del profile["country"]
```

Inspect dictionary data:

```python
profile.keys()
profile.values()
profile.items()
```

Copying rule:

```text
new_dict = old_dict  -> same reference
old_dict.copy()      -> separate top-level dictionary
```

Nested dictionaries group related data:

```python
learning_profile = {
    "student": "Sudharsan",
    "course": {
        "name": "Python from Scratch",
        "status": "In progress"
    }
}
```

## Key reminders

```text
Dictionaries store key-value pairs.
Use get() for safe fallback values.
in checks dictionary keys, not values.
copy() is shallow for nested data.
Use dictionaries when values need labels.
```

---

# Day 9 - Conditionals

## Main goal

Day 9 focused on decision-making with `if`, `elif`, `else`, logical operators, truthy/falsy checks, and short-hand conditionals.

## Core patterns

Basic conditional:

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Multiple branches:

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("Needs work")
```

Logical conditions:

```python
if age >= 18 and has_ticket:
    print("Entry allowed")
```

Use `in` for cleaner multi-value checks:

```python
if language in ["Python", "JavaScript"]:
    print("Relevant language")
```

Truthy/falsy checks:

```python
if project_name:
    print("Project saved")
else:
    print("Project name required")
```

Short-hand conditional:

```python
result = "Pass" if score >= 70 else "Fail"
```

## Key reminders

```text
Indentation defines blocks.
Use 4 spaces.
Use elif when only one branch should run.
Use parentheses for mixed and/or logic.
Avoid the bad pattern: value == "A" or "B".
Use short-hand conditionals only for simple assignments.
```

---

# Day 10 - Loops

## Main goal

Day 10 focused on repeating work with `for`, `while`, `range()`, dictionary loops, loop control, loop `else`, and nested loops.

## Core patterns

Loop through a list:

```python
for skill in skills:
    print(skill)
```

Loop through numbers:

```python
for number in range(1, 6):
    print(number)
```

Use `enumerate()` when index and value are both needed:

```python
for index, topic in enumerate(topics, start=1):
    print(f"{index}. {topic}")
```

Dictionary loops:

```python
for key in profile:
    print(key)

for value in profile.values():
    print(value)

for key, value in profile.items():
    print(f"{key}: {value}")
```

`while` loop:

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

Loop control:

```text
break    -> stop the whole loop
continue -> skip current run and continue
```

Loop `else` runs only when the loop finishes without `break`.

## Key reminders

```text
Use for loops for known collections or ranges.
Use while loops when repeating until a condition changes.
Dictionaries loop through keys by default.
range() excludes the stop value.
Use enumerate() over range(len(...)) when you need index + value.
Be careful with continue inside while loops.
Nested loops multiply work.
```

---

# Day 11 - Functions

## Main goal

Day 11 focused on defining reusable logic with `def`, calling functions, returning values, parameters, default arguments, `*args`, and callback basics.

## Core patterns

Define and call a function:

```python
def greet_student():
    print("Hello")


greet_student()
```

`print()` vs `return`:

```python
def get_status():
    return "In progress"

status = get_status()
```

Parameters and arguments:

```python
def show_student(name):
    print(f"Student: {name}")
```

Default parameter:

```python
def greet_student(name="Python Learner"):
    print(f"Hello, {name}")
```

`*args`:

```python
def show_topics(*topics):
    for topic in topics:
        print(topic)
```

Function as a parameter:

```python
def apply_operation(operation, value):
    return operation(value)
```

## Key reminders

```text
Calling a function runs it.
Defining a function does not run it.
Use return for reusable values.
Functions return None by default without return.
Required parameters come before default parameters.
*args collects positional arguments into a tuple.
Pass function_name when passing a function.
Use function_name() when calling immediately.
```

---

# Day 12 - Modules

## Main goal

Day 12 focused on splitting code into separate files and importing reusable code.

## Core patterns

A module is a Python file.

```text
helpers.py -> module name is helpers
```

Full module import:

```python
import helpers
student_name = helpers.get_student_name()
```

Specific function import:

```python
from helpers import get_student_name
student_name = get_student_name()
```

Aliases:

```python
import helpers as helper_tools
from helpers import format_topic_summary as format_summary
```

Built-in modules practiced:

```python
import math
import random
import datetime
import os
import sys
```

Important examples:

```python
math.sqrt(81)
math.pi
random.choice(items)
random.randint(70, 100)
random.shuffle(items)
datetime.datetime.now()
os.getcwd()
sys.platform
```

## Key reminders

```text
Import module names without .py.
Full imports require module_name.function_name().
Specific imports allow direct function calls.
Avoid import * while learning.
Do not name files after built-in modules.
random.shuffle() mutates the list and returns None.
__pycache__ is normal and should be ignored in Git.
If output shows None, check print() vs return.
```

---

# Day 13 - Comprehensions

## Main goal

Day 13 used list comprehension as the backbone but expanded into comprehensions more broadly: list, dictionary, set, generator expression awareness, tuple clarification, and light lambda awareness.

## Core patterns

List comprehension:

```python
uppercase_languages = [language.upper() for language in languages]
```

Filtering:

```python
even_numbers = [number for number in numbers if number % 2 == 0]
```

Transform + filter:

```python
even_squares = [number ** 2 for number in numbers if number % 2 == 0]
```

If/else transformation:

```python
score_results = ["Pass" if score >= 70 else "Fail" for score in scores]
```

Nested flattening:

```python
all_topics = [topic for topic_group in weekly_topics for topic in topic_group]
```

Dictionary comprehension:

```python
language_lengths = {language: len(language) for language in languages}
```

Set comprehension:

```python
unique_lengths = {len(language) for language in languages}
```

Generator expression:

```python
squares_generator = (number ** 2 for number in range(1, 6))
```

Tuple clarification:

```python
numbers_tuple = tuple(number for number in range(1, 6))
```

## Key reminders

```text
[] creates a list comprehension.
{} with one expression creates a set comprehension.
{} with key: value creates a dictionary comprehension.
() with comprehension-like syntax creates a generator expression.
Python does not have true tuple comprehension.
Use tuple(...) to create a tuple from an iterable.
Trailing if filters/skips items.
if/else before for transforms every item.
Nested comprehension order follows normal nested loop order.
If a comprehension gets hard to read, use a normal loop.
```

---

# Day 14 - Higher Order Functions

## Main goal

Day 14 focused on functions that work with other functions: callbacks, lambda, `map()`, `filter()`, `reduce()`, and sorting with `key` functions.

## Core patterns

Higher order function:

```python
def apply_operation(operation, value):
    return operation(value)
```

Callback rule:

```text
function_name   -> pass/store function
function_name() -> call function immediately
```

Lambda:

```python
double_number = lambda number: number * 2
```

Inline lambda callback:

```python
result = apply_operation(lambda number: number + 10, 40)
```

`map()` transforms:

```python
doubled_numbers = list(map(lambda number: number * 2, numbers))
```

`filter()` keeps/removes:

```python
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
```

`reduce()` creates one final value:

```python
from functools import reduce

total = reduce(lambda accumulator, number: accumulator + number, numbers)
```

Sorting with key:

```python
names_by_length = sorted(names, key=len)
students_by_score = sorted(students, key=lambda student: student["score"])
```

## Key reminders

```text
Use lambda for tiny one-expression temporary logic.
Use def for named, reusable, multi-step, or growing logic.
map() and filter() return lazy iterable objects.
Use list(), tuple(), or set() to consume map/filter results.
reduce() returns the final value directly.
Import reduce with from functools import reduce.
Do not use JavaScript-style import syntax.
Prefer sum(), max(), min(), join(), or a loop when clearer than reduce().
sorted() creates a new list.
.sort() mutates the original list.
key= accepts a function, not the function call.
Python key functions extract one sorting value; JavaScript sort callbacks compare two items.
```

---

# Week 2 Big Picture

## How the concepts connect

```text
Day 8 dictionaries    -> labeled data
Day 9 conditionals    -> decisions
Day 10 loops          -> repetition
Day 11 functions      -> reusable logic
Day 12 modules        -> reusable files
Day 13 comprehensions -> compact collection creation
Day 14 HOFs           -> functions passed into other functions
```

The main progression:

```text
data -> decision -> repetition -> reusable logic -> modular code -> compact data processing -> functional-style tools
```

## Collection and processing guide

| Need | Use |
|---|---|
| Labeled values | `dict` |
| Branching | `if / elif / else` |
| Repeat through known items | `for` |
| Repeat while condition changes | `while` |
| Reusable logic | `def` |
| Split helper code into files | modules/imports |
| Build a new list/dict/set compactly | comprehension |
| Tiny temporary function | `lambda` |
| Transform each item lazily | `map()` |
| Keep matching items lazily | `filter()` |
| Reduce many values to one | `reduce()` or a clearer built-in |
| Sort by a specific value | `sorted(..., key=...)` |

## Recurring mistakes to watch

```text
Use get() when a dictionary key may be missing.
Remember dictionary in checks keys.
Use elif when only one branch should run.
Avoid bad or comparisons like value == "A" or "B".
Use enumerate() when index and item are both needed.
Be careful with continue inside while loops.
Use return when a function should produce a reusable value.
Pass function_name without parentheses when passing a function.
Keep imports matched to actual file names.
Avoid import *.
Remember random.shuffle() returns None.
Do not confuse generator expressions with tuple/list comprehensions.
Use list comprehension brackets when the prompt asks for list comprehension.
Use lambda only for tiny one-expression logic.
Use from functools import reduce, not JavaScript-style import syntax.
Remember map/filter are lazy, reduce is not.
Use key=function_name, not key=function_name().
```

## Week 2 final status

```text
Week 2 - Cleared
Ready for Day 15 - Python Type Errors
```
