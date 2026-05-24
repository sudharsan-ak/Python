# Day 6 Notes - Tuples

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## What Day 6 covered

Day 6 focused on Python tuples. The goal was to understand how tuples store multiple values like lists, but with one major difference: tuples are immutable, meaning their items cannot be changed directly after creation.

Topics covered:

```text
creating tuples
empty tuples
one-item tuple comma rule
len()
type()
indexing
negative indexing
slicing
in checks
immutability
tuple to list conversion
list to tuple conversion
joining tuples
tuple repetition
deleting tuple variables
count()
index()
tuple vs list use cases
final mixed exercise
```

## 1. Tuple basics

A tuple stores multiple values in one variable.

```python
languages = ("JavaScript", "TypeScript", "Python", "Java")
```

Tuples use parentheses and comma-separated values.

```python
empty_tuple = ()
profile = ("Sudharsan", 30, "Lewisville", True)
```

Tuples can store mixed data types, just like lists.

The important beginner difference:

```text
list  -> mutable    -> can be changed directly
tuple -> immutable  -> cannot be changed directly
```

List example:

```python
skills = ["JavaScript", "React", "Python"]
skills[0] = "HTML"
```

Tuple example:

```python
skills = ("JavaScript", "React", "Python")
# skills[0] = "HTML"  # This would fail
```

## 2. `len()` and `type()`

`len()` returns how many items are in a tuple.

```python
languages = ("JavaScript", "TypeScript", "Python", "Java")

print(len(languages))  # 4
```

`type()` confirms the value is a tuple.

```python
print(type(languages))  # <class 'tuple'>
```

## 3. One-item tuple rule

This is a common beginner trap.

This is not a tuple:

```python
favorite_language = ("Python")
```

That is just a string inside parentheses.

Correct one-item tuple:

```python
favorite_language = ("Python",)
```

The comma is what makes it a tuple.

## 4. Indexing and negative indexing

Tuples are ordered, so items can be accessed by index.

```python
languages = ("JavaScript", "TypeScript", "Python", "Java")

print(languages[0])   # JavaScript
print(languages[1])   # TypeScript
print(languages[-1])  # Java
print(languages[-2])  # Python
```

Indexes start at `0`.

Negative indexes count from the end.

## 5. Slicing tuples

Slicing gets part of a tuple.

```python
tuple_name[start:end]
```

Rule:

```text
start is included
end is excluded
```

Examples:

```python
print(languages[:2])   # first two items
print(languages[2:])   # from index 2 to the end
print(languages[-2:])  # last two items
print(languages[:])    # full tuple copy
```

Slicing a tuple returns a tuple.

## 6. Checking items with `in`

Use `in` to check whether a value exists in a tuple.

```python
has_python = "Python" in languages
has_go = "Go" in languages

print(has_python)  # True
print(has_go)      # False
```

JavaScript comparison:

```javascript
languages.includes("Python")
```

Python:

```python
"Python" in languages
```

## 7. Tuple immutability

Tuples cannot be changed directly.

This fails:

```python
languages = ("JavaScript", "TypeScript", "Python")
languages[0] = "HTML"
```

Reason:

```text
A tuple is immutable.
Changing one item would mutate the tuple.
```

But a tuple variable can be reassigned.

This is allowed:

```python
coordinates = (10, 20)
coordinates = (30, 40)
```

That does not modify the original tuple. It points the variable to a new tuple.

Important distinction:

```text
Not allowed: changing an item inside the existing tuple
Allowed: reassigning the variable to a new tuple
```

## 8. Tuple to list and list to tuple conversion

If a tuple-like value needs to be changed, one beginner-friendly pattern is:

```text
tuple -> list -> modify list -> tuple
```

Example:

```python
languages = ("JavaScript", "TypeScript", "Python")

languages_list = list(languages)
languages_list.append("Go")
languages_list[0] = "HTML"

updated_languages = tuple(languages_list)
```

This does not edit the old tuple directly.

It creates a list copy, modifies the list, and creates a new tuple.

If you constantly need to add, remove, or edit items, use a list instead of a tuple.

## 9. Joining tuples

Use `+` to join tuples.

```python
frontend_skills = ("HTML", "CSS", "JavaScript")
backend_skills = ("Node.js", "MongoDB", "PostgreSQL")

full_stack_skills = frontend_skills + backend_skills
```

Important:

```text
+ creates a new tuple.
It does not modify the original tuples.
```

## 10. Tuple repetition

Tuples can be repeated with `*`.

```python
numbers = (1, 2)

repeated_numbers = numbers * 3

print(repeated_numbers)  # (1, 2, 1, 2, 1, 2)
```

This is not used every day, but it is valid Python syntax.

## 11. Deleting tuples

You cannot delete one item from a tuple directly.

This fails:

```python
# del languages[0]
```

Reason:

```text
Deleting one item would modify the tuple.
```

But you can delete the whole tuple variable.

```python
temporary_tuple = ("draft", "test", "sample")

del temporary_tuple
```

After deletion, this would fail:

```python
# print(temporary_tuple)
```

because the variable no longer exists.

## 12. Tuple methods: `count()` and `index()`

Tuples support `count()` and `index()`.

`count()` returns how many times a value appears.

```python
scores = (90, 85, 90, 70, 90)

print(scores.count(90))  # 3
```

`index()` returns the first index of a value.

```python
print(scores.index(70))  # 3
```

Important warning:

```text
index() fails if the value does not exist.
```

Safer pattern:

```python
if 100 in scores:
    print(scores.index(100))
else:
    print("100 is not in scores")
```

## 13. Tuple vs list use cases

Use a tuple when the values represent a fixed group.

Good tuple examples:

```python
coordinates = (10, 20)
rgb_color = (255, 255, 255)
date_parts = (2026, 5, 18)
```

Use a list when the values are expected to change.

Good list examples:

```python
skills = ["JavaScript", "React", "Node.js"]
tasks = ["study", "practice", "review"]
cart_items = ["laptop", "mouse", "keyboard"]
```

Simple rule:

```text
Use tuple when the structure should stay fixed.
Use list when the collection should change.
```

## What was practiced

Day 6 practice included:

```text
creating tuples
printing tuples
checking tuple length and type
creating empty tuples
creating one-item tuples
accessing items with indexes
using negative indexes
slicing tuples
checking membership with in
understanding immutability
converting tuple to list
modifying the list
converting list back to tuple
joining tuples
repeating tuples
deleting tuple variables
using count()
using index()
choosing between tuple and list
```

## Mistakes and corrections

| Mistake / Issue | Correction |
|---|---|
| Counted `20` instead of `90` in `repeated_scores.count()` | Use the exact value requested: `repeated_scores.count(90)` |
| Final exercise comment said `changing_skills` instead of `changing_tasks` | Match the actual variable name used in the exercise |
| Comment wording for coordinates was slightly clunky | Use: `coordinates should be a tuple because it represents a fixed pair of values` |
| Final exercise was initially too long | Keep final mixed exercises focused and non-repetitive |

Important correction:

```python
print(repeated_scores.count(90))
```

not:

```python
print(repeated_scores.count(20))
```

## Final mixed exercise status

The final mixed exercise was completed successfully in:

```text
day6-final.py
```

It covered tuple creation, indexing, slicing, membership checks, tuple/list conversion, joining tuples, `count()`, `index()`, one-item tuple syntax, tuple reassignment, and tuple vs list use cases.

No functional mistakes in the final mixed exercise.

Minor comment cleanup only:

```python
# changing_tasks should be a list because tasks can change over time
# coordinates should be a tuple because it represents a fixed pair of values
```

## Day 6 key takeaways

```text
Tuples are ordered.
Tuples are immutable.
Use () to create tuples.
Use len() to count tuple items.
Use type() to confirm tuple type.
A one-item tuple needs a trailing comma.
Use indexes and slices like lists/strings.
Use in to check membership.
You cannot directly change tuple items.
You can reassign a tuple variable to a new tuple.
Use list() when you need a temporary mutable version.
Use tuple() to convert a list back to a tuple.
Use + to join tuples into a new tuple.
Use * to repeat tuple values.
Use del to delete the whole tuple variable.
Use count() to count values.
Use index() to find the first matching index.
Use tuples for fixed grouped data.
Use lists for data that should change.
```

## Ready for next day

```text
Day 7 - Sets
```
