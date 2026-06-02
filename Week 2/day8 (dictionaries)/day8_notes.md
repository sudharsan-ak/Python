# Day 8 Notes - Dictionaries

Status: Cleared

Source backbone: https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 8 focused on Python dictionaries: storing labeled key-value data, accessing it safely, updating/removing values, inspecting dictionary contents, copying dictionaries, and working with nested dictionaries.

Core idea:

```text
dictionary = key-value collection
key        = label
value      = stored data
```

Use a dictionary when values need meaningful labels. If you are relying on list indexes to remember what data means, a dictionary is probably cleaner.

```python
profile = {
    "first_name": "Sudharsan",
    "age": 30,
    "city": "Lewisville"
}
```

## 1. Dictionary basics

Create dictionaries with `{}` and key-value pairs.

```python
profile = {
    "first_name": "Sudharsan",
    "age": 30,
    "is_learning_python": True
}
```

Key rules:

```text
String keys usually use quotes.
Values can be strings, numbers, booleans, lists, sets, tuples, or dictionaries.
len(dict_name) returns the number of key-value pairs.
type(dict_name) confirms the object type.
```

Empty dictionary:

```python
empty_profile = {}
```

Important callback from Day 7:

```text
{}    -> empty dictionary
set() -> empty set
```

## 2. Accessing values safely

Use square brackets when the key must exist.

```python
profile["first_name"]
profile["age"]
```

If the key is missing, square bracket access raises `KeyError`.

Use `get()` when the key might be missing.

```python
profile.get("country")                  # None if missing
profile.get("country", "Not provided") # fallback value
```

Check whether a key exists:

```python
"city" in profile
```

Important:

```text
in checks dictionary keys, not values.
```

```python
"city" in profile        # True
"Lewisville" in profile  # False if it is only a value
```

Quote rule inside f-strings:

```python
print(f"First name: {profile['first_name']}")
```

Single and double quotes both work for keys. Inside an f-string, use the opposite quote style to avoid conflicts.

## 3. Adding and updating data

Dictionaries are mutable.

```python
profile["country"] = "USA"   # add new key
profile["city"] = "Dallas"   # update existing key
```

Same syntax, two outcomes:

```text
new key      -> adds data
existing key -> updates data
```

Use `update()` for multiple additions/updates.

```python
profile.update({
    "city": "Dallas",
    "country": "USA",
    "language": "Python"
})
```

Python has spread-like dictionary unpacking with `**dict`, but `update()` and direct assignment are clearer beginner patterns.

## 4. Removing dictionary items

| Tool | Use |
|---|---|
| `pop("key")` | Remove key and return removed value |
| `pop("key", default)` | Remove safely if key may be missing |
| `popitem()` | Remove last inserted key-value pair |
| `del dict["key"]` | Delete a known key without returning value |
| `clear()` | Empty the dictionary |

```python
removed_language = profile.pop("language")
removed_state = profile.pop("state", "Not found")
del profile["country"]
removed_last_item = profile.popitem()
profile.clear()
```

Important distinctions:

```text
pop() returns the removed value.
del removes but returns nothing.
pop() without a default crashes if the key is missing.
pop() with a default does not crash if the key is missing.
popitem() returns a tuple like ("key", value).
clear() empties the dictionary but keeps the variable.
```

## 5. Dictionary views: keys(), values(), items()

Use these to inspect dictionary data.

```python
profile.keys()
profile.values()
profile.items()
```

They return view objects:

```text
dict_keys(...)
dict_values(...)
dict_items(...)
```

Convert to a list when list behavior is needed.

```python
profile_keys_list = list(profile.keys())
print(profile_keys_list[0])
```

Later, loops will make `.items()` especially useful.

## 6. Copying dictionaries

Direct assignment is not a real copy.

```python
developer_profile_reference = developer_profile
```

Both names point to the same dictionary.

Use `.copy()` for a separate top-level dictionary.

```python
profile_copy = profile.copy()
profile_copy["city"] = "Austin"
```

Rule:

```text
new_dict = old_dict        -> same dictionary reference
new_dict = old_dict.copy() -> separate top-level dictionary
```

Warning:

```text
copy() is shallow.
Nested lists/dictionaries may still be shared.
Deep copy matters later when nested data, loops, and functions become common.
```

## 7. Nested dictionaries

A nested dictionary is a dictionary inside another dictionary.

```python
learning_profile = {
    "student_name": "Sudharsan Srinivasan",
    "current_day": 8,
    "course": {
        "name": "Python from Scratch",
        "topic": "Dictionaries",
        "status": "In progress"
    }
}
```

Access and update nested values:

```python
learning_profile["course"]["name"]
learning_profile["course"]["status"] = "Almost done"
```

Add a nested dictionary as a top-level key:

```python
learning_profile["practice"] = {
    "file_name": "day8_dictionaries.py",
    "exercise_count": 7,
    "needs_review": True
}
```

Safe nested access pattern:

```python
course = learning_profile.get("course", {})
course_difficulty = course.get("difficulty", "Beginner")
```

Use nesting when related data belongs together. Do not create deep nesting without a real reason.

## 8. Choosing the right collection

```text
list  -> ordered values that can change
tuple -> grouped values that should stay fixed
set   -> unique values or group comparisons
dict  -> labeled key-value data
```

## What was practiced

```text
creating dictionaries
empty dictionaries
len() and type()
square bracket access
get() with fallback values
checking keys with in
adding/updating values
update()
pop(), popitem(), del, clear()
keys(), values(), items()
converting dictionary views to lists
copy() vs direct assignment
nested dictionaries
safe nested access with get()
choosing dict/list/tuple/set
```

## Mistakes and corrections

| Issue | Correction |
|---|---|
| Confusion about single vs double quotes for keys | Both work. Inside f-strings, use the opposite quote style. |
| Asked about JavaScript spread | Python uses `**dict` for unpacking, but `update()` is simpler for now. |
| Asked when deep copy matters | Later, with nested data, loops, functions, and mutation-heavy code. |
| Created a separate `practice` dictionary instead of adding it inside `learning_profile` | Correct: `learning_profile["practice"] = {...}`. |
| Final exercise initially missed printing updated `enrollment` after `pop()` | Fixed by printing both the removed value and updated dictionary. |
| Semicolon after `print()` | Works, but it is JavaScript muscle memory; avoid semicolons in Python. |

## Final mixed exercise status

Final scenario:

```text
Online course enrollment record
```

Practiced:

```text
dictionary creation
access
safe get()
key checks
adding/updating
removal
views
copying
nested dictionaries
safe nested get()
```

One prompt miss was corrected: after removing `"level"`, the updated `enrollment` dictionary also needed to be printed.

Final status:

```text
Day 8 - Dictionaries: Cleared
```

## Key reminders before Day 9

```text
Use dictionaries for labeled data.
Use square brackets when the key must exist.
Use get() when the key may be missing.
Use get("key", default) for fallback values.
Use in to check keys, not values.
Use dict["key"] = value to add or update.
Use update() for multiple additions/updates.
Use pop() when you need the removed value.
Use pop("key", default) when the key may be missing.
Use del only when the key exists and you do not need the removed value.
Use keys(), values(), and items() to inspect dictionary data.
Convert dictionary views with list() when list behavior is needed.
Use copy() for a separate top-level dictionary.
Remember copy() is shallow.
Use nested dictionaries to group related data.
Use chained square brackets for nested access.
Use get("nested_key", {}) for safer nested access.
```

## Next day

```text
Day 9 - Conditionals
```
