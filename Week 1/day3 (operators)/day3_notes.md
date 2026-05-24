# Day 3 Notes - Operators

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## What Day 3 covered

Day 3 focused on operators. The goal was to understand how Python assigns values, compares values, combines conditions, and decides the order of operations.

Topics covered:

```text
booleans
assignment operators
comparison operators
logical operators
operator precedence
final mixed exercise
```

## 1. Booleans

A boolean has only two possible values:

```python
True
False
```

Python booleans are capitalized.

Correct:

```python
is_learning_python = True
has_finished_day_3 = False
```

Incorrect:

```python
is_learning_python = true
has_finished_day_3 = false
```

Boolean variables should usually answer yes/no questions.

```python
is_software_engineer = True
has_experience = True
can_relocate = True
is_blocked = False
```

JavaScript comparison:

```javascript
const isEngineer = true;
```

Python:

```python
is_engineer = True
```

## 2. Assignment operators

Assignment stores a value in a variable.

```python
score = 50
```

Important distinction:

```text
= assigns a value
== compares two values
```

Example:

```python
age = 30      # assignment
age == 30     # comparison
```

Shortcut assignment operators:

```python
score += 10
score -= 5
score *= 2
score /= 10
```

These update the existing variable.

```python
score = 50
score += 10
print(score)  # 60
```

Python does not use JavaScript-style increment:

```python
score++
```

Use:

```python
score += 1
```

## 3. Comparison operators

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

print(age == 30)  # True
print(age != 25)  # True
print(age > 18)   # True
print(age <= 29)  # False
```

Python does not use JavaScript strict equality:

```python
age === 30
```

Use:

```python
age == 30
```

## 4. Logical operators

Logical operators combine boolean conditions.

Python uses:

```python
and
or
not
```

`and` means both sides must be true.

```python
age = 30
has_experience = True

print(age >= 18 and has_experience)
```

`or` means at least one side must be true.

```python
has_degree = False
has_experience = True

print(has_degree or has_experience)
```

`not` flips the boolean.

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

## 5. Cleaner boolean style

Avoid unnecessary comparisons to `True` or `False`.

Works but noisy:

```python
print(has_experience == True)
```

Cleaner:

```python
print(has_experience)
```

Works but noisy:

```python
print(is_blocked == False)
```

Cleaner:

```python
print(not is_blocked)
```

Rule:

```text
If a variable already stores True/False, use it directly.
```

## 6. Operator precedence

Operator precedence is the order Python uses when evaluating an expression.

Example:

```python
result = 10 + 5 * 2
print(result)  # 20
```

Multiplication happens before addition.

Use parentheses when you want a specific order:

```python
result = (10 + 5) * 2
print(result)  # 30
```

Basic order to remember:

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

For mixed logic, do not be clever. Use parentheses.

```python
(age >= 18 and score > 70) or is_holiday
```

## What was practiced

Day 3 practice included:

```text
creating boolean variables
printing booleans
checking boolean types
using assignment shortcuts
using comparison operators
combining conditions with and/or/not
checking scores against passing scores
using parentheses in mixed logic
understanding operation order
```

The final mixed exercise combined booleans, score updates, comparisons, logical operators, `not`, and operator precedence.

## Mistakes and corrections

| Issue / Risk | Correction |
|---|---|
| JavaScript boolean habit | Python uses `True` and `False` |
| Confusing `=` and `==` | `=` assigns, `==` compares |
| JavaScript increment habit | Use `+= 1`, not `++` |
| Unnecessary `== True` | Use the boolean directly |
| Mixed `and` / `or` readability | Use parentheses |
| Minor spacing issue like `/5` | Prefer `/ 5` |

Spacing correction:

```python
final_result = (20 + 10) / 5
```

## Day 3 key takeaways

```text
Boolean values are True and False.
Use = for assignment.
Use == for comparison.
Python does not use ===.
Python does not use ++.
Use += when incrementing.
Comparison operators return booleans.
and requires both conditions to be True.
or requires at least one condition to be True.
not flips a boolean.
Avoid unnecessary == True.
Use parentheses to make mixed logic obvious.
Normal division / returns a float.
```

## Ready for next day

```text
Day 4 - Strings
```
