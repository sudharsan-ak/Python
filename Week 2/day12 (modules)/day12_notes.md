# Day 12 Notes - Modules

Status: Cleared

Source backbone: https://github.com/Asabeneh/30-Days-Of-Python

## What Day 12 covered

Day 12 focused on Python modules: splitting reusable code into separate `.py` files, importing custom modules, using import aliases, and getting light practice with selected built-in modules.

Topics covered:

```text
custom modules
full module imports
specific function imports
multiple imports
module/function aliases
math
random
datetime / os / sys awareness
__pycache__
final mixed exercise
```

## 1. Module basics

A module is just a Python file.

```text
one .py file = one module
```

If the file is named `helpers.py`, import it as:

```python
import helpers
```

not:

```python
import helpers.py
```

The main reason to use modules is to separate reusable helper code from execution logic.

```text
helpers.py          -> reusable helper functions
modules_practice.py -> code that runs and uses those helpers
```

This keeps the main file cleaner and avoids putting every function and every execution step into one giant file.

JavaScript comparison:

```javascript
import { getStudentName } from "./helpers.js";
```

Python full-module import:

```python
import helpers
student_name = helpers.get_student_name()
```

Pattern:

```text
module_name.function_name()
```

## 2. Custom modules

A custom module is a `.py` file you create yourself.

Example helper module:

```python
def get_student_name():
    return "Sudharsan Srinivasan"
```

Example main file:

```python
import helpers
student_name = helpers.get_student_name()
```

Important rule:

```text
Full module import -> call with module_name.function_name().
```

Correct:

```python
helpers.get_student_name()
```

Wrong after full-module import:

```python
get_student_name()
```

That direct call only works when the function itself is imported directly.

## 3. Import styles

| Import style | Syntax | How to call |
|---|---|---|
| Full module import | `import helpers` | `helpers.get_student_name()` |
| Specific function import | `from helpers import get_student_name` | `get_student_name()` |
| Multiple imports | `from helpers import get_current_day, get_current_topic` | `get_current_day()` |
| Module alias | `import helpers as helper_tools` | `helper_tools.get_student_name()` |
| Function alias | `from helpers import format_topic_summary as format_summary` | `format_summary(...)` |

Blunt rule:

```text
Full module import or module alias -> use dot notation.
Specific function import or function alias -> call directly.
```

Avoid this while learning:

```python
from helpers import *
```

It hides where functions came from and makes bigger files harder to debug.

## 4. `math` module

`math` is a built-in module for math utilities.

```python
import math
```

Common tools practiced:

```python
math.sqrt(81)
math.ceil(19.25)
math.floor(19.25)
math.pi
math.pow(3, 4)
```

Key details:

```text
math.pi is a value, not a function.
math.sqrt() returns a float.
math.pow() returns a float.
** is usually cleaner for normal exponent work.
```

Example:

```python
power_result = 3 ** 4              # 81, int
math_power_result = math.pow(3, 4) # 81.0, float
```

JavaScript has `Math.sqrt()`, `Math.ceil()`, `Math.floor()`, and `Math.PI` globally. Python requires `import math` first.

## 5. `random` module

`random` is a built-in module for random values.

```python
import random
```

Common tools practiced:

```python
random.choice(items)
random.randint(70, 100)
random.random()
random.shuffle(items)
```

Key details:

```text
random.choice(sequence) picks one item.
random.randint(start, end) includes both start and end.
random.random() returns a float from 0 to less than 1.
random.shuffle(list_name) mutates the list in place and returns None.
```

Important trap:

```python
shuffled_tasks = random.shuffle(review_tasks)
```

This stores `None`, not the shuffled list.

Correct:

```python
random.shuffle(review_tasks)
print(review_tasks)
```

## 6. `datetime`, `os`, and `sys`

These were covered lightly.

| Module | Used for | Beginner example |
|---|---|---|
| `datetime` | current date/time | `datetime.datetime.now()` |
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

Useful parts:

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

`os.getcwd()` returns the current working directory: the folder Python is running from.

### `sys`

```python
import sys
python_version = sys.version
platform_name = sys.platform
```

On Windows, `sys.platform` commonly returns `win32`, even on 64-bit Windows.

## 7. File naming and `__pycache__`

Do not name your own files after built-in modules:

```text
math.py
random.py
datetime.py
os.py
sys.py
```

Those names can conflict with Python's real built-in modules.

When importing modules, Python may create:

```text
__pycache__/
```

That is normal. It stores compiled bytecode. You do not edit it, and Python will regenerate it if deleted.

Recommended `.gitignore` entries:

```gitignore
__pycache__/
*.pyc
```

## 8. Local Day 12 file naming

Practice files were renamed to avoid repeating `day12_` because they already live inside the `day12 (modules)` folder.

Clean local structure:

```text
day12 (modules)/
  __pycache__/
  helpers.py
  modules_practice.py
  import_styles.py
  math_module.py
  random_module.py
  builtin_awareness.py
  day12_final_helpers.py
  day12_final.py
```

This is fine. The only rule is that imports must match the actual file names.

After renaming `day12_helpers.py` to `helpers.py`, use:

```python
import helpers
from helpers import get_student_name
```

not:

```python
import day12_helpers
```

## What was practiced

Day 12 practice included:

```text
creating helper modules
importing a full custom module
calling module functions with dot notation
importing specific and multiple functions
using module aliases and function aliases
avoiding import *
using math.sqrt(), math.ceil(), math.floor(), math.pi, math.pow()
using random.choice(), random.randint(), random.random(), random.shuffle()
using datetime.datetime.now()
using os.getcwd()
using sys.version and sys.platform
checking output types from built-in modules
```

## Mistakes, prompt mismatches, and corrections

| Issue | Correction / Clarification |
|---|---|
| Asked about `__pycache__` appearing | Normal when importing modules; ignore it in Git. |
| Renamed Day 12 practice files | Fine, but imports must match the new file names. |
| Final exercise first showed `Session: None` and `None` | Stale/unsaved helper file caused old print-based behavior; saving and rerunning fixed it. |
| `print()` vs `return` trap | Helper functions that build values should `return`; printing gives `None` if caller expects a value. |
| Multi-import line `import math, random, datetime, os, sys` | Works, but one import per line is cleaner style. |

## Final mixed exercise status

The final mixed exercise used a Python study session toolkit scenario.

Files used:

```text
day12_final_helpers.py
day12_final.py
```

It covered:

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

## Day 12 key takeaways

```text
A module is a Python file.
Use modules to separate reusable helper code from execution logic.
Import a module using the file name without .py.
Full module imports require dot notation.
Specific function imports allow direct function calls.
Aliases can rename modules or functions locally.
Avoid import * while learning.
Built-in modules must be imported before use.
math.pi is a value, not a function.
math.pow() returns a float; ** is usually cleaner for exponent work.
random.randint(start, end) includes the end value.
random.shuffle() mutates the original list and returns None.
datetime.datetime.now() returns current date/time.
os.getcwd() returns the current working directory.
sys.version returns Python version information.
sys.platform returns the platform name.
Do not name your files after built-in modules.
__pycache__ is normal and should be ignored in Git.
If output shows None, check whether a function printed instead of returned, and make sure files were saved before running.
```

## Ready for next day

```text
Day 13 - Comprehension
```
