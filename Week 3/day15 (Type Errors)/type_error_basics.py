print(f"{'-' * 30} Topic 1: TypeError Basics {'-' * 30}")

# ------------------------------------------------------------
# Exercise 1
# The code below has a TypeError.
# Uncomment the broken line, run the file, and read the traceback.
# Then comment the broken line again and write the fixed version below it.

age = 30

# broken_message = "My age is " + age

# Write the fixed version below using an f-string.
# Print the fixed message.
fixed_message = f"My age is {age}"
print(fixed_message)

# ------------------------------------------------------------
# Exercise 2
# The code below has a TypeError.
# Uncomment the broken line, run the file, and read the traceback.
# Then comment the broken line again and write the fixed version below it.

price = 99.99

# broken_price_message = "The price is $" + price

# Write the fixed version below using str().
# Print the fixed message.
fixed_price_message = "The price is $" + str(price)
print(f"Fixed price message: {fixed_price_message}")

# ------------------------------------------------------------
# Exercise 3
# The code below has a TypeError.
# Uncomment the broken line, run the file, and read the traceback.
# Then comment the broken line again and write the fixed version below it.

score = "85"
bonus = 5

# final_score = score + bonus

# Fix final_score so it gives the numeric result 90.
# Print final_score.
final_score = int(score) + bonus
print(f"Final score: {final_score}")

# ------------------------------------------------------------
# Exercise 4
# Read this broken line without running it first:
# result = "Python" + 3

# In comments below, answer:
# 1. What type of error do you expect?
# 2. Why will it happen?
# 3. What are two possible fixes?

# Answers:
# 1. TypeError: can only concatenate str (not int) to str
# 2. We are trying to concatenate an integer 3 along with a string Python. Hence the type error.
# 3. Convert the integer into a string (str(3)) or use f string to concatenate

# ------------------------------------------------------------
# Exercise 5
# Create two variables:
# student_name with your name as a string
# completed_days with the number 14

# Then print this exact style of message using an f-string:
# Sudharsan has completed 14 days of Python.
student_name = "Sudharsan"
completed_days = 14
print(f"{student_name} has completed {completed_days} days of Python.")