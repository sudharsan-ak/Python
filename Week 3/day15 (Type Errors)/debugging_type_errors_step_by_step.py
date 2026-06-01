print(f"{'-' * 30} Topic 5: Debugging Type Errors Step by Step {'-' * 30}")

# ------------------------------------------------------------
# Exercise 1 - Read the traceback mentally
# Broken code:
user_age = 30
# message = "User age next year: " + user_age + 1
#
# In comments, answer:
# 1. Which operation will fail first?
# 2. Why is this not just a simple display issue?
# 3. What is the correct fixed version if the goal is:
#    User age next year: 31
# 
# Answers: 
# 1. The string concatenation will fail first. 
# 2. This is not a simple display issue because we are trying to concatenate a string and an integer.
# 3. The correct fix can be done in either of the two ways. 
# Method 1: Use a f string and add one to the age inline.
# Method 2: create a new variable, add and store the user age first, then use the updated variable and f string to display the final message.

# Then write the fixed code and print the message.
print(f"User age next year: {user_age + 1}")

# ------------------------------------------------------------
# Exercise 2 - Inspect types before fixing
# A value came from user input, so it is text.

hours_studied = "6"
extra_hours = 2

# broken_total_hours = hours_studied + extra_hours

# Step 1: Print the type of hours_studied.
# Step 2: Print the type of extra_hours.
# Step 3: Fix total_hours so it becomes the number 8.
# Step 4: Print total_hours.

print(f"Type of hours_studied: {type(hours_studied)}")
print(f"Type of extra_hours: {type(extra_hours)}")
total_hours = int(hours_studied) + extra_hours
print(f"Total hours: {total_hours}")

# ------------------------------------------------------------
# Exercise 3 - Fix the root cause, not just the crash line

# def get_completed_days():
#     completed_days = 15

# broken_days = get_completed_days()
# print(broken_days + 1)

# Step 1: In comments, explain where None is coming from.
# Step 2: Fix the function so it returns the value.
# Step 3: Store the returned value in completed_days.
# Step 4: Print completed_days + 1.

# Answers : None comes from the function call, because the function is not returning anything.

def get_completed_days():
    return 15

completed_days = get_completed_days()
print(f"Completed days: {completed_days + 1}")

# ------------------------------------------------------------
# Exercise 4 - Mixed data problem
# This list has mixed types.

scores = [80, "90", 75, "85"]

# broken_total = sum(scores)

# Step 1: In comments, explain why sum(scores) fails.
# Step 2: Create a new list called cleaned_scores.
# Step 3: Convert only the string numbers into integers.
# Step 4: Print cleaned_scores.
# Step 5: Print the total score.

# Answers: Sum fails because the scores list has unsupported operand type(s). 
# The operation expects a list of integers, but the list also contains strings.
cleaned_scores = [int(score) if isinstance(score, str) else score for score in scores]
print(f"Cleaned scores: {cleaned_scores}")
total_score = sum(cleaned_scores)
print(f"Total score: {total_score}")

# ------------------------------------------------------------
# Exercise 5 - Method returns None

topics = ["loops", "functions", "type errors"]

# broken_upper_topics = topics.append("debugging")
# print(broken_upper_topics)

# Step 1: In comments, explain why broken_upper_topics becomes None.
# Step 2: Append "debugging" correctly.
# Step 3: Create a new list called title_topics where each topic is title-cased.
# Step 4: Print title_topics.

# Answers: broken_upper_topics becomes None because list.append() changes the original list in place and returns None. It does not return the updated list.
topics.append("debugging")
title_topics = [topic.title() for topic in topics]
print(f"Title topics: {title_topics}")

# ------------------------------------------------------------
# Exercise 6 - Nested data debugging

course_progress = {
    "student": "Sudharsan",
    "week": 3,
    "stats": {
        "completed_days": "15",
        "practice_files": 5
    }
}

# broken_total_work = course_progress["completed_days"] + course_progress["practice_files"]

# Step 1: In comments, explain the first mistake in the broken line.
# Step 2: Access completed_days from the nested stats dictionary.
# Step 3: Access practice_files from the nested stats dictionary.
# Step 4: Convert completed_days to int.
# Step 5: Print total_work.

# Answer: "completed_days" and later "practice_files" is not a top level key inside course_progress dictionary, hence the access fails.
completed_days = int(course_progress["stats"]["completed_days"])
practice_files = course_progress["stats"]["practice_files"]
total_work = completed_days + practice_files
print(f"Total work: {total_work}")

# ------------------------------------------------------------
# Exercise 7 - Choose the correct fix
# The goal is to display a clean summary sentence.

student = {
    "name": "Sudharsan",
    "days_completed": 15,
    "current_topic": "Type Errors"
}

# broken_summary = student["name"] + " completed " + student["days_completed"] + " days and is learning " + student["current_topic"]

# Step 1: In comments, explain why converting everything with str() would work but is not the cleanest fix.
# Step 2: Fix it using an f-string.
# Step 3: Print the summary.

# Answers: Converting everything with str() works, but it becomes messy and tough to follow. Cleaner fix is to use an f-string and concatenate easily.
fixed_summary = f"{student['name']} completed {student['days_completed']} days and is learning {student['current_topic']}"
print(f"Fixed summary: {fixed_summary}")