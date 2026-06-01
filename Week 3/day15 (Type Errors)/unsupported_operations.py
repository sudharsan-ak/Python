print(f"{'-' * 30} Topic 2: Unsupported Operations Between Types {'-' * 30}")

# ------------------------------------------------------------
# Exercise 1
# The broken line tries to combine a string and an integer.

days_completed = 14

# message = "Days completed: " + days_completed

# Fix it using an f-string.
# Print the fixed message.
fixed_message = f"Days completed: {days_completed}"
print(fixed_message)

# ------------------------------------------------------------
# Exercise 2
# The broken line tries to do math with a string number and an integer.

current_score = "72"
extra_points = 8

# updated_score = current_score + extra_points

# Fix it so updated_score becomes the number 80.
# Print updated_score.
updated_score = int(current_score) + extra_points
print(f"Updated score: {updated_score}")

# ------------------------------------------------------------
# Exercise 3
# The broken line tries to combine a list and a string.

topics = ["Dictionaries", "Loops", "Functions"]

# updated_topics = topics + "Type Errors"

# Fix it by creating a new list called updated_topics.
# It should include the original topics plus "Type Errors".
# Print updated_topics.
updated_topics = topics + ["Type Errors"]
print(f"Updated topics: {updated_topics}")

# (or) we can do topics.copy() and assign to updated_topics, then updated_topics.append("Type Errors")

# ------------------------------------------------------------
# Exercise 4
# The broken line tries to subtract from a string.

price_text = "99.99"
discount = 10

# final_price = price_text - discount

# Fix it so final_price gives the numeric result 89.99.
# Print final_price.
final_price = float(price_text) - discount
print(f"Final price: {final_price}")

# ------------------------------------------------------------
# Exercise 5
# The broken line tries to divide a string by a number.

language = "Python"

# result = language / 2

# Do not force a weird fix.
# Instead, write a comment explaining why this operation does not make sense.
# Then create a variable called repeated_language that repeats "Python" 2 times.
# Print repeated_language.

# Reason: Python understands the division operation, but it cannot divide a string.
repeated_language = language * 2
print(f"Repeated language: {repeated_language}")

# ------------------------------------------------------------
# Exercise 6
# Choose the correct fix based on the goal.

student_name = "Sudharsan"
completed_days = 15

# broken_summary = student_name + " completed " + completed_days + " days."

# Goal: display a sentence, not do math.
# Fix it using an f-string.
# Print the fixed summary.
fixed_summary = f"{student_name} completed {completed_days} days."
print(fixed_summary)