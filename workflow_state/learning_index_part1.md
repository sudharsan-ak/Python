# Learning Index Part 1 - Weeks 1 and 2

Historical progress archive for the Python learning project.

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Scope

```text
Part 1 covers Week 1 and Week 2.
Week 1: Day 1 to Day 7 - Cleared
Week 2: Day 8 to Day 14 - Cleared
Current completed through: Day 14
Next: Day 15 - Python Type Errors
```

This file is now the completed Weeks 1-2 archive. Future active progress should move into Week 3 / `learning_index_part2.md` if we decide to create it.

---

## Completed days

| Day | Topic | Status | Notes file |
|---|---|---|---|
| Day 1 | Python basics: print, comments, variables, input, f-strings | Cleared | `week1_notes.md` |
| Day 2 | Built-in functions, data types, casting, arithmetic, collections intro | Cleared | `week1_notes.md` |
| Day 3 | Operators: booleans, assignment, comparison, logical operators, precedence | Cleared | `week1_notes.md` |
| Day 4 | Strings: formatting, indexing, slicing, methods, split/join, checks | Cleared | `week1_notes.md` |
| Day 5 | Lists: creation, indexing, slicing, modifying, adding, removing, copying, joining, sorting | Cleared | `week1_notes.md` |
| Day 6 | Tuples: creation, indexing, slicing, immutability, conversion, joining, deleting, use cases | Cleared | `week1_notes.md` |
| Day 7 | Sets: uniqueness, membership, add/update, remove, conversion, operations, relationship checks | Cleared | `week1_notes.md` |
| Day 8 | Dictionaries: key-value pairs, access, get(), update, removal, views, copy, nested dictionaries | Cleared | `week2_notes.md` |
| Day 9 | Conditionals: if, else, elif, logical checks, nesting, truthy/falsy, short-hand conditionals | Cleared | `week2_notes.md` |
| Day 10 | Loops: for, while, range(), enumerate(), break, continue, loop else, nested loops | Cleared | `week2_notes.md` |
| Day 11 | Functions: def, calls, return, parameters, defaults, keyword args, *args, callbacks | Cleared | `week2_notes.md` |
| Day 12 | Modules: custom modules, import styles, aliases, built-in modules, __pycache__ | Cleared | `week2_notes.md` |
| Day 13 | Comprehensions: list, dictionary, set, generator awareness, tuple clarification, lambda awareness | Cleared | `week2_notes.md` |
| Day 14 | Higher order functions: callbacks, lambda, map(), filter(), reduce(), sorting key functions | Cleared | `week2_notes.md` |

---

## Week summaries

### Week 1 - Python Foundations

Status:

```text
Cleared
```

Notes file:

```text
week1_notes.md
```

Covered:

```text
Day 1 - Python Basics
Day 2 - Variables, Built-in Functions, Data Types
Day 3 - Operators
Day 4 - Strings
Day 5 - Lists
Day 6 - Tuples
Day 7 - Sets
```

Main Week 1 foundation:

```text
printing output
comments
variables
basic data types
input()
type conversion
arithmetic
assignment/comparison/logical operators
strings
lists
tuples
sets
choosing the right collection type
```

### Week 2 - Core Control Flow and Data Handling

Status:

```text
Cleared
```

Notes file:

```text
week2_notes.md
```

Covered:

```text
Day 8 - Dictionaries
Day 9 - Conditionals
Day 10 - Loops
Day 11 - Functions
Day 12 - Modules
Day 13 - Comprehensions
Day 14 - Higher Order Functions
```

Main Week 2 foundation:

```text
dictionaries for labeled data
conditionals for decisions
loops for repetition
functions for reusable logic
modules for splitting helper code
comprehensions for compact collection creation
higher order functions for passing behavior into functions
lambda, map(), filter(), reduce(), and sorting key functions
```

---

## Day-specific key reminders

### Day 1-7 - Week 1

```text
Use print() for output.
Use snake_case for variable names.
input() always returns text.
Convert input before numeric math.
Use f-strings for readable output.
Use == for comparison and = for assignment.
Use and/or/not for logic.
Use lists for ordered mutable data.
Use tuples for fixed grouped data.
Use sets for uniqueness and group comparisons.
```

### Day 8 - Dictionaries

```text
Use dictionaries for key-value data.
Use square brackets when a key must exist.
Use get() when a key may be missing.
in checks dictionary keys, not values.
Use update() for multiple additions/updates.
Use pop() when you need the removed value.
Use copy() for a separate top-level dictionary.
Use nested dictionaries to group related data.
```

### Day 9 - Conditionals

```text
Use if / elif / else for branching.
Indentation defines Python blocks.
Use 4 spaces.
Use and when all conditions must pass.
Use or when at least one condition can pass.
Use parentheses for mixed logic.
Use in for clean multi-value checks.
Use if value and if not value for truthy/falsy checks.
Use short-hand conditionals only for simple assignments.
```

### Day 10 - Loops

```text
Use for loops for known collections or ranges.
Use while loops when repeating until a condition changes.
range() excludes the stop value.
Use enumerate() when index and item are both needed.
Dictionaries loop through keys by default.
Use .values() for values and .items() for key-value pairs.
break stops the whole loop.
continue skips the current loop run.
Loop else runs only when no break occurs.
Nested loops multiply work.
```

### Day 11 - Functions

```text
Use def to define functions.
Calling a function runs it.
Use return for reusable values.
Functions return None by default without return.
Parameters are placeholders; arguments are actual values.
Positional arguments are matched by order.
Keyword arguments are matched by name.
Default parameters provide fallback values.
*args collects extra positional arguments into a tuple.
Pass function_name without () when passing a function.
```

### Day 12 - Modules

```text
A module is a Python file.
Import using the file name without .py.
Full module import requires module_name.function_name().
Specific imports allow direct function calls.
Aliases can rename modules or functions locally.
Avoid import * while learning.
Do not name files after built-in modules.
__pycache__ is normal and should be ignored in Git.
Save helper files before rerunning imports.
```

### Day 13 - Comprehensions

```text
List comprehension: [expression for item in iterable].
Filtering: [item for item in iterable if condition].
Transform + filter: [transformed for item in iterable if condition].
if/else before for transforms every item.
Trailing if skips items.
Dictionary comprehension uses {key: value for item in iterable}.
Set comprehension uses {expression for item in iterable}.
Parentheses create a generator expression, not a tuple.
Use tuple(...) to create a tuple from an iterable.
```

### Day 14 - Higher Order Functions

```text
Functions can be passed around as values.
Higher order functions can accept other functions as arguments.
Callbacks are functions passed into another function to be called later.
Lambda creates a tiny one-expression anonymous function.
map() transforms every item lazily.
filter() keeps matching items lazily.
reduce() reduces many values into one final value.
Import reduce with from functools import reduce.
sorted(..., key=...) sorts by a calculated value.
sorted() creates a new list; .sort() mutates the original list.
Use lambda for tiny temporary logic and def for reusable/growing logic.
```

---

## Mistakes and corrections

Recurring mistakes from Weeks 1-2 are tracked separately in:

```text
mistakes_log.md
```

This includes Python syntax traps, JavaScript habit leaks, prompt mismatches, dictionary/list/set traps, function return issues, import issues, comprehension mistakes, generator/tuple/lambda confusion, and higher order function gotchas.

---

## Current confidence level

```text
Weeks 1-2 - Cleared
Ready for Day 15 - Python Type Errors
```
