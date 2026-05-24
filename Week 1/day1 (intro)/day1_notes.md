# Day 1 Notes - Python Basics

Status:

```text
Cleared
```

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## What Day 1 covered

Day 1 was the absolute beginner setup day. The goal was not to master Python yet. The goal was to understand how a Python file runs, how to print output, how to store values in variables, how basic data types look, and how to get simple user input.

Topics covered:

```text
print()
comments
variables
basic data types
strings
numbers
booleans
f-strings
input()
int() conversion
running a Python file
```

---

## 1. Printing output

Python uses `print()` to show output in the terminal.

```python
print("Hi, I'm Sudharsan")
```

JavaScript comparison:

```javascript
console.log("Hi, I'm Sudharsan");
```

The big beginner differences:

```text
Python uses print()
JavaScript uses console.log()
Python does not need semicolons
```

---

## 2. Comments

Comments are notes for humans. Python ignores them when running the file.

```python
# This prints a greeting
print("Hello")
```

Good comments explain the purpose of code. Bad comments only repeat obvious code.

Useful comment:

```python
# Convert input to int before doing math
age = int(input("Enter your age: "))
```

Less useful comment:

```python
# Print name
print(name)
```

---

## 3. Variables

Variables store values.

```python
name = "Sudharsan"
age = 30
city = "Lewisville"
```

Python uses `snake_case` for variable names.

Good:

```python
first_name = "Sudharsan"
years_experience = 6
```

Avoid JavaScript-style naming in Python:

```python
firstName = "Sudharsan"
yearsExperience = 6
```

That style is valid in many cases, but it is not Python style.

---

## 4. Strings vs numbers

A string is text. Strings need quotes.

```python
name = "Sudharsan"
city = "Lewisville"
```

Numbers usually do not need quotes.

```python
age = 30
years_experience = 6
```

Important distinction:

```python
age = 30
```

means `age` is a number.

```python
age = "30"
```

means `age` is text.

Both may print fine, but only the numeric version works directly in math.

```python
age = 30
print(age + 1)  # 31
```

This would fail:

```python
age = "30"
print(age + 1)
```

because Python cannot directly add a string and a number.

---

## 5. Basic data types introduced

Day 1 introduced the main idea that values have types.

Common types:

```python
name = "Sudharsan"        # str
age = 30                  # int
salary = 120000.50        # float
is_learning = True        # bool
skills = ["JS", "React"]  # list
```

The important beginner idea:

```text
Different types behave differently.
```

A number can be used in math.

A string is text.

A boolean is either `True` or `False`.

---

## 6. Booleans

Python booleans are capitalized:

```python
True
False
```

Not JavaScript-style lowercase:

```python
true
false
```

Example:

```python
is_engineer = True
is_learning_python = True
```

This was only introduced lightly on Day 1 and practiced more deeply later.

---

## 7. f-strings

f-strings are the clean Python way to place variables inside text.

```python
first_name = "Sudharsan"
last_name = "Srinivasan"

full_name = f"{first_name} {last_name}"

print(f"My name is {full_name}")
```

JavaScript comparison:

```javascript
const fullName = `${firstName} ${lastName}`;
```

Python f-string:

```python
full_name = f"{first_name} {last_name}"
```

The `f` before the quote tells Python to evaluate variables inside `{}`.

---

## 8. User input

Python uses `input()` to get user input from the terminal.

```python
name = input("What is your name? ")
print(f"Hello, {name}")
```

Important rule:

```text
input() always returns a string.
```

Even if the user types:

```text
30
```

Python receives it as:

```python
"30"
```

That matters when doing math.

---

## 9. Converting input for math

This is wrong for math:

```python
age = input("Enter your age: ")
next_year_age = age + 1
```

because `age` is a string.

Correct:

```python
age = int(input("Enter your age: "))
next_year_age = age + 1

print(f"Next year, you will be {next_year_age}")
```

`int()` converts a numeric string into an integer.

Another clean version:

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)
```

---

## What was practiced on Day 1

Day 1 exercises practiced:

```text
printing a greeting
creating variables
using strings and numbers
printing a sentence with f-strings
getting user input
converting input with int()
adding two user-provided numbers
combining first name and last name
printing years of software engineering experience
```

The goal was to get comfortable writing and running simple Python code.

---

## Corrections and mistakes from Day 1

| Issue | Correction |
|---|---|
| Stored `age` as `"30"` | Use `age = 30` when age should behave like a number |
| Converted input only inside `print()` | Prefer converting earlier and storing the clean numeric value |
| Extra spacing in variable assignment | Use clean spacing like `years_experience = 6` |
| Mixed text and number risk | Use `int()` before math or use f-strings for display |

Example correction:

Less clean:

```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print(int(num1) + int(num2))
```

Cleaner:

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)
```

Why this is better:

```text
After conversion, num1 and num2 are truly numbers.
The variable names match what the values are used for.
The final print stays simple.
```

---

## Day 1 key takeaways

```text
Python runs code line by line.
Use print() to show output.
Comments start with #.
Variables store values.
Strings need quotes.
Numbers usually do not need quotes.
input() always returns a string.
Use int() before doing math with input.
Use f-strings for clean output.
Use snake_case variable names.
Keep spacing clean.
```

---

## Ready for next day

```text
Day 2 - Variables, Built-in Functions, Data Types
```
