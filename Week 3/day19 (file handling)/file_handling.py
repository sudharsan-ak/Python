# ---------------------------------------------------------------------
# Topic 1 - File handling basics, paths, open(), and with open()

print(f"{'-' * 30} Topic 1 {'-' * 30}")

# 1. Create a variable called file_name and store "day19_topic1.txt".
# Use with open(...) to open it in write mode and write this exact text:
# "Learning file handling basics in Python."
file_name = "day19_topic1.txt"
with open(file_name, "w") as file:
    file.write("Learning file handling basics in Python.")

# 2. After the with block, print a confirmation that includes the file name.
print(f"File '{file_name}' created successfully.")

# 3. Create variables for read mode and write mode.
# Then print one sentence explaining what "r" does and one warning about what "w" does.
read_mode = "r"
write_mode = "w"
print(f"Read mode '{read_mode}' reads an existing file.")
print(f"Write mode '{write_mode}' writes to a file and overwrites existing content.")

# ---------------------------------------------------------------------
# Topic 2 - Reading files: full content vs line by line

print(f"{'-' * 30} Topic 2 {'-' * 30}")

# 1. Use the same file_name from Topic 1.
# Open it in read mode and read the full content into a variable called full_content.
# Print the full content with a clear label.
with open(file_name, "r") as file:
    full_content = file.read()

print(f"Full content of '{file_name}':\n{full_content}")

# 2. Print the length of full_content with a clear label.
print(f"Length of full content: {len(full_content)}")

# 3. Open the same file again in read mode.
# Loop through the file line by line and print each cleaned line using strip().
with open(file_name, "r") as file:
    for line in file:
        print(line.strip())

# ---------------------------------------------------------------------
# Topic 3 - Writing and appending files with w and a

print(f"{'-' * 30} Topic 3 {'-' * 30}")

# 1. Create a variable called log_file and store "day19_topic3_log.txt".
# Open it in write mode and write three starter log lines.
# Each line should end with \n so the file has separate lines.
log_file = "day19_topic3_log.txt"
with open(log_file, "w") as file:
    file.write("This is the first log line.\n")
    file.write("This is the second log line.\n")
    file.write("This is the third log line.\n")

# 2. Open the same file in append mode and add two more log lines.
# Again, make sure each appended line starts or ends cleanly on its own line.
with open(log_file, "a") as file:
    file.write("This is the fourth log line.\n")
    file.write("This is the fifth log line.\n")

# 3. Open the same file in read mode, read the full content, and print it with a clear label.
with open(log_file, "r") as file:
    full_content = file.read()

print(f"Full content of '{log_file}':\n{full_content}")

# ---------------------------------------------------------------------
# Topic 4 - Safe file handling habits and practical patterns

print(f"{'-' * 30} Topic 4 {'-' * 30}")

# 1. Create a variable called missing_file and store "missing_notes.txt".
# Try to open it in read mode using with open(..., encoding="utf-8").
# Handle FileNotFoundError and print a clear message if the file is missing.
missing_file = "missing_notes.txt"

try:
    with open(missing_file, "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print(f"File '{missing_file}' not found.")
else:
    print(f"Content of '{missing_file}':\n{content}")

# 2. Create a variable called safe_notes_file and store "day19_topic4_notes.txt".
# Open it in append mode and add one note line.
# The note should end with \n.
safe_notes_file = "day19_topic4_notes.txt"

with open(safe_notes_file, "a", encoding="utf-8") as file:
    file.write("This is a safe note.\n")

# 3. Open safe_notes_file in read mode, read the full content, and print it with a clear label.
with open(safe_notes_file, "r", encoding="utf-8") as file:
    full_content = file.read()
    
print(f"Full content of '{safe_notes_file}':\n{full_content}")