# Day 14 Notes - Higher Order Functions

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## What Day 14 covered

Day 14 focused on higher order functions - functions that work with other functions.

```text
higher order functions
callbacks
lambda
map()
filter()
reduce()
sorted(..., key=...)
.sort(key=...)
lambda vs def
```

Core idea:

```text
Functions can be passed around like values.
That idea powers callbacks, lambda, map/filter/reduce, and sorting key functions.
```

---

# 1. Higher order functions and callbacks

A higher order function can accept another function as an argument or return another function.

```python
def apply_operation(operation, value):
    return operation(value)
```

A callback is a function passed into another function so it can be called later.

Most important rule:

```text
function_name   -> pass/store the function
function_name() -> call the function immediately
```

Example mental model:

```text
operation = double_number
operation(10) becomes double_number(10)
```

---

# 2. Lambda

A `lambda` is a tiny anonymous one-expression function.

```python
lambda parameter: expression
```

Examples:

```python
lambda number: number * 2
lambda first, second: first + second
lambda score: "Pass" if score >= 70 else "Fail"
```

Rules:

```text
Lambda automatically returns the expression result.
Do not write return inside lambda.
Use lambda for tiny temporary logic.
Use def for named, reusable, multi-step, or growing logic.
```

Blunt rule:

```text
Tiny one-expression callback -> lambda is fine.
Reusable or growing logic -> def is cleaner.
```

---

# 3. map(), filter(), and comprehension comparison

## map()

`map()` transforms every item in an iterable.

```python
doubled_numbers = list(map(lambda number: number * 2, numbers))
```

## filter()

`filter()` keeps only items that pass a condition.

```python
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
```

## Lazy behavior

```text
map() and filter() return lazy iterable objects.
Use list(), tuple(), or set() when you need a real collection.
```

## Main difference

```text
map()    -> transforms every item
filter() -> keeps/removes items
```

## Comprehension comparison

```python
doubled_numbers = [number * 2 for number in numbers]
even_numbers = [number for number in numbers if number % 2 == 0]
even_squares = [number ** 2 for number in numbers if number % 2 == 0]
```

Practical Python rule:

```text
For simple transformations and filtering, comprehensions are usually cleaner than map()/filter() with lambda.
map() is still fine when a named function already exists.
```

---

# 4. reduce()

`reduce()` reduces many values into one final value.

```python
from functools import reduce

total = reduce(lambda accumulator, number: accumulator + number, numbers)
```

Patterns:

```python
reduce(function, iterable)
reduce(function, iterable, initial_value)
```

Mental model:

```text
accumulator -> running result
current item -> next value being processed
```

Important difference:

```text
map() / filter() -> lazy iterable object
reduce()         -> final value directly
```

Rules:

```text
Do not wrap reduce() with list().
Use from functools import reduce.
Use an initial value when a clear starting accumulator is needed.
Prefer sum(), max(), min(), join(), or a normal loop when clearer.
```

---

# 5. Sorting with key functions

Python sorting can accept a `key` function.

```python
names_by_length = sorted(names, key=len)
students_by_score = sorted(students, key=lambda student: student["score"])
students_by_score_desc = sorted(students, key=lambda student: student["score"], reverse=True)
```

Rule:

```text
key=function_name
not key=function_name()
```

Named key function:

```python
def get_student_name(student):
    return student["name"]

students_by_name = sorted(students, key=get_student_name)
```

Multiple sort values:

```python
students_by_score_then_name = sorted(
    students,
    key=lambda student: (student["score"], student["name"])
)
```

Python vs JavaScript:

```text
JavaScript sort callback -> compares two items
Python key function      -> extracts one sorting value from each item
```

---

# 6. sorted() vs .sort()

```text
sorted(iterable) -> creates a new sorted list
list.sort()      -> mutates the original list and returns None
```

Use `sorted()` when you want a new list.

Use `.sort()` only when you intentionally want to modify the original list.

---

# What was practiced

```text
storing functions in variables
passing functions into other functions
callback-style execution
lambda basics and inline lambdas
lambda vs def judgment
map() transformations
filter() selection
lazy map/filter objects
reduce() with and without initial values
sum() as a cleaner alternative
sorted() with key=len
sorted() with lambda and named key functions
reverse=True
sorting lists of dictionaries
```

---

# Mistakes, prompt mismatches, and corrections

| Issue / Question | Correction / Clarification |
|---|---|
| `import reduce from functools` | Python uses `from functools import reduce`. |
| `map()` / `filter()` vs generators | They create lazy iterable objects; consume with `list()`, `tuple()`, etc. |
| Generator expression used where list comprehension was requested | Use square brackets: `[x for x in items]`. |
| Used `values` where prompt asked for `names` | Code worked, but prompt-specific names matter. |
| `toal_score` typo | Fixed to `total_score`. |
| Extra joined topic-label output | Removed to avoid bloated final output. |
| `lamda` typo | Fixed to `lambda`. |
| Float display like `35.489999999999995` | Normal float behavior; use `{value:.2f}` for display. |

---

# Final mixed exercise summary

Scenario:

```text
Python study task analyzer
```

Covered:

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

Final result:

```text
Day 14 final mixed exercise cleared.
```

---

# Day 14 key takeaways

```text
Functions can be treated as values.
Callbacks are functions passed into another function to be called later.
Pass function_name when passing a function.
Use function_name() only when calling immediately.
Lambda is for tiny one-expression temporary logic.
Use def for named, reusable, multi-step, or growing logic.
map() transforms every item.
filter() keeps only matching items.
map() and filter() are lazy.
reduce() reduces many values into one final value.
reduce() is not lazy like map/filter.
Import reduce with from functools import reduce.
Prefer sum(), max(), min(), join(), or a loop when clearer.
sorted() creates a new sorted list.
.sort() mutates the original list.
key= accepts a function used to calculate the sorting value.
Use key=function_name, not key=function_name().
Python key functions extract one sorting value; JavaScript sort callbacks compare two items.
```
