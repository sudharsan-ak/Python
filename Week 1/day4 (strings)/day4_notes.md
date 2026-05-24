# Day 4 Notes - Strings

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## What Day 4 covered

Day 4 focused on strings. The goal was to understand how to create text, format text, access characters, slice strings, use string methods, search inside strings, and convert between strings and lists.

Topics covered:

```text
creating strings
single, double, and triple quotes
len()
concatenation
string repetition
escape characters
f-strings
indexing
slicing
string methods
search/check methods
split()
join()
character check methods
```

## 1. Creating strings

A string is text.

```python
first_name = "Sudharsan"
last_name = "Srinivasan"
city = "Lewisville"
language = "Python"
```

Single quotes and double quotes both work.

```python
name = 'Sudharsan'
name = "Sudharsan"
```

Choose the quote style that avoids unnecessary escaping.

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

## 2. `len()`

`len()` counts characters.

```python
print(len("Python"))  # 6
```

Spaces count too.

```python
full_name = "Sudharsan Srinivasan"
print(len(full_name))
```

## 3. Concatenation, repetition, and f-strings

Concatenation joins strings.

```python
full_name = first_name + " " + last_name
```

String repetition uses `*`.

```python
separator = "-"
print(separator * 20)
```

Use f-strings when inserting variables into text.

```python
print(f"{full_name} lives in {city}.")
```

Avoid messy concatenation when f-strings are cleaner.

```python
print(f"{full_name} is {age} years old")
```

## 4. Escape characters

Common escape characters:

```text
\n  new line
\t  tab
\\  backslash
\"  double quote
\'  single quote
```

Examples:

```python
multi_line_message = "Python\nStrings\nPractice"
tab_message = "Name:\tSudharsan"
```

But do not escape quotes unnecessarily. Change the outer quote style instead.

```python
quote = 'He said "Python is fun"'
```

## 5. Indexing

Strings are sequences of characters.

```python
language = "Python"
```

Index map:

```text
P  y  t  h  o  n
0  1  2  3  4  5
```

Examples:

```python
print(language[0])   # P
print(language[1])   # y
print(language[-1])  # n
```

Negative indexing counts from the end.

## 6. Slicing

Slicing gets part of a string.

```python
string[start:end]
```

Important rule:

```text
start is included
end is excluded
```

Examples:

```python
language = "Python"

print(language[:3])   # Pyt
print(language[3:])   # hon
print(language[-3:])  # hon
print(language[:])    # Python
```

Prefer `language[:3]` instead of `language[0:3]` when starting from the beginning.

## 7. Common string methods

String methods use this pattern:

```python
string.method()
```

Common methods:

```python
upper()
lower()
title()
capitalize()
strip()
replace()
```

Examples:

```python
print(first_name.upper())
print(last_name.lower())
print(full_name.title())
```

Important distinction:

```text
title()      -> capitalizes every word
capitalize() -> capitalizes only the first character of the whole string
```

`strip()` removes leading/trailing spaces.

```python
messy_name = "   Sudharsan   "
clean_name = messy_name.strip()
```

`replace()` swaps text.

```python
sentence = "I am learning JavaScript"
updated_sentence = sentence.replace("JavaScript", "Python")
```

## 8. Search and check methods

Common methods:

```python
startswith()
endswith()
find()
count()
```

Examples:

```python
first_name.startswith("Sud")
first_name.endswith("san")
```

`find()` returns the starting index, or `-1` if not found.

```python
sentence = "I am learning Python"

print(sentence.find("Python"))      # index
print(sentence.find("JavaScript"))  # -1
```

Boolean pattern with `find()`:

```python
has_python = sentence.find("Python") != -1
```

Do not store the raw `find()` result in a boolean-sounding variable like `has_python`.

`count()` counts occurrences.

```python
sentence.count("Python")
```

## 9. `split()` and `join()`

`split()` turns a string into a list.

```python
sentence = "I am learning Python"
words = sentence.split()
```

Split by a specific character:

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
Use ", " as the glue between each item.
```

## 10. Character check methods

These return `True` or `False`.

```python
isalpha()
isdigit()
isalnum()
islower()
isupper()
```

Examples:

```python
"Sudharsan".isalpha()             # True
"Sudharsan Srinivasan".isalpha()  # False because of space
"30".isdigit()                    # True
"Sudharsan10".isalnum()           # True
"Sudharsan_10".isalnum()          # False because of underscore
```

## What was practiced

Day 4 practice included:

```text
creating strings
using quotes correctly
using len()
concatenation and f-strings
escape characters
indexing and negative indexing
slicing
case methods
strip() and replace()
startswith() and endswith()
find() and count()
split() and join()
character check methods
triple-quoted f-strings
```

## Mistakes and corrections

| Mistake / Issue | Correction |
|---|---|
| Escaped quotes unnecessarily | Prefer quote choice that avoids escaping |
| Mixed up `startswith()` and `endswith()` | Read method names carefully |
| Used `find("Python")` when prompt asked for `"learning"` | Search for exactly what the prompt asks |
| Stored raw `find()` result in `has_python` | Use `sentence.find("Python") != -1` |
| Thought `title()` and `capitalize()` were the same | `title()` affects every word; `capitalize()` affects only the full string |
| Tried to split practice into `methods.py` too early | Keep beginner practice in one file until imports/modules are taught |
| Repeated variable setup unnecessarily | Reuse variables in the same file when appropriate |

## Final mixed exercise status

The final mixed exercise was completed successfully in:

```text
day4-final.py
```

It covered strings, f-strings, length, indexing, slicing, methods, `find()`, `count()`, `split()`, `join()`, and character checks.

No functional mistakes in the final mixed exercise.

## Day 4 key takeaways

```text
Strings are text.
Use f-strings for clean output.
Indexes start at 0.
Negative indexes count from the end.
Slicing includes start and excludes end.
Use [:3] for first 3 characters.
Use [-3:] for last 3 characters.
Use strip() for extra spaces.
Use replace() to swap text.
Use find() to get an index or -1.
Use split() to break strings into lists.
Use join() to combine list items into strings.
Use character check methods for validation-style checks.
```

## Ready for next day

```text
Day 5 - Lists
```
