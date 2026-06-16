# Day 7 Notes - Sets

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 7 focused on sets: unique, unordered collections used for membership checks, duplicate removal, and group comparisons.

## Core topics

```text
creating sets
empty set with set()
duplicates
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
set conversion
set operations
set relationships
set use cases
```

---

## Set basics

A set stores unique values.

```python
languages = {"JavaScript", "Python", "Java", "Python", "TypeScript"}
```

Even if `"Python"` appears twice, the set keeps it once.

Rules:

```text
Sets remove duplicates automatically.
Sets do not have dependable order.
Sets do not support indexing.
```

This does not work:

```python
# languages[0]
```

Sets are for uniqueness and membership, not first/last item logic.

---

## Empty set

Correct:

```python
empty_tools = set()
```

Wrong if you want a set:

```python
empty_data = {}
```

Rule:

```text
set() -> empty set
{}    -> empty dictionary
```

Use `type()` when unsure.

---

## Membership checks

Use `in` and `not in`.

```python
has_python = "Python" in languages
missing_go = "Go" not in languages
```

Python:

```python
"Python" in languages
```

JavaScript equivalent idea:

```javascript
set.has("Python")
```

---

## Adding and updating

```python
languages.add("Go")
languages.update(["Rust", "JavaScript", "C#"])
```

Comparison:

```text
list.append() -> one item
list.extend() -> multiple items

set.add()     -> one item
set.update()  -> multiple items
```

`update()` can accept a list, tuple, set, or another iterable.

```python
skills.update(["React", "TypeScript"])
skills.update(("Docker", "AWS"))
skills.update({"MongoDB", "PostgreSQL"})
```

---

## Removing from sets

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
removed_skill = languages.pop()
temporary_skills.clear()
del old_skills
```

Rule:

```text
Use remove() when the item must exist.
Use discard() when the item may not exist.
Use pop() carefully because sets have no dependable last item.
Use clear() when you want the empty set to remain.
Use del when you want the variable gone.
```

---

## Converting to a set

Use `set()` to remove duplicates.

```python
skill_list = ["React", "Node.js", "React", "MongoDB"]
unique_skills = set(skill_list)
```

Tuple example:

```python
scores_tuple = (90, 85, 90, 70)
unique_scores = set(scores_tuple)
```

Important:

```text
set(list_or_tuple) removes duplicates.
After converting to a set, order should not be trusted.
```

---

## Core set operations

```python
frontend_skills = {"HTML", "CSS", "JavaScript", "React"}
backend_skills = {"JavaScript", "Node.js", "MongoDB"}
```

```python
all_skills = frontend_skills.union(backend_skills)
common_skills = frontend_skills.intersection(backend_skills)
frontend_only = frontend_skills.difference(backend_skills)
not_shared = frontend_skills.symmetric_difference(backend_skills)
```

Rules:

```text
union() returns everything from both sets.
intersection() returns only shared items.
difference() returns items only in the first set.
symmetric_difference() returns items not shared.
difference() direction matters.
```

---

## Relationship checks

These return booleans.

```python
required_skills = {"JavaScript", "React"}
candidate_skills = {"JavaScript", "React", "Node.js"}

required_skills.issubset(candidate_skills)
candidate_skills.issuperset(required_skills)
```

`isdisjoint()` checks whether two sets have zero overlap.

```python
frontend_skills = {"HTML", "CSS", "React"}
database_skills = {"MongoDB", "PostgreSQL"}

frontend_skills.isdisjoint(database_skills)
```

---

## Set vs list vs tuple

| Type | Use when | Allows duplicates? | Order/indexing? | Mutable? |
|---|---|---:|---:|---:|
| `list` | Items can change and order matters | Yes | Yes | Yes |
| `tuple` | Fixed grouped data | Yes | Yes | No |
| `set` | Unique values or comparisons | No | No dependable order | Yes |

Rule:

```text
Use list when order and duplicates matter.
Use tuple when the group should stay fixed.
Use set when uniqueness or comparison matters.
```

---

## What was practiced

```text
creating sets with duplicates
checking length and type
creating empty sets
membership checks
add() and update()
remove(), discard(), pop(), clear(), del
list/tuple to set conversion
union(), intersection(), difference(), symmetric_difference()
issubset(), issuperset(), isdisjoint()
choosing list vs tuple vs set
```

Final mixed exercise was cleared in `day7-final.py`.

---

## Mistakes, questions, and corrections

| Issue / Question | Correction / Clarification |
|---|---|
| Set print order changed across runs | Normal. Never depend on set order. |
| Asked why order does not matter | Sets are for uniqueness/membership, not positions. |
| Compared `append()` / `extend()` with `add()` / `update()` | One item vs multiple items. |
| Asked if `update()` can take another set | Yes, it can take list, tuple, set, or iterable. |
| Confused `union()` and `symmetric_difference()` | `union()` includes overlap; `symmetric_difference()` excludes overlap. |
| Minor label typo | Fix spelling for cleaner output. |

---

## Key takeaways

```text
Sets store unique values.
Sets remove duplicates automatically.
Sets do not have dependable order.
Sets do not support indexing.
Use set() for an empty set.
{} creates an empty dictionary.
Use in and not in for membership checks.
Use add() for one item.
Use update() for multiple items.
Use remove() when the item must exist.
Use discard() when the item may not exist.
Use pop() carefully because the removed item is unpredictable.
Use set(list_or_tuple) to remove duplicates.
Do not trust order after set conversion.
union() returns everything.
intersection() returns overlap.
difference() returns first-set-only items.
symmetric_difference() returns non-shared items.
issubset(), issuperset(), and isdisjoint() return booleans.
Use sets for uniqueness, membership checks, and group comparisons.
```
