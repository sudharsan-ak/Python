# ---------------------------------------------------------------------
# Day 20 - Final Mixed Exercise: Python Package Manager
# Scenario: Project setup checklist for a small API helper project

print(f"{'-' * 30} Day 20 Final Exercise {'-' * 30}")

# 1. Create these variables:
# project_name -> "API Helper Tool"
# built_in_module -> "datetime"
# external_package -> "requests"
# package_manager -> "pip"
project_name = "API Helper Tool"
built_in_module = "datetime"
external_package = "requests"
package_manager = "pip"

# 2. Print a short project setup summary using the variables
print(f"Project Summary:")
print(f"Project name: {project_name}")
print(f"Built-in module: {built_in_module}")
print(f"External package: {external_package}")
print(f"Package manager: {package_manager}")

# 3. Create these command variables:
# install_command -> command to install requests
# check_command -> command to list installed packages
# show_command -> command to show details for requests
# uninstall_command -> command that would uninstall requests
install_command = "python -m pip install requests"
check_command = "python -m pip list"
show_command = "python -m pip show requests"
uninstall_command = "python -m pip uninstall requests"

# 4. Print all command variables with clear labels
print(f"Install command: {install_command}")
print(f"Check command: {check_command}")
print(f"Show command: {show_command}")
print(f"Uninstall command: {uninstall_command}")

# 5. Create these requirements-related variables:
# requirements_file -> "requirements.txt"
# dependency_line -> "requests==2.33.1"
# install_from_requirements_command -> command to install from requirements.txt
requirements_file = "requirements.txt"
dependency_line = "requests==2.33.1"
install_from_requirements_command = "python -m pip install -r requirements.txt"

# 6. Print a sentence explaining what requirements.txt is for
print(f"{requirements_file} is for letting other developers install all packages listed inside the text file")

# 7. Print the dependency line and install-from-requirements command with clear labels
print(f"Dependency line: {dependency_line}")
print(f"Install from requirements command: {install_from_requirements_command}")

# 8. Create these virtual environment variables:
# create_venv_command -> "python -m venv .venv"
# activate_venv_command -> use a raw string for the PowerShell activation command
create_venv_command = "python -m venv .venv"
activate_venv_command = r".\.venv\Scripts\Activate.ps1"

# 9. Print both virtual environment commands with clear labels
print(f"Create virtual environment command: {create_venv_command}")
print(f"Activate virtual environment command: {activate_venv_command}")

# 10. Print three final checklist lines:
# - one line explaining the difference between installing and importing
# - one line explaining why we should not blindly run pip freeze in a messy environment
# - one line explaining why uninstalling requests could break this project
print(f"installing a package makes that package available for the python environment, importing allows python to use that package during runtime")
print(f"Blindly running pip freeze may dump a giant messy list of packages that our file might not actually need.")
print(f"If the current file uses the package requests, uninstalling it can break the code")