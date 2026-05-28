# Week 1 Notes - Python Foundations

Status:

```text
Day 1 - Cleared
Day 2 - Cleared
Day 3 - Cleared
Day 4 - Cleared
Day 5 - Cleared
Day 6 - Cleared
Day 7 - Cleared
```

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## What Week 1 covered

Week 1 built the Python foundation from absolute scratch. The goal was to become comfortable writing basic Python code, understanding values and types, using operators, and working with the first major collection types.

Completed topics:

```text
Day 1 - Python Basics
Day 2 - Variables, Built-in Functions, Data Types
Day 3 - Operators
Day 4 - Strings
Day 5 - Lists
Day 6 - Tuples
Day 7 - Sets
```

Main foundation built:

```text
print output
comments
variables
basic data types
f-strings
input()
type conversion
arithmetic
comparison operators
logical operators
strings
lists
tuples
sets
collection choice
```

---

# Day 1 - Python Basics

## Main goal

Day 1 introduced how a Python file runs and how to write basic output, store values, and accept simple user input.

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

## Printing output

Python uses `print()` to show output in the terminal.

```python
print("Hello, Python")
```

JavaScript comparison:

```javascript
console.log("Hello, JavaScript");
```

Important difference:

```text
Python uses print()
JavaScript uses console.log()
Python does not require semicolons
```

## Comments

Comments start with `#`.

```python
# This prints a greeting
print("Hello")
```

Good comments explain why something is being done.

```python
# Convert input to int before doing math
age = int(input("Enter your age: "))
```

Avoid useless comments that only repeat the code.

## Variables

Variables store values.

```python
first_name = "Sudharsan"
age = 30
city = "Lewisville"
```

Python style uses `snake_case`.

```python
years_experience = 6
```

Avoid JavaScript-style naming while learning Python.

```python
yearsExperience = 6
```

## Strings, numbers, and booleans

Strings are text and need quotes.

```python
name = "Sudharsan"
```

Numbers usually do not need quotes.

```python
age = 30
```

Python booleans are capitalized.

```python
is_learning_python = True
is_finished = False
```

Not:

```python
is_learning_python = true
```

## f-strings

f-strings are the clean Python way to insert variables into text.

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

## input()

`input()` gets user input from the terminal.

```python
name = input("What is your name? ")
print(f"Hello, {name}")
```

Important rule:

```text
input() always returns a string.
```

So this is wrong for math:

```python
age = input("Enter your age: ")
next_year_age = age + 1
```

Correct:

```python
age = int(input("Enter your age: "))
next_year_age = age + 1
```

## Day 1 key takeaways

```text
Python runs code line by line.
Use print() to show output.
Comments start with #.
Variables store values.
Use snake_case.
Strings need quotes.
Numbers usually do not need quotes.
Python booleans are True and False.
Use f-strings for clean output.
input() always returns text.
Use int() before math with numeric input.
```

---

# Day 2 - Variables, Built-in Functions, Data Types

## Main goal

Day 2 expanded the basics into Python's built-in functions, type checking, type conversion, arithmetic, and the first intro to collections.

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
intro to lists, dictionaries, tuples, and sets
```

## Built-in functions

Common built-in functions practiced:

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

Use `type()` when confused about what kind of value you are working with.

## Clear variable naming

Variable names should describe the value they currently store.

Better:

```python
user_age = int(input("Enter age: "))
next_year_age = user_age + 1
```

Worse:

```python
user_age = int(input("Enter age: ")) + 1
```

Why the first one is better:

```text
user_age stores the user's actual age.
next_year_age stores the calculated future age.
The names match the values.
```

Boolean variables should read like yes/no questions.

```python
is_learning_python = True
has_experience = True
can_relocate = True
```

## Multiple assignment

Python can assign multiple variables in one line.

```python
first_name, last_name, age = "Sudharsan", "Srinivasan", 30
```

Swapping values:

```python
x, y = 100, 200
x, y = y, x
```

Unpacking:

```python
skills = ["JavaScript", "React", "Python"]
skill_one, skill_two, skill_three = skills
```

Rule:

```text
The number of variables must match the number of values.
```

## Data types

Main types introduced:

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
tuple -> fixed-style grouped data
set   -> unique values
```

## Type conversion

Type conversion means changing one type into another.

```python
age = int("30")
price = float("99.99")
age_text = str(30)
letters = list("Python")
unique_numbers = set([1, 2, 2, 3])
```

Important trap:

```python
bool("False")
```

This returns `True` because non-empty strings are truthy.

## Arithmetic

Operators practiced:

```text
+    addition
-    subtraction
*    multiplication
/    division
//   floor division
%    modulus / remainder
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

## Assignment shortcuts

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

## Day 2 key takeaways

```text
Use type() to inspect values.
Use len() for strings and collections.
Use clear variable names.
input() always returns a string.
Convert input before doing math.
Use int(), float(), and str() for casting.
Use +=, -=, *=, and /= to update existing values.
Use % to get the remainder.
Lists store ordered data.
Dictionaries store key-value data.
Tuples are fixed-style grouped data.
Sets store unique values.
```

---

# Day 3 - Operators

## Main goal

Day 3 focused on assignment, comparison, boolean logic, and how Python evaluates expressions.

Topics covered:

```text
booleans
assignment operators
comparison operators
logical operators
operator precedence
```

## Booleans

Python booleans are:

```python
True
False
```

Use boolean variable names that read clearly.

```python
is_software_engineer = True
has_experience = True
is_blocked = False
```

## Assignment vs comparison

This assigns a value:

```python
age = 30
```

This compares a value:

```python
age == 30
```

Rule:

```text
= assigns
== compares
```

Python does not use JavaScript strict equality.

```python
# age === 30  # wrong in Python
age == 30
```

## Comparison operators

Comparison operators return `True` or `False`.

```text
==   equal to
!=   not equal to
>    greater than
<    less than
>=   greater than or equal to
<=   less than or equal to
```

Example:

```python
age = 30

print(age == 30)
print(age != 25)
print(age >= 18)
```

## Logical operators

Python uses:

```python
and
or
not
```

`and` requires both sides to be true.

```python
age = 30
has_experience = True

print(age >= 18 and has_experience)
```

`or` requires at least one side to be true.

```python
has_degree = False
has_experience = True

print(has_degree or has_experience)
```

`not` flips a boolean.

```python
is_blocked = False
print(not is_blocked)
```

JavaScript comparison:

```javascript
age >= 18 && hasExperience
hasDegree || hasExperience
!isBlocked
```

Python:

```python
age >= 18 and has_experience
has_degree or has_experience
not is_blocked
```

## Cleaner boolean style

Avoid unnecessary comparisons.

Noisy:

```python
has_experience == True
```

Cleaner:

```python
has_experience
```

Noisy:

```python
is_blocked == False
```

Cleaner:

```python
not is_blocked
```

## Operator precedence

Python follows an order when evaluating expressions.

```python
result = 10 + 5 * 2
print(result)  # 20
```

Multiplication happens before addition.

Use parentheses when needed.

```python
result = (10 + 5) * 2
print(result)  # 30
```

For mixed logic, use parentheses instead of trying to be clever.

```python
(age >= 18 and score > 70) or is_holiday
```

## Day 3 key takeaways

```text
Use True and False, not true and false.
Use = for assignment.
Use == for comparison.
Python does not use ===.
Python does not use ++.
Use += 1 to increment.
Comparison operators return booleans.
and requires both conditions to be true.
or requires at least one condition to be true.
not flips a boolean.
Avoid unnecessary == True and == False.
Use parentheses for mixed logic.
```

---

# Day 4 - Strings

## Main goal

Day 4 focused on text: creating strings, formatting them, indexing/slicing, searching, modifying, and converting strings to/from lists.

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

## Creating strings

A string is text.

```python
first_name = "Sudharsan"
last_name = "Srinivasan"
city = "Lewisville"
language = "Python"
```

Single and double quotes both work.

```python
name = 'Sudharsan'
name = "Sudharsan"
```

Choose the quote style that avoids unnecessary escaping.

```python
message = "I'm learning Python"
quote = 'He said "Python is fun"'
```

## len()

`len()` counts characters.

```python
print(len("Python"))  # 6
```

Spaces count too.

## Concatenation, repetition, and f-strings

Concatenation:

```python
full_name = first_name + " " + last_name
```

Repetition:

```python
separator = "-"
print(separator * 20)
```

f-string:

```python
print(f"{full_name} lives in {city}.")
```

Use f-strings instead of messy concatenation when inserting values.

## Escape characters

Common escape characters:

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

Do not escape quotes unnecessarily. Often, choosing the other quote style is cleaner.

## Indexing

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
print(language[0])
print(language[1])
print(language[-1])
```

Negative indexes count from the end.

## Slicing

Slicing gets part of a string.

```python
string[start:end]
```

Rule:

```text
start is included
end is excluded
```

Examples:

```python
language = "Python"

print(language[:3])
print(language[3:])
print(language[-3:])
print(language[:])
```

## Common string methods

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
title()       -> capitalizes every word
capitalize()  -> capitalizes only the first character of the whole string
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

## Search and check methods

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

`find()` returns the starting index or `-1` if missing.

```python
sentence = "I am learning Python"

print(sentence.find("Python"))
print(sentence.find("JavaScript"))
```

Boolean pattern:

```python
has_python = sentence.find("Python") != -1
```

Do not store raw `find()` output in a boolean-sounding variable.

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
Use ", " as the glue between each item.
```

## Character check methods

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
"Sudharsan".isalpha()
"30".isdigit()
"Sudharsan10".isalnum()
```

Important:

```text
"Sudharsan Srinivasan".isalpha() is False because of the space.
"Sudharsan_10".isalnum() is False because of the underscore.
```

## Day 4 key takeaways

```text
Strings are text.
Use f-strings for clean output.
Indexes start at 0.
Negative indexes count from the end.
Slicing includes start and excludes end.
Use strip() for extra spaces.
Use replace() to swap text.
Use find() to get an index or -1.
Use find(...) != -1 when storing a boolean.
Use split() to break strings into lists.
Use join() to combine list items into a string.
Use character check methods for validation-style checks.
```

---

# Day 5 - Lists

## Main goal

Day 5 focused on ordered, mutable collections.

Topics covered:

```text
creating lists
len()
indexing
negative indexing
slicing
in
modifying items
append()
insert()
extend()
remove()
pop()
del
clear()
copy()
joining with +
count()
index()
reverse()
sort()
sorted()
```

## List basics

A list stores multiple values inside one variable.

```python
skills = ["JavaScript", "React", "Node.js", "Python", "MongoDB"]
```

Lists use square brackets.

```python
empty_list = []
```

Important rule:

```text
Text values need quotes.
Numbers do not need quotes.
Booleans do not need quotes.
Existing variables do not need quotes.
```

## len()

`len()` returns how many items are in the list.

```python
skills = ["JavaScript", "React", "Python"]
print(len(skills))  # 3
```

## Indexing and slicing

Lists are ordered. Indexes start at `0`.

```python
skills = ["JavaScript", "React", "Node.js", "Python", "MongoDB"]

print(skills[0])
print(skills[1])
print(skills[-1])
print(skills[-2])
```

Slicing gets part of a list.

```python
print(skills[:3])
print(skills[2:])
print(skills[-2:])
print(skills[:])
```

Rule:

```text
start is included
end is excluded
```

## Membership and modifying items

Use `in` to check whether an item exists.

```python
has_python = "Python" in skills
```

Lists are mutable, so items can be changed.

```python
skills[2] = "Node.js"
skills[-1] = "PostgreSQL"
```

## Adding items

```text
append() -> add one item to the end
insert() -> add one item at a specific index
extend() -> add multiple items from another list
```

Examples:

```python
skills.append("AWS")
skills.insert(1, "TypeScript")
skills.extend(["Express", "Docker", "PostgreSQL"])
```

Important difference:

```python
skills.append(["Express", "Docker"])
```

adds one nested list.

```python
skills.extend(["Express", "Docker"])
```

adds each item separately.

## Removing items

```text
remove() -> remove by value
pop()    -> remove by index and optionally return removed item
del      -> delete by index or slice
clear()  -> empty the whole list
```

Examples:

```python
skills.remove("AWS")
removed_skill = skills.pop()
removed_first_skill = skills.pop(0)
del skills[1]
temporary_items.clear()
```

Important:

```text
remove() removes the first matching value.
remove() crashes if the value does not exist.
pop() returns the removed item.
del removes but returns nothing.
clear() keeps the list variable but empties it.
```

## Copying lists

Bad copy:

```python
skills_copy = skills
```

Both variables point to the same list.

Good copy:

```python
skills_copy = skills.copy()
```

Another valid option:

```python
skills_copy = skills[:]
```

Prefer `.copy()` while learning because it is clearer.

## Joining lists

Use `+` to create a new combined list.

```python
frontend_skills = ["HTML", "CSS", "JavaScript", "React"]
backend_skills = ["Node.js", "Express", "MongoDB", "PostgreSQL"]

full_stack_skills = frontend_skills + backend_skills
```

Difference:

```text
extend() modifies the original list.
+ creates a new combined list.
```

## count() and index()

`count()` counts occurrences.

```python
postgres_count = skills.count("PostgreSQL")
```

`index()` finds the first position.

```python
python_index = skills.index("Python")
```

Warning:

```text
index() crashes if the value does not exist.
```

Safer pattern:

```python
if "Java" in skills:
    java_index = skills.index("Java")
```

## reverse(), sort(), and sorted()

`reverse()` reverses the original list.

```python
cities.reverse()
```

`sort()` sorts the original list.

```python
numbers.sort()
numbers.sort(reverse=True)
```

`sorted()` creates a sorted copy.

```python
sorted_numbers = sorted(numbers)
```

Do not do this:

```python
sorted_skills = skills.sort()
```

`sort()` mutates the list and returns `None`.

Correct:

```python
skills.sort()
```

or:

```python
sorted_skills = sorted(skills)
```

## Day 5 key takeaways

```text
Lists are ordered and mutable.
Indexes start at 0.
Negative indexes count from the end.
Slicing includes start and excludes end.
Use in to check membership.
Use append(), insert(), and extend() to add items.
Use remove(), pop(), del, and clear() to remove items.
Use copy() for independent list copies.
Use + to create a new combined list.
Use count() to count occurrences.
Use index() to find the first matching position.
Use reverse() to reverse the original list.
Use sort() to sort the original list.
Use sorted() to create a sorted copy.
Do not assign the result of sort() to a variable.
```

---

# Day 6 - Tuples

## Main goal

Day 6 focused on ordered but immutable collections.

Topics covered:

```text
creating tuples
empty tuples
one-item tuple comma rule
len()
type()
indexing
negative indexing
slicing
in checks
immutability
tuple to list conversion
list to tuple conversion
joining tuples
tuple repetition
deleting tuple variables
count()
index()
tuple vs list use cases
```

## Tuple basics

A tuple stores multiple values like a list, but it is immutable.

```python
languages = ("JavaScript", "TypeScript", "Python", "Java")
```

Important difference:

```text
list  -> mutable    -> can be changed directly
tuple -> immutable  -> cannot be changed directly
```

List:

```python
skills = ["JavaScript", "React", "Python"]
skills[0] = "HTML"
```

Tuple:

```python
skills = ("JavaScript", "React", "Python")
# skills[0] = "HTML"  # This would fail
```

## One-item tuple rule

This is not a tuple:

```python
favorite_language = ("Python")
```

Correct one-item tuple:

```python
favorite_language = ("Python",)
```

The comma is what makes it a tuple.

## Indexing and slicing

Tuples are ordered, so they support indexing and slicing.

```python
languages = ("JavaScript", "TypeScript", "Python", "Java")

print(languages[0])
print(languages[-1])
print(languages[:2])
print(languages[-2:])
```

Slicing a tuple returns a tuple.

## Membership checks

Use `in`:

```python
has_python = "Python" in languages
```

## Immutability

Tuples cannot be changed directly.

Not allowed:

```python
languages[0] = "HTML"
```

Allowed:

```python
coordinates = (10, 20)
coordinates = (30, 40)
```

That reassigns the variable to a new tuple. It does not modify the old tuple.

## Tuple to list conversion

When tuple-like data needs to change temporarily:

```text
tuple -> list -> modify list -> tuple
```

Example:

```python
languages = ("JavaScript", "TypeScript", "Python")

languages_list = list(languages)
languages_list.append("Go")

updated_languages = tuple(languages_list)
```

If you constantly need to add, remove, or edit items, use a list instead.

## Joining and repeating tuples

Use `+` to join tuples.

```python
frontend_skills = ("HTML", "CSS", "JavaScript")
backend_skills = ("Node.js", "MongoDB", "PostgreSQL")

full_stack_skills = frontend_skills + backend_skills
```

Use `*` to repeat tuples.

```python
numbers = (1, 2)
repeated_numbers = numbers * 3
```

## Deleting tuples

You cannot delete one item from a tuple directly.

```python
# del languages[0]  # not allowed
```

But you can delete the whole variable.

```python
temporary_tuple = ("draft", "test", "sample")
del temporary_tuple
```

## count() and index()

```python
scores = (90, 85, 90, 70, 90)

print(scores.count(90))
print(scores.index(70))
```

Warning:

```text
index() fails if the value does not exist.
```

## Tuple vs list

Use tuples for fixed grouped data.

```python
coordinates = (10, 20)
rgb_color = (255, 255, 255)
date_parts = (2026, 5, 18)
```

Use lists for data that should change.

```python
skills = ["JavaScript", "React", "Node.js"]
tasks = ["study", "practice", "review"]
```

## Day 6 key takeaways

```text
Tuples are ordered.
Tuples are immutable.
Use () to create tuples.
A one-item tuple needs a trailing comma.
Use indexes and slices like lists and strings.
Use in to check membership.
You cannot directly change tuple items.
You can reassign a tuple variable to a new tuple.
Use list() when you need a temporary mutable version.
Use tuple() to convert a list back to a tuple.
Use + to join tuples.
Use * to repeat tuples.
Use del to delete the whole tuple variable.
Use count() to count values.
Use index() to find the first matching index.
Use tuples for fixed grouped data.
Use lists for data that should change.
```

---

# Day 7 - Sets

## Main goal

Day 7 focused on unique, unordered collections and comparing groups of data.

Topics covered:

```text
creating sets
empty set with set()
duplicates removed automatically
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
list/tuple to set conversion
union()
intersection()
difference()
symmetric_difference()
issubset()
issuperset()
isdisjoint()
set use cases
```

## Set basics

A set stores unique values.

```python
languages = {"JavaScript", "Python", "Java", "Python", "TypeScript"}
```

Even though `"Python"` appears twice, the set keeps it once.

Important rules:

```text
Sets remove duplicates automatically.
Sets do not have dependable order.
Sets do not support indexing.
```

This does not work:

```python
# languages[0]
```

## Empty set

Correct empty set:

```python
empty_tools = set()
```

This is not an empty set:

```python
empty_data = {}
```

`{}` creates an empty dictionary.

Rule:

```text
set() -> empty set
{}    -> empty dictionary
```

## Set order

Do not trust set order.

```text
The printed order may look stable sometimes.
The printed order may change sometimes.
Never depend on set order.
```

Sets are for uniqueness and membership checks, not position-based logic.

## Membership checks

Use `in`:

```python
has_python = "Python" in languages
```

Use `not in`:

```python
missing_go = "Go" not in languages
```

## Adding and updating sets

Use `add()` for one item.

```python
languages.add("Go")
```

Use `update()` for multiple items.

```python
languages.update(["Rust", "JavaScript", "C#"])
```

Comparison with lists:

```text
list.append() -> adds one item
list.extend() -> adds multiple items

set.add()     -> adds one item
set.update()  -> adds multiple items
```

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

Important:

```text
Use remove() when the item must exist.
Use discard() when the item may not exist.
Use pop() carefully because sets have no dependable last item.
Use clear() when you want the empty set to remain.
Use del when you want the variable gone.
```

## Converting lists/tuples to sets

Use `set()` to remove duplicates.

```python
skill_list = ["React", "Node.js", "React", "MongoDB", "Node.js", "Docker"]
unique_skills = set(skill_list)
```

Important:

```text
set(list_or_tuple) removes duplicates.
After converting to a set, order should not be trusted.
```

## Core set operations

Example sets:

```python
frontend_skills = {"HTML", "CSS", "JavaScript", "React"}
backend_skills = {"JavaScript", "Node.js", "Express", "MongoDB"}
```

`union()` returns everything from both sets.

```python
all_skills = frontend_skills.union(backend_skills)
```

`intersection()` returns only shared items.

```python
common_skills = frontend_skills.intersection(backend_skills)
```

`difference()` returns items in the first set but not the second.

```python
frontend_only = frontend_skills.difference(backend_skills)
backend_only = backend_skills.difference(frontend_skills)
```

Direction matters.

```text
A.difference(B) is not the same as B.difference(A).
```

`symmetric_difference()` returns items that are not shared.

```python
not_shared = frontend_skills.symmetric_difference(backend_skills)
```

Key distinction:

```text
union() includes shared items.
symmetric_difference() excludes shared items.
```

## Set relationship checks

`issubset()` checks if everything in one set exists inside another.

```python
required_skills = {"JavaScript", "React"}
candidate_skills = {"JavaScript", "React", "Node.js", "MongoDB"}

required_is_subset = required_skills.issubset(candidate_skills)
```

`issuperset()` checks whether one set contains everything from another.

```python
candidate_is_superset = candidate_skills.issuperset(required_skills)
```

`isdisjoint()` checks whether two sets have zero overlap.

```python
frontend_skills = {"HTML", "CSS", "React"}
database_skills = {"MongoDB", "PostgreSQL"}

frontend_database_disjoint = frontend_skills.isdisjoint(database_skills)
```

## Set vs list vs tuple

| Type | Use when | Allows duplicates? | Order/indexing? | Mutable? |
|---|---|---:|---:|---:|
| `list` | Items can change and order matters | Yes | Yes | Yes |
| `tuple` | Fixed grouped data | Yes | Yes | No |
| `set` | Unique values or comparisons | No | No dependable order | Yes |

## Day 7 key takeaways

```text
Sets store unique values.
Sets remove duplicates automatically.
Sets do not have dependable order.
Sets do not support indexing.
Use set() to create an empty set.
{} creates an empty dictionary.
Use len() to count unique set items.
Use in and not in for membership checks.
Use add() to add one item.
Use update() to add multiple items.
Use remove() when the item must exist.
Use discard() when the item may not exist.
Use pop() carefully because the removed item is unpredictable.
Use clear() to empty a set.
Use del to delete the set variable.
Use set(list_or_tuple) to remove duplicates.
union() returns everything from both sets.
intersection() returns only shared items.
difference() returns items only in the first set.
symmetric_difference() returns items not shared.
issubset(), issuperset(), and isdisjoint() return booleans.
Use sets for uniqueness, membership checks, and group comparisons.
```

---

# Week 1 Big Picture

## How the concepts connect

Week 1 moved from simple values to collections.

```text
Day 1-2:
single values, variables, types, input, output

Day 3:
operators and boolean logic

Day 4:
strings as text sequences

Day 5:
lists as ordered, changeable collections

Day 6:
tuples as ordered, fixed collections

Day 7:
sets as unique, unordered collections for membership and comparison
```

The main progression:

```text
value -> variable -> type -> operation -> collection -> choosing the right collection
```

## Collection decision guide

| Need | Use |
|---|---|
| Ordered items that can change | `list` |
| Fixed grouped values | `tuple` |
| Unique values or group comparison | `set` |
| Labeled key-value data | `dict` |

Dictionaries started on Day 8, so they belong to Week 2, but this decision guide is useful from now on.

## Recurring mistakes to watch

| Pattern | Watch for |
|---|---|
| String `"30"` vs number `30` | Use numbers for math |
| `input()` returns string | Convert with `int()` or `float()` before math |
| Misleading variable names | Store calculated values in correctly named variables |
| JavaScript habits | Avoid `true`, `false`, `===`, `++`, camelCase, and semicolons |
| Mixed logic readability | Use parentheses with `and` / `or` |
| Unnecessary escaping | Choose cleaner quote style |
| `find()` misuse | Use `find(...) != -1` for boolean checks |
| `append()` vs `extend()` | One item vs multiple items |
| `pop()` vs `del` | `pop()` returns removed item; `del` does not |
| `sort()` vs `sorted()` | Mutate original vs return sorted copy |
| One-item tuple trap | Use `("Python",)` |
| Empty set trap | Use `set()`, not `{}` |
| Set order trap | Never depend on printed set order |
| Set indexing trap | Sets do not support indexing |

## Week 1 final status

```text
Week 1 - Cleared
Ready to continue Week 2 from Day 8 / Day 9 onward.
```
