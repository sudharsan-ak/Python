# Python Learning Index

Lightweight rolling tracker for the Python learning project.

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

---

## Current status

```text
Week 1 - Cleared
Day 8 - Cleared
Day 9 - Cleared
Day 10 - Cleared
Day 11 - Cleared
Next: Day 12 - Modules
```

Detailed status:

```text
Day 1 - Cleared
Day 2 - Cleared
Day 3 - Cleared
Day 4 - Cleared
Day 5 - Cleared
Day 6 - Cleared
Day 7 - Cleared
Day 8 - Cleared
Day 9 - Cleared
Day 10 - Cleared
Day 11 - Cleared
Next: Day 12 - Modules
```

---

## Current Project Sources structure

Current preferred source structure after Day 11:

```text
README.md
learning_index.md
week1_notes.md
day8_notes.md
day9_notes.md
day10_notes.md
day11_notes.md
```

Notes:

```text
Day 1 to Day 7 are consolidated into week1_notes.md.
day8_notes.md, day9_notes.md, day10_notes.md, and day11_notes.md stay separate because Week 2 is still active.
When Day 8 to Day 14 are complete, consolidate them into week2_notes.md.
```

---

## Completed days

| Day | Topic | Status | Notes file |
|---|---|---|---|
| Day 1 | Python basics: print, comments, variables, input, f-strings | Cleared | `week1_notes.md` |
| Day 2 | Built-in functions, data types, casting, arithmetic, collections intro | Cleared | `week1_notes.md` |
| Day 3 | Operators: booleans, assignment, comparison, logical operators, precedence | Cleared | `week1_notes.md` |
| Day 4 | Strings: formatting, indexing, slicing, methods, split/join, checks | Cleared | `week1_notes.md` |
| Day 5 | Lists: creation, indexing, slicing, modifying, adding, removing, copying, joining, sorting | Cleared | `week1_notes.md` |
| Day 6 | Tuples: creation, indexing, slicing, immutability, conversion, joining, deleting, use cases | Cleared | `week1_notes.md` |
| Day 7 | Sets: uniqueness, membership, add/update, remove, conversion, operations, relationship checks | Cleared | `week1_notes.md` |
| Day 8 | Dictionaries: key-value pairs, access, get(), update, removal, views, copy, nested dictionaries | Cleared | `day8_notes.md` |
| Day 9 | Conditionals: if, else, elif, logical checks, nesting, truthy/falsy, short-hand conditionals | Cleared | `day9_notes.md` |
| Day 10 | Loops: for, while, range(), break, continue, loop else, nested loops | Cleared | `day10_notes.md` |
| Day 11 | Functions: def, calls, return, parameters, defaults, keyword args, *args, callbacks | Cleared | `day11_notes.md` |

---

## Week summaries

### Week 1 - Python Foundations

Status:

```text
Cleared
```

Notes file:

```text
week1_notes.md
```

Covered:

```text
Day 1 - Python Basics
Day 2 - Variables, Built-in Functions, Data Types
Day 3 - Operators
Day 4 - Strings
Day 5 - Lists
Day 6 - Tuples
Day 7 - Sets
```

Main Week 1 foundation:

```text
printing output
comments
variables
basic data types
input()
type conversion
arithmetic
assignment/comparison/logical operators
strings
lists
tuples
sets
choosing the right collection type
```

### Week 2 - Core Control Flow and Data Handling

Status:

```text
In progress
```

Current Week 2 notes:

```text
day8_notes.md
day9_notes.md
day10_notes.md
day11_notes.md
```

Completed so far:

```text
Day 8 - Dictionaries
Day 9 - Conditionals
Day 10 - Loops
Day 11 - Functions
```

Next:

```text
Day 12 - Modules
```

---

## Next day

```text
Day 12 - Modules
```

Expected Day 12 focus:

```text
what modules are
creating a module
importing a module
importing functions from a module
renaming imports
selected built-in modules
final mixed exercise
```

---

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
```

---

## Learning workflow rules

```text
Teach one topic at a time.
Combine tiny related topics when it improves flow.
Do not over-combine big concepts.
Give exercises as copy-paste comment blocks.
Review submitted code before moving forward.
Do not move to the next topic until the current one is cleared.
After reviewing and clearing each topic, ask before proceeding to the next topic.
Reuse existing variables in the same file when appropriate.
Do not introduce imports/modules too early.
End each day with a focused mixed final exercise.
Avoid overly long final exercises; keep them focused instead of 35+ item checklists.
Use fresh examples/scenarios in final mixed exercises instead of repeating the exact same topic-exercise examples.
After the final mixed exercise is cleared, ask before generating notes or updating the learning index.
Daily notes should be clean study notes, not a chat transcript or code dump.
Completed weeks should be consolidated into weekX_notes.md.
Weekly notes should summarize and organize; they should not paste all daily notes together.
```

---

## Recurring mistakes to watch for

| Pattern | Watch for |
|---|---|
| String `"30"` vs number `30` | Use numbers for math |
| `input()` returns string | Convert with `int()` or `float()` before math |
| Misleading variable names | Example: use `next_year_age`, not `user_age`, for calculated future age |
| Forgetting prompt details | Read every task carefully before coding |
| Raw output becomes hard to read | Add labels when helpful |
| JavaScript habits | Avoid `true`, `false`, `===`, `++`, camelCase, and semicolons |
| Mixed logic readability | Use parentheses with `and` / `or` |
| Unnecessary escaping | Pick the cleaner quote style |
| `find()` result misuse | Use `find(...) != -1` when storing booleans |
| Method mix-ups | Carefully distinguish `startswith()` vs `endswith()` |
| `title()` vs `capitalize()` | `title()` affects every word; `capitalize()` affects only the first character |
| `append()` vs `extend()` | `append()` adds one item; `extend()` adds each item from another list |
| `pop()` vs `del` | `pop()` returns the removed item; `del` does not |
| `sort()` vs `sorted()` | `sort()` mutates original; `sorted()` returns a new sorted list |
| One-item tuple trap | Use `("Python",)`, not `("Python")` |
| Tuple mutation confusion | You can reassign a tuple variable, but you cannot change tuple items directly |
| Empty set trap | Use `set()` for an empty set; `{}` creates a dictionary |
| Set order trap | Printed set order is not dependable; never rely on it |
| Set indexing trap | Sets cannot be accessed with `[0]` |
| `add()` vs `update()` | `add()` adds one item; `update()` adds multiple items |
| `remove()` vs `discard()` | `remove()` crashes if missing; `discard()` does not |
| `union()` vs `symmetric_difference()` | `union()` includes overlap; `symmetric_difference()` excludes overlap |
| `difference()` direction | `A.difference(B)` is not the same as `B.difference(A)` |
| Dictionary key quote confusion | Single or double quotes both work; inside f-strings, use the opposite quote style |
| Dictionary missing key crash | Square bracket access crashes if the key is missing; use `get()` when unsure |
| Dictionary `in` confusion | `in` checks keys, not values |
| Separate nested dict mistake | If a prompt says add a top-level nested key, assign it into the parent dictionary, not a separate variable |
| Direct dictionary assignment | `new_dict = old_dict` is a reference, not a real copy |
| Shallow copy trap | `.copy()` copies the top-level dictionary but not deeply nested mutable data |
| Forgetting full print requirements | If asked to print removed value and updated dictionary, print both |
| Prompt mismatch vs bug | Code can run correctly but still not follow an exact prompt literal; call this a prompt mismatch, not a bug |
| Uneven indentation | Code may run, but standard 4-space indentation is cleaner and safer |
| Incomplete branch testing | If an exercise asks for a branch test, test both requested paths |
| `or` comparison trap | Write `language == "Python" or language == "JavaScript"`, or better, `language in ["Python", "JavaScript"]` |
| Overusing short-hand conditionals | Use one-liners only when the assignment is simple and readable |
| Loop variable name confusion | `for value in dict_name` still loops through keys; use `.values()` for values |
| Plural loop variable names | Use singular names like `key`, `value`, `topic` for one item |
| Misleading output labels | Section labels should match what the code actually prints |
| Infinite while loops | Make sure the loop changes something that eventually makes the condition false |
| `continue` in while loops | Update the counter before `continue` if `continue` would skip the normal update |
| Generic repeated labels | Use specific labels when terminal output gets long |
| Nested loop variable reuse | Do not reuse the same variable name for outer and inner loop items |
| print() vs return confusion | print() shows output; return gives a reusable value back to the program |
| Dead code after return | Code after return does not run; remove it outside demos |
| Prompt string/casing mismatches | Exact punctuation and casing matter in assessment-style prompts |
| Function call vs assignment mistake | Use function_name(...) to call; function_name = (...) overwrites the function name |
| *args naming mismatch | Generic *args works, but follow prompt-specific names like *topics when requested |
| Function callback call timing | Pass function_name without () when another function should call it later |
| Default and *args order confusion | Prefer required_param, *args, default_param=value for the beginner pattern |

---

## Day-specific key reminders

### Day 1

```text
Python runs line by line.
print() shows output.
Variables store values.
Strings need quotes.
Numbers usually do not.
input() always returns text.
Use int() before math with input.
```

### Day 2

```text
Use built-in functions like len(), type(), int(), float(), str().
Lists are ordered collections.
Dictionaries store key-value data.
Tuples are fixed-style grouped data.
Sets store unique values.
Assignment shortcuts like += update existing values.
% gives the remainder.
```

### Day 3

```text
Booleans are True/False.
Comparison operators return booleans.
and requires both sides to be true.
or requires at least one condition to be true.
not flips a boolean.
Parentheses make mixed logic clearer.
```

### Day 4

```text
Strings are sequences of characters.
Indexing gets one character.
Slicing gets part of a string.
Use strip(), replace(), upper(), lower(), title().
Use split() to create a list from a string.
Use join() to create a string from a list.
Use isalpha(), isdigit(), isalnum(), islower(), isupper() for checks.
```

### Day 5

```text
Lists are ordered and mutable.
Use [] to create lists.
Use indexes and slices like strings.
Use append(), insert(), and extend() to add items.
Use remove(), pop(), del, and clear() to remove items.
Use copy() for independent list copies.
Use sort() to sort the original list.
Use sorted() to create a sorted copy.
```

### Day 6

```text
Tuples are ordered and immutable.
Use () to create tuples.
A one-item tuple needs a trailing comma.
Tuple items cannot be changed directly.
Tuple variables can be reassigned to a new tuple.
Use list() to temporarily modify tuple data.
Use tuple() to convert a list back to a tuple.
Use tuples for fixed grouped data.
Use lists for data that should change.
```

### Day 7

```text
Sets store unique values.
Use {} to create a set with values.
Use set() to create an empty set.
{} by itself creates an empty dictionary.
Sets remove duplicates automatically.
Sets do not have dependable order.
Sets do not support indexing.
Use in and not in for membership checks.
Use add() to add one item.
Use update() to add multiple items.
Use remove() when the item must exist.
Use discard() when the item may not exist.
Use pop() carefully because the removed item is unpredictable.
Use clear() to empty a set.
Use del to delete the set variable.
Use set(list_or_tuple) to remove duplicates.
Use union() for everything from both sets.
Use intersection() for shared items.
Use difference() for items only in the first set.
Use symmetric_difference() for items not shared.
Use issubset(), issuperset(), and isdisjoint() for boolean relationship checks.
```

### Day 8

```text
Dictionaries store key-value pairs.
Use dictionaries when values need labels.
{} creates an empty dictionary.
Use len() to count key-value pairs.
Use square bracket access when the key must exist.
Use get() when the key might be missing.
Use get("key", default) for fallback values.
Use in to check whether a key exists.
in checks dictionary keys, not values.
Use dict["key"] = value to add or update data.
Use update() to add/update multiple key-value pairs.
Use pop() to remove a key and return its value.
Use pop("key", default) when the key may not exist.
Use del when the key exists and you do not need the removed value.
Use popitem() to remove the last inserted key-value pair.
Use clear() to empty a dictionary.
Use keys(), values(), and items() to inspect dictionary data.
Use list() to convert dictionary views when list behavior is needed.
Use copy() for a separate top-level dictionary.
copy() is shallow; nested data needs more care later.
Use nested dictionaries to group related data.
Use chained square brackets for nested dictionary access.
Use get("nested_key", {}) for safer nested access.
```

### Day 9

```text
Use if for a single condition.
Use else for the fallback path.
Use elif for multiple connected branches.
Indentation defines the block.
Use 4 spaces for standard Python indentation.
Use == for comparison, not =.
Use and when all conditions must be true.
Use or when at least one condition must be true.
Use parentheses when combining and / or.
Use not for opposite checks.
Use if value for truthy checks.
Use if not value for empty/falsy checks.
Empty strings, lists, dictionaries, tuples, sets, 0, None, and False are falsy.
Non-empty strings, lists, dictionaries, tuples, and sets are truthy.
Use if list_name to check whether a list has items.
Use if dict_name to check whether a dictionary has data.
Use if "key" in dict_name to check whether a specific key exists.
Use nested conditionals only when a second check depends on a first check.
Prefer flatter if / elif / else chains when they read cleaner.
Use short-hand conditionals only for simple two-way assignments.
Do not force complex logic into one line.
```

### Day 10

```text
Use for loops for known items or ranges.
Use while loops for condition-based repetition.
Use clear singular/plural loop variable names.
Strings loop character by character.
Dictionaries loop through keys by default.
Use .values() for values and .items() for key-value pairs.
The object after in controls behavior, not the loop variable name.
range() excludes the stop value.
Use negative step values to count backward.
Use range(len(...)) when indexes are actually needed.
break stops the whole loop.
continue skips only the current loop run.
In while loops, update counters before continue when needed.
Loop else runs only when no break occurs.
Nested loops run the full inner loop for every outer item.
Nested loops multiply work and can become slow on large data.
```


### Day 11

```text
Functions group reusable logic.
Use def to define a function.
Calling a function runs it.
Use print() to display output.
Use return to produce a reusable value.
A function returns None by default without return.
Code after return does not run.
Parameters are placeholders in function definitions.
Arguments are real values passed during function calls.
Positional arguments are matched by order.
Keyword arguments are matched by parameter name.
Default parameters provide fallback values.
Required parameters come before default parameters.
Use *args for any number of positional arguments.
*args becomes a tuple inside the function.
You can loop through *args.
Use required_param, *args, default_param=value as the clean beginner pattern.
Pass function_name without () when passing a function into another function.
Use function_name() when calling the function immediately.
```

---

## Current confidence level

```text
Ready for Day 12 - Modules
```
