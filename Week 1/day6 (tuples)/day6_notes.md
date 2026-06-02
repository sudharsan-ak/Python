# Day 6 Notes - Tuples

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 6 focused on tuples: ordered collections like lists, but immutable.

## Core topics

```text
creating tuples
empty tuples
one-item tuple comma rule
len()
type()
indexing
slicing
in checks
immutability
tuple/list conversion
joining tuples
tuple repetition
deleting tuples
count()
index()
tuple vs list use cases
```

---

## Tuple basics

A tuple stores multiple values.

```python
languages = ("JavaScript", "TypeScript", "Python", "Java")
empty_tuple = ()
profile = ("Sudharsan", 30, "Lewisville", True)
```

Main difference:

```text
list  -> mutable    -> can be changed directly
tuple -> immutable  -> cannot be changed directly
```

List:

```python
skills = ["JavaScript", "React", "Python"]
skills[0] = "HTML"
```

Tuple:

```python
skills = ("JavaScript", "React", "Python")
# skills[0] = "HTML"  # fails
```

---

## len(), type(), and one-item tuples

```python
print(len(languages))
print(type(languages))
```

One-item tuple trap:

```python
favorite_language = ("Python")   # string
favorite_language = ("Python",)  # tuple
```

The comma creates the tuple.

---

## Indexing, slicing, and membership

Tuples are ordered.

```python
print(languages[0])
print(languages[-1])
print(languages[:2])
print(languages[-2:])
```

Rules:

```text
Indexes start at 0.
Negative indexes count from the end.
Slicing includes start and excludes end.
Slicing a tuple returns a tuple.
```

Membership:

```python
has_python = "Python" in languages
```

---

## Immutability

Tuples cannot be changed directly.

```python
languages = ("JavaScript", "TypeScript", "Python")
# languages[0] = "HTML"  # fails
```

But a tuple variable can be reassigned.

```python
coordinates = (10, 20)
coordinates = (30, 40)
```

Important:

```text
Changing an item inside a tuple is not allowed.
Pointing the variable to a new tuple is allowed.
```

---

## Tuple/list conversion

When tuple-like data needs a temporary change:

```python
languages = ("JavaScript", "TypeScript", "Python")

languages_list = list(languages)
languages_list.append("Go")
updated_languages = tuple(languages_list)
```

Use this only when needed. If data changes often, use a list.

---

## Joining, repetition, deletion, count(), index()

```python
full_stack_skills = frontend_skills + backend_skills
repeated_numbers = (1, 2) * 3

scores = (90, 85, 90, 70)
scores.count(90)
scores.index(70)
```

You cannot delete one tuple item directly, but you can delete the whole variable.

```python
del temporary_tuple
```

Warning:

```text
index() crashes if the value does not exist.
```

Safe pattern:

```python
if 100 in scores:
    print(scores.index(100))
```

---

## Tuple vs list

Use tuples for fixed grouped data.

```python
coordinates = (10, 20)
rgb_color = (255, 255, 255)
date_parts = (2026, 5, 18)
```

Use lists for data expected to change.

```python
skills = ["JavaScript", "React", "Node.js"]
tasks = ["study", "practice", "review"]
cart_items = ["laptop", "mouse", "keyboard"]
```

Rule:

```text
Use tuple when structure should stay fixed.
Use list when the collection should change.
```

---

## What was practiced

```text
creating tuples
checking length and type
one-item tuple syntax
indexing and slicing
membership checks
immutability
tuple/list conversion
joining and repeating tuples
deleting tuple variables
count() and index()
choosing tuple vs list
```

Final mixed exercise was cleared in `day6-final.py`.

---

## Mistakes and corrections

| Issue | Correction |
|---|---|
| Counted wrong value in `repeated_scores.count()` | Use `repeated_scores.count(90)` |
| Comment variable mismatch | Match comments to actual variable names |
| Clunky coordinate explanation | Coordinates are fixed pair values |
| Final exercise got too long initially | Keep final mixed exercises focused |

---

## Key takeaways

```text
Tuples are ordered.
Tuples are immutable.
A one-item tuple needs a trailing comma.
Use indexes and slices like lists/strings.
Use in to check membership.
You cannot directly change tuple items.
You can reassign a tuple variable to a new tuple.
Use list() for a temporary mutable version.
Use tuple() to convert back.
Use + to join tuples.
Use * to repeat tuples.
Use del to delete the whole tuple variable.
Use count() and index().
Use tuples for fixed grouped data.
Use lists for data that should change.
```

## Ready for next day

```text
Day 7 - Sets
```
