# Topic 1: Importing a full custom module
print(f"{"-" * 30}Topic 1{"-" * 30}")
# 1. Import the full helpers module
import helpers

# 2. Call get_student_name from helpers
# Store the returned value in a variable called student_name
student_name = helpers.get_student_name()

# 3. Call get_current_day from helpers
# Store the returned value in a variable called current_day
current_day = helpers.get_current_day()

# 4. Call get_current_topic from helpers
# Store the returned value in a variable called current_topic
current_topic = helpers.get_current_topic()

# 5. Call build_progress_message from helpers
# Pass student_name, current_day, and current_topic
# Store the returned value in a variable called progress_message
progress_message = helpers.build_progress_message(student_name, current_day, current_topic)

# 6. Call print_separator from helpers
helpers.print_separator()

# 7. Print progress_message using an f-string with this label:
# Progress: <progress_message>
print(f"Progress: {progress_message}")

# 8. Call print_separator from helpers again
helpers.print_separator()