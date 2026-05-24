# Day 7 Notes - Sets

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## What Day 7 covered

Day 7 focused on Python sets. The main goal was to understand how sets store unique values, how they differ from lists and tuples, and how to compare groups of data.

Topics covered:

```text
creating sets
empty set with set()
duplicates removed automatically
set order
len()
type()
in / not in
add()
update()
remove()
discard()
pop()
clear()
del
list/tuple to set conversion
union()
intersection()
difference()
symmetric_difference()
issubset()
issuperset()
isdisjoint()
set use cases
final mixed exercise
```

## 1. Set basics

A set stores unique values.

```python
languages = {"JavaScript", "Python", "Java", "Python", "TypeScript"}
```

Even though `"Python"` appears twice, the set keeps it only once.

Important rules:

```text
Sets remove duplicates automatically.
Sets do not have dependable order.
Sets do not support indexing.
```

This does not work:

```python
# languages[0]
```

A set is not for first item, last item, or position-based logic.

## 2. Empty set

Correct empty set:

```python
empty_tools = set()
```

This is not an empty set:

```python
empty_data = {}
```

`{}` creates an empty dictionary.

Rule:

```text
set() -> empty set
{}    -> empty dictionary
```

Use `type()` when unsure:

```python
print(type(empty_tools))
print(type(empty_data))
```

## 3. Set order

A set does not preserve a dependable order.

You saw this directly when the same set printed in a different order across runs.

Correct mental model:

```text
The printed order may look stable sometimes.
The printed order may change sometimes.
Never depend on set order.
```

This is fine:

```python
"Python" in languages
```

This is wrong:

```python
# languages[0]
```

Sets are built for uniqueness and membership checks, not indexing.

## 4. Membership checks

Use `in`:

```python
has_python = "Python" in languages
```

Use `not in`:

```python
missing_go = "Go" not in languages
```

JavaScript comparison:

```javascript
set.has("Python")
```

Python:

```python
"Python" in languages
```

## 5. Adding and updating sets

Sets are mutable, meaning they can be changed after creation.

Use `add()` for one item:

```python
languages.add("Go")
```

Use `update()` for multiple items:

```python
languages.update(["Rust", "JavaScript", "C#"])
```

Comparison with lists:

```text
list.append() -> adds one item
list.extend() -> adds multiple items

set.add()     -> adds one item
set.update()  -> adds multiple items
```

`update()` can accept a list, tuple, or another set.

```python
skills.update(["React", "TypeScript"])
skills.update(("Docker", "AWS"))
skills.update({"MongoDB", "PostgreSQL"})
```

## 6. Removing from sets

Main removal tools:

| Method | Meaning |
|---|---|
| `remove(item)` | Removes item, crashes if missing |
| `discard(item)` | Removes item, does not crash if missing |
| `pop()` | Removes and returns an unpredictable item |
| `clear()` | Empties the set |
| `del set_name` | Deletes the variable |

Examples:

```python
languages.remove("Java")
languages.discard("Ruby")
removed_skill = full_stack_skills.pop()
temporary_skills.clear()
del old_skills
```

Important:

```text
Use remove() when the item must exist.
Use discard() when the item may not exist.
Use pop() carefully because sets have no dependable last item.
Use clear() when you want the empty set to remain.
Use del when you want the variable gone.
```

## 7. Converting lists/tuples to sets

Use `set()` to remove duplicates.

List example:

```python
skill_list = ["React", "Node.js", "React", "MongoDB", "Node.js", "Docker"]
unique_skills = set(skill_list)
```

Tuple example:

```python
scores_tuple = (90, 85, 90, 70, 85, 100)
unique_scores = set(scores_tuple)
```

Important:

```text
set(list_or_tuple) removes duplicates.
After converting to a set, order should not be trusted.
```

You can convert back:

```python
unique_skills_list = list(unique_skills)
```

But the original order is not guaranteed.

## 8. Core set operations

Use set operations to compare groups.

Example:

```python
frontend_skills = {"HTML", "CSS", "JavaScript", "React"}
backend_skills = {"JavaScript", "Node.js", "Express", "MongoDB"}
```

### `union()`

Everything from both sets:

```python
all_skills = frontend_skills.union(backend_skills)
```

Mental model:

```text
union = everything
```

### `intersection()`

Only shared items:

```python
common_skills = frontend_skills.intersection(backend_skills)
```

Mental model:

```text
intersection = overlap
```

### `difference()`

Items in the first set but not the second:

```python
frontend_only = frontend_skills.difference(backend_skills)
backend_only = backend_skills.difference(frontend_skills)
```

Important:

```text
difference() direction matters.
A.difference(B) is not the same as B.difference(A).
```

### `symmetric_difference()`

Items that are not shared:

```python
not_shared = frontend_skills.symmetric_difference(backend_skills)
```

Mental model:

```text
symmetric_difference = everything except the overlap
```

Key distinction:

```text
union() includes shared items.
symmetric_difference() excludes shared items.
```

They only match when two sets have no overlap.

## 9. Set relationship checks

These return `True` or `False`.

### `issubset()`

Checks whether everything in one set exists inside another set.

```python
required_skills = {"JavaScript", "React"}
candidate_skills = {"JavaScript", "React", "Node.js", "MongoDB"}

required_is_subset = required_skills.issubset(candidate_skills)
```

### `issuperset()`

Checks whether one set contains everything from another set.

```python
candidate_is_superset = candidate_skills.issuperset(required_skills)
```

### `isdisjoint()`

Checks whether two sets have zero overlap.

```python
frontend_skills = {"HTML", "CSS", "React"}
database_skills = {"MongoDB", "PostgreSQL"}

frontend_database_disjoint = frontend_skills.isdisjoint(database_skills)
```

If they share nothing, result is `True`.

If they share at least one item, result is `False`.

## 10. Set vs list vs tuple

| Type | Use when | Allows duplicates? | Order/indexing? | Mutable? |
|---|---|---:|---:|---:|
| `list` | Items can change and order matters | Yes | Yes | Yes |
| `tuple` | Fixed grouped data | Yes | Yes | No |
| `set` | Unique values or comparisons | No | No dependable order | Yes |

Simple rule:

```text
Use list when order and duplicates matter.
Use tuple when the group should stay fixed.
Use set when uniqueness or comparison matters.
```

## What was practiced

Day 7 practice included:

```text
creating sets with duplicates
checking set length and type
creating an empty set with set()
confirming {} creates a dictionary
membership checks with in and not in
explaining why sets cannot be indexed
adding with add()
updating with update()
removing with remove(), discard(), pop(), clear(), and del
converting lists/tuples to sets
using union(), intersection(), difference(), symmetric_difference()
using issubset(), issuperset(), isdisjoint()
choosing between list, tuple, and set
```

## Mistakes, questions, and corrections

| Issue / Question | Correction / Clarification |
|---|---|
| Set print order changed across runs | Completely normal. The real rule is never depend on set order. |
| Asked why order does not matter | Sets are built for uniqueness and membership checks, not positions. |
| Compared `append()` / `extend()` with `add()` / `update()` | `append()` and `add()` add one item; `extend()` and `update()` add multiple items. |
| Asked if `update()` can take another set | Yes, `update()` can take a list, tuple, set, or other iterable. |
| Confused `union()` and `symmetric_difference()` | `union()` includes shared items; `symmetric_difference()` excludes shared items. |
| Minor typo in output label: `unqiue` | Fix spelling for cleaner output. |
| Minor label/casing style issues | Not functional, but clean labels make terminal output easier to read. |

## Final mixed exercise status

The final mixed exercise was completed successfully in:

```text
day7-final.py
```

It covered:

```text
set creation
duplicate removal
empty set creation
membership checks
add()
update()
remove()
discard()
list to set conversion
union()
intersection()
difference()
symmetric_difference()
issubset()
issuperset()
set vs list explanation
```

No functional mistakes in the final mixed exercise.

## Day 7 key takeaways

```text
Sets store unique values.
Sets remove duplicates automatically.
Sets do not have dependable order.
Sets do not support indexing.
Use set() to create an empty set.
{} creates an empty dictionary.
Use len() to count unique set items.
Use in and not in for membership checks.
Sets are mutable, so you can add/remove items.
Use add() to add one item.
Use update() to add multiple items.
Use remove() when the item must exist.
Use discard() when the item may not exist.
Use pop() carefully because the removed item is unpredictable.
Use clear() to empty a set.
Use del to delete the set variable.
Use set(list_or_tuple) to remove duplicates.
Converting through a set means order should not be trusted.
union() returns everything from both sets.
intersection() returns only shared items.
difference() returns items only in the first set.
symmetric_difference() returns items not shared.
issubset(), issuperset(), and isdisjoint() return booleans.
Use sets for uniqueness, membership checks, and group comparisons.
```

## Ready for next day

```text
Day 8 - Dictionaries
```
