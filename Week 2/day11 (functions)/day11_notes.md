# Day 11 Notes - Functions

Status: Cleared

Source backbone: https://github.com/Asabeneh/30-Days-Of-Python

## What Day 11 covered

Day 11 focused on Python functions: reusable blocks of code, calling functions, returning reusable values, passing inputs with parameters, using default/keyword arguments, accepting flexible inputs with `*args`, and passing one function into another.

Topics covered:

```text
function basics
def and function calls
print() vs return
parameters and arguments
positional vs keyword arguments
default parameters
*args
required parameter + *args + default option
function as a parameter / callback basics
final mixed exercise
```

---

# 1. Function basics

A function is a reusable block of code.

```python
def welcome_message():
    print("Welcome to Day 11 - Functions")

welcome_message()
```

Mental model:

```text
Define function -> Python learns what the function should do
Call function   -> Python actually runs it
```

A function definition needs `def`, a function name, parentheses, a colon, and an indented body.

Python vs JavaScript:

```text
JavaScript -> function greetUser() { console.log("Hello") }
Python     -> def greet_user(): print("Hello")
```

---

# 2. `print()` vs `return`

Use `print()` when the function only needs to display output.

Use `return` when the function should produce a reusable value.

```python
def get_day_status():
    return "Day 11 is in progress"

day_status = get_day_status()
```

Main rule:

```text
print() -> show output to the user
return  -> give a reusable value back to the program
```

Important reminders:

```text
A function returns None by default if there is no return.
Code after return does not run.
return can send back any data type: string, number, list, dict, bool, etc.
```

---

# 3. Parameters and arguments

A **parameter** is the placeholder in the function definition.

An **argument** is the actual value passed during the function call.

```python
def greet_student(name):
    print(f"Hello, {name}")

greet_student("Sudharsan Srinivasan")
```

Mental model:

```text
parameter -> placeholder in the function definition
argument  -> real value passed during the function call
```

Multiple parameters are allowed, and with positional arguments, order matters.

```python
def add_scores(score1, score2):
    return score1 + score2
```

Arguments can be strings, numbers, booleans, lists, dictionaries, tuples, sets, or functions.

---

# 4. Keyword arguments and default parameters

```text
positional argument -> matched by order
keyword argument    -> matched by parameter name
```

```python
def show_student_profile(name, role):
    print(f"Name: {name}")
    print(f"Role: {role}")

show_student_profile(role="Python Learner", name="Ashwin")
```

Use keyword arguments when clarity matters or when order is easy to mix up.

Default parameters provide fallback values.

```python
def greet_student(name="Python Learner"):
    print(f"Hello, {name}")
```

Parameter order rule:

```text
Required parameters first.
Default parameters after.
```

```python
def calculate_final_score(base_score, bonus=10):
    return base_score + bonus
```

Python does not allow a required parameter after a default parameter.

---

# 5. Arbitrary positional arguments with `*args`

`*args` lets a function accept any number of positional arguments.

```python
def show_topics(*topics):
    for topic in topics:
        print(f"Topic: {topic}")
```

Inside the function, `topics` becomes a tuple.

```text
*topics collects many positional arguments into one tuple.
```

Important clarification:

```text
Function-call arguments may visually look tuple-like because they are comma-separated.
But they are still separate arguments at call time.
The *args parameter bundles those separate arguments into a tuple inside the function.
```

Difference:

```python
show_topics("Functions", "Parameters", "Return values")
# topics = ("Functions", "Parameters", "Return values")

show_topics(("Functions", "Parameters", "Return values"))
# topics = (("Functions", "Parameters", "Return values"),)
```

Common calculation pattern:

```python
def add_scores(*scores):
    total = 0
    for score in scores:
        total += score
    return total
```

---

# 6. Required parameter + `*args` + default parameter

Clean beginner pattern:

```python
def show_learning_plan(student_name, *topics, status="In progress"):
    print(f"Student: {student_name}")
    print(f"Status: {status}")
    for topic in topics:
        print(f"Planned topic: {topic}")
```

Mapping:

```text
student_name -> first required value
topics       -> extra positional values collected as a tuple
status       -> keyword-style default option
```

Rule to remember:

```text
def function_name(required_param, *args, default_param=value):
```

Anything after `*args` should usually be passed by keyword.

---

# 7. Function as a parameter

In Python, functions can be passed into other functions.

```python
def say_welcome():
    print("Welcome to function callbacks")

def run_action(action):
    action()

run_action(say_welcome)
```

Important distinction:

```text
say_welcome   -> pass the function itself
say_welcome() -> call the function immediately
```

A passed function can return a value or accept arguments.

```python
def double_number(number):
    return number * 2

def apply_operation(operation, value):
    return operation(value)

result = apply_operation(double_number, 15)
```

Beginner rule:

```text
Pass function_name without ().
Call it later inside another function.
```

Do not overuse this yet. Day 14 covers higher order functions more deeply.

---

# What was practiced

```text
defining and calling functions
functions without parameters
print() inside functions
return values
returning strings, numbers, lists, dictionaries, and booleans
parameters and arguments
positional arguments
keyword arguments
default parameters
*args and looping through *args
checking empty *args with if not topics
required parameters + *args + keyword-only defaults
passing function names into other functions
calling passed functions inside another function
```

---

# Mistakes, prompt mismatches, and corrections

| Issue | Correction / Clarification |
|---|---|
| Extra variable inside `print_separator()` | Valid, but `print("-" * 30)` is cleaner for a tiny one-line operation. |
| `Hello <name>` instead of `Hello, <name>` | Prompt mismatch, not a logic bug. Exact output matters. |
| `"Python learner"` instead of `"Python Learner"` | Prompt mismatch due to casing. |
| `return total/count` | Works, but `return total / count` is cleaner style. |
| `
` inside f-strings for multi-line output | Valid, but separate `print()` calls are easier while learning. |
| Visual similarity between function-call arguments and tuples | Both can look comma-separated, but context matters. `*args` bundles separate arguments into a tuple inside the function. |
| `show_student_topics = (...)` | Real bug. It assigned a tuple to the function name instead of calling the function. Correct: `show_student_topics(...)`. |
| `*args` where prompt asked for `*topics` | Works logically, but prompt-specific parameter names should be followed when requested. |
| `print()` after `return` in demo function | Good for demonstrating unreachable code, but dead code should not stay in real code. |

---

# Final mixed exercise status

Final scenario:

```text
Python course progress report
```

It covered:

```text
function definition and calling
returning a student name
using a returned value as an argument
parameters
*args with a loop
keyword/default arguments
returning and looping through a list
boolean-returning function
passing a function into another function
```

Final status:

```text
Cleared
```

---

# Day 11 key takeaways

```text
Functions group reusable logic.
Use def to define a function.
Calling a function runs it.
Use print() to display output.
Use return to produce a reusable value.
A function returns None by default if there is no return.
Code after return does not run.
A parameter is a placeholder in the function definition.
An argument is the actual value passed during the function call.
Positional arguments are matched by order.
Keyword arguments are matched by parameter name.
Use default parameters for fallback values.
Required parameters must come before default parameters.
Use *args when a function should accept any number of positional arguments.
*args collects values into a tuple inside the function.
A clean beginner pattern is required_param, *args, default_param=value.
Anything after *args should usually be passed by keyword.
Pass function_name when passing the function itself.
Use function_name() only when you want to call it immediately.
```

---

# Ready for next day

```text
Day 12 - Modules
```
