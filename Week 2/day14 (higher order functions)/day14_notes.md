# Day 14 Notes - Higher Order Functions

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## What Day 14 covered

Day 14 focused on higher order functions: functions that work with other functions. The goal was to understand how Python treats functions as values, how callbacks work, how lambda fits into small temporary logic, and how `map()`, `filter()`, `reduce()`, and sorting `key` functions use the same foundation.

Topics covered:

```text
higher order functions
functions as values
passing functions as arguments
callbacks
lambda in detail
map()
filter()
reduce()
sorted(..., key=...)
list.sort(key=...)
lambda vs def
final mixed exercise
```

## 1. Higher order functions and callbacks

A higher order function is a function that accepts another function as an argument or returns another function.

For this day, the focus was on passing functions into other functions.

```python
def double_number(number):
    return number * 2


def apply_operation(operation, value):
    result = operation(value)
    return result


result = apply_operation(double_number, 10)
```

Mental model:

```text
operation = double_number
value = 10
operation(value) becomes double_number(10)
```

A callback is a function passed into another function so it can be called later.

```python
def show_start_message():
    print("Starting Python practice")


def run_practice_session(start_callback):
    start_callback()


run_practice_session(show_start_message)
```

Important rule:

```text
function_name   -> pass or store the function
function_name() -> call the function immediately
```

## 2. Lambda in detail

A lambda is a small anonymous one-expression function.

Pattern:

```python
lambda parameter: expression
```

Examples:

```python
double_number = lambda number: number * 2
add_numbers = lambda first_number, second_number: first_number + second_number
check_pass_status = lambda score: "Pass" if score >= 70 else "Fail"
```

Lambda automatically returns the expression result. Do not write `return` inside lambda.

Good lambda usage:

```python
increased_value = apply_operation(lambda number: number + 10, 40)
```

Use lambda when the logic is tiny, one-expression, temporary, and often passed directly into another function.

Use `def` when the logic needs a clear name, has multiple steps, may be reused, may grow later, or needs easier debugging.

Blunt rule:

```text
Tiny temporary one-expression callback -> lambda is fine.
Named reusable logic or logic that may grow -> def is cleaner.
```

## 3. `map()`

`map()` transforms every item in an iterable.

Pattern:

```python
map(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4]
doubled_numbers = list(map(lambda number: number * 2, numbers))
```

`map()` returns a lazy map object. Use `list(...)`, `tuple(...)`, or another collection constructor to consume it when needed.

Equivalent list comprehension:

```python
doubled_numbers = [number * 2 for number in numbers]
```

Practical rule:

```text
map() transforms values.
If map() uses a simple lambda, list comprehension is often cleaner.
If a named function already exists, map() can be fine.
```

## 4. `filter()`

`filter()` keeps only items that pass a condition.

Pattern:

```python
filter(function, iterable)
```

The function should return `True` or `False`.

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
```

Equivalent list comprehension:

```python
even_numbers = [number for number in numbers if number % 2 == 0]
```

Practical rule:

```text
filter() keeps/removes values.
It does not transform values by itself.
```

## 5. `map()` vs `filter()` vs comprehension

```text
map()    -> many items in, many transformed items out
filter() -> many items in, fewer selected items out
```

Example with both:

```python
even_squares = list(
    map(lambda number: number ** 2, filter(lambda number: number % 2 == 0, numbers))
)
```

Cleaner comprehension:

```python
even_squares = [number ** 2 for number in numbers if number % 2 == 0]
```

Day 14 reinforced the Day 13 rule: comprehensions are often cleaner for simple Python transformations and filtering.

## 6. `reduce()`

`reduce()` reduces many values into one final value.

It must be imported:

```python
from functools import reduce
```

Example:

```python
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda accumulator, number: accumulator + number, numbers)
```

Mental model:

```text
accumulator -> running result
number      -> current item
```

With an initial value:

```python
total_with_bonus = reduce(lambda accumulator, number: accumulator + number, numbers, 100)
```

Pattern:

```python
reduce(function, iterable, initial_value)
```

Important difference:

```text
map() / filter() -> lazy iterable object
reduce()         -> final value directly
```

Do not wrap `reduce()` with `list(...)`.

Python usually prefers clearer built-ins for common reductions:

```python
total = sum(numbers)
highest = max(numbers)
lowest = min(numbers)
sentence = " ".join(words)
```

Use `reduce()` only when a running accumulator is natural and no clearer built-in exists.

## 7. Sorting with key functions

Python sorting can accept a `key` function.

```python
names = ["Sudharsan", "Ashwin", "Python", "AI"]
names_by_length = sorted(names, key=len)
```

Important:

```text
key=len      -> pass the function
key=len()    -> wrong here
```

Sorting dictionaries by a field:

```python
students_by_score = sorted(students, key=lambda student: student["score"])
```

Descending sort:

```python
students_by_score_desc = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)
```

Named key function:

```python
def get_student_name(student):
    return student["name"]


students_by_name = sorted(students, key=get_student_name)
```

Tuple key for multiple sort values:

```python
students_by_score_then_name = sorted(
    students,
    key=lambda student: (student["score"], student["name"])
)
```

Python vs JavaScript sorting:

```text
JavaScript sort callback -> compares two items
Python key function      -> extracts one sorting value from each item
```

## 8. `sorted()` vs `.sort()`

`sorted()` creates a new sorted list.

```python
sorted_numbers = sorted(numbers)
```

`.sort()` mutates the original list.

```python
numbers.sort()
```

Rule:

```text
Use sorted() when you want a new list.
Use .sort() when you intentionally want to modify the original list.
```

## What was practiced

Day 14 practice included:

```text
storing functions in variables
passing functions into other functions
callback-style function execution
lambda with one parameter
lambda with multiple parameters
lambda with conditional expressions
inline lambda callbacks
lambda vs def judgment
map() transformations
filter() selection
lazy map/filter objects consumed with list()
reduce() with lambdas and named functions
reduce() with initial values
sum() comparison for simple totals
sorted() with key=len
sorted() with lambda key functions
sorted() with named key functions
reverse=True
sort keys for lists of dictionaries
```

## Mistakes, prompt mismatches, and corrections

| Issue / Question | Correction / Clarification |
|---|---|
| Asked whether `import reduce from functools` works | Python uses `from functools import reduce`, not JavaScript-style import order. |
| Asked whether `map()` / `filter()` are like generator expressions | Correct: they produce lazy iterable objects that must be consumed by `list()`, `tuple()`, etc. |
| Used generator expression inside `list()` where prompt asked for list comprehension | Correct list comprehension uses square brackets directly: `[number ** 2 for number in numbers if condition]`. |
| Used `values` where prompt asked for `names` | Code worked, but prompt-specific variable names matter in exercises. |
| Typo: `toal_score` | Fixed to `total_score`. |
| Extra final exercise output printed joined topic labels | Removed to avoid bloated output. |
| Typo: `lamda` | Fixed to `lambda`. |
| Floating price total displayed as `35.489999999999995` | Normal floating-point behavior; use formatting like `{value:.2f}` when clean display is needed. |

## Final mixed exercise status

The final mixed exercise used a Python study task analyzer scenario.

It covered:

```text
callback-style function passing
inline lambda
map()
filter()
reduce()
sum()
sorted(..., key=...)
named key function
list comprehension
lambda vs def comments
```

Final file:

```text
day14_final.py
```

Final status:

```text
Cleared
```

## Day 14 key takeaways

```text
Functions can be treated as values.
Higher order functions can accept other functions as arguments.
Callbacks are functions passed into another function to be called later.
Pass function_name when passing a function.
Use function_name() only when calling immediately.
Lambda creates a tiny one-expression anonymous function.
Do not use return inside lambda.
Use lambda for tiny temporary logic.
Use def for named, reusable, multi-step, or growing logic.
map() transforms every item.
filter() keeps only matching items.
map() and filter() return lazy iterable objects.
Use list(), tuple(), or set() to consume map/filter results.
reduce() reduces many values into one final value.
Import reduce with from functools import reduce.
reduce() reducer functions take accumulator and current item.
Use an initial value when needed.
Do not wrap reduce() with list().
Prefer sum(), max(), min(), join(), or a normal loop when clearer.
sorted() creates a new sorted list.
.sort() mutates the original list.
key= accepts a function used to calculate the sorting value.
Use key=function_name, not key=function_name().
Use key=lambda item: item["field"] for tiny dictionary-field sorting.
Use def for key logic that deserves a name or may grow.
```

## Ready for next day

```text
Day 15 - Python Type Errors
```
