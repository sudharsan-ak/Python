print(f"{'-' * 30} Topic 3: List/String/Dictionary Misuse {'-' * 30}")

# ------------------------------------------------------------
# Exercise 1
# The broken line tries to access a list using a string key.

skills = ["Python", "React", "Node.js"]

# first_skill = skills["first"]

# Fix it by accessing the first skill correctly.
# Print first_skill.
first_skill = skills[0]
print(f"First skill: {first_skill}")

# ------------------------------------------------------------
# Exercise 2
# The broken line tries to access a string using a string key.

language = "Python"

# first_letter = language["first"]

# Fix it by accessing the first letter correctly.
# Print first_letter.
first_letter = language[0]
print(f"First letter: {first_letter}")

# ------------------------------------------------------------
# Exercise 3
# The broken line tries to access a list of dictionaries like it is one dictionary.

students = [
    {"name": "Sudharsan", "score": 90},
    {"name": "Alex", "score": 85}
]

# first_student_name = students["name"]

# Fix it by first accessing the first dictionary, then the "name" key.
# Print first_student_name.
first_student_name = students[0]["name"]
print(f"First student name: {first_student_name}")

# ------------------------------------------------------------
# Exercise 4
# The broken line tries to call a dictionary like a function.

profile = {
    "name": "Sudharsan",
    "role": "Software Engineer",
    "city": "Dallas"
}

# user_role = profile("role")

# Fix it by using the correct dictionary access pattern.
# Print user_role.
user_role = profile["role"]
print(f"User role: {user_role}")

# ------------------------------------------------------------
# Exercise 5
# This one is slightly different.
# The broken line may not give a TypeError.
# Read it and answer in comments what error you expect and why.

course = {
    "name": "Python from Scratch",
    "status": "In Progress"
}

# course_day = course["day"]

# In comments below, answer:
# 1. What error do you expect?
# 2. Why is this not the same as using the wrong index type?
# 3. Fix it using get() with a fallback value of "Not provided".
# Print course_day.

# Answers:
# 1. KeyError, since "day" is not a key in course dictionary.
# 2. This error occurs because the key is not present in the dictionary, not because of wrong index type.
course_day = course.get("day", "Not provided")
print(f"Course day: {course_day}")

# ------------------------------------------------------------
# Exercise 6
# Choose the correct access pattern.

projects = [
    {
        "title": "Portfolio Website",
        "tech_stack": ["React", "TypeScript", "Supabase"]
    },
    {
        "title": "Jobflow Automator",
        "tech_stack": ["Node.js", "Playwright", "PostgreSQL"]
    }
]

# Print the title of the second project.
# Print the first technology from the first project's tech_stack.
print(f"Second project title: {projects[1]['title']}")
print(f"First technology from first project: {projects[0]['tech_stack'][0]}")