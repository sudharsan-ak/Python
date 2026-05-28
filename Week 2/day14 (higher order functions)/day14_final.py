# Day 14 - Final Mixed Exercise
# Scenario: Python study task analyzer

print(f"{'-' * 30} Day 14 Final Mixed Exercise {'-' * 30}")

# 1. Import reduce from functools
from functools import reduce

# 2. Create a function called apply_formatter
# It should accept two parameters:
# formatter
# text
# Inside the function:
# - call formatter(text)
# - return the result
def apply_formatter(formatter, text):
    return formatter(text)

# 3. Call apply_formatter with an inline lambda
# The lambda should strip the text and convert it to title case
# Pass "   higher order functions   "
# Store the result in formatted_topic
# Print: Formatted topic: <value>
formatted_topic = apply_formatter(lambda text: text.strip().title(), "   higher order functions   ")
print(f"Formatted topic: {formatted_topic}")

# 4. Create a list called study_minutes with values:
# 25, 40, 30, 50, 15
study_minutes = [25, 40, 30, 50, 15]

# 5. Use map() with a lambda to create doubled_minutes
# Each value should be multiplied by 2
# Convert the result to a list
# Print: Doubled minutes: <list>
doubled_minutes = list(map(lambda number: number * 2, study_minutes))
print(f"Doubled minutes: {doubled_minutes}")

# 6. Use filter() with a lambda to create long_sessions
# Keep only study sessions greater than or equal to 30 minutes
# Convert the result to a list
# Print: Long sessions: <list>
long_sessions = list(filter(lambda number: number >= 30, study_minutes))
print(f"Long sessions: {long_sessions}")

# 7. Use reduce() with a lambda to create total_minutes
# Add all study_minutes together
# Print: Total minutes: <value>
total_minutes = reduce(lambda accumulator, number: accumulator + number, study_minutes)
print(f"Total minutes: {total_minutes}")

# 8. Also calculate the total using sum()
# Store the result in total_minutes_with_sum
# Print: Total minutes with sum: <value>
total_minutes_with_sum = sum(study_minutes)
print(f"Total minutes with sum: {total_minutes_with_sum}")

# 9. Create a list called topics with values:
# "lambda", "map", "filter", "reduce", "sorting"
topics = ["lambda", "map", "filter", "reduce", "sorting"]

# 10. Use map() with a lambda to create topic_labels
# Each label should look like:
# Topic: Lambda
# Convert the result to a list
# Print: Topic labels: <list>
topic_labels = list(map(lambda topic: f"Topic: {topic.title()}", topics))
print(f"Topic labels: {topic_labels}")

# 11. Use filter() with a lambda to create short_topics
# Keep only topics whose length is less than or equal to 6
# Convert the result to a list
# Print: Short topics: <list>
short_topics = list(filter(lambda topic: len(topic) <= 6, topics))
print(f"Short topics: {short_topics}")

# 12. Create a list called task_scores with these dictionaries:
# {"task": "callbacks", "score": 82, "minutes": 25}
# {"task": "lambda", "score": 90, "minutes": 20}
# {"task": "map/filter", "score": 88, "minutes": 35}
# {"task": "reduce", "score": 75, "minutes": 30}
# {"task": "sorting", "score": 92, "minutes": 40}
task_scores = [
    {"task": "callbacks", "score": 82, "minutes": 25},
    {"task": "lambda", "score": 90, "minutes": 20},
    {"task": "map/filter", "score": 88, "minutes": 35},
    {"task": "reduce", "score": 75, "minutes": 30},
    {"task": "sorting", "score": 92, "minutes": 40}
]

# 13. Use sorted() with a lambda and reverse=True
# Sort task_scores by score from highest to lowest
# Store the result in tasks_by_score
# Print: Tasks by score: <list>
tasks_by_score = sorted(task_scores, key=lambda task: task["score"], reverse=True)
print(f"Tasks by score: {tasks_by_score}")

# 14. Create a normal function called get_task_minutes
# It should accept one parameter called task
# It should return task["minutes"]
def get_task_minutes(task):
    return task["minutes"]

# 15. Use sorted() with get_task_minutes
# Sort task_scores by minutes from lowest to highest
# Store the result in tasks_by_minutes
# Print: Tasks by minutes: <list>
tasks_by_minutes = sorted(task_scores, key=get_task_minutes)
print(f"Tasks by minutes: {tasks_by_minutes}")

# 16. Use reduce() with a lambda and an initial value of 0
# Calculate the total minutes from task_scores
# Store the result in total_task_minutes
# Print: Total task minutes: <value>
total_task_minutes = reduce(lambda accumulator, task: accumulator + task["minutes"], task_scores, 0)
print(f"Total task minutes: {total_task_minutes}")

# 17. Create a list comprehension called passing_task_names
# Keep only tasks with score greater than or equal to 80
# Store only the task name, converted to title case
# Print: Passing task names: <list>
passing_task_names = [task["task"].title() for task in task_scores if task["score"] >= 80]
print(f"Passing task names: {passing_task_names}")

# 18. Add two comments:
# - One explaining when lambda is okay
# - One explaining when def is better
# Use inline lambda if the logic is tiny and not re-used
# Use def if the logic is longer with multiple conditions, re-used and can grow over time 