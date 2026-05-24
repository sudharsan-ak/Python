# Day 5 Notes - Lists

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## What Day 5 covered

Day 5 focused on Python lists. The goal was to learn how to store multiple values in one ordered collection, access items, change items, add/remove items, copy lists safely, combine lists, and sort/reverse them.

Topics covered:

```text
creating lists
len()
indexing
negative indexing
slicing
in
modifying items
append()
insert()
extend()
remove()
pop()
del
clear()
copy()
joining with +
count()
index()
reverse()
sort()
sorted()
final mixed exercise
```

## 1. List basics

A list stores multiple values inside one variable.

```python
skills = ["JavaScript", "React", "Node.js", "Python", "MongoDB"]
```

Lists use square brackets and comma-separated items.

```python
empty_list = []
skills = ["JavaScript", "React", "Python"]
```

Important rule:

```text
Text values need quotes.
Numbers do not need quotes.
Booleans do not need quotes.
Existing variables do not need quotes.
```

Examples:

```python
scores = [85, 90, 95]
profile = ["Sudharsan", 30, 5.5, True, "Lewisville"]
```

If you write text without quotes:

```python
skills = [JavaScript, React, Python]
```

Python treats those as variable names and fails if they are not defined.

JavaScript comparison:

```javascript
const skills = ["JavaScript", "React", "Python"];
```

Python:

```python
skills = ["JavaScript", "React", "Python"]
```

## 2. `len()`

`len()` returns how many items are in the list.

```python
skills = ["JavaScript", "React", "Python"]
print(len(skills))  # 3
```

An empty list has length `0`.

## 3. Indexing and negative indexing

Lists are ordered. Indexes start at `0`.

```python
skills = ["JavaScript", "React", "Node.js", "Python", "MongoDB"]
```

Index map:

```text
JavaScript   React   Node.js   Python   MongoDB
0            1       2         3        4
```

Examples:

```python
print(skills[0])   # first item
print(skills[1])   # second item
print(skills[-1])  # last item
print(skills[-2])  # second-to-last item
```

Negative indexes count from the end.

## 4. Slicing

Slicing gets part of a list.

```python
list_name[start:end]
```

Rule:

```text
start is included
end is excluded
```

Examples:

```python
print(skills[:3])   # first 3 items
print(skills[2:])   # from index 2 to the end
print(skills[-2:])  # last 2 items
print(skills[:])    # full copy
```

Same slicing idea as strings.

## 5. Checking and modifying items

Use `in` to check whether an item exists.

```python
has_python = "Python" in skills
```

JavaScript comparison:

```javascript
skills.includes("Python")
```

Python:

```python
"Python" in skills
```

Lists are mutable, so items can be changed.

```python
skills[2] = "Node.js"
skills[-1] = "PostgreSQL"
```

Do not confuse checking with modifying:

```text
"Python" in skills       -> returns True/False
skills[2] = "Node.js"    -> changes the list
```

## 6. Adding items

Three methods were covered:

```text
append() -> add one item to the end
insert() -> add one item at a specific index
extend() -> add multiple items from another list
```

Examples:

```python
skills.append("AWS")
skills.insert(1, "TypeScript")

backend_skills = ["Express", "Docker", "PostgreSQL"]
skills.extend(backend_skills)
```

Important difference:

```python
skills.append(["Express", "Docker"])
```

adds the whole list as one nested item.

```python
skills.extend(["Express", "Docker"])
```

adds each item separately.

Rule:

```text
append() for one item at the end.
insert() for one item at a specific index.
extend() for multiple items from another list.
```

## 7. Removing items

Four removal tools were covered:

```text
remove() -> remove by value
pop()    -> remove by index and optionally return removed item
del      -> delete by index or slice
clear()  -> empty the whole list
```

Examples:

```python
skills.remove("AWS")

removed_skill = skills.pop()
removed_city = cities.pop(0)

del skills[1]
del cities[-2:]

temporary_items.clear()
```

Important notes:

```text
remove() removes the first matching value.
remove() crashes if the value does not exist.
pop() returns the removed item.
del removes but returns nothing.
clear() keeps the list variable but empties it.
```

`pop()` and `del` can use any valid index, including negative indexes. Invalid indexes cause an error.

## 8. Copying lists

Bad copy:

```python
skills_copy = skills
```

This does not create an independent copy. Both names point to the same list.

Correct copy:

```python
skills_copy = skills.copy()
```

Another valid copy:

```python
cities_copy = cities[:]
```

Prefer `.copy()` while learning because it is clearer.

## 9. Joining lists

Use `+` to create a new combined list.

```python
frontend_skills = ["HTML", "CSS", "JavaScript", "React"]
backend_skills = ["Node.js", "Express", "MongoDB", "PostgreSQL"]

full_stack_skills = frontend_skills + backend_skills
```

Difference:

```text
extend() modifies the original list.
+ creates a new combined list.
```

## 10. Counting and finding items

`count()` counts how many times a value appears.

```python
postgres_count = skills.count("PostgreSQL")
java_count = skills.count("Java")
```

If the item does not exist, `count()` returns `0`.

`index()` finds the first position of an item.

```python
python_index = skills.index("Python")
```

Important:

```text
index() returns the first matching index.
index() crashes if the value does not exist.
```

Safe future pattern:

```python
if "Java" in skills:
    java_index = skills.index("Java")
```

Day 4 comparison:

```text
find() is for strings and returns -1 if missing.
index() is used for lists and crashes if missing.
```

## 11. Reversing and sorting

`reverse()` reverses the original list.

```python
cities.reverse()
```

`sort()` sorts the original list.

```python
numbers.sort()
numbers.sort(reverse=True)
```

`reverse=True` means descending order.

`reverse=False` means ascending order, but it is the default, so this is unnecessary:

```python
numbers.sort()
```

`sorted()` creates a sorted copy and keeps the original unchanged.

```python
sorted_numbers = sorted(numbers)
```

Important warning:

```python
sorted_skills = skills.sort()
```

Do not do this. `sort()` mutates the list and returns `None`.

Correct:

```python
skills.sort()
```

or:

```python
sorted_skills = sorted(skills)
```

Rule:

```text
Use sort() when you want to change the original.
Use sorted() when you want a sorted copy.
```

## What was practiced

Day 5 practice included:

```text
creating lists
checking length
indexing and slicing
checking membership with in
modifying list items
adding with append(), insert(), extend()
removing with remove(), pop(), del, clear()
copying with copy() and slicing
joining with +
counting with count()
finding with index()
reversing with reverse()
sorting with sort() and sorted()
```

## Mistakes and corrections

| Mistake / Issue | Correction |
|---|---|
| Unsure if list items need quotes | Strings need quotes; numbers, booleans, and variables do not |
| Extra trailing spaces | Not functional, but keep code clean |
| Misspelled `temporary_items` as `temporay_items` | Fixed to `temporary_items` |
| Confusion between `pop()` and `del` | `pop()` returns removed item; `del` does not |
| Confusion between `find()` and `index()` | `find()` for strings; `index()` for lists |
| Final exercise could have become too long | Kept it to 20 focused tasks |

Important correction:

```python
temporary_items = ["draft", "test", "sample"]
```

not:

```python
temporay_items = ["draft", "test", "sample"]
```

## Final mixed exercise status

The final mixed exercise was completed successfully in:

```text
day5_final.py
```

It covered list creation, `len()`, indexing, slicing, `in`, modifying, adding, removing, copying, sorting, and proving the original list stayed unchanged after sorting the copy.

No functional mistakes in the final mixed exercise.

## Day 5 key takeaways

```text
Lists are ordered and mutable.
Indexes start at 0.
Negative indexes count from the end.
Slicing includes start and excludes end.
Use in to check membership.
Use append(), insert(), and extend() to add items.
Use remove(), pop(), del, and clear() to remove items.
Use copy() for independent list copies.
Use + to create a new combined list.
Use count() to count occurrences.
Use index() to find the first matching position.
Use reverse() to reverse the original list.
Use sort() to sort the original list.
Use sorted() to create a sorted copy.
Do not assign the result of sort() to a variable.
```

## Ready for next day

```text
Day 6 - Tuples
```
