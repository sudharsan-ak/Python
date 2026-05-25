# Day 11 Notes - Functions

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## What Day 11 covered

Day 11 focused on Python functions: reusable blocks of code, calling functions, passing data into functions, returning values, default/keyword arguments, `*args`, and passing one function into another.

Topics covered:

```text
function basics
def keyword
calling functions
print() vs return
parameters and arguments
positional arguments
keyword arguments
default parameters
*args
required parameter + *args + default parameter
function as a parameter / callback basics
final mixed exercise
```

## 1. Function basics

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

A function definition needs:

```text
def keyword
function name
parentheses
colon
indented body
```

Important distinction:

```text
Writing the function defines it.
Calling the function runs it.
```

Python vs JavaScript:

```text
JavaScript -> function greetUser() { console.log("Hello") }
Python     -> def greet_user(): print("Hello")
```

Python uses `def`, indentation, `print()`, and `snake_case` names.

## 2. `print()` vs `return`

`print()` displays output in the terminal.

```python
def print_day_status():
    print("Day 11 is in progress")
```

`return` sends a value back to the program so it can be stored and reused.

```python
def get_day_status():
    return "Day 11 is in progress"

day_status = get_day_status()
print(f"Returned status: {day_status}")
```

Main rule:

```text
print() -> show output to the user
return  -> give a reusable value back to the program
```

If a function does not return anything, Python returns `None` by default.

```python
def greet_user():
    print("Hello")

message = greet_user()
print(message)  # None
```

A function stops when it reaches `return`.

```python
def check_return_behavior():
    return "This line is returned"
    print("This line will not run")
```

That print after `return` is unreachable. It is fine for a demo, but should not stay in real code.

Functions can return different data types:

```python
def get_score():
    return 95


def get_completed_topics():
    return ["Function basics", "print vs return"]


def get_learning_profile():
    return {"student": "Sudharsan Srinivasan", "current_day": 11}
```

## 3. Parameters and arguments

A parameter is a placeholder in the function definition.

```python
def greet_student(name):
    print(f"Hello, {name}")
```

An argument is the actual value passed when calling the function.

```python
greet_student("Sudharsan Srinivasan")
```

Mental model:

```text
parameter -> placeholder in the function definition
argument  -> real value passed during the function call
```

Functions can accept multiple parameters.

```python
def show_learning_goal(student_name, goal):
    print(f"Student: {student_name}")
    print(f"Goal: {goal}")
```

With positional arguments, order matters.

```text
first argument  -> first parameter
second argument -> second parameter
```

Parameters can be used with `return`.

```python
def add_scores(score1, score2):
    return score1 + score2
```

Arguments can be strings, numbers, booleans, lists, dictionaries, tuples, sets, or other Python values.

## 4. Keyword arguments

Positional arguments are matched by order.

```python
def show_student_profile(name, role):
    print(f"Name: {name}")
    print(f"Role: {role}")

show_student_profile("Sudharsan Srinivasan", "Full Stack Software Engineer")
```

Keyword arguments are matched by parameter name.

```python
show_student_profile(role="Python Learner", name="Ashwin")
```

Rule:

```text
positional argument -> matched by order
keyword argument    -> matched by parameter name
```

Use keyword arguments when clarity matters or when the order is easy to mix up.

JavaScript comparison:

```text
JavaScript commonly passes an object: showProfile({ role, name })
Python can use keyword args directly: show_student_profile(role="...", name="...")
```

## 5. Default parameters

Default parameters provide fallback values.

```python
def greet_student(name="Python Learner"):
    print(f"Hello, {name}")

greet_student("Sudharsan Srinivasan")
greet_student()
```

If a value is provided, Python uses it. If no value is provided, Python uses the default.

Multiple default parameters:

```python
def show_course_status(course="Python", status="In progress"):
    print(f"Course: {course}")
    print(f"Status: {status}")
```

Valid calls:

```python
show_course_status()
show_course_status("JavaScript", "Completed")
show_course_status(status="Almost done")
```

The last call keeps the default `course` and overrides only `status`.

Important parameter order rule:

```text
Required parameters first.
Default parameters after.
```

Correct:

```python
def calculate_final_score(base_score, bonus=10):
    return base_score + bonus
```

Wrong:

```python
def calculate_final_score(bonus=10, base_score):
    return base_score + bonus
```

Python does not allow a required parameter after a default parameter.

## 6. Arbitrary positional arguments with `*args`

`*args` lets a function accept any number of positional arguments.

```python
def show_topics(*topics):
    for topic in topics:
        print(f"Topic: {topic}")

show_topics("Functions", "Parameters", "Return values")
```

Inside the function, `topics` becomes a tuple.

```text
*topics collects many positional arguments into one tuple.
```

Important clarification from the session:

```text
Function call arguments may visually look tuple-like because they are comma-separated.
But they are still separate arguments at call time.
The *args parameter is what bundles them into a tuple inside the function.
```

Example:

```python
def show_topics(*topics):
    print(topics)

show_topics("Functions", "Parameters", "Return values")
```

Inside the function:

```text
topics = ("Functions", "Parameters", "Return values")
```

Passing one tuple as one argument is different:

```python
show_topics(("Functions", "Parameters", "Return values"))
```

Inside the function:

```text
topics = (("Functions", "Parameters", "Return values"),)
```

Common calculation pattern:

```python
def add_scores(*scores):
    total = 0
    for score in scores:
        total += score
    return total
```

## 7. Required parameters with `*args` and defaults

You can combine a required parameter, `*args`, and a default keyword-style option.

Clean beginner pattern:

```python
def show_learning_plan(student_name, *topics, status="In progress"):
    print(f"Student: {student_name}")
    print(f"Status: {status}")
    for topic in topics:
        print(f"Planned topic: {topic}")
```

Call it like this:

```python
show_learning_plan(
    "Sudharsan Srinivasan",
    "Functions",
    "Default parameters",
    "Arbitrary arguments",
    status="Practicing"
)
```

Parameter mapping:

```text
student_name -> "Sudharsan Srinivasan"
topics       -> ("Functions", "Default parameters", "Arbitrary arguments")
status       -> "Practicing"
```

Rule to remember:

```text
def function_name(required_param, *args, default_param=value):
```

Anything after `*args` should usually be passed by keyword.

## 8. Function as a parameter

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

A passed function can return a value.

```python
def get_topic_message():
    return "Functions can be passed as arguments"


def print_function_result(result_function):
    result = result_function()
    print(f"Result: {result}")
```

A passed function can also accept an argument.

```python
def double_number(number):
    return number * 2


def apply_operation(operation, value):
    return operation(value)


doubled_value = apply_operation(double_number, 15)
```

Mapping:

```text
operation = double_number
value = 15
operation(value) becomes double_number(15)
```

Do not overuse this yet. For now, remember:

```text
Pass function name without ().
Call it later inside another function.
```

## What was practiced

Day 11 practice included:

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
*args
looping through *args
checking empty *args with if not topics
required parameters + *args + keyword-only defaults
passing function names into other functions
calling passed functions inside another function
```

## Mistakes, prompt mismatches, and corrections

| Issue | Correction / Clarification |
|---|---|
| Extra variable inside `print_separator()` | Valid, but `print("-" * 30)` is cleaner for a tiny one-line operation. |
| `Hello <name>` instead of `Hello, <name>` | Prompt mismatch, not a logic bug. Exact output matters. |
| `"Python learner"` instead of `"Python Learner"` | Prompt mismatch due to casing. |
| `return total/count` | Works, but `return total / count` is cleaner style. |
| `\n` inside f-strings for multi-line output | Valid, but separate `print()` calls are often easier while learning. |
| Visual similarity between function-call arguments and tuples | Both can look comma-separated, but context matters. `*args` bundles separate arguments into a tuple inside the function. |
| `show_student_topics = (...)` | Real bug. That assigned a tuple to the function name instead of calling the function. Correct: `show_student_topics(...)`. |
| `*args` where prompt asked for `*topics` | Works logically, but prompt-specific parameter names should be followed when requested. |
| `print()` after `return` in demo function | Good for demonstrating unreachable code, but dead code should not stay in real code. |

## Final mixed exercise status

The final mixed exercise used a fresh Python course progress report scenario.

It covered:

```text
function definition and calling
returning a student name
using a returned value as an argument
parameters
*args with a loop
keyword arguments
default parameters
returning a list
looping through returned list data
boolean-returning function
passing a function into another function
```

Final output correctly included:

```text
Python Course Progress Report
Student: Sudharsan Srinivasan
Total study minutes: 135
Day: 11
Topic: Functions
Status: Final practice
Completed topic: Function basics
Completed topic: Return values
Completed topic: Parameters
Completed topic: Default arguments
Completed topic: *args
Completed topic: Callbacks
Ready for review: True
```

Final status:

```text
Cleared
```

## Day 11 key takeaways

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

## Ready for next day

```text
Day 12 - Modules
```
