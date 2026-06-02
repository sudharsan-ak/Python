# Day 12 Notes - Modules

Status: Cleared

Source backbone: https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 12 focused on using **modules** to split reusable Python code into separate files and import that code where needed.

Core idea:

```text
A module is a Python file.
Reusable/helper code can live in one file.
Execution logic can live in another file.
```

Example structure:

```text
helpers.py           -> reusable helper functions
modules_practice.py  -> main file that imports and uses helpers
```

This keeps code cleaner and avoids dumping every helper function and every execution step into one giant file.

---

## 1. Module basics

If a file is named:

```text
helpers.py
```

Python imports it as:

```python
import helpers
```

not:

```python
import helpers.py
```

Full-module import uses dot notation:

```python
student_name = helpers.get_student_name()
```

Pattern:

```text
module_name.function_name()
```

JavaScript comparison:

```javascript
import { getStudentName } from "./helpers.js";
```

Python equivalent for full-module import:

```python
import helpers
student_name = helpers.get_student_name()
```

---

## 2. Custom modules

A custom module is a `.py` file you create yourself.

Example helper file:

```python
# helpers.py
def get_student_name():
    return "Sudharsan Srinivasan"
```

Example main file:

```python
# modules_practice.py
import helpers

student_name = helpers.get_student_name()
```

Important rule:

```text
Full module import -> call with module_name.function_name().
```

So after `import helpers`, this is correct:

```python
helpers.get_student_name()
```

This is wrong unless the function was imported directly:

```python
get_student_name()
```

---

## 3. Import styles

| Style | Syntax | How to call |
|---|---|---|
| Full module import | `import helpers` | `helpers.get_student_name()` |
| Specific function import | `from helpers import get_student_name` | `get_student_name()` |
| Multiple imports | `from helpers import get_current_day, get_current_topic` | `get_current_day()` |
| Module alias | `import helpers as helper_tools` | `helper_tools.get_student_name()` |
| Function alias | `from helpers import format_topic_summary as format_summary` | `format_summary(...)` |

Main rule:

```text
Full module import or module alias -> use dot notation.
Specific function import or function alias -> call directly.
```

Avoid while learning:

```python
from helpers import *
```

It hides where names came from and makes larger files harder to debug.

---

## 4. Built-in `math` module

`math` is a built-in module for math utilities.

```python
import math
```

Common tools practiced:

| Tool | Use |
|---|---|
| `math.sqrt(81)` | square root |
| `math.ceil(19.25)` | round up |
| `math.floor(19.25)` | round down |
| `math.pi` | pi value |
| `math.pow(3, 4)` | power calculation |

Key rules:

```text
math.pi is a value, not a function.
math.sqrt() returns a float.
math.pow() returns a float.
** is usually cleaner for normal exponent work.
```

Example:

```python
power_result = 3 ** 4              # 81
math_power_result = math.pow(3, 4) # 81.0
```

JavaScript comparison:

```text
JavaScript -> Math.sqrt(), Math.ceil(), Math.floor(), Math.PI
Python     -> import math first, then math.sqrt(), math.ceil(), math.pi
```

---

## 5. Built-in `random` module

`random` is used for random values.

```python
import random
```

Common tools practiced:

| Tool | Use |
|---|---|
| `random.choice(items)` | picks one item |
| `random.randint(70, 100)` | random integer, end included |
| `random.random()` | random float from 0 to less than 1 |
| `random.shuffle(items)` | shuffles a list in place |

Important trap:

```python
shuffled_tasks = random.shuffle(review_tasks)
```

This stores `None`, because `shuffle()` mutates the original list and returns nothing useful.

Correct pattern:

```python
random.shuffle(review_tasks)
print(review_tasks)
```

---

## 6. Light built-in module awareness

These modules were covered lightly.

| Module | Used for | Beginner example |
|---|---|---|
| `datetime` | date/time values | `datetime.datetime.now()` |
| `os` | operating-system/folder info | `os.getcwd()` |
| `sys` | Python runtime/system info | `sys.version`, `sys.platform` |

### `datetime`

```python
import datetime
current_datetime = datetime.datetime.now()
```

The repeated name is normal:

```text
datetime module -> datetime class -> now() method
```

Useful fields:

```python
current_datetime.year
current_datetime.month
current_datetime.day
```

### `os`

```python
import os
current_folder = os.getcwd()
```

`os.getcwd()` returns the folder Python is running from.

### `sys`

```python
import sys
python_version = sys.version
platform_name = sys.platform
```

On Windows, `sys.platform` commonly returns `win32`, even on 64-bit Windows.

---

## 7. File naming and `__pycache__`

Do not name your own files after built-in modules:

```text
math.py
random.py
datetime.py
os.py
sys.py
```

Those names can conflict with Python's real modules.

When Python imports a module, it may create:

```text
__pycache__/
```

That is normal. It stores compiled bytecode. You do not edit it.

Recommended `.gitignore` entries:

```gitignore
__pycache__/
*.pyc
```

---

## 8. Local Day 12 file naming

Because the files already live inside the `day12 (modules)` folder, practice files do not all need to start with `day12_`.

Clean structure:

```text
day12 (modules)/
  helpers.py
  modules_practice.py
  import_styles.py
  math_module.py
  random_module.py
  builtin_awareness.py
  day12_final_helpers.py
  day12_final.py
```

This is fine as long as imports match the actual file names.

After renaming `day12_helpers.py` to `helpers.py`, use:

```python
import helpers
from helpers import get_student_name
```

not:

```python
import day12_helpers
```

---

## What was practiced

Day 12 practice included:

```text
creating helper modules
importing a full custom module
calling module functions with dot notation
specific function imports
multiple imports
module aliases
function aliases
math.sqrt(), math.ceil(), math.floor(), math.pi, math.pow()
random.choice(), random.randint(), random.random(), random.shuffle()
datetime.datetime.now()
os.getcwd()
sys.version and sys.platform
checking output types
```

---

## Mistakes, prompt mismatches, and corrections

| Issue | Correction / Clarification |
|---|---|
| `__pycache__` appeared | Normal when importing modules; ignore it in Git. |
| Practice files were renamed | Fine, but imports must match the new file names. |
| Final exercise first showed `Session: None` and `None` | Stale/unsaved helper file caused old print-based behavior; saving and rerunning fixed it. |
| `print()` vs `return` trap | Helper functions that build reusable values should `return`; otherwise the caller receives `None`. |
| Multi-import line `import math, random, datetime, os, sys` | Works, but one import per line is cleaner style. |

---

## Final mixed exercise status

Final scenario:

```text
Python study session toolkit
```

Files used:

```text
day12_final_helpers.py
day12_final.py
```

Covered:

```text
custom helper module
module alias
specific function import
function alias
math.ceil()
random.choice()
datetime.datetime.now()
os.getcwd()
sys.platform
*args
return values
conditionals
f-strings
```

Final status:

```text
Cleared
```

---

## Day 12 key takeaways

```text
A module is a Python file.
Import a module using the file name without .py.
Use modules to separate reusable helper code from execution logic.
Full module imports require dot notation.
Specific function imports allow direct function calls.
Aliases can rename modules or functions locally.
Avoid import * while learning.
Built-in modules must be imported before use.
Do not name files after built-in modules.
math.pi is a value, not a function.
math.pow() returns a float; ** is usually cleaner.
random.randint(start, end) includes the end value.
random.shuffle() mutates the original list and returns None.
datetime.datetime.now() returns current date/time.
os.getcwd() returns the current working directory.
sys.version returns Python version information.
sys.platform returns the platform name.
__pycache__ is normal and should be ignored in Git.
If output shows None, check print() vs return and make sure files were saved.
```

---

## Ready for next day

```text
Day 13 - Comprehension
```
