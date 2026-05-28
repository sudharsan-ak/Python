# Week 1 Notes - Python Foundations

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## What Week 1 covered

Week 1 built the foundation for writing basic Python code and choosing the right basic collection type.

Completed days:

```text
Day 1 - Python Basics
Day 2 - Variables, Built-in Functions, Data Types
Day 3 - Operators
Day 4 - Strings
Day 5 - Lists
Day 6 - Tuples
Day 7 - Sets
```

Main foundation:

```text
print()
comments
variables
basic data types
f-strings
input()
type conversion
arithmetic
comparison operators
logical operators
strings
lists
tuples
sets
collection choice
```

---

# Day 1 - Python Basics

## Main goal

Day 1 introduced how a Python file runs, how to print output, store values, and accept simple input.

## Core syntax

```python
print("Hello, Python")

first_name = "Sudharsan"
age = 30
is_learning_python = True

full_name = f"{first_name} Srinivasan"
print(f"My name is {full_name}")

user_age = int(input("Enter your age: "))
next_year_age = user_age + 1
```

## Key rules

```text
Python runs code line by line.
Use print() for terminal output.
Comments start with #.
Variables store values.
Use snake_case for variable names.
Strings need quotes.
Numbers usually do not need quotes.
Python booleans are True and False.
Use f-strings for clean output.
input() always returns a string.
Use int() before doing math with numeric input.
Python does not require semicolons.
```

## JavaScript comparison

```text
JavaScript -> console.log()
Python     -> print()

JavaScript -> true / false
Python     -> True / False

JavaScript -> camelCase is common
Python     -> snake_case is standard
```

---

# Day 2 - Variables, Built-in Functions, Data Types

## Main goal

Day 2 expanded variables into built-in functions, type checking, type conversion, arithmetic, assignment shortcuts, and first collection awareness.

## Common built-in functions

```python
print()
len()
type()
input()
int()
float()
str()
```

Use `type()` when you are unsure what kind of value you are working with.

```python
name = "Sudharsan"
age = 30

print(len(name))
print(type(age))
```

## Variable naming

Variable names should match the value they currently hold.

Better:

```python
user_age = int(input("Enter age: "))
next_year_age = user_age + 1
```

Worse:

```python
user_age = int(input("Enter age: ")) + 1
```

Boolean names should read like yes/no questions.

```python
is_learning_python = True
has_experience = True
can_relocate = True
```

## Multiple assignment

```python
first_name, last_name, age = "Sudharsan", "Srinivasan", 30

x, y = 100, 200
x, y = y, x
```

Rule:

```text
The number of variables must match the number of values.
```

## Data types

```python
name = "Sudharsan"                         # str
age = 30                                   # int
rating = 4.9                               # float
is_learning_python = True                  # bool
skills = ["JavaScript", "React", "Python"] # list
profile = {"name": name, "age": age}       # dict
coordinates = (2, 3)                       # tuple
unique_numbers = {1, 2, 3}                 # set
```

Mental model:

```text
str   -> text
int   -> whole number
float -> decimal number
bool  -> True / False
list  -> ordered collection
dict  -> key-value data
tuple -> fixed grouped data
set   -> unique values
```

## Type conversion

```python
age = int("30")
price = float("99.99")
age_text = str(30)
letters = list("Python")
unique_numbers = set([1, 2, 2, 3])
```

Important trap:

```python
bool("False")  # True
```

Non-empty strings are truthy, even if the text says `"False"`.

## Arithmetic and assignment shortcuts

```text
+    addition
-    subtraction
*    multiplication
/    division, returns float
//   floor division
%    remainder
**   exponent
```

```python
score = 50

score += 10
score -= 5
score *= 2
score /= 10
```

Python does not use `score++`; use `score += 1`.

---

# Day 3 - Operators

## Main goal

Day 3 focused on assignment, comparison, boolean logic, and expression evaluation.

## Assignment vs comparison

```python
age = 30      # assignment
age == 30     # comparison
```

Rule:

```text
=  assigns
== compares
```

Python does not use JavaScript's `===`.

## Comparison operators

```text
==   equal to
!=   not equal to
>    greater than
<    less than
>=   greater than or equal to
<=   less than or equal to
```

Comparison operators return `True` or `False`.

## Logical operators

```python
and
or
not
```

Examples:

```python
age = 30
has_experience = True
has_degree = False
is_blocked = False

can_apply = age >= 18 and has_experience
has_background = has_degree or has_experience
is_available = not is_blocked
```

JavaScript comparison:

```text
JavaScript -> &&, ||, !
Python     -> and, or, not
```

## Cleaner boolean style

Noisy:

```python
has_experience == True
is_blocked == False
```

Cleaner:

```python
has_experience
not is_blocked
```

## Operator precedence

```python
result = 10 + 5 * 2      # 20
result = (10 + 5) * 2    # 30
```

Use parentheses when mixing `and` / `or`.

```python
(age >= 18 and score > 70) or is_holiday
```

## Key rules

```text
Use True and False, not true and false.
Use = for assignment.
Use == for comparison.
Python does not use ===.
Python does not use ++.
Use += 1 to increment.
and requires both sides to be true.
or requires at least one side to be true.
not flips a boolean.
Avoid unnecessary == True and == False.
Use parentheses for mixed logic.
```

---

# Day 4 - Strings

## Main goal

Day 4 focused on creating, formatting, indexing, slicing, searching, modifying, and converting strings.

## Creating strings

```python
first_name = "Sudharsan"
last_name = 'Srinivasan'
message = "I'm learning Python"
quote = 'He said "Python is fun"'
```

Single and double quotes both work. Choose the one that avoids unnecessary escaping.

## String length, concatenation, repetition, and f-strings

```python
print(len("Python"))

full_name = first_name + " " + last_name
separator = "-" * 20

print(f"{full_name} is learning Python.")
```

Use f-strings instead of messy concatenation when inserting values.

## Escape characters

```text
\n  new line
\t  tab
\\  backslash
\"  double quote
\'  single quote
```

## Indexing and slicing

```python
language = "Python"

print(language[0])    # P
print(language[-1])   # n
print(language[:3])   # Pyt
print(language[3:])   # hon
print(language[-3:])  # hon
```

Rules:

```text
Indexes start at 0.
Negative indexes count from the end.
Slicing includes start and excludes end.
```

## Common string methods

```python
name.upper()
name.lower()
name.title()
name.capitalize()
name.strip()
sentence.replace("JavaScript", "Python")
```

Important distinction:

```text
title()      -> capitalizes every word
capitalize() -> capitalizes only the first character of the whole string
```

## Search/check methods

```python
first_name.startswith("Sud")
first_name.endswith("san")
sentence.find("Python")
sentence.count("Python")
```

`find()` returns the starting index or `-1`.

Boolean pattern:

```python
has_python = sentence.find("Python") != -1
```

Do not store raw `find()` output in a boolean-sounding variable.

## split() and join()

```python
sentence = "I am learning Python"
words = sentence.split()

skills_text = "JavaScript,React,Python,Node"
skills_list = skills_text.split(",")

joined_skills = ", ".join(skills_list)
```

Read `join()` as:

```text
Use this string as the glue between each list item.
```

## Character checks

```python
"Sudharsan".isalpha()
"30".isdigit()
"Sudharsan10".isalnum()
"python".islower()
"PYTHON".isupper()
```

Important:

```text
"Sudharsan Srinivasan".isalpha() is False because of the space.
"Sudharsan_10".isalnum() is False because of the underscore.
```

---

# Day 5 - Lists

## Main goal

Day 5 focused on ordered, mutable collections.

## List basics

```python
skills = ["JavaScript", "React", "Node.js", "Python"]
empty_list = []
```

Lists are ordered and mutable.

```python
print(skills[0])
print(skills[-1])
print(skills[:2])
print("Python" in skills)

skills[2] = "Express"
```

## Adding items

```python
skills.append("AWS")                       # one item at end
skills.insert(1, "TypeScript")             # one item at index
skills.extend(["Docker", "PostgreSQL"])    # multiple items
```

Important:

```text
append(["A", "B"]) adds one nested list.
extend(["A", "B"]) adds each item separately.
```

## Removing items

```python
skills.remove("AWS")        # remove by value
removed_skill = skills.pop()
removed_first = skills.pop(0)
del skills[1]
skills.clear()
```

Important:

```text
remove() removes the first matching value and crashes if missing.
pop() removes and returns the removed item.
del removes but returns nothing.
clear() empties the list but keeps the variable.
```

## Copying and joining

```python
skills_copy = skills.copy()
another_copy = skills[:]

frontend_skills = ["HTML", "CSS", "JavaScript"]
backend_skills = ["Node.js", "MongoDB"]
full_stack_skills = frontend_skills + backend_skills
```

Rules:

```text
new_list = old_list is not a real copy.
copy() creates an independent top-level list.
extend() modifies the original list.
+ creates a new combined list.
```

## count(), index(), reverse(), sort(), sorted()

```python
skills.count("Python")
skills.index("Python")

skills.reverse()
skills.sort()

sorted_skills = sorted(skills)
```

Important:

```text
index() crashes if the value is missing.
sort() mutates the original list and returns None.
sorted() creates a sorted copy.
Do not assign the result of sort() to a variable.
```

---

# Day 6 - Tuples

## Main goal

Day 6 focused on ordered but immutable collections.

## Tuple basics

```python
languages = ("JavaScript", "TypeScript", "Python")
empty_tuple = ()
one_item_tuple = ("Python",)
```

Important:

```text
list  -> mutable
tuple -> immutable
```

A one-item tuple needs the comma.

```python
("Python")   # string
("Python",)  # tuple
```

## Indexing, slicing, and membership

```python
print(languages[0])
print(languages[-1])
print(languages[:2])
print("Python" in languages)
```

Tuples are ordered, so indexing and slicing work.

## Immutability

Not allowed:

```python
languages[0] = "HTML"
```

Allowed:

```python
coordinates = (10, 20)
coordinates = (30, 40)
```

That reassigns the variable to a new tuple. It does not modify the old tuple.

## Temporary modification pattern

```python
languages = ("JavaScript", "TypeScript", "Python")

languages_list = list(languages)
languages_list.append("Go")

updated_languages = tuple(languages_list)
```

Use this only when tuple-like data needs a temporary change. If the data changes often, use a list.

## Joining, repetition, deleting, count/index

```python
frontend_skills = ("HTML", "CSS")
backend_skills = ("Node.js", "MongoDB")

full_stack_skills = frontend_skills + backend_skills
repeated_numbers = (1, 2) * 3

scores = (90, 85, 90)
scores.count(90)
scores.index(85)

del temporary_tuple
```

You cannot delete one tuple item directly, but you can delete the whole tuple variable.

---

# Day 7 - Sets

## Main goal

Day 7 focused on unique, unordered collections and comparing groups of data.

## Set basics

```python
languages = {"JavaScript", "Python", "Java", "Python"}
empty_set = set()
```

Important:

```text
Sets store unique values.
Duplicates are removed automatically.
Sets do not have dependable order.
Sets do not support indexing.
set() creates an empty set.
{} creates an empty dictionary.
```

## Membership

```python
has_python = "Python" in languages
missing_go = "Go" not in languages
```

Sets are good for uniqueness and fast membership checks.

## Adding and updating

```python
languages.add("Go")
languages.update(["Rust", "JavaScript", "C#"])
```

Comparison with lists:

```text
list.append() -> one item
list.extend() -> multiple items

set.add()     -> one item
set.update()  -> multiple items
```

## Removing

```python
languages.remove("Java")     # crashes if missing
languages.discard("Ruby")    # does not crash if missing
removed_skill = languages.pop()
languages.clear()
del old_skills
```

Important:

```text
Use remove() when the item must exist.
Use discard() when the item may not exist.
Use pop() carefully because sets have no dependable last item.
Use clear() to empty the set.
Use del to delete the variable.
```

## Converting to set

```python
skill_list = ["React", "Node.js", "React", "MongoDB"]
unique_skills = set(skill_list)
```

After converting to a set, do not trust item order.

## Set operations

```python
frontend_skills = {"HTML", "CSS", "JavaScript", "React"}
backend_skills = {"JavaScript", "Node.js", "MongoDB"}

all_skills = frontend_skills.union(backend_skills)
common_skills = frontend_skills.intersection(backend_skills)
frontend_only = frontend_skills.difference(backend_skills)
not_shared = frontend_skills.symmetric_difference(backend_skills)
```

Rules:

```text
union() returns everything from both sets.
intersection() returns shared items.
difference() returns items only in the first set.
symmetric_difference() returns items not shared.
difference() direction matters.
```

## Relationship checks

```python
required_skills = {"JavaScript", "React"}
candidate_skills = {"JavaScript", "React", "Node.js"}

required_skills.issubset(candidate_skills)
candidate_skills.issuperset(required_skills)
frontend_skills.isdisjoint({"PostgreSQL", "MongoDB"})
```

These return booleans.

---

# Week 1 Big Picture

## Concept progression

```text
Day 1-2 -> values, variables, types, input, output
Day 3   -> operators and boolean logic
Day 4   -> strings as text sequences
Day 5   -> lists as ordered, changeable collections
Day 6   -> tuples as ordered, fixed collections
Day 7   -> sets as unique, unordered collections
```

Progression:

```text
value -> variable -> type -> operation -> collection -> choosing the right collection
```

## Collection decision guide

| Need | Use |
|---|---|
| Ordered items that can change | `list` |
| Fixed grouped values | `tuple` |
| Unique values or group comparison | `set` |
| Labeled key-value data | `dict` |

Dictionaries started in Week 2, but this decision guide is useful from now on.

## Recurring mistakes to watch

| Pattern | Watch for |
|---|---|
| String `"30"` vs number `30` | Use numbers for math |
| `input()` returns string | Convert before math |
| Misleading variable names | Name variables based on what they store |
| JavaScript habits | Avoid `true`, `false`, `===`, `++`, camelCase, semicolons |
| Mixed logic readability | Use parentheses with `and` / `or` |
| Unnecessary escaping | Pick the cleaner quote style |
| `find()` misuse | Use `find(...) != -1` for boolean checks |
| `append()` vs `extend()` | One item vs multiple items |
| `pop()` vs `del` | `pop()` returns removed item; `del` does not |
| `sort()` vs `sorted()` | Mutate original vs create sorted copy |
| One-item tuple trap | Use `("Python",)` |
| Empty set trap | Use `set()`, not `{}` |
| Set order/indexing trap | Never depend on order or indexing |

## Week 1 final status

```text
Week 1 - Cleared
Ready for Week 2.
```
