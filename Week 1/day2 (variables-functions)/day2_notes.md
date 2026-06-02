# Day 2 Notes - Variables, Built-in Functions, Data Types

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 2 expanded the basics from Day 1: built-in functions, cleaner variable naming, multiple assignment, common data types, type conversion, arithmetic, assignment shortcuts, and first awareness of Python collections.

## Core topics

```text
built-in functions
variable naming
multiple assignment
data types
type checking
type conversion
arithmetic
assignment shortcuts
collection intro
```

---

## Built-in functions

Common functions practiced:

```python
print()
len()
type()
input()
int()
float()
str()
```

Examples:

```python
name = "Sudharsan"
age = 30

print(len(name))
print(type(age))
```

Use `type()` when confused about whether a value is text, a number, a list, a dictionary, etc.

Remember:

```text
input() always returns a string.
```

---

## Variable naming

Use `snake_case`.

```python
first_name = "Sudharsan"
years_experience = 6
```

Boolean names should read like yes/no questions.

```python
is_learning_python = True
has_experience = True
can_relocate = True
```

Constants use uppercase by convention.

```python
MAX_LOGIN_ATTEMPTS = 5
DEFAULT_CITY = "Lewisville"
```

Important:

```text
A variable name should describe what the value currently stores.
```

Better:

```python
user_age = int(input("Enter age: "))
next_year_age = user_age + 1
```

Worse:

```python
user_age = int(input("Enter age: ")) + 1
```

because `user_age` no longer stores the user's current age.

---

## Multiple assignment

Python can assign multiple values at once.

```python
first_name, last_name, age = "Sudharsan", "Srinivasan", 30
```

Swap values:

```python
x, y = 100, 200
x, y = y, x
```

Unpack a list:

```python
skills = ["JavaScript", "React", "Python"]
skill_one, skill_two, skill_three = skills
```

Rule:

```text
The number of variables must match the number of values.
```

---

## Data types

```python
name = "Sudharsan"                         # str
age = 30                                   # int
rating = 4.9                               # float
is_learning_python = True                  # bool
skills = ["JavaScript", "React", "Python"] # list
profile = {"name": name, "age": age}       # dict
coordinates = (2, 3)                       # tuple
unique_numbers = {1, 2, 3}                 # set
```

Mental model:

```text
str   -> text
int   -> whole number
float -> decimal number
bool  -> True / False
list  -> ordered collection
dict  -> key-value data
tuple -> fixed grouped data
set   -> unique values
```

---

## Type conversion

Type conversion changes one type into another.

```python
age = int("30")
price = float("99.99")
age_text = str(30)
letters = list("Python")
unique_numbers = set([1, 2, 2, 3])
```

Important trap:

```python
bool("False")  # True
```

Any non-empty string is truthy, even if the text says `"False"`.

---

## Arithmetic and shortcuts

Operators:

```text
+    addition
-    subtraction
*    multiplication
/    division, returns float
//   floor division
%    remainder
**   exponent
```

Shortcut assignment:

```python
score = 50

score += 10
score -= 5
score *= 2
score /= 10
```

Python does not use `score++`. Use:

```python
score += 1
```

---

## What was practiced

```text
using len() and type()
getting input and converting it
using clear variable names
multiple assignment
swapping values
unpacking lists
creating common data types
casting strings to numbers
using set() to remove duplicates
doing arithmetic
using assignment shortcuts
calculating tax/final price
```

---

## Mistakes and corrections

| Issue | Correction |
|---|---|
| Misleading calculated-age variable | Use `next_year_age` after adding 1 |
| Forgot requested type output | Read every prompt item carefully |
| Confused `"30"` and `30` | Use `int()` before math |
| Raw output hard to read | Add labels when helpful |

Key correction:

```python
user_age = int(input("Enter age: "))
next_year_age = user_age + 1
```

---

## Key takeaways

```text
Use type() to inspect values.
Use len() for strings and collections.
Use snake_case.
Use clear variable names.
input() always returns a string.
Convert input before math.
Use int(), float(), and str() for casting.
Use set() to remove duplicates.
Use +=, -=, *=, /= to update values.
Use % to get the remainder.
```

## Ready for next day

```text
Day 3 - Operators
```
