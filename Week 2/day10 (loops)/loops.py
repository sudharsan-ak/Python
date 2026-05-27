# ---------------------------------------------------------------------
# Topic 1 Exercise: Basic for loops with strings and lists
print(f"{"-" * 30}Topic 1{"-" * 30}")
# 1. Create a list called languages with:
# "JavaScript", "Python", "TypeScript", "React"
languages = ["JavaScript", "Python", "TypeScript", "React"]

# 2. Use a for loop to print each language with this format:
# Language: JavaScript
# Language: Python
# etc.
for language in languages:
    print(f"Language: {language}")

# 3. Create a variable called favorite_language and set it to "Python"
favorite_language = "Python"

# 4. Use a for loop to print each letter in favorite_language
for letter in favorite_language:
    print(letter)

# 5. Create a list called projects with:
# "Portfolio", "Jobflow Automator", "Event Management"
projects = ["Portfolio", "Jobflow Automator", "Event Management"]

# 6. Use a for loop to print each project with this format:
# Project: Portfolio
# Project: Jobflow Automator
# etc.
for project in projects:
    print(f"Project: {project}")

# 7. Inside a for loop over languages, check:
# If the language is "Python", print "Python is part of my learning path"
# Otherwise, print "{language} is part of my tech stack"
for language in languages:
    if language == "Python":
        print(f"{language} is part of my learning path")
    else:
        print(f"{language} is part of my tech stack")

# 8. Create a list called scores with: 85, 92, 76, 60
scores = [85, 92, 76, 60]

# 9. Use a for loop to print each score with this format:
# Score: 85
# Score: 92
# etc.
for score in scores:
    print(f"Score: {score}")

# ---------------------------------------------------------------------
# Topic 2 Exercise: range() and counting loops
print(f"{"-" * 30}Topic 2{"-" * 30}")
# 1. Use range() to print numbers from 0 to 4
for number in range(5):
    print(number)

# 2. Use range() to print numbers from 1 to 5
print("----Range 1 to 5-----")
for number in range(1, 6):
    print(number)

# 3. Use range() to print even numbers from 2 to 10
print("----Even Numbers----")
for number in range(2, 11, 2):
    print(number)

# 4. Use range() to print numbers from 5 down to 1
print("----Counting backwards--")
for number in range(5, 0, -1):
    print(number)

# 5. Create a list called tasks with:
# "Review notes", "Practice loops", "Submit exercise"
tasks = ["Review notes", "Practice loops", "Submit exercise"]

# 6. Use range(len(tasks)) to print each task with its index:
# 0: Review notes
# 1: Practice loops
# 2: Submit exercise
for index in range(len(tasks)):
    print(f"{index}: {tasks[index]}")

# 7. Create a list called scores with: 90, 82, 75, 60
scores = [90, 82, 75, 60]

# 8. Use range(len(scores)) to print each score with its index:
# Score 0: 90
# Score 1: 82
# etc.
print("----Range scores-----")
for index in range(len(scores)):
    print(f"Score {index}: {scores[index]}")

# 9. Use range(3) to print:
# Loop run 1
# Loop run 2
# Loop run 3
# Hint: range(3) gives 0, 1, 2, so adjust the printed number.
print("----Range 3----")
for number in range(3):
    print(f"Loop run {number + 1}")

# ---------------------------------------------------------------------
# Topic 3 Exercise: Looping through dictionaries
print(f"{"-" * 30}Topic 3{"-" * 30}")

# 1. Create a dictionary called developer_profile with:
# "name" -> "Sudharsan"
# "role" -> "Full Stack Software Engineer"
# "city" -> "Lewisville"
# "experience_years" -> 6
developer_profile = {
    "name": "Sudharsan",
    "role": "Full Stack Software Engineer",
    "city": "Lewisville",
    "experience_years": 6
}

# 2. Use a for loop to print only the keys from developer_profile
print("--------Keys-----------")
for key in developer_profile:
    print(key)

# 3. Use a for loop with .values() to print only the values from developer_profile
print("--------Values-----------")
for value in developer_profile.values():
    print(value)

# 4. Use a for loop with .items() to print both keys and values in this format:
# name: Sudharsan
# role: Full Stack Software Engineer
# etc.
print("---Keys and Values------")
for key, value in developer_profile.items():
    print(f"{key}: {value}")

# 5. Create a dictionary called skill_levels with:
# "JavaScript" -> "Advanced"
# "Python" -> "Beginner"
# "React" -> "Advanced"
# "Node.js" -> "Advanced"
skill_levels = {
    "JavaScript": "Advanced",
    "Python": "Beginner",
    "React": "Advanced",
    "Node.js": "Advanced"
}

# 6. Use a for loop with .items() to print each skill and level in this format:
# JavaScript - Advanced
# Python - Beginner
# etc.
print("---Skill and Levels------")
for skill, level in skill_levels.items():
    print(f"{skill} - {level}")

# 7. Inside a for loop over skill_levels.items():
# If the level is "Advanced", print "{skill} is a strong skill"
# Otherwise, print "{skill} still needs practice"
for skill, level in skill_levels.items():
    if level == "Advanced":
        print(f"{skill} is a strong skill")
    else:
        print(f"{skill} still needs practice")

# 8. Create a dictionary called course_progress with:
# "day" -> 10
# "topic" -> "Loops"
# "status" -> "In progress"
course_progress = {
    "day": 10,
    "topic": "Loops",
    "status": "In progress"
}

# 9. Use a for loop with .items() to print:
# day => 10
# topic => Loops
# status => In progress
print("---Course Progress---")
for key, value in course_progress.items():
    print(f"{key} => {value}")

# ---------------------------------------------------------------------
# Topic 4 Exercise: while loops
print(f"{"-" * 30}Topic 4{"-" * 30}")
# 1. Create a variable called count and set it to 1
count = 1

# 2. Use a while loop to print numbers from 1 to 5
# Expected output:
# 1
# 2
# 3
# 4
# 5
while count <= 5:
    print(count)
    count += 1

# 3. Create a variable called countdown and set it to 5
countdown = 5

# 4. Use a while loop to print numbers from 5 down to 1
# Expected output:
# 5
# 4
# 3
# 2
# 1
print("--Countdown--")
while countdown >= 1:
    print(countdown)
    countdown -= 1

# 5. Create a variable called attempts and set it to 1
attempts = 1

# 6. Use a while loop to print:
# Attempt 1
# Attempt 2
# Attempt 3
# Stop after attempt 3
print("--Attempts--")
while attempts <= 3:
    print(f"Attempt {attempts}")
    attempts += 1

# 7. Create a variable called points and set it to 0
points = 0

# 8. Use a while loop to keep adding 10 to points while points is less than 50
# Print the points after each update
# Expected output:
# Points: 10
# Points: 20
# Points: 30
# Points: 40
# Points: 50
print("--Points--")
while points < 50:
    points += 10
    print(f"Points: {points}")

# 9. Create a variable called is_practicing and set it to True
# Create a variable called practice_count and set it to 1
is_practicing = True
practice_count = 1

# 10. Use a while loop that runs while is_practicing is True
# Print "Practice round 1", "Practice round 2", etc.
# When practice_count equals 3, set is_practicing to False
# Remember to still update practice_count so your loop is clean
print("--Practice--")
while is_practicing:
    print(f"Practice round {practice_count}")
    if practice_count == 3:
        is_practicing = False
    practice_count += 1

# ---------------------------------------------------------------------
# Topic 5 Exercise: break and continue
print(f"{"-" * 30}Topic 5{"-" * 30}")
# 1. Create a list called languages with:
# "JavaScript", "TypeScript", "Python", "React", "Node.js"
languages = ["JavaScript", "TypeScript", "Python", "React", "Node.js"]

# 2. Use a for loop to print each language.
# If the language is "Python", print "Found Python - stopping loop" and stop the loop using break.
print("---Languages---")
for language in languages:
    if language == "Python":
        print("Found Python - stopping loop")
        break
    print(language)

# 3. Create a list called tools with:
# "VS Code", "Docker", "Postman", "Git", "Jira"
tools = ["VS Code", "Docker", "Postman", "Git", "Jira"]

# 4. Use a for loop to print each tool.
# If the tool is "Postman", skip it using continue.
print("---Tools---")
for tool in tools:
    if tool == "Postman":
        continue
    print(tool)

# 5. Use range(1, 8) to print numbers from 1 to 7.
# If the number is 5, stop the loop using break.
print("---Numbers---")
for number in range(1, 8):
    if number == 5:
        break
    print(number)

# 6. Use range(1, 8) to print numbers from 1 to 7.
# If the number is 4, skip it using continue.
print("---Numbers---")
for number in range(1, 8):
    if number == 4:
        continue
    print(number)

# 7. Create a variable called attempt and set it to 1.
attempt = 1

# 8. Use a while loop that runs while attempt is less than or equal to 5.
# Print "Attempt 1", "Attempt 2", etc.
# If attempt equals 3, print "Login successful" and stop the loop using break.
# Remember to update attempt properly.
print("---Attempts---")
while attempt <= 5:
    print(f"Attempt {attempt}")
    if attempt == 3:
        print("Login successful")
        break
    attempt += 1

# 9. Create a variable called count and set it to 1.
count = 1

# 10. Use a while loop to print numbers from 1 to 5.
# Skip number 3 using continue.
# Be careful: update count before continue so you do not create an infinite loop.
print("---Numbers---")
while count <= 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1

# ---------------------------------------------------------------------
# Topic 6 Exercise: loop else
print(f"{"-" * 30}Topic 6{"-" * 30}")
# 1. Create a list called languages with:
# "JavaScript", "TypeScript", "React", "Node.js"
languages = ["JavaScript", "TypeScript", "React", "Node.js"]

# 2. Use a for loop to search for "Python".
# If "Python" is found, print "Python found" and stop the loop using break.
# Add an else block that prints "Python not found".
for language in languages:
    if language == "Python":
        print("Python found")
        break
else:
    print("Python not found")

# 3. Create another list called updated_languages with:
# "JavaScript", "Python", "React"
updated_languages = ["JavaScript", "Python", "React"]

# 4. Use a for loop to search for "Python" in updated_languages.
# If "Python" is found, print "Python found" and stop the loop using break.
# Add an else block that prints "Python not found".
for language in updated_languages:
    if language == "Python":
        print("Python found")
        break
else:
    print("Python not found")

# 5. Create a list called required_skills with:
# "JavaScript", "React", "Python"
required_skills = ["JavaScript", "React", "Python"]

# 6. Use a for loop to search for "Python" in required_skills.
# If found, print "Required skill found" and stop the loop.
# Add an else block that prints "Required skill missing".
for skill in required_skills:
    if skill == "Python":
        print("Required skill found")
        break
else:
    print("Required skill missing")

# 7. Create a variable called attempt and set it to 1.
attempt = 1

# 8. Use a while loop that runs while attempt is less than or equal to 3.
# Print "Attempt 1", "Attempt 2", etc.
# Increase attempt by 1 each time.
# Add an else block that prints "All attempts completed".
while attempt <= 3:
    print(f"Attempt {attempt}")
    attempt += 1
else:
    print("All attempts completed")

# 9. Create a variable called login_attempt and set it to 1.
login_attempt = 1

# 10. Use a while loop that runs while login_attempt is less than or equal to 3.
# Print "Login attempt 1", "Login attempt 2", etc.
# If login_attempt equals 2, print "Login successful" and stop using break.
# Add an else block that prints "Login failed after all attempts".
# Remember: if break happens, else should not run.
while login_attempt <= 3:
    print(f"Login attempt {login_attempt}")
    if login_attempt == 2:
        print("Login successful")
        break
    login_attempt += 1
else:
    print("Login failed after all attempts")

# ---------------------------------------------------------------------
# Topic 7 Exercise: Nested loops
print(f"{"-" * 30}Topic 7{"-" * 30}")
# 1. Create a list called frontend_skills with:
# "HTML", "CSS", "React"
frontend_skills = ["HTML", "CSS", "React"]

# 2. Create a list called backend_skills with:
# "Node.js", "Python"
backend_skills = ["Node.js", "Python"]

# 3. Use a nested for loop to print every frontend/backend pair in this format:
# HTML + Node.js
# HTML + Python
# CSS + Node.js
# etc.
print("---Frontend/Backend---")
for frontend_skill in frontend_skills:
    for backend_skill in backend_skills:
        print(f"{frontend_skill} + {backend_skill}")

# 4. Use nested range() loops to print a 3x3 grid:
# Row 1, Column 1
# Row 1, Column 2
# Row 1, Column 3
# Row 2, Column 1
# etc.
print("---Grid---")
for row in range(3):
    for column in range(3):
        print(f"Row {row + 1}, Column {column + 1}")

# 5. Create a dictionary called learning_plan with:
# "Day 8" -> ["Dictionaries", "Nested dictionaries"]
# "Day 9" -> ["Conditionals", "Truthy/falsy"]
# "Day 10" -> ["For loops", "While loops", "Nested loops"]
learning_plan = {
    "Day 8": ["Dictionaries", "Nested dictionaries"],
    "Day 9": ["Conditionals", "Truthy/falsy"],
    "Day 10": ["For loops", "While loops", "Nested loops"]
}

# 6. Use a loop over learning_plan.items()
# For each day, print the day name first, like:
# Day 8:

# 7. Inside that loop, use another loop to print each topic for that day:
# - Dictionaries
# - Nested dictionaries
# etc.
print("---Learning Plan Topics---")
for day, topics in learning_plan.items():
    print(day + ":")
    for topic in topics:
        print(f"- {topic}")

# 8. Create a list called users with:
# "Admin", "Editor"
users = ["Admin", "Editor"]

# 9. Create a list called permissions with:
# "read", "write", "delete"
permissions = ["read", "write", "delete"]

# 10. Use a nested loop to print every user-permission pair:
# Admin can read
# Admin can write
# Admin can delete
# Editor can read
# etc.
for user in users:
    for permission in permissions:
        print(f"{user} can {permission}")

# ---------------------------------------------------------------------
# Day 10 Addendum Exercise: enumerate()
# 1. Create a list called topics with:
# "Dictionaries", "Conditionals", "Loops", "Functions"
topics = ["Dictionaries", "Conditionals", "Loops", "Functions"]

# 2. Use enumerate() to print each topic with its zero-based index:
# 0: Dictionaries
# 1: Conditionals
# etc.
for index, topic in enumerate(topics):
    print(f"{index}: {topic}")

# 3. Use enumerate(topics, start=1) to print each topic with human-friendly numbering:
# 1. Dictionaries
# 2. Conditionals
# etc.
for index, topic in enumerate(topics, start=1):
    print(f"{index}. {topic}")

# 4. Create a list called scores with:
# 85, 90, 88, 92
scores = [85, 90, 88, 92]

# 5. Use enumerate(scores, start=1) to print:
# Score 1: 85
# Score 2: 90
# etc.
for index, score in enumerate(scores, start=1):
    print(f"Score {index}: {score}")

# 6. Create a list called tasks with:
# "review notes", "practice loops", "fix mistakes", "submit exercise"
tasks = ["review notes", "practice loops", "fix mistakes", "submit exercise"]

# 7. Use enumerate(tasks, start=1).
# If the task is "fix mistakes", print:
# Task 3 needs extra attention
# Otherwise print:
# Task 1: review notes
# Task 2: practice loops
# etc.
for index, task in enumerate(tasks, start=1):
    if task == "fix mistakes":
        print(f"Task {index} needs extra attention")
    else:
        print(f"Task {index}: {task}")
