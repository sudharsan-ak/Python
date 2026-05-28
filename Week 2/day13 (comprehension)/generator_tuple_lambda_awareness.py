# Topic 9: Generator Expression Awareness
print(f"{'-' * 30} Topic 9 {'-' * 30}")

# 1. Use list comprehension to create a list called squares_list.
# It should contain squares of numbers from 1 to 5.
squares_list = [number ** 2 for number in range(1, 6)]

# 2. Print squares_list with a clear label.
print(f"Squares List: {squares_list}")

# 3. Use a generator expression to create a variable called squares_generator.
# It should generate squares of numbers from 1 to 5.
# Use parentheses, not square brackets.
squares_generator = (number ** 2 for number in range(1, 6))

# 4. Print squares_generator with a clear label.
# This should show a generator object, not the actual values.
print(f"Squares Generator: {squares_generator}")

# 5. Create another generator expression called cubes_generator.
# It should generate cubes of numbers from 1 to 5.
cubes_generator = (number ** 3 for number in range(1, 6))

# 6. Convert cubes_generator to a list and store it in cubes_from_generator.
cubes_from_generator = list(cubes_generator)

# 7. Print cubes_from_generator with a clear label.
print(f"Cubes From Generator: {cubes_from_generator}")

# 8. Create a generator expression called numbers_generator.
# It should generate numbers from 1 to 3.
numbers_generator = (number for number in range(1, 4))

# 9. Convert numbers_generator to a list and print it with a clear label.
print(f"Numbers List: {list(numbers_generator)}")

# 10. Convert numbers_generator to a list again and print it with a clear label.
# This should show an empty list because the generator was already consumed.
print(f"Numbers List Again: {list(numbers_generator)}")

# --------------------------------------------------
# Topic 10: Tuple Comprehension Clarification
print(f"{'-' * 30} Topic 10 {'-' * 30}")

# 1. Create a variable called numbers_generator.
# Use parentheses with comprehension-style syntax.
# It should generate numbers from 1 to 5.
numbers_generator = (number for number in range(1, 6))

# 2. Print numbers_generator with a clear label.
# This should show a generator object, not a tuple.
print(f"Numbers Generator: {numbers_generator}")

# 3. Create a variable called numbers_tuple.
# Use tuple() with a generator expression inside it.
# It should contain numbers from 1 to 5.
numbers_tuple = tuple(number for number in range(1, 6))

# 4. Print numbers_tuple with a clear label.
print(f"Numbers Tuple: {numbers_tuple}")

# 5. Create a variable called squared_tuple.
# Use tuple() with a generator expression inside it.
# It should contain squares of numbers from 1 to 5.
squared_tuple = tuple(number ** 2 for number in range(1, 6))

# 6. Print squared_tuple with a clear label.
print(f"Squared Tuple: {squared_tuple}")

# 7. Create a variable called languages_tuple.
# Use tuple() with a generator expression inside it.
# It should contain uppercase versions of:
# "python", "javascript", "react"
languages_tuple = tuple(
    language.upper()
    for language in ["python", "javascript", "react"]
)

# 8. Print languages_tuple with a clear label.
print(f"Languages Tuple: {languages_tuple}")

# --------------------------------------------------
# Topic 11: Light Lambda Awareness
print(f"{'-' * 30} Topic 11 {'-' * 30}")

# 1. Create a lambda function called double_number.
# It should accept one parameter called number.
# It should return number * 2.
double_number = lambda number: number * 2

# 2. Call double_number with 8 and print the result with a clear label.
print(f"Doubled Number: {double_number(8)}")

# 3. Create a lambda function called add_numbers.
# It should accept two parameters: first_number and second_number.
# It should return their sum.
add_numbers = lambda first_number, second_number: first_number + second_number

# 4. Call add_numbers with 15 and 25 and print the result with a clear label.
print(f"Sum of Numbers: {add_numbers(15, 25)}")

# 5. Create a lambda function called is_passing.
# It should accept one parameter called score.
# It should return True if score is greater than or equal to 70.
is_passing = lambda score: score >= 70

# 6. Call is_passing with 88 and print the result with a clear label.
print(f"Is Passing: {is_passing(88)}")

# 7. Create a list called task_titles with:
# "review notes", "write code", "submit exercise"
task_titles = ["review notes", "write code", "submit exercise"]

# 8. Use list comprehension to create a list called formatted_task_titles.
# Each task title should be converted to title case using .title().
# This is not a lambda task - it is here to remind you not everything needs lambda.
formatted_task_titles = [task_title.title() for task_title in task_titles]

# 9. Print formatted_task_titles with a clear label.
print(f"Formatted task titles: {formatted_task_titles}")