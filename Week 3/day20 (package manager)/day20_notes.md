# Day 20 Notes - Python Package Manager

Source backbone: https://github.com/Asabeneh/30-Days-Of-Python

## Core idea

Day 20 focused on how Python projects install, inspect, remove, and document external packages.

```text
pip installs packages.
import uses installed packages in Python code.
requirements.txt records project dependencies.
virtual environments isolate project packages.
```

## 1. Package manager basics

A package manager helps manage external code. Python commonly uses `pip`, similar to `npm` in Node.js.

Preferred beginner command style:

```bash
python -m pip install package_name
```

This runs pip through the Python interpreter you are using.

## 2. Package vs module

```text
module  -> usually one Python file
package -> collection/folder of modules/code
```

Built-in modules come with Python:

```python
import datetime
import re
```

External packages must be installed first, then imported:

```bash
python -m pip install requests
```

```python
import requests
```

```text
install -> terminal command
import  -> Python code
```

## 3. Common pip commands

```bash
python -m pip install requests      # install package
python -m pip list                  # list installed packages
python -m pip show requests         # show package details
python -m pip uninstall requests    # uninstall package
```

If code imports `requests`, uninstalling it can break the code.

Missing external package error:

```text
ModuleNotFoundError: No module named 'requests'
```

This usually means the package is not installed in the environment being used.

## 4. requirements.txt

`requirements.txt` lists external packages needed by a project.

```text
requests==2.33.1
```

`==` pins an exact package version.

Install all dependencies from the file:

```bash
python -m pip install -r requirements.txt
```

Useful command awareness:

```bash
python -m pip freeze
python -m pip freeze > requirements.txt
```

Do not blindly run `pip freeze > requirements.txt` in a messy environment, because it can dump packages the project does not actually use.

Beginner rule:

```text
List packages your project directly uses.
Let pip handle their dependencies.
```

## 5. Virtual environment awareness

A virtual environment gives one project its own isolated package space.

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

```text
global environment  -> shared package space
virtual environment -> project-specific package space
```

Use virtual environments for real projects so dependencies do not become a junk drawer.

## Safe habits

```text
Use python -m pip for clarity.
Install only packages the project needs.
Check package names carefully.
Use requirements.txt for dependencies.
Avoid messy pip freeze dumps.
Do not uninstall blindly.
Do not run random install commands from strangers.
Use a virtual environment for real projects.
```

## Final mixed exercise

Scenario: project setup checklist for a small API helper project.

Practiced: built-in module vs external package, pip commands, requirements.txt, virtual environment commands, install vs import, and safe package habits.

Final mixed exercise status: cleared.