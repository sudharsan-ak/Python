# Day 3 Notes - Operators

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 3 focused on operators: assigning values, comparing values, combining conditions, and understanding evaluation order.

## Core topics

```text
booleans
assignment operators
comparison operators
logical operators
clean boolean style
operator precedence
```

---

## Booleans

Python booleans are capitalized.

```python
is_learning_python = True
has_finished_day_3 = False
```

Do not use JavaScript lowercase booleans in Python.

```python
# Wrong in Python
true
false
```

Good boolean names answer yes/no questions.

```python
is_software_engineer = True
has_experience = True
can_relocate = True
is_blocked = False
```

---

## Assignment vs comparison

```python
age = 30      # assignment
age == 30     # comparison
```

Rule:

```text
=  assigns
== compares
```

Python does not use JavaScript `===`.

---

## Assignment shortcuts

Shortcut operators update an existing value.

```python
score = 50

score += 10
score -= 5
score *= 2
score /= 10
```

Python does not use `score++`.

Use:

```python
score += 1
```

---

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
print(age > 18)
print(age <= 29)
```

---

## Logical operators

Python uses:

```python
and
or
not
```

Examples:

```python
can_apply = age >= 18 and has_experience
has_background = has_degree or has_experience
is_available = not is_blocked
```

JavaScript comparison:

```text
JavaScript -> &&, ||, !
Python     -> and, or, not
```

---

## Cleaner boolean style

Noisy:

```python
has_experience == True
is_blocked == False
```

Cleaner:

```python
has_experience
not is_blocked
```

Rule:

```text
If a variable already stores True/False, use it directly.
```

---

## Operator precedence

Python evaluates some operations before others.

```python
result = 10 + 5 * 2      # 20
result = (10 + 5) * 2    # 30
```

Basic order:

```text
1. ()
2. **
3. * / // %
4. + -
5. comparisons
6. not
7. and
8. or
```

When mixing `and` and `or`, use parentheses.

```python
(age >= 18 and score > 70) or is_holiday
```

---

## What was practiced

```text
creating boolean variables
checking boolean types
using assignment shortcuts
using comparison operators
combining conditions with and/or/not
checking scores against passing scores
using parentheses in mixed logic
understanding operation order
```

---

## Mistakes and corrections

| Issue | Correction |
|---|---|
| JavaScript boolean habit | Use `True` and `False` |
| Confused `=` and `==` | `=` assigns, `==` compares |
| JavaScript increment habit | Use `+= 1`, not `++` |
| Unnecessary `== True` | Use the boolean directly |
| Mixed `and` / `or` readability | Use parentheses |
| Minor operator spacing issue | Prefer clean spacing like `/ 5` |

---

## Key takeaways

```text
Boolean values are True and False.
Use = for assignment.
Use == for comparison.
Python does not use ===.
Python does not use ++.
Use += when incrementing.
Comparison operators return booleans.
and requires both conditions to be true.
or requires at least one condition to be true.
not flips a boolean.
Avoid unnecessary == True and == False.
Use parentheses to make mixed logic obvious.
Normal division / returns a float.
```
