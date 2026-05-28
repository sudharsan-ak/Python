# Topic 1: Higher Order Functions + Callbacks
print(f"{'-' * 30} Topic 1 {'-' * 30}")

# 1. Create a function called greet_student
# It should print: Welcome to Day 14
def greet_student():
    print("Welcome to Day 14")

# 2. Create a variable called greeting_action
# Store the greet_student function inside it
# Do not call the function during assignment
greeting_action = greet_student

# 3. Call greeting_action
greeting_action()

# 4. Create a function called double_number
# It should accept one parameter called number
# It should return number * 2
def double_number(number):
    return number * 2

# 5. Create a function called triple_number
# It should accept one parameter called number
# It should return number * 3
def triple_number(number):
    return number * 3

# 6. Create a function called apply_operation
# It should accept two parameters:
# operation
# value
# Inside the function:
# - call operation(value)
# - store the result in a variable called result
# - return result
def apply_operation(operation, value):
    result = operation(value)
    return result

# 7. Call apply_operation with double_number and 10
# Store the result in a variable called doubled_result
# Print: Doubled result: <value>
doubled_result = apply_operation(double_number, 10)
print(f"Doubled result: {doubled_result}")

# 8. Call apply_operation with triple_number and 10
# Store the result in a variable called tripled_result
# Print: Tripled result: <value>
tripled_result = apply_operation(triple_number, 10)
print(f"Tripled result: {tripled_result}")

# 9. Create a function called show_start_message
# It should print: Starting Python practice
def show_start_message():
    print("Starting Python practice")

# 10. Create a function called show_end_message
# It should print: Finished Python practice
def show_end_message():
    print("Finished Python practice")

# 11. Create a function called run_practice_session
# It should accept two parameters:
# start_callback
# end_callback
# Inside the function:
# - call start_callback()
# - print: Practicing higher order functions
# - call end_callback()
def run_practice_session(start_callback, end_callback):
    start_callback()
    print("Practicing higher order functions")
    end_callback()

# 12. Call run_practice_session
# Pass show_start_message and show_end_message as arguments
# Do not use parentheses when passing them
run_practice_session(show_start_message, show_end_message)

# 13. Create a function called format_student_name
# It should accept one parameter called name
# It should return name.title()
def format_student_name(name):
    return name.title()

# 14. Create a function called process_student_name
# It should accept two parameters:
# formatter
# student_name
# Inside the function:
# - call formatter(student_name)
# - store the result in formatted_name
# - return formatted_name
def process_student_name(formatter, student_name):
    formatted_name = formatter(student_name)
    return formatted_name

# 15. Call process_student_name with format_student_name and "sudharsan srinivasan"
# Store the result in cleaned_name
# Print: Cleaned name: <value>
cleaned_name = process_student_name(format_student_name, "sudharsan srinivasan")
print(f"Cleaned name: {cleaned_name}")