# Mistakes Log - Python Learning Project

Recurring mistakes, prompt mismatches, and Python traps observed during the learning project.

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Scope

```text
Current scope: Day 1 through Day 15
Next update: after Day 16, if new reusable mistakes are found
```

Use this file as the dedicated place for mistakes and gotchas. Keep `learning_index_part1.md` focused on historical progress, week summaries, and day-specific reminders.

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
| Import/file-name mismatch | If a file is renamed, update all imports that reference it |
| Built-in module filename conflict | Do not create files like math.py or random.py |
| `import *` confusion | Avoid it; it hides where names came from |
| `math.pi()` mistake | `math.pi` is a value, not a function |
| `random.shuffle()` assignment trap | It mutates the list and returns None |
| Stale/unsaved file run | Save all changed files before rerunning, especially helper modules |
| Helper function returns `None` | Check whether the function used print instead of return |
| `__pycache__` confusion | Normal generated folder; ignore it in Git |
| List comprehension syntax order | Use `[expression for item in iterable]`, not JavaScript-style syntax |
| Filtering vs if/else comprehension confusion | Trailing `if` skips items; `if/else` before `for` transforms every item |
| Nested comprehension order confusion | Keep `for` clauses in the same order as normal nested loops |
| Over-complicated comprehensions | If a comprehension becomes hard to read, use normal loops |
| Dictionary comprehension duplicate keys | Later values overwrite earlier values for the same key |
| Set comprehension order confusion | Sets remove duplicates and printed order is not dependable |
| Tuple comprehension misconception | `(x for x in items)` is a generator expression, not a tuple |
| Generator consumption | Once a generator is consumed, converting/looping again may produce no values |
| Lambda overuse | Use `lambda` only for tiny one-expression temporary functions; use `def` for real logic |
| Passing function call instead of function | Use `function_name` when passing a function; `function_name()` calls it immediately |
| Lambda return keyword mistake | Lambda automatically returns its expression; do not write `return` inside lambda |
| Lambda overuse in real logic | Use `def` when logic is named, reused, multi-step, or likely to grow |
| map/filter lazy object confusion | `map()` and `filter()` return lazy objects; consume with `list()`, `tuple()`, or `set()` when needed |
| map vs filter mix-up | `map()` transforms every item; `filter()` keeps/removes items |
| Generator expression vs list comprehension | `list((x for x in items))` consumes a generator; `[x for x in items]` is the actual list comprehension |
| Python import order confusion | Use `from functools import reduce`, not JavaScript-style `import reduce from functools` |
| reduce output confusion | `reduce()` returns one final value directly; do not wrap it with `list()` |
| reduce overuse | Prefer `sum()`, `max()`, `min()`, `join()`, or a normal loop when clearer |
| reduce accumulator naming | Reducer functions should clearly separate `accumulator` from the current item |
| Floating-point display surprise | Decimal totals may display precision artifacts; use formatting like `{value:.2f}` for display |
| sorted key function call mistake | Use `key=function_name`, not `key=function_name()` |
| Python sort vs JavaScript sort confusion | Python `key` extracts one value per item; JavaScript comparator compares two items |
| `.sort()` return trap | `.sort()` mutates the list and returns `None`; use `sorted()` for a new list |
| Extra output bloat | If the prompt asks for one print, avoid adding extra debug-style output unless useful |
| Small typo in required variable names | Typos like `toal_score` can work if used consistently but still violate prompt-specific naming |
| TypeError panic debugging | Read the traceback first; do not randomly change code before finding the exact crashed line |
| Type conversion without intent | Use f-string/str() for display, but int()/float() for real numeric math |
| List/string/dict access mismatch | Lists and strings use numeric indexes; dictionaries use keys |
| Calling dictionaries/lists like functions | `profile("name")` and `skills(0)` are calls; use square brackets for access |
| Missing dictionary key vs wrong type | Missing dict keys usually cause KeyError; wrong index type on list/string usually causes TypeError |
| NoneType method call | If `.upper()` or another method is called on None, trace where None came from first |
| Dictionary get() without fallback | `dict.get("missing")` returns None; provide a fallback if later code expects a real value |
| append()/sort() return misunderstanding | These mutate the list and return None; do not assign them when expecting a new list |
| Blind string conversion | Converting everything to str() can make code run but still produce wrong logic like "855" instead of 90 |
| isinstance() introduced | Use `isinstance(value, str)` to check mixed data before converting, but prefer a loop when it is clearer |

---

## How to use this file

```text
Before starting a new day, skim the most relevant mistakes for that day's topic.
During code review, classify issues as:
- real mistakes
- prompt mismatches
- optional style notes
After each completed day, add only reusable mistakes that are likely to happen again.
```

## Current status

```text
Mistakes log updated through Day 15.
Ready to keep using during Day 16 - Python Date Time.
```
