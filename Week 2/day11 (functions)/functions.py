# ---------------------------------------------------------------------
# Topic 1 Exercise: Function Basics
print(f"{"-" * 30}Topic 1{"-" * 30}")
# 1. Create a function called welcome_message
# It should print: Welcome to Day 11 - Functions
def welcome_message():
    print("Welcome to Day 11 - Functions")

# 2. Call welcome_message
welcome_message()

# 3. Create a function called show_learning_status
# It should print: I am learning how to write reusable Python code
def show_learning_status():
    print("I am learning how to write reusable Python code")

# 4. Call show_learning_status
show_learning_status()

# 5. Create a function called print_separator
# It should print 30 hyphens using string repetition
def print_separator():
    hyphen = "-"
    print(hyphen * 30)

# 6. Call print_separator
print_separator()

# 7. Create a function called show_today_topics
# Inside the function, create a list called topics with:
# "def keyword", "calling functions", "function body"
# Then use a for loop to print each topic with this format:
# Topic: def keyword
# Topic: calling functions
# Topic: function body
def show_today_topics():
    topics = ["def keyword", "calling functions", "function body"]
    for topic in topics:
        print(f"Topic: {topic}")

# 8. Call show_today_topics
show_today_topics()

# 9. Create a function called show_completion_message
# It should print: Topic 1 practice complete
def show_completion_message():
    print("Topic 1 practice complete")

# 10. Call show_completion_message
show_completion_message()

# ---------------------------------------------------------------------
# Topic 2 Exercise: print() vs return
print(f"{"-" * 30}Topic 2{"-" * 30}")

# 1. Create a function called print_day_status
# It should print: Day 11 is in progress
def print_day_status():
    print("Day 11 is in progress")

# 2. Call print_day_status
print_day_status()

# 3. Create a function called get_day_status
# It should return: Day 11 is in progress
def get_day_status():
    return "Day 11 is in progress"

# 4. Store the result of get_day_status in a variable called day_status
day_status = get_day_status()

# 5. Print day_status with this format:
# Returned status: Day 11 is in progress
print(f"Returned status: {day_status}")

# 6. Create a function called calculate_practice_minutes
# It should return 45 + 15
def calculate_practice_minutes():
    return 45 + 15

# 7. Store the returned value in a variable called total_minutes
total_minutes = calculate_practice_minutes()

# 8. Print total_minutes with this format:
# Total practice minutes: 60
print(f"Total practice minutes: {total_minutes}")

# 9. Create a function called get_completed_topics
# It should return this list:
# ["Function basics", "print vs return"]
def get_completed_topics():
    return ["Function basics", "print vs return"]

# 10. Store the returned list in a variable called completed_topics
completed_topics = get_completed_topics()

# 11. Use a for loop to print each completed topic with this format:
# Completed: Function basics
# Completed: print vs return
for topic in completed_topics:
    print(f"Completed: {topic}")

# 12. Create a function called get_learning_profile
# It should return a dictionary with:
# "student" -> your name
# "current_day" -> 11
# "current_topic" -> "Functions"
def get_learning_profile():
    return {
        "student": "Sudharsan Srinivasan",
        "current_day": 11,
        "current_topic": "Functions"
    }

# 13. Store the returned dictionary in a variable called learning_profile
learning_profile = get_learning_profile()

# 14. Print the student and current_topic from learning_profile with this format:
# Student: Sudharsan Srinivasan
# Current topic: Functions
print(f"Student: {learning_profile['student']}")
print(f"Current topic: {learning_profile['current_topic']}")

# 15. Create a function called check_return_behavior
# Inside the function:
# - return "This line is returned"
# - after the return, add print("This line will not run")
def check_return_behavior():
    return "This line is returned"
    print("This line will not run")

# 16. Call check_return_behavior and store the result in a variable called return_test
return_test = check_return_behavior()

# 17. Print return_test
print(return_test)

# ---------------------------------------------------------------------
# Topic 3 Exercise: Parameters and Arguments
print(f"{"-" * 30}Topic 3{"-" * 30}")

# 1. Create a function called greet_student
# It should accept one parameter called name
# It should print: Hello, <name>
def greet_student(name):
    print(f"Hello, {name}")

# 2. Call greet_student with your name
greet_student("Sudharsan Srinivasan")

# 3. Call greet_student with "Python Learner"
greet_student("Python Learner")

# 4. Create a function called show_learning_goal
# It should accept two parameters: student_name and goal
# It should print:
# Student: <student_name>
# Goal: <goal>
def show_learning_goal(student_name, goal):
    print(f"Student: {student_name}\nGoal: {goal}")

# 5. Call show_learning_goal with your name and "Learn Python functions"
show_learning_goal("Sudharsan Srinivasan", "Learn Python functions")

# 6. Create a function called add_scores
# It should accept two parameters: score1 and score2
# It should return score1 + score2
def add_scores(score1, score2):
    return score1 + score2

# 7. Call add_scores with 40 and 35
# Store the returned value in a variable called total_score
total_score = add_scores(40, 35)

# 8. Print total_score with this format:
# Total score: 75
print(f"Total score: {total_score}")

# 9. Create a function called calculate_average
# It should accept two parameters: total and count
# It should return total / count
def calculate_average(total, count):
    return total / count

# 10. Call calculate_average using total_score and 2
# Store the returned value in a variable called average_score
average_score = calculate_average(total_score, 2)

# 11. Print average_score with this format:
# Average score: 37.5
print(f"Average score: {average_score}")

# 12. Create a function called count_topics
# It should accept one parameter called topics
# It should return the length of topics
def count_topics(topics):
    return len(topics)

# 13. Reuse your completed_topics list from Topic 2
# Call count_topics with completed_topics
# Store the returned value in a variable called completed_topic_count
completed_topic_count = count_topics(completed_topics)

# 14. Print completed_topic_count with this format:
# Completed topic count: 2
print(f"Completed topic count: {completed_topic_count}")

# 15. Create a function called show_profile_summary
# It should accept one parameter called profile
# It should print the student and current_day from the dictionary with this format:
# Student: Sudharsan Srinivasan
# Current day: 11
def show_profile_summary(profile):
    print(f"Student: {profile['student']}\nCurrent day: {profile['current_day']}")

# 16. Reuse your learning_profile dictionary from Topic 2
# Call show_profile_summary with learning_profile
show_profile_summary(learning_profile)

# 17. Create a function called is_passing_score
# It should accept one parameter called score
# It should return True if score is greater than or equal to 60
# Otherwise, it should return False
def is_passing_score(score):
    return score >= 60

# 18. Call is_passing_score with total_score
# Store the returned value in a variable called has_passing_score
has_passing_score = is_passing_score(total_score)

# 19. Print has_passing_score with this format:
# Passing score: True
print(f"Passing score: {has_passing_score}")

# ---------------------------------------------------------------------
# Topic 4 Exercise: Keyword Arguments and Default Parameters
print(f"{"-" * 30}Topic 4{"-" * 30}")

# 1. Create a function called show_student_profile
# It should accept two parameters: name and role
# It should print:
# Name: <name>
# Role: <role>
def show_student_profile(name, role):
    print(f"Name: {name}\nRole: {role}")

# 2. Call show_student_profile using positional arguments:
# "Sudharsan Srinivasan", "Full Stack Software Engineer"
show_student_profile("Sudharsan Srinivasan", "Full Stack Software Engineer")

# 3. Call show_student_profile using keyword arguments:
# role="Python Learner", name="Ashwin"
show_student_profile(role="Python Learner", name="Ashwin")

# 4. Create a function called greet_student
# It should accept one parameter called name with default value "Python Learner"
# It should print:
# Hello, <name>
def greet_student(name="Python Learner"):
    print(f"Hello, {name}")

# 5. Call greet_student with your name
greet_student("Sudharsan Srinivasan")

# 6. Call greet_student without passing any argument
greet_student()

# 7. Create a function called show_course_status
# It should accept two parameters:
# course with default value "Python"
# status with default value "In progress"
# It should print:
# Course: <course>
# Status: <status>
def show_course_status(course="Python", status="In progress"):
    print(f"Course: {course}\nStatus: {status}")

# 8. Call show_course_status without arguments
show_course_status()

# 9. Call show_course_status with positional arguments:
# "JavaScript", "Completed"
show_course_status("JavaScript", "Completed")

# 10. Call show_course_status with only status as a keyword argument:
# status="Almost done"
show_course_status(status="Almost done")

# 11. Create a function called calculate_final_score
# It should accept:
# base_score
# bonus with default value 10
# It should return base_score + bonus
def calculate_final_score(base_score, bonus=10):
    return base_score + bonus

# 12. Call calculate_final_score with 80
# Store the result in a variable called final_score_default_bonus
final_score_default_bonus = calculate_final_score(80)

# 13. Print final_score_default_bonus with this format:
# Final score with default bonus: 90
print(f"Final score with default bonus: {final_score_default_bonus}")

# 14. Call calculate_final_score with base_score=80 and bonus=20
# Store the result in a variable called final_score_custom_bonus
final_score_custom_bonus = calculate_final_score(base_score=80, bonus=20)

# 15. Print final_score_custom_bonus with this format:
# Final score with custom bonus: 100
print(f"Final score with custom bonus: {final_score_custom_bonus}")

# 16. Create a function called show_day_summary
# It should accept:
# day
# topic with default value "Functions"
# status with default value "In progress"
# It should print:
# Day: <day>
# Topic: <topic>
# Status: <status>
def show_day_summary(day, topic="Functions", status="In progress"):
    print(f"Day: {day}\nTopic: {topic}\nStatus: {status}")

# 17. Call show_day_summary with day=11
show_day_summary(11)

# 18. Call show_day_summary with:
# day=11
# status="Topic 4 practice"
show_day_summary(day=11, status="Topic 4 practice")

# ---------------------------------------------------------------------
# Topic 5 Exercise: Arbitrary Arguments / *args
print(f"{"-" * 30}Topic 5{"-" * 30}")
# 1. Create a function called show_topics
# It should accept any number of topics using *topics
# Inside the function, loop through topics and print each one with this format:
# Topic: <topic>
def show_topics(*args):
    for topic in args:
        print(f"Topic: {topic}")

# 2. Call show_topics with:
# "Functions", "Parameters", "Return values"
show_topics("Functions", "Parameters", "Return values")

# 3. Create a function called count_topics
# It should accept any number of topics using *topics
# It should return the length of topics
def count_topics(*topics):
    return len(topics)

# 4. Call count_topics with:
# "Function basics", "print vs return", "parameters", "default parameters"
# Store the returned value in a variable called topic_count
topic_count = count_topics("Function basics", "print vs return", "parameters", "default parameters")

# 5. Print topic_count with this format:
# Topic count: 4
print(f"Topic count: {topic_count}")

# 6. Create a function called add_scores
# It should accept any number of scores using *scores
# Inside the function:
# - create a variable called total and set it to 0
# - loop through scores
# - add each score to total
# - return total
def add_scores(*scores):
    total = 0
    for score in scores:
        total += score
    return total

# 7. Call add_scores with 20, 30, 40
# Store the returned value in a variable called total_score_from_args
total_score_from_args = add_scores(20, 30, 40)

# 8. Print total_score_from_args with this format:
# Total score from args: 90
print(f"Total score from args: {total_score_from_args}")

# 9. Create a function called show_student_topics
# It should accept:
# student_name
# any number of topics using *topics
# It should print:
# Student: <student_name>
# Then loop through topics and print each topic with this format:
# Learning: <topic>
def show_student_topics(student_name, *topics):
    print(f"Student: {student_name}")
    for topic in topics:
        print(f"Learning: {topic}")

# 10. Call show_student_topics with:
# "Sudharsan Srinivasan", "Functions", "Arguments", "Return values"
show_student_topics("Sudharsan Srinivasan", "Functions", "Arguments", "Return values")

# 11. Create a function called show_learning_plan
# It should accept:
# student_name
# any number of topics using *topics
# status with default value "In progress"
# It should print:
# Student: <student_name>
# Status: <status>
# Then loop through topics and print each topic with this format:
# Planned topic: <topic>
def show_learning_plan(student_name, *topics, status="In progress"):
    print(f"Student: {student_name}\nStatus: {status}")
    for topic in topics:
        print(f"Planned topic: {topic}")

# 12. Call show_learning_plan with:
# "Sudharsan Srinivasan"
# "Functions"
# "Default parameters"
# "Arbitrary arguments"
# status="Practicing"
show_learning_plan("Sudharsan Srinivasan", "Functions", "Default parameters", "Arbitrary arguments", status="Practicing")

# 13. Create a function called check_topics
# It should accept any number of topics using *topics
# If no topics are provided, print:
# No topics provided
# Otherwise, loop through topics and print each one with this format:
# Checked topic: <topic>
def check_topics(*topics):
    if not topics:
        print("No topics provided")
    else:
        for topic in topics:
            print(f"Checked topic: {topic}")

# 14. Call check_topics without passing any arguments
check_topics()

# 15. Call check_topics with:
# "Functions", "Loops"
check_topics("Functions", "Loops")

# ---------------------------------------------------------------------
# Topic 6 Exercise: Function as a Parameter
print(f"{"-" * 30}Topic 6{"-" * 30}")
# 1. Create a function called say_welcome
# It should print: Welcome to function callbacks
def say_welcome():
    print("Welcome to function callbacks")

# 2. Create a function called run_action
# It should accept one parameter called action
# Inside the function, call action()
def run_action(action):
    action()

# 3. Call run_action and pass say_welcome
# Important: pass say_welcome, not say_welcome()
run_action(say_welcome)

# 4. Create a function called get_topic_message
# It should return: Functions can be passed as arguments
def get_topic_message():
    return "Functions can be passed as arguments"

# 5. Create a function called print_function_result
# It should accept one parameter called result_function
# Inside the function:
# - call result_function()
# - store the returned value in a variable called result
# - print result with this format:
# Result: Functions can be passed as arguments
def print_function_result(result_function):
    result = result_function()
    print(f"Result: {result}")

# 6. Call print_function_result and pass get_topic_message
print_function_result(get_topic_message)

# 7. Create a function called double_number
# It should accept one parameter called number
# It should return number * 2
def double_number(number):
    return number * 2

# 8. Create a function called apply_operation
# It should accept two parameters: operation and value
# Inside the function:
# - call operation(value)
# - store the returned value in a variable called result
# - return result
def apply_operation(operation, value):
    result = operation(value)
    return result

# 9. Call apply_operation with double_number and 15
# Store the returned value in a variable called doubled_value
doubled_value = apply_operation(double_number, 15)

# 10. Print doubled_value with this format:
# Doubled value: 30
print(f"Doubled value: {doubled_value}")

# 11. Create a function called is_even
# It should accept one parameter called number
# It should return True if number is divisible by 2
# Otherwise, return False
def is_even(number):
    return number % 2 == 0

# 12. Call apply_operation with is_even and 30
# Store the returned value in a variable called even_check
even_check = apply_operation(is_even, 30)

# 13. Print even_check with this format:
# Is even: True
print(f"Is even: {even_check}")