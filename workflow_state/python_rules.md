# Python Rules - Coding Rules Learned So Far

This file contains cumulative Python coding rules learned so far. Keep this focused on coding/syntax/style rules, not project workflow.

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Global coding rules learned so far

```text
Use snake_case.
Use clear variable names.
Use f-strings for output.
Use type() when confused.
Use len() for strings/lists/tuples/sets/dictionaries.
input() always returns a string.
Convert input before doing math.
Use int() for whole numbers.
Use float() for decimal numbers.
Use str() when converting values to text.
Use = for assignment.
Use == for comparison.
Python does not use ===.
Python does not use ++.
Use += when incrementing.
Python booleans are True and False, not true and false.
Avoid unnecessary == True and == False.
Use parentheses for mixed and/or logic.
Keep operator spacing clean.
Strings need quotes inside lists/tuples/sets/dictionaries.
Numbers, booleans, and existing variables do not need quotes inside lists/tuples/sets/dictionaries.
Use in to check membership or key existence depending on the data type.
Use copy() when you need an independent list or dictionary copy.
Use sorted() when you want a sorted copy.
Use sort() when you intentionally want to mutate the original list.
Do not assign the result of sort() to a variable.
Use a trailing comma for one-item tuples.
Use list() to temporarily modify tuple data.
Use tuple() to convert a list back into a tuple.
Use tuples for fixed grouped data.
Use lists for data that should change.
Use sets for unique values, membership checks, and group comparisons.
Use dictionaries for labeled key-value data.
Use set() for an empty set.
Remember {} creates an empty dictionary, not an empty set.
Never depend on set order.
Do not index sets.
Use add() for one set item.
Use update() for multiple set items.
Use remove() when the set item must exist.
Use discard() when the set item may not exist.
Use union(), intersection(), difference(), and symmetric_difference() for set operations.
Use issubset(), issuperset(), and isdisjoint() for boolean relationship checks.
Use dictionary square bracket access when the key must exist.
Use get() when a dictionary key might be missing.
Use get("key", default) for safe fallback values.
Use in on dictionaries to check keys, not values.
Use dict["key"] = value to add or update dictionary data.
Use update() to add/update multiple dictionary key-value pairs.
Use pop() to remove a dictionary key and return its value.
Use pop("key", default) when a dictionary key may not exist.
Use del dict["key"] only when the key exists and you do not need the removed value.
Use popitem() carefully; it removes the last inserted key-value pair.
Use clear() to empty a dictionary.
Use keys(), values(), and items() to inspect dictionary data.
Convert dictionary views with list() if list behavior is needed.
Use copy() for a separate top-level dictionary copy.
Remember dictionary copy() is shallow; nested data needs more care later.
Use nested dictionaries when related data should be grouped together.
Use chained square brackets for nested dictionary access.
Use get("nested_key", {}) for safer nested dictionary access.
Use if to run code only when a condition is true.
Use else for the opposite branch.
Use elif for multiple connected branches where only one should run.
Use 4 spaces for Python indentation.
Use and when all required conditions must pass.
Use or when at least one condition can pass.
Use parentheses when mixing and / or.
Use not to check the opposite condition.
Use if value for truthy checks.
Use if not value for empty/falsy checks.
Use in for cleaner multi-value checks like language in ["Python", "JavaScript"].
Use if list_name to check whether a list has items.
Use if dict_name to check whether a dictionary has data.
Use if "key" in dict_name to check whether a dictionary key exists.
Use short-hand conditionals only for simple two-way assignments.
Prefer normal if / elif / else for direct actions, multiple branches, or complex logic.
Use for loops to repeat work over known items.
Use clear singular/plural naming in loops.
Use range() when looping through numbers/counts.
Remember the stop value in range() is excluded.
Use a negative step to count backward with range().
Use range(len(list_name)) only when indexes are needed.
Use enumerate(list_name) when both index and item are needed.
Use enumerate(list_name, start=1) for human-friendly numbering.
Prefer enumerate() over range(len(...)) when you need both index and value.
Dictionaries loop through keys by default.
Use .values() for dictionary values.
Use .items() for dictionary key-value pairs.
The object after in controls loop behavior; the variable name after for does not.
Use while loops when repeating while a condition is true.
Every while loop needs a condition that can eventually become false.
Use break to stop the whole loop.
Use continue to skip the current loop run.
Be careful with continue in while loops because it can skip the counter update.
Loop else runs only when the loop finishes without break.
Nested loops run the inner loop fully for each outer loop item.
Nested loops multiply work, so use them carefully.
Use def to define a function.
Calling a function runs it.
Defining a function does not run it automatically.
Use print() when a function only needs to display output.
Use return when a function should produce a reusable value.
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
Use if not topics to check whether no arbitrary arguments were passed.
A clean beginner function pattern is required_param, *args, default_param=value.
Anything after *args should usually be passed by keyword.
Functions can be passed as arguments to other functions.
Pass function_name when passing the function itself.
Use function_name() only when you want to call it immediately.
A module is a Python file.
Use modules to separate reusable helper code from execution logic.
Import a module using the file name without .py.
Full module imports require dot notation: module_name.function_name().
Specific function imports allow direct calls without the module prefix.
Aliases can rename modules or functions locally.
Avoid import * while learning.
Built-in modules must be imported before use.
Do not name files after built-in modules like math.py, random.py, datetime.py, os.py, or sys.py.
math.pi is a value, not a function.
math.pow() returns a float; ** is usually cleaner for exponent work.
random.randint(start, end) includes the end value.
random.shuffle(list_name) mutates the list in place and returns None.
datetime.datetime.now() returns current date/time.
os.getcwd() returns the current working directory.
sys.version returns Python runtime version information.
sys.platform returns the platform name.
__pycache__ is normal and should be ignored in Git.
Use list comprehension when creating a new list from an iterable with simple transformation or filtering.
List comprehension pattern: [expression for item in iterable].
Filtering pattern: [item for item in iterable if condition].
Transform plus filter pattern: [transformed_item for item in iterable if condition].
if/else transformation pattern: [value_if_true if condition else value_if_false for item in iterable].
Use trailing if when some items should be skipped.
Use if/else before the for when every item should produce an output.
Use nested list comprehension carefully for one-level flattening.
Nested flattening pattern: [item for inner_list in outer_list for item in inner_list].
Keep nested comprehension for clauses in the same order as normal nested loops.
Use dictionary comprehension to create key-value pairs: {key_expression: value_expression for item in iterable}.
Use .items() when creating dictionaries from existing dictionaries.
Remember duplicate dictionary keys get overwritten by later values.
Use set comprehension to create unique values: {expression for item in iterable}.
Remember set comprehension removes duplicates and set order is not dependable.
Parentheses with comprehension-like syntax create a generator expression, not a tuple.
Use tuple(generator_expression) or tuple(existing_iterable) to create a tuple.
Generators are lazy and can be consumed once.
Lambda is a small one-expression anonymous function.
Use lambda lightly for tiny temporary functions; use def for named or complex logic.
Functions are first-class values in Python.
A higher order function can accept another function as an argument or return a function.
A callback is a function passed into another function so it can be called later.
Store or pass a function using function_name without parentheses.
Call a function immediately using function_name().
Lambda creates a tiny anonymous one-expression function.
Lambda syntax is lambda parameter: expression.
Do not use return inside lambda.
Use lambda for tiny temporary one-expression logic.
Use def for named, reusable, multi-step, complex, or growing logic.
map(function, iterable) transforms each item and returns a lazy map object.
filter(function, iterable) keeps only items where the function returns True and returns a lazy filter object.
Use list(), tuple(), or set() to consume map() and filter() results when a concrete collection is needed.
map() is for transformation; filter() is for keeping/removing items.
A list comprehension is often cleaner than map() or filter() with a simple lambda.
Import reduce using from functools import reduce.
Python does not use JavaScript-style import syntax like import reduce from functools.
reduce(function, iterable) reduces many values into one final value.
reduce(function, iterable, initial_value) starts the accumulator with an explicit initial value.
Reducer functions should accept accumulator and current item parameters.
reduce() returns the final value directly; do not wrap reduce() with list().
Prefer sum(), max(), min(), join(), or a normal loop when clearer than reduce().
sorted(iterable) returns a new sorted list.
list.sort() mutates the original list and returns None.
Use key= to tell sorted() or .sort() what value to sort by.
Use key=function_name, not key=function_name().
Use key=len to sort strings by length.
Use key=lambda item: item["field"] to sort dictionaries by a simple field.
Use a named def key function when sorting logic deserves a name or may grow.
Use reverse=True to sort descending.
A tuple key like (item["score"], item["name"]) sorts by the first value, then the second value.
Python sorting key functions extract one sorting value per item; JavaScript sort callbacks compare two items.
Floating-point totals may display tiny precision artifacts; format output with :.2f when clean decimal display is needed.
```

---
