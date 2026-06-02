# Day 1 Notes - Python Basics

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 1 introduced the basic shape of Python: running a file, printing output, writing comments, storing values in variables, using basic data types, formatting output, and accepting simple user input.

## Core topics

```text
print()
comments
variables
strings
numbers
booleans
f-strings
input()
int() conversion
running a Python file
```

---

## Core syntax

```python
# This is a comment
print("Hello, Python")

first_name = "Sudharsan"
last_name = "Srinivasan"
age = 30
is_learning_python = True

full_name = f"{first_name} {last_name}"
print(f"My name is {full_name}")
```

Python comparison:

```text
Python     -> print()
JavaScript -> console.log()

Python     -> True / False
JavaScript -> true / false

Python style -> snake_case
JS style     -> camelCase
```

---

## Variables and basic types

Variables store values.

```python
name = "Sudharsan"        # str
age = 30                  # int
salary = 120000.50        # float
is_learning = True        # bool
skills = ["JS", "React"]  # list
```

Important distinction:

```python
age = 30    # number, works in math
age = "30"  # string/text, does not directly work in math
```

Rule:

```text
Use numbers when the value should be calculated.
Use strings when the value is text.
```

---

## f-strings

Use f-strings to place variables inside text.

```python
first_name = "Sudharsan"
last_name = "Srinivasan"

full_name = f"{first_name} {last_name}"
print(f"My name is {full_name}")
```

The `f` before the string allows Python to evaluate values inside `{}`.

---

## User input

`input()` gets text from the terminal.

```python
name = input("What is your name? ")
print(f"Hello, {name}")
```

Important:

```text
input() always returns a string.
```

Wrong for math:

```python
age = input("Enter your age: ")
next_year_age = age + 1
```

Correct:

```python
age = int(input("Enter your age: "))
next_year_age = age + 1

print(f"Next year, you will be {next_year_age}")
```

---

## What was practiced

```text
printing output
creating variables
using strings, numbers, and booleans
using f-strings
getting input
converting input with int()
adding user-provided numbers
printing simple profile information
```

---

## Mistakes and corrections

| Issue | Correction |
|---|---|
| Stored numeric age as `"30"` | Use `age = 30` when age should behave like a number |
| Converted input too late | Convert input before doing math |
| Mixed string and number in math | Use `int()` for math or f-strings for display |
| Extra spacing in assignments | Use clean spacing like `years_experience = 6` |

Cleaner input pattern:

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)
```

---

## Key takeaways

```text
Python runs code line by line.
Use print() for output.
Comments start with #.
Use snake_case.
Strings need quotes.
Numbers usually do not need quotes.
Python booleans are True and False.
input() always returns a string.
Use int() before math with numeric input.
Use f-strings for clean output.
Python does not need semicolons.
```

## Ready for next day

```text
Day 2 - Variables, Built-in Functions, Data Types
```
