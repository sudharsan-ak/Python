# Day 4 Notes - Strings

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 4 focused on strings: creating, formatting, indexing, slicing, searching, modifying, checking, splitting, and joining text.

## Core topics

```text
creating strings
quotes
len()
concatenation
repetition
escape characters
f-strings
indexing
slicing
string methods
split()
join()
character checks
```

---

## Creating strings

A string is text.

```python
first_name = "Sudharsan"
last_name = 'Srinivasan'
language = "Python"
```

Single and double quotes both work. Choose the one that avoids unnecessary escaping.

```python
message = "I'm learning Python"
quote = 'He said "Python is fun"'
```

Triple quotes are useful for multi-line strings.

```python
summary = f"""Name: {full_name}
City: {city}
Language: {language}"""
```

---

## Length, joining text, and f-strings

`len()` counts characters, including spaces.

```python
print(len("Python"))
print(len("Sudharsan Srinivasan"))
```

Concatenation joins strings.

```python
full_name = first_name + " " + last_name
```

Repetition uses `*`.

```python
separator = "-" * 20
```

Use f-strings for readable output.

```python
print(f"{full_name} lives in {city}.")
```

---

## Escape characters

```text
\n  new line
\t  tab
\\  backslash
\"  double quote
\'  single quote
```

Example:

```python
multi_line_message = "Python\nStrings\nPractice"
tab_message = "Name:\tSudharsan"
```

But avoid unnecessary escaping when changing the quote style is cleaner.

---

## Indexing and slicing

Strings are sequences. Indexes start at `0`.

```python
language = "Python"

print(language[0])   # P
print(language[-1])  # n
```

Slicing:

```python
print(language[:3])   # Pyt
print(language[3:])   # hon
print(language[-3:])  # hon
print(language[:])    # Python
```

Rules:

```text
Negative indexes count from the end.
Slicing includes start and excludes end.
Use [:3] instead of [0:3] when starting from the beginning.
```

---

## Common string methods

```python
name.upper()
name.lower()
name.title()
name.capitalize()
name.strip()
sentence.replace("JavaScript", "Python")
```

Important:

```text
title()       -> capitalizes every word
capitalize() -> capitalizes only the first character of the whole string
strip()       -> removes leading/trailing spaces
replace()     -> swaps matching text
```

---

## Search and check methods

```python
first_name.startswith("Sud")
first_name.endswith("san")
sentence.find("Python")
sentence.count("Python")
```

`find()` returns the starting index or `-1`.

```python
has_python = sentence.find("Python") != -1
```

Do not store the raw `find()` result in a boolean-sounding variable.

---

## split() and join()

`split()` turns a string into a list.

```python
sentence = "I am learning Python"
words = sentence.split()
```

Split by a specific separator:

```python
skills_text = "JavaScript,React,Python,Node"
skills_list = skills_text.split(",")
```

`join()` turns a list into a string.

```python
joined_skills = ", ".join(skills_list)
```

Read it as:

```text
Use this string as the glue between each item.
```

---

## Character check methods

These return `True` or `False`.

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

## What was practiced

```text
creating strings
using quote styles correctly
using len()
concatenation and f-strings
escape characters
indexing and slicing
case methods
strip() and replace()
startswith() and endswith()
find() and count()
split() and join()
character checks
```

Final mixed exercise was cleared in `day4-final.py`.

---

## Mistakes and corrections

| Issue | Correction |
|---|---|
| Escaped quotes unnecessarily | Pick the cleaner quote style |
| Mixed up `startswith()` and `endswith()` | Read method names carefully |
| Searched for wrong text | Match the prompt exactly |
| Stored raw `find()` result in `has_python` | Use `find(...) != -1` |
| Confused `title()` and `capitalize()` | `title()` affects every word; `capitalize()` affects only the whole string |
| Repeated setup unnecessarily | Reuse variables in the same file when appropriate |

---

## Key takeaways

```text
Strings are text.
Use f-strings for clean output.
Indexes start at 0.
Negative indexes count from the end.
Slicing includes start and excludes end.
Use strip() for extra spaces.
Use replace() to swap text.
Use find() to get an index or -1.
Use find(...) != -1 for boolean checks.
Use split() to break strings into lists.
Use join() to combine list items into strings.
Use character check methods for validation-style checks.
```
