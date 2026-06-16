# Day 18 Notes - Regular Expressions

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 18 focused on using regular expressions to search, validate, extract, and clean text with Python's built-in `re` module.

Core idea:

```text
Regex is a pattern language for working with text.
Use it when normal string methods are not enough.
```

---

# Topic 1 - Regex basics, raw strings, and `re`

Import regex tools with:

```python
import re
```

Use raw strings for regex patterns:

```python
pattern = r"\d"
```

Reason:

```text
Regex uses backslashes, and raw strings prevent Python from treating them as escape characters first.
```

Basic result mental model:

```text
match object -> pattern found
None         -> pattern not found
```

---

# Topic 2 - `search()`, `.group()`, `findall()`, and `match()`

## `re.search()`

Finds the first match anywhere in the text.

```python
result = re.search(r"TICKET", message)
```

Returns a match object or `None`.

## `.group()`

Gets the actual matched text from a match object.

```python
if result:
    print(result.group())
```

Rule:

```text
Check that the result exists before calling .group().
```

## `re.findall()`

Finds all matches and returns a list.

```python
numbers = re.findall(r"\d+", text)
```

If nothing is found, it returns `[]`.

## `re.match()`

Checks only from the beginning of the string.

```text
search() -> checks anywhere
match()  -> checks only the start
```

---

# Topic 3 - Character classes, quantifiers, and anchors

Useful beginner patterns:

| Pattern | Meaning |
|---|---|
| `\d` | one digit |
| `\w` | one word character: letter, digit, underscore |
| `\s` | one whitespace character |
| `[A-Z]` | one uppercase letter |
| `[a-z]` | one lowercase letter |
| `[0-9]` | one digit |
| `+` | one or more of the previous pattern |
| `*` | zero or more of the previous pattern |
| `?` | zero or one of the previous pattern |
| `{4}` | exactly four times |
| `^` | start of string |
| `$` | end of string |

Examples:

```python
re.search(r"\d", "INV-2045")       # finds "2"
re.search(r"\d+", "INV-2045")      # finds "2045"
re.search(r"INV-\d{4}", "INV-2045") # finds "INV-2045"
```

Validation pattern:

```python
re.search(r"^INV-\d{4}$", "INV-2045")
```

Use anchors when the whole string must match the expected format.

---

# Topic 4 - Groups and extraction

Parentheses create capture groups:

```python
result = re.search(r"CASE-(\d{4})", text)
```

Group rules:

```text
group()  -> full matched text
group(1) -> first captured group
group(2) -> second captured group
```

Example:

```python
result = re.search(r"CASE-(\d{4})", "Case CASE-4821 opened")

if result:
    print(result.group())   # CASE-4821
    print(result.group(1))  # 4821
```

Important `findall()` behavior:

```text
findall() with no groups -> returns full matches
findall() with groups    -> returns captured group values
```

Example:

```python
re.findall(r"CASE-\d{4}", text)    # ['CASE-4821']
re.findall(r"CASE-(\d{4})", text)  # ['4821']
```

Use `\.` when you need a real dot because `.` has special regex meaning.

---

# Topic 5 - `re.sub()` for cleanup and replacement

`re.sub()` replaces matching text and returns a new string.

```python
safe_text = re.sub(pattern, replacement, text)
```

Common uses:

```python
re.sub(r"\s+", " ", text)                         # clean spacing
re.sub(r"[\w.]+@\w+\.\w+", "[email-hidden]", text) # hide email
re.sub(r"\d{3}-\d{3}-\d{4}", "[phone-hidden]", text) # hide phone
re.sub(r"!+", "", text)                            # remove exclamation marks
```

Use `count=1` to replace only the first match:

```python
re.sub(r"retry", "attempt", text, count=1)
```

---

# Topic 6 - Practical regex patterns

Practical use guide:

| Need | Use |
|---|---|
| Validate whole string | `^...$` with `search()` or `fullmatch()` |
| Find first useful value | `re.search()` |
| Extract a part of a match | groups + `.group(1)` |
| Find all matching values | `re.findall()` |
| Clean or hide text | `re.sub()` |

Good habit:

```text
Build small regex patterns one piece at a time.
Do not write giant unreadable regex too early.
```

---

# Small regex addendum - useful tools to remember

```text
re.fullmatch() -> cleaner full-string validation than ^...$ with search().
re.finditer()  -> like findall(), but returns match objects with positions.
re.split()     -> split messy text using multiple separators.
re.compile()   -> reuse the same regex pattern cleanly.
re.IGNORECASE  -> search without caring about uppercase/lowercase.
|              -> OR pattern, such as approved|failed|pending.
.              -> wildcard for almost any character; use \. for a real dot.
\b             -> word boundary for whole-word matching.
```

Advanced regex tools like named groups, non-capturing groups, lazy matching, and lookaround were mentioned only as awareness and were not part of Day 18 core practice.

---

# Final mixed exercise summary

Final scenario:

```text
Event registration intake parser
```

Practiced:

```text
registration ID validation
name extraction with groups
email extraction into username and domain
session ID extraction with findall()
phone number extraction
safe message cleanup with re.sub()
anchors for validation
groups for extracting only the needed part
```

Final result:

```text
Day 18 final mixed exercise cleared.
```
