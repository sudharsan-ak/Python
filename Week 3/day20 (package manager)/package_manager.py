# ---------------------------------------------------------------------
# Topic 1 - Package Manager Basics, pip, Package vs Module

print(f"{'-' * 30} Topic 1 {'-' * 30}")

# 1. Create a variable called built_in_module and set it to "datetime"
built_in_module = "datetime"

# 2. Create a variable called external_package and set it to "requests"
external_package = "requests"

# 3. Create a variable called package_manager and set it to "pip"
package_manager = "pip"

# 4. Print a sentence explaining that built_in_module comes with Python
print(f"{built_in_module} comes with Python.")

# 5. Print a sentence explaining that external_package would need to be installed before importing
print(f"{external_package} would need to be installed before importing.")

# 6. Create a variable called module_meaning and set it to a short explanation of what a module is
module_meaning = "A module is usually one Python file"

# 7. Create a variable called package_meaning and set it to a short explanation of what a package is
package_meaning = "A package is a folder or collection of modules"

# 8. Print both explanations with clear labels
print(f"Module meaning: {module_meaning}")
print(f"Package meaning: {package_meaning}")

# ---------------------------------------------------------------------
# Topic 2 - Installing and Using External Packages

print(f"{'-' * 30} Topic 2 {'-' * 30}")

# 1. Create a variable called install_command and set it to the command used to install requests
install_command = "python -m pip install requests"

# 2. Create a variable called package_name and set it to "requests"
package_name = "requests"

# 3. Print a sentence explaining that the package is installed from the terminal, not from inside normal Python code
print(f"{package_name} is installed from the terminal before python code can import and use it during runtime")

# 4. Import requests
import requests

# 5. Print a sentence showing that requests was imported successfully
print(f"requests was imported successfully")

# 6. Print the installed requests version using requests.__version__
print(f"requests version: {requests.__version__}")

# ---------------------------------------------------------------------
# Topic 3 - Checking, Showing, and Uninstalling Packages

print(f"{'-' * 30} Topic 3 {'-' * 30}")

# 1. Create variables for these package commands:
# check_command -> command that lists installed packages
# show_command -> command that shows details for requests
# uninstall_command -> command that would uninstall requests
check_command = "python -m pip list"
show_command = "python -m pip show requests"
uninstall_command = "python -m pip uninstall requests"

# 2. Print each command with a clear label
print(f"Check command: {check_command}")
print(f"Show command: {show_command}")
print(f"Uninstall command: {uninstall_command}")

# 3. Print a warning sentence explaining why we are not uninstalling requests right now
print(f"Current file uses the package requests, uninstalling it can break the code")

# 4. Print a sentence explaining what ModuleNotFoundError may mean when importing an external package
print(f"If import fails with ModuleNotFoundError, check whether the package is installed in the same environment.")

# ---------------------------------------------------------------------
# Topic 4 - requirements.txt and Project Dependency Setup

print(f"{'-' * 30} Topic 4 {'-' * 30}")

# 1. Create a variable called requirements_file and set it to "requirements.txt"
requirements_file = "requirements.txt"

# 2. Create a variable called dependency_line and set it to "requests==2.33.1"
dependency_line = "requests==2.33.1"

# 3. Create a variable called install_from_requirements_command
#    and set it to the command used to install packages from requirements.txt
install_from_requirements_command = "python -m pip install -r requirements.txt"

# 4. Print a sentence explaining what requirements.txt is for
print(f"{requirements_file} is for letting other developers install all packages listed inside the text file")

# 5. Print the dependency line with a clear label
print(f"Dependency line: {dependency_line}")

# 6. Print the install-from-requirements command with a clear label
print(f"Install from requirements command: {install_from_requirements_command}")

# 7. Print a warning explaining why we should not blindly run pip freeze > requirements.txt
#    in a messy environment
print(f"Blindly running pip freeze may dump a giant messy list of packages that our file might not actually need.")

# ---------------------------------------------------------------------
# Topic 5 - Virtual Environment Awareness and Safe Package Habits

print(f"{'-' * 30} Topic 5 {'-' * 30}")

# 1. Create a variable called virtual_environment_meaning
#    and set it to a short explanation of what a virtual environment does
virtual_environment_meaning = "A virtual environment gives a project its own isolated Python package space."

# 2. Create a variable called create_venv_command
#    and set it to the command used to create a virtual environment
create_venv_command = "python -m venv .venv"

# 3. Create a variable called activate_venv_command
#    and set it to the PowerShell command used to activate a virtual environment
activate_venv_command = ".\.venv\Scripts\Activate.ps1"

# 4. Create a variable called safe_install_habit
#    and set it to one safe habit for installing packages
safe_install_habit = "Install only packages the project actually needs."

# 5. Print all four values with clear labels
print(f"Virtual environment meaning: {virtual_environment_meaning}")
print(f"Create virtual environment command: {create_venv_command}")
print(f"Activate virtual environment command: {activate_venv_command}")
print(f"Safe install habit: {safe_install_habit}")

# 6. Print one sentence explaining why a messy global Python environment can be a problem
print(f"A messy global environment can make it hard to know which packages a project really depends on.")