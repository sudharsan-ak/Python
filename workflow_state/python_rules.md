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
A TypeError usually means the operation is valid in general, but the given value types do not work together.
Read the last line of a traceback first to identify the error type and message.
Use the traceback line number to find the exact line that crashed.
Use type() to inspect values when a type-related error is unclear.
Choose type conversions based on intent: f-string/str() for display, int()/float() for numeric math.
Do not fix type errors by blindly converting everything to strings.
List and string indexes must be integers or slices, not arbitrary string labels.
Dictionaries use keys for access; lists and strings use numeric indexes.
Use square brackets for dictionary/list/string access; parentheses call functions.
A missing dictionary key usually causes KeyError, not TypeError.
Use get("key", fallback) when a dictionary key may be missing and later code expects a usable value.
Calling a method on None usually means a value was missing, a function forgot to return, or a mutating method returned None.
Remember append() mutates the list and returns None.
Remember sort() mutates the list and returns None.
Use sorted() when you need a new sorted list.
Use return when a function result must be reused by later code.
isinstance(value, type_name) checks whether a value belongs to a type and returns True or False.
Use isinstance(value, str) when mixed data requires checking whether a value is a string before converting it.
Prefer a normal for loop over a complex comprehension when debugging mixed-type data.
When debugging, fix the root cause of the bad value instead of only changing the crashed line.
Use datetime.datetime.now() after import datetime.
Use datetime.now() after from datetime import datetime.
Do not name Python files after the built-in datetime module, such as datetime.py.
date(year, month, day) creates a date object.
time(hour, minute, second) creates a time object.
datetime(year, month, day, hour, minute, second) creates a datetime object.
Use datetime attributes like .year, .month, .day, .hour, .minute, and .second without parentheses.
Use datetime methods like .date() and .time() with parentheses.
Use strftime() to format date/time objects into strings.
Use strptime() to parse strings into datetime objects.
The strptime() format string must match the input string exactly.
Use %H for 24-hour input such as 18:30.
Use %I with %p for 12-hour AM/PM input such as 06:30 PM.
Use timedelta for date/time duration math.
datetime + timedelta gives a future datetime.
datetime - timedelta gives a past datetime.
datetime - datetime gives a timedelta duration.
date - date gives a timedelta duration.
Use timedelta.days for the whole day part of a duration.
Use timedelta.total_seconds() when the full duration in seconds is needed.
Do not assume timedelta.seconds means total seconds; it is only the leftover seconds after days are counted.
Avoid subtracting plain time objects directly when date context matters; use datetime objects for duration calculations.
datetime.combine(date_object, time_object) can combine separate date and time objects into one datetime object when needed.
Use try / except to handle risky operations that may fail at runtime.
Prefer catching specific exceptions instead of using a bare except.
Use except ValueError for invalid numeric conversion or parsing values.
Use except TypeError when the operation receives the wrong type.
Use except ZeroDivisionError when division by zero is possible.
Use except KeyError when a required dictionary key may be missing.
Use except IndexError when a list/string index may be out of range.
Use except SomeError as error when the original exception message is useful for debugging or display.
Only one matching except block runs for a raised exception.
Use else after try / except for logic that should run only when no exception happened.
Use finally for code that must run whether the try block succeeds or fails.
Do not force else or finally into every try / except block; use them only when they make the flow clearer.
Keep try blocks focused on the risky operation instead of wrapping unrelated code.
Put success-only processing in else when it depends on successful risky code.
Use fallback values in except only when a default value is truly acceptable.
Do not silently replace bad data with defaults when the bad data should be rejected.
Use .get("key", fallback) for optional dictionary fields.
Use try / except KeyError for missing required dictionary fields when the missing field is an error path.
Use datetime.strptime() inside try / except ValueError when parsing date text from uncertain input.
Use separate except blocks when different failures need different messages.
Avoid using exception handling as a replacement for simple checks or clean data access.
For money-style output, use formatting like :.2f when two decimal places are required.

Use the built-in re module for regular expression work.
Use raw strings like r"\d+" for regex patterns.
A regex pattern describes text to search, validate, extract, or replace.
re.search(pattern, text) finds the first match anywhere in the text.
re.search() returns a match object when found and None when not found.
Check that a match object exists before calling .group().
Use match.group() to get the full matched text.
Use match.group(1), match.group(2), etc. to get captured group values.
re.findall(pattern, text) returns all matches as a list.
re.findall() returns an empty list when no matches are found.
re.match(pattern, text) checks only from the beginning of the string.
Use \d for one digit, \w for one word character, and \s for one whitespace character.
Use + for one or more of the previous pattern.
Use * for zero or more of the previous pattern.
Use ? for zero or one of the previous pattern.
Use {n} for exactly n repetitions.
Use character ranges like [A-Z], [a-z], and [0-9] for grouped character choices.
Use ^ to mark the start of a string and $ to mark the end of a string.
Use anchors when the whole string must match a validation format.
Use parentheses to create capture groups.
Use \. to match a real dot because . is a regex wildcard.
Remember findall() with groups returns captured group values instead of full matches.
Use re.sub(pattern, replacement, text) to replace or clean matching text.
re.sub() returns a new string and does not mutate the original string.
Use an empty replacement string with re.sub() to remove matched text.
Use count=1 with re.sub() when only the first match should be replaced.
Use re.fullmatch() as a cleaner full-string validation option.
Use re.finditer() when you need all match objects and their positions.
Use re.split() when text needs to be split using multiple separators.
Use re.compile() when the same regex pattern is reused multiple times.
Use re.IGNORECASE when matching should ignore uppercase/lowercase differences.
Use | for OR-style alternatives inside a regex pattern.
Use \b for whole-word boundaries.
Keep regex patterns small and readable instead of writing giant patterns too early.
Do not hardcode exact values when the goal is to parse a reusable pattern.
```

---
