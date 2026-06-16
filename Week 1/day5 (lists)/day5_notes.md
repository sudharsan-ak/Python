# Day 5 Notes - Lists

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 5 focused on lists: ordered, mutable collections used to store multiple values in one variable.

## Core topics

```text
creating lists
len()
indexing
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
joining lists
count()
index()
reverse()
sort()
sorted()
```

---

## List basics

A list stores multiple values in order.

```python
skills = ["JavaScript", "React", "Node.js", "Python", "MongoDB"]
empty_list = []
```

Rules:

```text
Strings need quotes.
Numbers do not need quotes.
Booleans do not need quotes.
Existing variables do not need quotes.
```

Examples:

```python
scores = [85, 90, 95]
profile = ["Sudharsan", 30, 5.5, True, "Lewisville"]
```

---

## len(), indexing, slicing, and membership

```python
print(len(skills))

print(skills[0])
print(skills[-1])
print(skills[:3])
print(skills[2:])
print(skills[-2:])
```

Rules:

```text
Indexes start at 0.
Negative indexes count from the end.
Slicing includes start and excludes end.
```

Use `in` to check whether an item exists.

```python
has_python = "Python" in skills
```

---

## Modifying items

Lists are mutable.

```python
skills[2] = "Express"
skills[-1] = "PostgreSQL"
```

Checking does not modify:

```python
"Python" in skills
```

Assignment modifies:

```python
skills[2] = "Node.js"
```

---

## Adding items

```python
skills.append("AWS")
skills.insert(1, "TypeScript")
skills.extend(["Docker", "PostgreSQL"])
```

Rules:

```text
append() -> add one item to the end
insert() -> add one item at a specific index
extend() -> add multiple items from another iterable
```

Important:

```python
skills.append(["Express", "Docker"])  # adds one nested list
skills.extend(["Express", "Docker"])  # adds each item separately
```

---

## Removing items

```python
skills.remove("AWS")
removed_skill = skills.pop()
removed_first = skills.pop(0)
del skills[1]
temporary_items.clear()
```

Rules:

```text
remove() removes by value and crashes if missing.
pop() removes by index and returns the removed item.
pop() without index removes the last item.
del removes by index/slice and returns nothing.
clear() empties the list but keeps the variable.
```

---

## Copying and joining

Bad copy:

```python
skills_copy = skills
```

This points both names to the same list.

Good copy:

```python
skills_copy = skills.copy()
another_copy = skills[:]
```

Join lists:

```python
full_stack_skills = frontend_skills + backend_skills
```

Difference:

```text
extend() modifies the original list.
+ creates a new combined list.
```

---

## count(), index(), reverse(), sort(), sorted()

```python
skills.count("Python")
skills.index("Python")
skills.reverse()
skills.sort()
skills.sort(reverse=True)

sorted_skills = sorted(skills)
```

Important:

```text
index() crashes if the value does not exist.
sort() mutates the original list and returns None.
sorted() creates a sorted copy.
```

Wrong:

```python
sorted_skills = skills.sort()
```

Correct:

```python
skills.sort()
```

or:

```python
sorted_skills = sorted(skills)
```

---

## What was practiced

```text
creating lists
length, indexing, slicing
membership checks
modifying items
adding and removing items
copying lists
joining lists
counting and finding values
reversing and sorting
```

Final mixed exercise was cleared in `day5_final.py`.

---

## Mistakes and corrections

| Issue | Correction |
|---|---|
| Unsure if list items need quotes | Strings need quotes; numbers, booleans, variables do not |
| Misspelled `temporary_items` | Fixed variable spelling |
| Confused `pop()` and `del` | `pop()` returns removed item; `del` does not |
| Confused `find()` and `index()` | `find()` is for strings; `index()` is for lists |
| Risk of assigning `.sort()` result | Use `sorted()` for a new sorted list |

---

## Key takeaways

```text
Lists are ordered and mutable.
Indexes start at 0.
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
