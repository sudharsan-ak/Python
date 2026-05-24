# Day 8 Notes - Dictionaries

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## What Day 8 covered

Day 8 focused on Python dictionaries. The goal was to understand how dictionaries store labeled data using key-value pairs, how to access values safely, how to add/update/remove data, how to inspect dictionary contents, how copying works, and how nested dictionaries are structured.

Topics covered:

```text
creating dictionaries
empty dictionaries
key-value pairs
len()
type()
square bracket access
get()
checking keys with in
adding and updating data
update()
removing items with pop(), popitem(), del, clear()
keys(), values(), items()
copy()
direct assignment vs real copy
nested dictionaries
dictionary use cases
final mixed exercise
```

## 1. Dictionary basics

A dictionary stores data as key-value pairs.

```python
profile = {
    "first_name": "Sudharsan",
    "last_name": "Srinivasan",
    "age": 30,
    "city": "Lewisville",
    "is_learning_python": True
}
```

Mental model:

```text
key   -> value
name  -> "Sudharsan"
age   -> 30
city  -> "Lewisville"
```

Use a dictionary when each value needs a meaningful label.

```python
# Fragile: meaning depends on position
profile = ["Sudharsan", "Srinivasan", 30, "Lewisville"]

# Clear: meaning comes from keys
profile = {
    "first_name": "Sudharsan",
    "last_name": "Srinivasan",
    "age": 30,
    "city": "Lewisville"
}
```

String keys usually use quotes in Python.

## 2. Empty dictionary

An empty dictionary is created with `{}`.

```python
empty_profile = {}
```

Important callback from Day 7:

```text
{}    -> empty dictionary
set() -> empty set
```

Use `type()` when unsure.

```python
print(type(empty_profile))  # <class 'dict'>
```

## 3. Length and type

`len()` returns the number of key-value pairs.

```python
print(len(profile))
print(type(profile))
```

For this dictionary:

```python
profile = {"first_name": "Sudharsan", "age": 30, "city": "Lewisville"}
```

`len(profile)` returns `3` because there are three keys.

## 4. Accessing values

Use square brackets when the key must exist.

```python
profile["first_name"]
profile["city"]
profile["age"]
```

Normal dictionaries do not use dot access.

```python
# profile.first_name  # wrong for normal dictionaries
```

If the key does not exist, square bracket access raises a `KeyError`.

Use `get()` when the key might be missing.

```python
profile.get("country")                  # None if missing
profile.get("country", "Not provided") # fallback value
```

Rule:

```text
Square brackets -> key must exist.
get()           -> key might be missing.
```

## 5. Checking whether a key exists

Use `in` to check if a key exists.

```python
has_city = "city" in profile
has_country = "country" in profile
```

Important:

```text
in checks dictionary keys, not values.
```

Example:

```python
"city" in profile        # True
"Lewisville" in profile  # False, because it is a value
```

## 6. f-strings and dictionary key quotes

Dictionary keys can use single or double quotes.

```python
profile["first_name"]
profile['first_name']
```

Inside an f-string, use the opposite quote style to avoid quote conflicts.

```python
print(f"First name: {profile['first_name']}")
```

## 7. Adding and updating dictionary data

Dictionaries are mutable.

Add a new key-value pair:

```python
profile["country"] = "USA"
```

Update an existing value:

```python
profile["city"] = "Dallas"
```

Same syntax, two behaviors:

```text
If the key does not exist -> add it.
If the key already exists -> update it.
```

Use `update()` for multiple additions/updates.

```python
profile.update({
    "city": "Dallas",
    "country": "USA",
    "favorite_language": "JavaScript"
})
```

Python has spread-like dictionary unpacking with `**`, but for now direct assignment and `update()` are the cleaner beginner patterns.

## 8. Removing dictionary items

Main removal tools:

| Tool | Meaning |
|---|---|
| `pop("key")` | Removes a key and returns its value |
| `pop("key", default)` | Removes safely and returns default if missing |
| `popitem()` | Removes the last inserted key-value pair |
| `del dict["key"]` | Deletes a key without returning the value |
| `clear()` | Empties the dictionary |

Examples:

```python
removed_language = profile.pop("favorite_language")
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
popitem() returns a tuple like (key, value).
clear() empties the dictionary but keeps the variable.
```

## 9. Dictionary views: keys(), values(), items()

Use these to inspect dictionary data.

```python
profile_keys = profile.keys()
profile_values = profile.values()
profile_items = profile.items()
```

They return dictionary view objects:

```text
dict_keys([...])
dict_values([...])
dict_items([...])
```

Convert to a list if list behavior is needed.

```python
profile_keys_list = list(profile.keys())
print(profile_keys_list[0])
```

Loops will make `items()` more useful later.

## 10. Copying dictionaries

Direct assignment is not a real copy.

```python
developer_profile_reference = developer_profile
```

Both names point to the same dictionary. If one changes, the other changes too.

Use `.copy()` for a separate top-level dictionary.

```python
profile_copy = profile.copy()
profile_copy["city"] = "Austin"
```

The original `profile` stays unchanged.

Rule:

```text
=       -> same dictionary reference
copy()  -> new top-level dictionary
```

Warning: `copy()` is shallow. Nested lists/dictionaries may still be shared. Deep copying will matter later when loops, functions, and nested data become common.

## 11. Nested dictionaries

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

Access nested values with chained square brackets.

```python
learning_profile["course"]["name"]
learning_profile["course"]["topic"]
```

Update nested values:

```python
learning_profile["course"]["status"] = "Almost done"
```

Add a new top-level key whose value is another dictionary:

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

## 12. Dict vs list vs tuple vs set

```text
list  -> order matters and items can change
tuple -> values are grouped and should stay fixed
set   -> values should be unique or compared as groups
dict  -> values need meaningful labels
```

Blunt rule: if index positions are carrying the meaning, you probably need a dictionary.

## What was practiced

Day 8 practice included:

```text
creating dictionaries
printing dictionaries
checking length and type
creating an empty dictionary
accessing values with square brackets
using get() for missing keys and default values
checking keys with in
adding new key-value pairs
updating existing values
using update()
removing items with pop(), del, popitem(), and clear()
using keys(), values(), and items()
converting dict_keys to a list
copying dictionaries with copy()
comparing copy() with direct assignment
creating nested dictionaries
accessing and updating nested values
safe nested get() patterns
choosing between dict/list/tuple/set
```

## Mistakes, questions, and corrections

| Issue / Question | Correction / Clarification |
|---|---|
| Asked whether square bracket access requires single quotes | Single or double quotes both work; inside f-strings, use the opposite quote style to avoid conflicts. |
| Asked about JavaScript spread | Python does not use `...`; dictionary unpacking uses `**dict`, but `update()` is simpler for now. |
| Asked when deep copy matters | Deep copy matters later with nested data, loops, functions, and mutation-heavy code. |
| Created separate `practice` dictionary instead of adding it to `learning_profile` | Correct pattern: `learning_profile["practice"] = {...}`. |
| Final exercise initially missed printing `enrollment` after removing `level` | Fixed by printing both `removed_level` and the updated `enrollment`. |
| Semicolon appeared after one print statement | Works, but it is JavaScript muscle memory; avoid semicolons in Python. |
| Minor label/casing style issues | Not functional, but cleaner labels make terminal output easier to read. |

## Final mixed exercise status

The final mixed exercise was completed successfully in:

```text
day8-final.py
```

It used a fresh online course enrollment scenario instead of repeating the same `profile` examples from the topic exercises. It covered the full Day 8 dictionary flow: creation, access, `get()`, key checks, adding/updating, removal, views, copying, nested dictionaries, and safe nested access.

One real miss was corrected: after removing `level`, the updated `enrollment` dictionary also needed to be printed.

Final status:

```text
Cleared
```

## Day 8 key takeaways

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
Direct assignment is not a real copy.
Use copy() for a separate top-level dictionary.
copy() is shallow; nested data needs more care later.
Use nested dictionaries to group related data.
Use chained square brackets for nested dictionary access.
Use get("nested_key", {}) for safer nested access.
```

## Ready for next day

```text
Day 9 - Conditionals
```
