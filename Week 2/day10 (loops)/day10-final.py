# ---------------------------------------------------------------------
# Day 10 - Final Mixed Exercise: Loops
# Scenario: Python bootcamp progress tracker

# 1. Create a list called completed_topics with:
# "Dictionaries", "Conditionals", "For loops", "While loops", "Nested loops"
completed_topics = ["Dictionaries", "Conditionals", "For loops", "While loops", "Nested loops"]

# 2. Use a for loop to print each completed topic with this format:
# Completed: Dictionaries
# Completed: Conditionals
# etc.
for topic in completed_topics:
    print(f"Completed: {topic}")

# 3. Use range() to print study sessions from 1 to 4:
# Study session 1
# Study session 2
# Study session 3
# Study session 4
for session in range(1, 5):
    print(f"Study session {session}")

# 4. Create a dictionary called topic_scores with:
# "Dictionaries" -> 85
# "Conditionals" -> 90
# "Loops" -> 88
topic_scores = {
    "Dictionaries": 85,
    "Conditionals": 90,
    "Loops": 88
}

# 5. Loop through topic_scores.items() and print each topic and score:
# Dictionaries: 85
# Conditionals: 90
# Loops: 88
for topic, score in topic_scores.items():
    print(f"{topic}: {score}")


# 6. Inside a loop over topic_scores.items():
# If the score is greater than or equal to 90, print "{topic} is excellent"
# Otherwise, print "{topic} is cleared"
for topic, score in topic_scores.items():
    if score >= 90:
        print(f"{topic} is excellent")
    else:
        print(f"{topic} is cleared")

# 7. Create a list called practice_tasks with:
# "review notes", "solve exercises", "take break", "final review"
practice_tasks = ["review notes", "solve exercises", "take break", "final review"]

# 8. Loop through practice_tasks.
# If the task is "take break", skip it using continue.
# Print every other task with this format:
# Task: review notes
for task in practice_tasks:
    if task == "take break":
        continue
    print(f"Task: {task}")

# 9. Create a list called required_topics with:
# "Variables", "Lists", "Loops", "Functions"
required_topics = ["Variables", "Lists", "Loops", "Functions"]

# 10. Use a for loop with else to search for "Loops".
# If found, print "Loops found in required topics" and stop using break.
# If not found, print "Loops not found"
for topic in required_topics:
    if topic == "Loops":
        print("Loops found in required topics")
        break
else:
    print("Loops not found")

# 11. Create a variable called attempt and set it to 1.
attempt = 1

# 12. Use a while loop that runs while attempt is less than or equal to 3.
# Print "Quiz attempt 1", "Quiz attempt 2", etc.
# If attempt equals 2, print "Quiz passed" and stop using break.
# Add an else block that prints "Quiz not passed".
# Remember: if break happens, else should not run.
while attempt <= 3:
    print(f"Quiz attempt {attempt}")
    if attempt == 2:
        print("Quiz passed")
        break
    attempt += 1
else:
    print("Quiz not passed")

# 13. Create a variable called points and set it to 0.
points = 0

# 14. Use a while loop to keep adding 20 to points while points is less than 100.
# Print the points after each update:
# Points: 20
# Points: 40
# etc.
while points < 100:
    points += 20
    print(f"Points: {points}")

# 15. Create a dictionary called weekly_plan with:
# "Day 8" -> ["Dictionaries", "Nested dictionaries"]
# "Day 9" -> ["Conditionals", "Truthy/falsy"]
# "Day 10" -> ["For loops", "While loops", "Break and continue"]
weekly_plan = {
    "Day 8": ["Dictionaries", "Nested dictionaries"],
    "Day 9": ["Conditionals", "Truthy/falsy"],
    "Day 10": ["For loops", "While loops", "Break and continue"]
}

# 16. Use a nested loop to print each day and its topics:
# Day 8:
# - Dictionaries
# - Nested dictionaries
# Day 9:
# - Conditionals
# - Truthy/falsy
# etc.
for day, topics in weekly_plan.items():
    print(f"{day}:")
    for topic in topics:
        print(f"- {topic}")