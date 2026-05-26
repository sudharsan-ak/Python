# Topic 5: datetime, os, and sys awareness

# 1. Import the datetime module
import datetime

# 2. Import the os module
import os

# 3. Import the sys module
import sys

# 4. Use datetime.datetime.now()
# Store the result in a variable called current_datetime
current_datetime = datetime.datetime.now()

# 5. Print current_datetime with this format:
# Current datetime: <current_datetime>
print(f"Current datetime: {current_datetime}")

# 6. Print the current year using current_datetime.year with this format:
# Current year: <year>
print(f"Current year: {current_datetime.year}")

# 7. Print the current month using current_datetime.month with this format:
# Current month: <month>
print(f"Current month: {current_datetime.month}")

# 8. Print the current day using current_datetime.day with this format:
# Current day: <day>
print(f"Current day: {current_datetime.day}")

# 9. Use os.getcwd()
# Store the result in a variable called current_folder
current_folder = os.getcwd()

# 10. Print current_folder with this format:
# Current folder: <current_folder>
print(f"Current folder: {current_folder}")

# 11. Store sys.version in a variable called python_version
python_version = sys.version

# 12. Print python_version with this format:
# Python version: <python_version>
print(f"Python version: {python_version}")

# 13. Store sys.platform in a variable called platform_name
platform_name = sys.platform

# 14. Print platform_name with this format:
# Platform: <platform_name>
print(f"Platform: {platform_name}")

# 15. Print the type of current_datetime with this format:
# Current datetime type: <type>
print(f"Current datetime type: {type(current_datetime)}")

# 16. Print the type of current_folder with this format:
# Current folder type: <type>
print(f"Current folder type: {type(current_folder)}")