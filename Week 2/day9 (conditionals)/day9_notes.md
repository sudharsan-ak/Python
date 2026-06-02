# Day 9 Notes - Conditionals

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 9 covered Python decision-making with `if`, `else`, `elif`, logical operators, nested conditionals, truthy/falsy values, and short-hand conditionals.

```text
Conditionals let Python choose which code runs based on whether a condition is True or False.
```

Covered:
```text
if / else / elif
indentation
comparison conditions
user input checks
and / or / not
nested conditionals
truthy/falsy values
strings, lists, and dictionaries in conditions
dictionary key checks
short-hand conditionals
```

## 1. Basic `if`, indentation, and comparisons

Pattern:
```python
if condition:
    code_to_run
```

Example:
```python
age = 30

if age >= 18:
    print("Adult")
```

Rules:
```text
Use : after the condition.
Indent the block under the if.
Use 4 spaces for standard Python indentation.
The condition should evaluate to True or False.
Python uses indentation instead of JavaScript-style {}.
```

Comparison operators:
```text
== equal to
!= not equal to
>  greater than
<  less than
>= greater than or equal to
<= less than or equal to
```

Important:
```text
=  assignment
== comparison
Python does not use JavaScript's ===
```

## 2. `if / else`

Use `if / else` for two possible paths.

```python
score = 72

if score >= 60:
    print("Passed")
else:
    print("Failed")
```

Rules:
```text
if has a condition.
else does not have a condition.
else means everything that did not match the if.
```

Wrong:
```python
else score < 60:
```

Correct:
```python
else:
```

## 3. User input with conditionals

`input()` always returns a string.

Convert before numeric comparisons:
```python
entered_age = int(input("Enter your age: "))

if entered_age >= 18:
    print("Adult")
else:
    print("Minor")
```

For text input, use `.strip()`:
```python
favorite_language = input("Enter language: ").strip()
```

## 4. `if / elif / else`

Use `elif` when there are multiple connected branches and only one should run.

```python
score = 92

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Needs improvement")
```

Rules:
```text
Python checks from top to bottom.
It stops after the first true branch.
For ranges, check highest/most specific conditions first.
```

Bad order:
```python
if score >= 70:
    print("Passed")
elif score >= 80:
    print("Good")
elif score >= 90:
    print("Excellent")
```

For `score = 95`, this prints `"Passed"` because the first condition already matches.

## 5. Multiple `if` statements vs `elif`

Multiple `if` statements are independent checks.

```python
if score >= 90:
    print("Excellent")

if score >= 80:
    print("Good")
```

Both can run.

Use `if / elif / else` when only one final path should run.

```text
Multiple if statements -> multiple checks can be true.
if / elif / else -> one connected decision chain.
```

## 6. Logical operators

```text
and -> all conditions must pass
or  -> at least one condition must pass
not -> opposite check
```

Examples:
```python
if age >= 18 and has_id:
    print("Entry allowed")

if has_coupon or is_member:
    print("Discount applied")

if not project_name:
    print("Project name is required")
```

JavaScript comparison:
```text
JavaScript -> &&, ||, !
Python     -> and, or, not
```

Use parentheses when mixing `and` and `or`:
```python
if (age >= 18 and has_ticket) or is_vip:
    print("Event entry allowed")
```

## 7. Common `or` trap

Wrong:
```python
if language == "Python" or "JavaScript":
    print("Good language")
```

This is wrong because `"JavaScript"` is a non-empty string, so it is truthy.

Correct:
```python
if language == "Python" or language == "JavaScript":
    print("Good language")
```

Cleaner:
```python
if language in ["Python", "JavaScript"]:
    print("Good language")
```

Use `in` when checking one value against multiple allowed values.

## 8. Nested conditionals

A nested conditional is an `if` inside another `if`.

```python
if customer_age >= 18:
    if has_membership_card:
        print("Member access granted")
    else:
        print("Membership card required")
else:
    print("Must be at least 18")
```

Use nesting when the second check only matters after the first check passes.

```text
One or two levels is okay.
Three or more levels is usually a sign to refactor.
```

Cleaner failure-first version:
```python
if age < 18:
    print("Too young")
elif not has_id:
    print("ID required")
else:
    print("Entry allowed")
```

## 9. Truthy and falsy values

Falsy values:
```text
False
None
0
""
[]
{}
()
set()
```

Truthy values:
```text
True
non-zero numbers
non-empty strings/lists/dictionaries/tuples/sets
```

Common patterns:
```python
if username:
    print("Username provided")

if not project_name:
    print("Project name is required")

if cart_items:
    print("Cart has items")

if profile:
    print("Profile exists")
```

Dictionary key check:
```python
if "role" in profile:
    print("Role exists")
```

Important distinction:
```text
if profile -> checks whether dictionary has any data.
if "role" in profile -> checks whether a specific key exists.
```

## 10. Short-hand conditionals

Use short-hand conditionals for simple two-way assignments.

Pattern:
```python
value_if_true if condition else value_if_false
```

Example:
```python
result = "Passed" if score >= 60 else "Failed"
```

JavaScript comparison:
```text
JavaScript -> condition ? valueIfTrue : valueIfFalse
Python     -> value_if_true if condition else value_if_false
```

Rule:
```text
Short-hand conditional -> simple two-way assignment.
Normal if / elif / else -> actions, multiple branches, or complex logic.
```

Do not force complex branching into one line.

## What was practiced

```text
basic if statements
if / else
if / elif / else
user input with int() and strip()
logical conditions with and / or
parentheses for mixed logic
nested conditionals
truthy/falsy checks
strings, lists, and dictionaries in conditions
dictionary key checks
short-hand conditional assignment
```

## Mistakes, prompt mismatches, and corrections

| Type | Issue | Correction |
|---|---|---|
| Style | Used 2-space indentation early | Code worked, but standard Python style is 4 spaces. |
| Testing gap | Initially tested only valid menu choices | Retested invalid input and confirmed the `else` branch. |
| Prompt mismatch | Used `"Admin"` instead of prompt's `"admin"` while staying internally consistent | Prompt mismatch, not a runtime bug. |
| Style | Nested block had uneven indentation | Use consistent 4-space indentation. |
| Testing gap | Empty project-name branch was initially skipped | Retested by pressing Enter and confirmed the empty-input branch. |
| Style | Wrote `age >=18` | Prefer `age >= 18` for readability. |

## Final mixed exercise status

Scenario:
```text
Python workshop check-in system
```

Covered:
```text
if / else
and
if / elif / else
input().strip()
truthy/falsy input checks
language matching with in
list truthiness
dictionary key checks
nested conditionals
short-hand conditional assignment
```

Tested with:
```text
workshop_track: Backend
preferred_language: Python
```

Final status:
```text
Cleared
```

## Day 9 key takeaways

```text
Use if to run code only when a condition is true.
Use else for the fallback path.
Use elif for multiple connected branches.
Indentation defines Python blocks.
Use 4 spaces.
Use == for comparison and = for assignment.
Use and when all required conditions must pass.
Use or when at least one condition can pass.
Use parentheses when mixing and / or.
Use in for clean multi-value checks.
Avoid if value == True when if value is cleaner.
Use not value to check missing or empty values.
Empty strings, lists, dictionaries, tuples, sets, 0, None, and False are falsy.
Use if list_name to check whether a list has items.
Use if dict_name to check whether a dictionary has data.
Use if "key" in dict_name to check whether a dictionary key exists.
Use nested conditionals only when the second check depends on the first.
Prefer flatter elif chains when they read cleaner.
Use short-hand conditionals only for simple two-way assignments.
Do not force complex branching into a one-liner.
```

## Ready for next day

```text
Day 10 - Loops
```
