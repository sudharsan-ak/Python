# Topic 1 helper module
# 1. Create a function called get_student_name
# It should return your full name
def get_student_name():
    return "Sudharsan Srinivasan"

# 2. Create a function called get_current_day
# It should return the number 12
def get_current_day():
    return 12

# 3. Create a function called get_current_topic
# It should return "Modules"
def get_current_topic():
    return "Modules"

# 4. Create a function called build_progress_message
# It should accept three parameters: name, day, topic
# It should return this exact format:
# <name> is learning Day <day> - <topic>
def build_progress_message(name, day, topic):
    return f"{name} is learning Day {day} - {topic}"

# 5. Create a function called print_separator
# It should print 30 hyphens using string multiplication
def print_separator():
    print("-" * 30)

# 6. Create a function called get_course_name
# It should return "Python from Scratch"
def get_course_name():
    return "Python from Scratch"

# 7. Create a function called format_topic_summary
# It should accept two parameters: day and topic
# It should return this exact format:
# Day <day> focus: <topic>
def format_topic_summary(day, topic):
    return f"Day {day} focus: {topic}"

# 8. Create a function called calculate_total_minutes
# It should accept any number of study minute values using *minutes
# It should return the total number of minutes
def calculate_total_minutes(*minutes):
    total = 0
    for minute in minutes:
        total += minute
    return total