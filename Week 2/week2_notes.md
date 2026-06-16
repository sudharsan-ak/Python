# Week 2 Notes - Core Control Flow and Data Handling

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Week 2 overview

Week 2 moved from basic collections into labeled data, decisions, repetition, reusable logic, modules, comprehensions, and higher order functions.

```text
Day 8 - Dictionaries
Day 9 - Conditionals
Day 10 - Loops
Day 11 - Functions
Day 12 - Modules
Day 13 - Comprehensions
Day 14 - Higher Order Functions
```

Main foundation:

```text
key-value data, branching logic, iteration, function design, module imports,
comprehension patterns, lambda/callbacks, map/filter/reduce, sorting key functions
```

---

# Day 8 - Dictionaries

## Core idea

Dictionaries store labeled key-value data. Use them when values need meaningful names.

## Core syntax

```python
profile = {
    "first_name": "Sudharsan",
    "last_name": "Srinivasan",
    "city": "Lewisville"
}

profile["first_name"]
profile.get("country", "Not provided")

profile["city"] = "Dallas"
profile.update({"country": "USA", "language": "Python"})

removed_language = profile.pop("language")
del profile["country"]

profile.keys()
profile.values()
profile.items()
```

Nested dictionaries:

```python
learning_profile = {
    "student": "Sudharsan",
    "course": {"name": "Python from Scratch", "status": "In progress"}
}
```

## Remember

```text
Use square brackets when a key must exist.
Use get() when a key may be missing.
in checks dictionary keys, not values.
new_dict = old_dict is a reference, not a copy.
copy() creates a separate top-level dictionary.
copy() is shallow for nested data.
```

---

# Day 9 - Conditionals

## Core idea

Conditionals let code make decisions using `if`, `elif`, `else`, logical operators, and truthy/falsy checks.

## Core syntax

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("Needs work")

if age >= 18 and has_ticket:
    print("Entry allowed")

if language in ["Python", "JavaScript"]:
    print("Relevant language")

result = "Pass" if score >= 70 else "Fail"
```

## Remember

```text
Indentation defines blocks.
Use 4 spaces.
Use elif when only one branch should run.
Use parentheses for mixed and/or logic.
Avoid: value == "A" or "B".
Use in for clean multi-value checks.
Use short-hand conditionals only for simple assignments.
```

---

# Day 10 - Loops

## Core idea

Loops repeat work. Use `for` for known collections/ranges and `while` when repeating until a condition changes.

## Core syntax

```python
for skill in skills:
    print(skill)

for number in range(1, 6):
    print(number)

for index, topic in enumerate(topics, start=1):
    print(f"{index}. {topic}")

for key in profile:
    print(key)

for value in profile.values():
    print(value)

for key, value in profile.items():
    print(f"{key}: {value}")

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

## Remember

```text
range() excludes the stop value.
Use enumerate() when index and item are both needed.
Dictionaries loop through keys by default.
Use .values() for values and .items() for key-value pairs.
Be careful with continue inside while loops because it can skip updates.
Nested loops multiply work.
```

---

# Day 11 - Functions

## Core idea

Functions package reusable logic. Day 11 covered `def`, calls, `return`, parameters, defaults, `*args`, and passing functions.

## Core syntax

```python
def greet_student():
    print("Hello")

greet_student()


def get_status():
    return "In progress"

status = get_status()


def show_student(name):
    print(f"Student: {name}")


def greet_student(name="Python Learner"):
    print(f"Hello, {name}")


def show_topics(*topics):
    for topic in topics:
        print(topic)


def apply_operation(operation, value):
    return operation(value)
```

## Remember

```text
Defining a function does not run it.
Calling a function runs it.
print() displays; return gives back a reusable value.
Functions return None by default without return.
Required parameters come before default parameters.
*args collects extra positional arguments into a tuple.
Pass function_name when passing a function.
Use function_name() when calling immediately.
```

---

# Day 12 - Modules

## Core idea

A module is a Python file. Modules help split reusable helper code from main execution code.

## Core syntax

```text
helpers.py -> module name is helpers
```

```python
import helpers
student_name = helpers.get_student_name()

from helpers import get_student_name
student_name = get_student_name()

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

math.sqrt(81)
math.pi
random.choice(items)
random.randint(70, 100)
random.shuffle(items)
datetime.datetime.now()
os.getcwd()
sys.platform
```

## Remember

```text
Import module names without .py.
Full imports require module_name.function_name().
Specific imports allow direct function calls.
Aliases rename modules/functions locally.
Avoid import * while learning.
Do not name files after built-in modules.
random.shuffle() mutates the list and returns None.
__pycache__ is normal and should be ignored in Git.
If output shows None, check print() vs return.
Save helper files before rerunning imports.
```

---

# Day 13 - Comprehensions

## Core idea

Comprehensions build collections compactly. Day 13 covered list, dictionary, set, generator expression awareness, and tuple clarification.

## Core syntax

```python
uppercase_languages = [language.upper() for language in languages]
even_numbers = [number for number in numbers if number % 2 == 0]
even_squares = [number ** 2 for number in numbers if number % 2 == 0]
score_results = ["Pass" if score >= 70 else "Fail" for score in scores]

all_topics = [topic for topic_group in weekly_topics for topic in topic_group]

language_lengths = {language: len(language) for language in languages}
unique_lengths = {len(language) for language in languages}

squares_generator = (number ** 2 for number in range(1, 6))
numbers_tuple = tuple(number for number in range(1, 6))
```

## Remember

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

## Core idea

Higher order functions work with other functions. Day 14 covered callbacks, lambda, `map()`, `filter()`, `reduce()`, and sorting with `key` functions.

## Core syntax

```python
def apply_operation(operation, value):
    return operation(value)

result = apply_operation(lambda number: number + 10, 40)

double_number = lambda number: number * 2

doubled_numbers = list(map(lambda number: number * 2, numbers))
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

from functools import reduce
total = reduce(lambda accumulator, number: accumulator + number, numbers)

names_by_length = sorted(names, key=len)
students_by_score = sorted(students, key=lambda student: student["score"])
```

Callback rule:

```text
function_name   -> pass/store function
function_name() -> call function immediately
```

## Remember

```text
Use lambda for tiny one-expression temporary logic.
Use def for named, reusable, multi-step, or growing logic.
map() transforms every item lazily.
filter() keeps matching items lazily.
Use list(), tuple(), or set() to consume map/filter results.
reduce() returns one final value directly.
Import reduce with from functools import reduce.
Prefer sum(), max(), min(), join(), or a loop when clearer than reduce().
sorted() creates a new list.
.sort() mutates the original list.
key= accepts a function, not the function call.
Python key functions extract one sorting value; JavaScript sort callbacks compare two items.
```

---

# Week 2 Big Picture

## Concept progression

```text
Day 8  -> dictionaries for labeled data
Day 9  -> conditionals for decisions
Day 10 -> loops for repetition
Day 11 -> functions for reusable logic
Day 12 -> modules for reusable files
Day 13 -> comprehensions for compact collection creation
Day 14 -> higher order functions for passing behavior into functions
```

Main progression:

```text
data -> decision -> repetition -> reusable logic -> modular code -> compact data processing -> functional-style tools
```

## Processing decision guide

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
| Reduce many values to one | `reduce()` or clearer built-in |
| Sort by a specific value | `sorted(..., key=...)` |

## Common mistakes and gotchas

| Pattern | Watch for |
|---|---|
| Dictionary missing key | Use `get()` when unsure |
| Dictionary membership | `in` checks keys, not values |
| Condition branches | Use `elif` when only one branch should run |
| Bad `or` comparison | Avoid `value == "A" or "B"` |
| Index + item loop | Use `enumerate()` |
| `continue` in `while` | Make sure updates still happen |
| Function output | Use `return` for reusable values |
| Passing functions | Pass `function_name`, not `function_name()` |
| Imports | Match imports to actual file names |
| `random.shuffle()` | Mutates list and returns `None` |
| Tuple comprehension | `(x for x in items)` is a generator, not a tuple |
| map/filter | Lazy objects; convert when a concrete collection is needed |
| reduce | Import from `functools`; do not wrap with `list()` |
| lambda | Use only for tiny temporary logic |
| sorting key | Use `key=function_name`, not `key=function_name()` |
| `.sort()` | Mutates original list and returns `None` |
