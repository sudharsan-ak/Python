# Learning Index Part 1 - Weeks 1 and 2

Historical progress archive for the Python learning project.

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Scope

```text
Part 1 covers Week 1 and Week 2.
Week 1: Day 1 to Day 7 - Cleared
Week 2: Day 8 to Day 14 - In progress
Current completed through: Day 13
Next: Day 14 - Higher Order Functions
```

After Day 14 is cleared, update this file one final time with Day 14 and freeze it as the completed Weeks 1-2 archive.

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
| Day 8 | Dictionaries: key-value pairs, access, get(), update, removal, views, copy, nested dictionaries | Cleared | `day8_notes.md` |
| Day 9 | Conditionals: if, else, elif, logical checks, nesting, truthy/falsy, short-hand conditionals | Cleared | `day9_notes.md` |
| Day 10 | Loops: for, while, range(), break, continue, loop else, nested loops | Cleared | `day10_notes.md` |
| Day 11 | Functions: def, calls, return, parameters, defaults, keyword args, *args, callbacks | Cleared | `day11_notes.md` |
| Day 12 | Modules: custom modules, import styles, aliases, built-in modules, __pycache__ | Cleared | `day12_notes.md` |
| Day 13 | Comprehensions: list, dictionary, set, generator awareness, tuple clarification, lambda awareness | Cleared | `day13_notes.md` |

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
In progress
```

Current Week 2 notes:

```text
day8_notes.md
day9_notes.md
day10_notes.md
day11_notes.md
day12_notes.md
day13_notes.md
```

Completed so far:

```text
Day 8 - Dictionaries
Day 9 - Conditionals
Day 10 - Loops
Day 11 - Functions
Day 12 - Modules
Day 13 - Comprehensions
```

Next:

```text
Day 14 - Higher Order Functions
```

---

## Next day

```text
Day 14 - Higher Order Functions
```

Expected Day 14 focus:

```text
what higher order functions are
functions as values
passing functions as arguments
callbacks
lambda in detail
map()
filter()
reduce()
sorting with key functions
small anonymous functions
when to use lambda vs def
final mixed exercise
```

Later addendum reminder:

```text
Cover iterators and generators in more detail later:
iter()
next()
lazy evaluation
memory efficiency
generator expressions
generator functions
yield
```

---


---

## Mistakes and corrections

Recurring mistakes from Weeks 1-2 are tracked separately in:

```text
mistakes_log.md
```

This includes Python syntax traps, JavaScript habit leaks, prompt mismatches, comprehension mistakes, generator/tuple/lambda awareness issues, and debugging reminders.

---

## Day-specific key reminders

### Day 1

```text
Python runs line by line.
print() shows output.
Variables store values.
Strings need quotes.
Numbers usually do not.
input() always returns text.
Use int() before math with input.
```

### Day 2

```text
Use built-in functions like len(), type(), int(), float(), str().
Lists are ordered collections.
Dictionaries store key-value data.
Tuples are fixed-style grouped data.
Sets store unique values.
Assignment shortcuts like += update existing values.
% gives the remainder.
```

### Day 3

```text
Booleans are True/False.
Comparison operators return booleans.
and requires both sides to be true.
or requires at least one condition to be true.
not flips a boolean.
Parentheses make mixed logic clearer.
```

### Day 4

```text
Strings are sequences of characters.
Indexing gets one character.
Slicing gets part of a string.
Use strip(), replace(), upper(), lower(), title().
Use split() to create a list from a string.
Use join() to create a string from a list.
Use isalpha(), isdigit(), isalnum(), islower(), isupper() for checks.
```

### Day 5

```text
Lists are ordered and mutable.
Use [] to create lists.
Use indexes and slices like strings.
Use append(), insert(), and extend() to add items.
Use remove(), pop(), del, and clear() to remove items.
Use copy() for independent list copies.
Use sort() to sort the original list.
Use sorted() to create a sorted copy.
```

### Day 6

```text
Tuples are ordered and immutable.
Use () to create tuples.
A one-item tuple needs a trailing comma.
Tuple items cannot be changed directly.
Tuple variables can be reassigned to a new tuple.
Use list() to temporarily modify tuple data.
Use tuple() to convert a list back into a tuple.
Use tuples for fixed grouped data.
Use lists for data that should change.
```

### Day 7

```text
Sets store unique values.
Use {} to create a set with values.
Use set() to create an empty set.
{} by itself creates an empty dictionary.
Sets remove duplicates automatically.
Sets do not have dependable order.
Sets do not support indexing.
Use in and not in for membership checks.
Use add() to add one item.
Use update() to add multiple items.
Use remove() when the item must exist.
Use discard() when the item may not exist.
Use pop() carefully because the removed item is unpredictable.
Use clear() to empty a set.
Use del to delete the set variable.
Use set(list_or_tuple) to remove duplicates.
Use union() for everything from both sets.
Use intersection() for shared items.
Use difference() for items only in the first set.
Use symmetric_difference() for items not shared.
Use issubset(), issuperset(), and isdisjoint() for boolean relationship checks.
```

### Day 8

```text
Dictionaries store key-value pairs.
Use dictionaries when values need labels.
{} creates an empty dictionary.
Use len() to count key-value pairs.
Use square bracket access when the key must exist.
Use get() when the key might be missing.
Use get("key", default) for fallback values.
Use in to check whether a key exists.
in checks dictionary keys, not values.
Use dict["key"] = value to add or update data.
Use update() to add/update multiple key-value pairs.
Use pop() to remove a key and return its value.
Use pop("key", default) when the key may not exist.
Use del when the key exists and you do not need the removed value.
Use popitem() to remove the last inserted key-value pair.
Use clear() to empty a dictionary.
Use keys(), values(), and items() to inspect dictionary data.
Use list() to convert dictionary views when list behavior is needed.
Use copy() for a separate top-level dictionary.
copy() is shallow; nested data needs more care later.
Use nested dictionaries to group related data.
Use chained square brackets for nested dictionary access.
Use get("nested_key", {}) for safer nested access.
```

### Day 9

```text
Use if for a single condition.
Use else for the fallback path.
Use elif for multiple connected branches.
Indentation defines the block.
Use 4 spaces for standard Python indentation.
Use == for comparison, not =.
Use and when all conditions must be true.
Use or when at least one condition must be true.
Use parentheses when combining and / or.
Use not for opposite checks.
Use if value for truthy checks.
Use if not value for empty/falsy checks.
Empty strings, lists, dictionaries, tuples, sets, 0, None, and False are falsy.
Non-empty strings, lists, dictionaries, tuples, and sets are truthy.
Use if list_name to check whether a list has items.
Use if dict_name to check whether a dictionary has data.
Use if "key" in dict_name to check whether a specific key exists.
Use nested conditionals only when a second check depends on a first check.
Prefer flatter if / elif / else chains when they read cleaner.
Use short-hand conditionals only for simple two-way assignments.
Do not force complex logic into one line.
```

### Day 10

```text
Use for loops for known items or ranges.
Use while loops for condition-based repetition.
Use clear singular/plural loop variable names.
Strings loop character by character.
Dictionaries loop through keys by default.
Use .values() for values and .items() for key-value pairs.
The object after in controls behavior, not the loop variable name.
range() excludes the stop value.
Use negative step values to count backward.
Use range(len(...)) when indexes are actually needed.
Use enumerate(...) when both index and item are needed.
Use enumerate(..., start=1) for human-friendly numbering.
break stops the whole loop.
continue skips only the current loop run.
In while loops, update counters before continue when needed.
Loop else runs only when no break occurs.
Nested loops run the full inner loop for every outer item.
Nested loops multiply work and can become slow on large data.
```

### Day 11

```text
Functions group reusable logic.
Use def to define a function.
Calling a function runs it.
Use print() to display output.
Use return to produce a reusable value.
A function returns None by default without return.
Code after return does not run.
Parameters are placeholders in function definitions.
Arguments are real values passed during function calls.
Positional arguments are matched by order.
Keyword arguments are matched by parameter name.
Default parameters provide fallback values.
Required parameters come before default parameters.
Use *args for any number of positional arguments.
*args becomes a tuple inside the function.
You can loop through *args.
Use required_param, *args, default_param=value as the clean beginner pattern.
Pass function_name without () when passing a function into another function.
Use function_name() when calling the function immediately.
```

### Day 12

```text
A module is a Python file.
Use modules to separate reusable helper code from execution logic.
Import a module using the file name without .py.
Full module imports require dot notation.
Specific imports allow direct function calls.
Aliases can rename modules or functions locally.
Avoid import * while learning.
Built-in modules must be imported before use.
math provides math utilities like sqrt(), ceil(), floor(), pi, and pow().
math.pi is a value, not a function.
math.pow() returns a float; ** is usually cleaner for exponent work.
random provides random values and selection tools.
random.randint(start, end) includes the end value.
random.shuffle() mutates the original list and returns None.
datetime.datetime.now() returns the current date/time.
os.getcwd() returns the current working directory.
sys.version returns Python version information.
sys.platform returns the platform name.
Do not name your files after built-in modules.
__pycache__ is normal and should be ignored in Git.
If output shows None, check whether a function printed instead of returned, and make sure files were saved before running.
```

### Day 13

```text
Comprehensions create new collections from iterables using compact loop-like syntax.
List comprehension uses square brackets: [expression for item in iterable].
Use list comprehension for simple transformation, filtering, or transform-plus-filter cases.
Use trailing if to filter and skip non-matching items.
Use if/else before the for when every item should produce an output.
Nested list comprehension can flatten one level of nested lists.
Nested comprehension for clauses follow the same order as normal nested loops.
Dictionary comprehension uses key-value syntax: {key: value for item in iterable}.
Dictionary comprehension can use .items() when looping through existing dictionaries.
Duplicate dictionary keys overwrite earlier values.
Set comprehension uses one expression inside curly braces: {expression for item in iterable}.
Set comprehension removes duplicates and does not preserve dependable order.
Generator expressions use parentheses and produce values lazily.
Generators can be consumed once.
There is no true tuple comprehension.
Use tuple(...) to create a tuple from a generator expression or iterable.
Lambda creates a tiny one-expression anonymous function.
Use lambda lightly for awareness now; learn it properly with higher order functions.
```

---

## Current confidence level

```text
Ready for Day 14 - Higher Order Functions
```
