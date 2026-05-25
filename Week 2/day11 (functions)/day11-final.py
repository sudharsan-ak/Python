# ---------------------------------------------------------------------
# Day 11 - Final Mixed Exercise: Functions
# Scenario: Python course progress report

# 1. Create a function called print_report_header
# It should print: Python Course Progress Report
def print_report_header():
    print("Python Course Progress Report")

# 2. Call print_report_header
print_report_header()

# 3. Create a function called get_student_name
# It should return your full name
def get_student_name():
    return "Sudharsan Srinivasan"

# 4. Store the returned value in a variable called student_name
student_name = get_student_name()

# 5. Create a function called show_student
# It should accept one parameter called name
# It should print: Student: <name>
def show_student(name):
    print(f"Student: {name}")

# 6. Call show_student using student_name
show_student(student_name)

# 7. Create a function called calculate_total_minutes
# It should accept any number of minutes using *minutes
# It should return the total using a loop, not sum()
def calculate_total_minutes(*minutes):
    total = 0
    for minute in minutes:
        total += minute
    return total

# 8. Call calculate_total_minutes with 30, 45, 60
# Store the returned value in a variable called total_minutes
total_minutes = calculate_total_minutes(30, 45, 60)

# 9. Print total_minutes with this format:
# Total study minutes: 135
print(f"Total study minutes: {total_minutes}")

# 10. Create a function called show_day_status
# It should accept:
# day
# topic with default value "Functions"
# status with default value "In progress"
# It should print:
# Day: <day>
# Topic: <topic>
# Status: <status>
def show_day_status(day, topic="Functions", status="In progress"):
    print(f"Day: {day}\nTopic: {topic}\nStatus: {status}")

# 11. Call show_day_status using keyword arguments:
# day=11
# status="Final practice"
show_day_status(day=11, status="Final practice")

# 12. Create a function called get_completed_topics
# It should return this list:
def get_completed_topics():
    return ["Function basics", "Return values", "Parameters", "Default arguments", "*args", "Callbacks"]

# 13. Store the returned list in a variable called completed_topics
completed_topics = get_completed_topics()

# 14. Create a function called print_topics
# It should accept one parameter called topics
# It should loop through topics and print each one with this format:
# Completed topic: <topic>
def print_topics(topics):
    for topic in topics:
        print(f"Completed topic: {topic}")

# 15. Call print_topics using completed_topics
print_topics(completed_topics)

# 16. Create a function called is_ready_for_review
# It should accept one parameter called topic_count
# It should return True if topic_count is greater than or equal to 6
# Otherwise, return False
def is_ready_for_review(topic_count):
    return topic_count >= 6

# 17. Create a function called run_check
# It should accept two parameters: check_function and value
# It should return check_function(value)
def run_check(check_function, value):
    return check_function(value)

# 18. Call run_check with is_ready_for_review and len(completed_topics)
# Store the returned value in a variable called ready_for_review
ready_for_review = run_check(is_ready_for_review, len(completed_topics))

# 19. Print ready_for_review with this format:
# Ready for review: True
print(f"Ready for review: {ready_for_review}")