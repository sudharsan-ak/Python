# Topic 3: map() and filter()
print(f"{'-' * 30} Topic 3 {'-' * 30}")

# 1. Create a list called numbers with values:
# 1, 2, 3, 4, 5, 6, 7, 8
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# 2. Use map() with a lambda to create doubled_numbers
# Each number should be multiplied by 2
# Convert the result to a list
# Print: Doubled numbers: <list>
doubled_numbers = list(map(lambda number: number * 2, numbers))
print(f"Doubled numbers: {doubled_numbers}")

# 3. Use map() with a lambda to create squared_numbers
# Each number should be raised to the power of 2
# Convert the result to a list
# Print: Squared numbers: <list>
squared_numbers = list(map(lambda number: number ** 2, numbers))
print(f"Squared numbers: {squared_numbers}")

# 4. Create a normal function called cube_number
# It should accept one parameter called number
# It should return number ** 3
def cube_number(number):
    return number ** 3

# 5. Use map() with cube_number to create cubed_numbers
# Convert the result to a list
# Print: Cubed numbers: <list>
cubed_numbers = list(map(cube_number, numbers))
print(f"Cubed numbers: {cubed_numbers}")

# 6. Create a list called names with values:
# "sudharsan", "ashwin", "python learner"
names = ["sudharsan", "ashwin", "python learner"]

# 7. Use map() with a lambda to create formatted_names
# Each name should be converted to title case
# Convert the result to a list
# Print: Formatted names: <list>
formatted_names = list(map(lambda name: name.title(), names))
print(f"Formatted names: {formatted_names}")

# 8. Use filter() with a lambda to create even_numbers
# Keep only numbers that are divisible by 2
# Convert the result to a list
# Print: Even numbers: <list>
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# 9. Use filter() with a lambda to create odd_numbers
# Keep only numbers that are not divisible by 2
# Convert the result to a list
# Print: Odd numbers: <list>
odd_numbers = list(filter(lambda number: number % 2 != 0, numbers))
print(f"Odd numbers: {odd_numbers}")

# 10. Create a list called scores with values:
# 95, 62, 88, 45, 70, 100
scores = [95, 62, 88, 45, 70, 100]

# 11. Create a normal function called is_passing_score
# It should accept one parameter called score
# It should return True if score is greater than or equal to 70
# Otherwise, return False
def is_passing_score(score):
    return score >= 70

# 12. Use filter() with is_passing_score to create passing_scores
# Convert the result to a list
# Print: Passing scores: <list>
passing_scores = list(filter(is_passing_score, scores))
print(f"Passing scores: {passing_scores}")

# 13. Use filter() with a lambda to create long_names
# Keep only names where len(name) is greater than 6
# Convert the result to a list
# Print: Long names: <list>
long_names = list(filter(lambda name: len(name) > 6, names))
print(f"Long names: {long_names}")

# 14. Create even_squares using filter() and map()
# First keep only even numbers from numbers
# Then square those even numbers
# Convert the final result to a list
# Print: Even squares with map/filter: <list>
even_squares = list(map(lambda number: number ** 2, filter(lambda number: number % 2 == 0, numbers)))
print(f"Even squares with map/filter: {even_squares}")

# 15. Create even_squares_comprehension using list comprehension
# It should produce the same result as step 14
# Print: Even squares with comprehension: <list>
even_squares_comprehension = [number ** 2 for number in numbers if number % 2 == 0]
print(f"Even squares with comprehension: {even_squares_comprehension}")

# 16. Add a comment explaining which version is easier to read:
# map/filter chain or list comprehension
# list comprehension is easier to read because map/filter chain is nested and can be harder to understand at first glance