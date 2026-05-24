# Day 2 Notes - Variables, Built-in Functions, Data Types

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## What Day 2 covered

Day 2 expanded the basics from Day 1. The main goal was to get comfortable with Python variables, built-in functions, data types, type conversion, arithmetic, and the first intro to collections.

Topics covered:

```text
built-in functions
variable naming
multiple variable assignment
data types
type checking
type conversion
numbers and arithmetic
assignment shortcuts
lists, dictionaries, tuples, sets intro
```

## 1. Built-in functions

Built-in functions are functions Python gives you by default.

Main functions practiced:

```python
print()
len()
type()
input()
int()
float()
str()
```

`print()` shows output.

```python
print("Hello")
```

`len()` returns the length of a string or collection.

```python
name = "Sudharsan"
print(len(name))
```

`type()` shows the data type of a value.

```python
age = 30
print(type(age))  # <class 'int'>
```

Use `type()` when confused about whether something is a string, number, list, etc.

`input()` gets user input from the terminal.

```python
user_age = input("Enter your age: ")
```

Important:

```text
input() always returns a string.
```

`int()`, `float()`, and `str()` are used for type conversion.

```python
age = int("30")
price = float("99.99")
age_text = str(30)
```

## 2. Variable naming

Python style uses `snake_case`.

Good:

```python
first_name = "Sudharsan"
years_experience = 6
```

Avoid JavaScript-style camelCase while learning Python:

```python
yearsExperience = 6
```

Boolean names should read like yes/no questions.

```python
is_learning_python = True
has_experience = True
can_relocate = True
```

Constants use uppercase by convention:

```python
MAX_LOGIN_ATTEMPTS = 5
DEFAULT_CITY = "Lewisville"
```

Important rule:

```text
Variable names should describe the value they currently store.
```

Bad:

```python
user_age = int(input("Enter age: ")) + 1
```

Better:

```python
user_age = int(input("Enter age: "))
next_year_age = user_age + 1
```

## 3. Multiple variable assignment

Python can assign multiple variables in one line.

```python
first_name, last_name, age = "Sudharsan", "Srinivasan", 30
```

Swapping values:

```python
x, y = 100, 200
x, y = y, x
```

Unpacking a list:

```python
skills = ["JavaScript", "React", "Python"]
skill_one, skill_two, skill_three = skills
```

Rule:

```text
The number of variables must match the number of values.
```

This fails:

```python
a, b = [1, 2, 3]
```

because there are 3 values but only 2 variables.

## 4. Data types

Main data types introduced:

```python
name = "Sudharsan"                         # str
age = 30                                   # int
rating = 4.9                               # float
is_learning_python = True                  # bool
skills = ["JavaScript", "React", "Python"] # list

profile = {
    "name": name,
    "age": age,
    "city": "Lewisville"
}                                          # dict

coordinates = (2, 3)                       # tuple
unique_numbers = {1, 2, 3, 3, 4}           # set
```

Simple mental model:

```text
str   -> text
int   -> whole number
float -> decimal number
bool  -> True/False
list  -> ordered collection
dict  -> key-value data
tuple -> fixed-style grouped data
set   -> unique values
```

Dictionaries are similar in idea to JavaScript objects.

## 5. Type conversion / casting

Type conversion means changing one type into another.

Common conversions:

```python
int()
float()
str()
bool()
list()
set()
tuple()
```

Examples:

```python
age = int("30")
price = float("99.99")
age_text = str(30)
letters = list("Python")
unique_numbers = set([1, 2, 2, 3])
```

Important boolean trap:

```python
bool("False")
```

returns:

```text
True
```

because non-empty strings are truthy.

## 6. Numbers and arithmetic

Arithmetic operators practiced:

```text
+    addition
-    subtraction
*    multiplication
/    division
//   floor division
%    modulus
**   exponent
```

Example:

```python
num1 = 20
num2 = 6

print(num1 + num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
```

Important:

```text
/ returns a float.
% returns the remainder.
```

Modulus is useful for checking even/odd numbers later.

```python
number % 2
```

## 7. Assignment shortcut operators

Shortcut operators update an existing value.

```python
score = 50

score += 10
score -= 5
score *= 2
score /= 10
```

Python does not use:

```python
score++
```

Use:

```python
score += 1
```

## What was practiced

Day 2 practice included:

```text
using len() and type()
getting input and converting it
using clear variable names
multiple assignment
swapping values
unpacking lists
creating common data types
printing types
using lists and dictionaries
casting strings to numbers
using set() to remove duplicates
doing arithmetic
using assignment shortcuts
calculating tax/final price
```

## Mistakes and corrections

| Issue | Correction |
|---|---|
| Misleading variable name for calculated age | Use `next_year_age` after adding 1 |
| Forgetting to print requested types | Read every prompt item carefully |
| Confusing `"30"` and `30` | Use `int()` before math |
| Raw output can be hard to read | Add labels when helpful |
| Over-formatting dictionaries | Keep normal readable Python formatting |

Key correction:

```python
user_age = int(input("Enter age: "))
next_year_age = user_age + 1
```

not:

```python
user_age = int(input("Enter age: ")) + 1
```

## Day 2 key takeaways

```text
Use type() to inspect values.
Use len() for strings/lists.
Use snake_case.
Use clear variable names.
input() always returns a string.
Convert input before doing math.
Use int() for whole numbers.
Use float() for decimal numbers.
Use str() when converting values to text.
Use set() to remove duplicates.
Dictionaries store key-value data.
Lists store ordered data.
Tuples are fixed-style grouped data.
Sets store unique values.
Use +=, -=, *=, /= to update values.
Use % to get the remainder.
```

## Ready for next day

```text
Day 3 - Operators
```
