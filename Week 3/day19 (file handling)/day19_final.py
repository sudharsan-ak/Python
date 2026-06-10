# ---------------------------------------------------------------------
# Day 19 - Final Mixed Exercise: File Handling
# Scenario: Support shift handoff log

print(f"{'-' * 30} Day 19 Final {'-' * 30}")

# 1. Create a file called "shift_handoff_log.txt".
# Use write mode to add three starting support log lines.
# Each line should end cleanly with \n.
file_name = "shift_handoff_log.txt"
with open(file_name, "w") as file:
    file.write("09:00 - Login issue resolved\n")
    file.write("09:30 - User logged in\n")
    file.write("10:00 - User logged out\n")

# Example line style:
# "09:00 - Login issue resolved"

# 2. Reopen the same file in append mode.
# Add two more handoff log lines without deleting the existing ones.
with open(file_name, "a") as file:
    file.write("10:30 - User logged in\n")
    file.write("11:00 - User logged out\n")

# 3. Open the log file in read mode and read the full content.
# Print it with a clear label.
with open(file_name, "r") as file:
    full_content = file.read()

print(f"Full content of '{file_name}':\n{full_content}")

# 4. Open the same log file again and read it line by line.
# Print each cleaned line with a human-friendly line number.
# Example:
# 1. 09:00 - Login issue resolved
with open(file_name, "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}. {line.strip()}")

# 5. Try to read a file called "archived_shift_log.txt".
# Handle FileNotFoundError and print a clear message if it does not exist.
try:
    with open("archived_shift_log.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File 'archived_shift_log.txt' not found.")
else:
    print(f"Content of 'archived_shift_log.txt':\n{content}")

# 6. Create a summary file called "shift_summary.txt".
# Write a short summary that includes:
# - the log file name
# - the total number of log lines from shift_handoff_log.txt
# - a final status message like "Shift handoff summary created."
summary_file = "shift_summary.txt"
with open(summary_file, "w") as file:
    file.write(f"Shift handoff log file: {file_name}\n")
    file.write(f"Total number of log lines: {len(full_content.splitlines())}\n")
    file.write(f"Shift handoff summary created.")