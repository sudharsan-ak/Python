# Week 1 Notes - Python Foundations

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Week 1 overview

Week 1 built the base for writing simple Python programs and choosing between basic collection types.

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
print(), comments, variables, data types, input(), type conversion, f-strings,
operators, strings, lists, tuples, sets, and basic collection choice
```

---

# Day 1 - Python Basics

## Core idea

Python runs code line by line. Day 1 introduced output, comments, variables, f-strings, and simple input.

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

## Remember

```text
Use print() for terminal output.
Comments start with #.
Use snake_case for variable names.
Strings need quotes.
Booleans are True and False.
input() always returns a string.
Convert input before numeric math.
Python does not require semicolons.
```

JavaScript comparison:

```text
console.log() -> print()
true/false   -> True/False
camelCase    -> snake_case
```

---

# Day 2 - Variables, Built-in Functions, Data Types

## Core idea

Day 2 focused on storing values clearly, checking types, converting values, and understanding basic data types.

## Core syntax

```python
name = "Sudharsan"
age = 30
rating = 4.9
is_active = True

print(len(name))
print(type(age))

age = int("30")
price = float("99.99")
age_text = str(30)
```

Common built-ins:

```text
print(), len(), type(), input(), int(), float(), str()
```

Data type mental model:

```text
str   -> text
int   -> whole number
float -> decimal number
bool  -> True / False
list  -> ordered, changeable collection
dict  -> labeled key-value data
tuple -> ordered, fixed collection
set   -> unique unordered values
```

## Remember

```text
Variable names should describe what the value currently stores.
Boolean names should read like yes/no values: is_active, has_ticket, can_apply.
Multiple assignment works only when variable count matches value count.
bool("False") is True because non-empty strings are truthy.
Python does not use score++; use score += 1.
```

Arithmetic operators:

```text
+ addition, - subtraction, * multiplication, / division,
// floor division, % remainder, ** exponent
```

---

# Day 3 - Operators

## Core idea

Day 3 focused on assignment, comparison, boolean logic, and expression evaluation.

## Core syntax

```python
age = 30      # assignment
age == 30     # comparison

can_apply = age >= 18 and has_experience
has_background = has_degree or has_experience
is_available = not is_blocked
```

Comparison operators:

```text
== equal, != not equal, > greater, < less, >= greater/equal, <= less/equal
```

## Remember

```text
= assigns.
== compares.
Python does not use ===.
Use and/or/not instead of &&/||/!.
Avoid unnecessary == True and == False.
Use parentheses when mixed and/or logic is hard to read.
```

Cleaner boolean style:

```python
if has_experience:
    print("Experienced")

if not is_blocked:
    print("Available")
```

---

# Day 4 - Strings

## Core idea

Day 4 focused on text: creation, formatting, indexing, slicing, common methods, searching, splitting, and joining.

## Core syntax

```python
first_name = "Sudharsan"
message = "I'm learning Python"
quote = 'He said "Python is fun"'

full_name = first_name + " " + last_name
print(f"{full_name} is learning Python.")
```

Important escape characters:

```text
\n new line, \t tab, \\ backslash, \" double quote, \' single quote
```

Indexing and slicing:

```python
language = "Python"

language[0]    # P
language[-1]   # n
language[:3]   # Pyt
language[3:]   # hon
language[-3:]  # hon
```

Common methods:

```text
upper(), lower(), title(), capitalize(), strip(), replace()
startswith(), endswith(), find(), count(), split(), join()
```

## Remember

```text
Indexes start at 0.
Negative indexes count from the end.
Slicing includes start and excludes end.
title() capitalizes every word; capitalize() only the first character.
find() returns an index or -1.
Use sentence.find("Python") != -1 for boolean checks.
join() means: use this string as glue between items.
Spaces and underscores affect isalpha() / isalnum() results.
```

---

# Day 5 - Lists

## Core idea

Day 5 focused on lists: ordered, mutable collections.

## Core syntax

```python
skills = ["JavaScript", "React", "Node.js", "Python"]

skills[0]
skills[-1]
skills[:2]
"Python" in skills

skills[2] = "Express"
```

Add items:

```python
skills.append("AWS")
skills.insert(1, "TypeScript")
skills.extend(["Docker", "PostgreSQL"])
```

Remove items:

```python
skills.remove("AWS")
removed_skill = skills.pop()
removed_first = skills.pop(0)
del skills[1]
skills.clear()
```

Copy, combine, sort:

```python
skills_copy = skills.copy()
another_copy = skills[:]
full_stack_skills = frontend_skills + backend_skills

skills.sort()
sorted_skills = sorted(skills)
```

## Remember

```text
append() adds one item.
extend() adds multiple items from another iterable.
append(["A", "B"]) creates a nested list.
remove() crashes if the value is missing.
pop() removes and returns the removed item.
del removes but returns nothing.
new_list = old_list is not a real copy.
sort() mutates the original list and returns None.
sorted() returns a new sorted list.
```

---

# Day 6 - Tuples

## Core idea

Day 6 focused on tuples: ordered collections that cannot be changed after creation.

## Core syntax

```python
languages = ("JavaScript", "TypeScript", "Python")
empty_tuple = ()
one_item_tuple = ("Python",)

languages[0]
languages[-1]
languages[:2]
"Python" in languages
```

Immutability:

```python
# Not allowed:
languages[0] = "HTML"

# Allowed: reassigning the variable to a new tuple
coordinates = (10, 20)
coordinates = (30, 40)
```

Temporary modification pattern:

```python
languages_list = list(languages)
languages_list.append("Go")
updated_languages = tuple(languages_list)
```

## Remember

```text
list -> mutable.
tuple -> immutable.
A one-item tuple needs a comma: ("Python",).
("Python") is just a string in parentheses.
Tuples support indexing, slicing, count(), and index().
You cannot delete one tuple item, but you can delete the whole tuple variable.
If the data changes often, use a list instead.
```

---

# Day 7 - Sets

## Core idea

Day 7 focused on sets: unique, unordered collections useful for membership checks and group comparisons.

## Core syntax

```python
languages = {"JavaScript", "Python", "Java", "Python"}
empty_set = set()

"Python" in languages
"Go" not in languages
```

Add/remove:

```python
languages.add("Go")
languages.update(["Rust", "JavaScript", "C#"])

languages.remove("Java")
languages.discard("Ruby")
removed_skill = languages.pop()
languages.clear()
```

Set operations:

```python
frontend_skills.union(backend_skills)
frontend_skills.intersection(backend_skills)
frontend_skills.difference(backend_skills)
frontend_skills.symmetric_difference(backend_skills)
```

Relationship checks:

```python
required_skills.issubset(candidate_skills)
candidate_skills.issuperset(required_skills)
frontend_skills.isdisjoint(database_skills)
```

## Remember

```text
Sets keep unique values only.
Set order is not dependable.
Sets do not support indexing.
set() creates an empty set; {} creates an empty dictionary.
add() adds one item; update() adds multiple items.
remove() crashes if missing; discard() does not.
pop() removes an unpredictable item.
difference() direction matters.
```

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

Main progression:

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

## Common mistakes and gotchas

| Pattern | Watch for |
|---|---|
| `input()` returns string | Convert before math |
| String `"30"` vs number `30` | Use numbers for math |
| JavaScript habits | Avoid `true`, `false`, `===`, `++`, camelCase, semicolons |
| Mixed logic | Use parentheses with `and` / `or` |
| `find()` misuse | Use `find(...) != -1` for boolean checks |
| `append()` vs `extend()` | One item vs multiple items |
| `pop()` vs `del` | `pop()` returns removed item; `del` does not |
| `sort()` vs `sorted()` | Mutate original vs create sorted copy |
| One-item tuple | Use `("Python",)` |
| Empty set | Use `set()`, not `{}` |
| Set order/indexing | Never depend on order or indexing |

## Week 1 final status

```text
Week 1 - Cleared
Ready for Week 2.
```
