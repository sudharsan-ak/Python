# Day 19 Notes - File Handling

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 19 focused on basic file handling: reading, writing, appending, and handling missing files safely.

Core idea:

```text
Use file handling when a program needs to read saved content or save output beyond the current program run.
```

---

# Topic 1 - File handling basics, paths, `open()`, and `with open(...)`

## File handling

File handling lets Python work with files on your computer, such as notes, logs, reports, and saved summaries.

A simple file name like this:

```python
file_name = "notes.txt"
```

means Python looks for the file in the folder where the script is running.

Beginner path rule:

```text
Keep files in the same folder first.
Do not overcomplicate paths too early.
```

## `with open(...)`

Manual open and close works:

```python
file = open("notes.txt", "w")
file.write("Hello")
file.close()
```

Better default:

```python
with open("notes.txt", "w") as file:
    file.write("Hello")
```

`with open(...)` automatically closes the file after the block ends.

## Main file modes

```text
"r" -> read an existing file
"w" -> write to a file; overwrites existing content when opened
"a" -> append to the end of a file
```

Important:

```text
"r" needs the file to exist.
"w" can create a file, but resets existing content.
"a" can create a file and adds to existing content.
```

---

# Topic 2 - Reading files

## Read the full file

Use `read()` when the file is small and you want the whole content as one string.

```python
with open(file_name, "r") as file:
    full_content = file.read()
```

After reading, normal string tools work:

```python
len(full_content)
full_content.splitlines()
```

## Read line by line

Use a file loop when you want to process one line at a time.

```python
with open(file_name, "r") as file:
    for line in file:
        print(line.strip())
```

`strip()` removes extra whitespace, including newline characters.

Beginner reading guide:

```text
Need whole file? use read().
Need one line at a time? loop through the file.
```

---

# Topic 3 - Writing and appending files

## Write mode

```python
with open("report.txt", "w") as file:
    file.write("Line one\n")
```

Write mode creates the file if it does not exist.

If the file already exists, `"w"` overwrites the old content when the file is opened.

Important distinction:

```text
Opening with "w" resets the file.
Multiple write() calls inside the same open block continue from the current file position.
```

## Newline habit

`write()` does not add a new line automatically.

Use `\n` when separate lines are needed:

```python
file.write("Line one\n")
file.write("Line two\n")
```

## Append mode

```python
with open("report.txt", "a") as file:
    file.write("Another line\n")
```

Append mode adds to the end of the file instead of deleting existing content.

Use append mode for logs, notes, history, and activity records.

---

# Topic 4 - Safe file handling habits

## `encoding="utf-8"`

`utf-8` tells Python how to read and write normal modern text.

Plain meaning:

```text
Files store bytes.
Encoding tells Python how to turn those bytes into readable characters.
UTF-8 handles regular English text, many languages, symbols, and emojis.
```

Good habit:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

## Missing files

Reading a missing file raises `FileNotFoundError`.

```python
try:
    with open("missing_notes.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print(content)
```

Use `try / except` for expected risky reads, not around every file operation by default.

## Safe beginner habits

```text
Use with open(...) by default.
Use "r" only when the file should already exist.
Use "w" only when replacing content is intended.
Use "a" when adding to existing content.
Use \n when writing multiple lines.
Use encoding="utf-8" for normal text files when practical.
Handle FileNotFoundError when reading uncertain files.
Keep try blocks focused on the risky operation.
```

---

# Final mixed exercise summary

Final scenario:

```text
Support shift handoff log
```

Practiced:

```text
writing a starter log file
appending more log lines
reading full file content
reading line by line with numbering
handling a missing archive file
creating a summary file
counting file lines with splitlines()
```

Final result:

```text
Day 19 final mixed exercise cleared.
```

---

# Mistakes and corrections from Day 19

Important corrections:

```text
Opening a file with "w" resets existing content once, when the file is opened.
Multiple write() calls inside the same open block keep adding from the current position.
write() does not automatically add new lines.
Use \n when each written item should appear on its own line.
Append mode keeps adding content and can duplicate lines if the script is run repeatedly.
Reading a missing file in "r" mode raises FileNotFoundError.
Use with open(...) instead of manual close() for beginner-safe file handling.
Use encoding="utf-8" as a good text-file habit.
```

---

# Day 19 status

```text
Day 19 - File Handling: Cleared
Week 3 Day 5: Cleared
Next: Day 20 - Python Package Manager
```

## What to remember before Day 20

```text
Use with open(...) as the default file pattern.
Choose file mode intentionally.
Do not use "w" unless overwriting is okay.
Use "a" when adding to existing file content.
Use read() for full content and a file loop for line-by-line processing.
Handle missing files with FileNotFoundError when the file may not exist.
```
