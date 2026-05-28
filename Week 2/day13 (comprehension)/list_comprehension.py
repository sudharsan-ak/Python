# Topic 1: List Comprehension Basics
print(f"{"-" * 30}Topic 1{"-" * 30}")
# 1. Create a list called languages with:
# "Python", "JavaScript", "React", "Node.js"
languages = ["Python", "JavaScript", "React", "Node.js"]

# 2. Create an empty list called language_labels
language_labels = []

# 3. Use a normal for loop to add this format to language_labels:
# "Learning <language>"
# Example: "Learning Python"
for language in languages:
    language_labels.append(f"Learning {language}")

# 4. Print language_labels with a clear label
print(f"Language Labels: {language_labels}")

# 5. Use list comprehension to create a new list called language_labels_comprehension
# It should create the same "Learning <language>" values from languages
language_labels_comprehension = [f"Learning {language}" for language in languages]

# 6. Print language_labels_comprehension with a clear label
print(f"Language Labels Comprehension: {language_labels_comprehension}")

# 7. Use list comprehension to create a list called uppercase_languages
# Each language should be converted to uppercase
uppercase_languages = [language.upper() for language in languages]

# 8. Print uppercase_languages with a clear label
print(f"Uppercase Languages: {uppercase_languages}")

# 9. Use list comprehension to create a list called language_lengths
# Each item should be the length of each language string
language_lengths = [len(language) for language in languages]

# 10. Print language_lengths with a clear label
print(f"Language Lengths: {language_lengths}")

# 11. Print the original languages list with a clear label
# This proves list comprehension created new lists and did not modify the original list
print(f"Original Languages: {languages}")

# --------------------------------------------------
# Topic 2: Number Transformations with range()
print(f"{"-" * 30}Topic 2{"-" * 30}")
# 1. Use list comprehension to create a list called numbers
# It should contain numbers from 1 to 10
numbers = [number for number in range(1,11)]

# 2. Print numbers with a clear label
print(f"Numbers: {numbers}")

# 3. Use list comprehension to create a list called squares
# Each item should be the square of numbers from 1 to 10
squares = [number ** 2 for number in numbers]

# 4. Print squares with a clear label
print(f"Squares: {squares}")

# 5. Use list comprehension to create a list called cubes
# Each item should be the cube of numbers from 1 to 10
cubes = [number ** 3 for number in numbers]

# 6. Print cubes with a clear label
print(f"Cubes: {cubes}")

# 7. Use list comprehension to create a list called numbers_plus_ten
# Each item should be numbers from 1 to 10 with 10 added
numbers_plus_ten = [number + 10 for number in numbers]

# 8. Print numbers_plus_ten with a clear label
print(f"Numbers Plus Ten: {numbers_plus_ten}")

# 9. Use list comprehension to create a list called number_labels
# Each item should use this format:
# "Number: <number>"
# Example: "Number: 1"
number_labels = [f"Number: {number}" for number in numbers]

# 10. Print number_labels with a clear label
print(f"Number Labels: {number_labels}")

# --------------------------------------------------
# Topic 3: Filtering with if inside list comprehension
print(f"{"-" * 30}Topic 3{"-" * 30}")
# 1. Reuse the numbers list from Topic 2.
# Print numbers with a clear label.
print(f"Numbers: {numbers}")

# 2. Use list comprehension to create a list called even_numbers
# It should keep only even numbers from numbers.
even_numbers = [number for number in numbers if number % 2 == 0]

# 3. Print even_numbers with a clear label.
print(f"Even Numbers: {even_numbers}")

# 4. Use list comprehension to create a list called odd_numbers
# It should keep only odd numbers from numbers.
odd_numbers = [number for number in numbers if number % 2 != 0]

# 5. Print odd_numbers with a clear label.
print(f"Odd Numbers: {odd_numbers}")

# 6. Create a list called scores with:
# 45, 72, 88, 39, 100, 67, 91
scores = [45, 72, 88, 39, 100, 67, 91]

# 7. Use list comprehension to create a list called passing_scores
# It should keep only scores greater than or equal to 70.
passing_scores = [score for score in scores if score >= 70]

# 8. Print passing_scores with a clear label.
print(f"Passing Scores: {passing_scores}")

# 9. Reuse the languages list from Topic 1.
# Use list comprehension to create a list called long_languages
# It should keep only languages where the length is greater than 5.
long_languages = [language for language in languages if len(language) > 5]

# 10. Print long_languages with a clear label.
print(f"Long Languages: {long_languages}")

# 11. Use list comprehension to create a list called js_related_languages
# It should keep only languages that contain "Java" OR "Node".
js_related_languages = [language for language in languages if "Java" in language or "Node" in language]

# 12. Print js_related_languages with a clear label.
print(f"JS Related Languages: {js_related_languages}")

# --------------------------------------------------
# Topic 4: Transform + Filter Together
print(f"{"-" * 30}Topic 4{"-" * 30}")
# 1. Reuse the numbers list from Topic 2.
# Use list comprehension to create a list called even_squares.
# It should include the square of only even numbers.
even_squares = [number ** 2 for number in numbers if number % 2 == 0]

# 2. Print even_squares with a clear label.
print(f"Even Squares: {even_squares}")

# 3. Use list comprehension to create a list called odd_cubes.
# It should include the cube of only odd numbers.
odd_cubes = [number ** 3 for number in numbers if number % 2 != 0]

# 4. Print odd_cubes with a clear label.
print(f"Odd Cubes: {odd_cubes}")

# 5. Reuse the scores list from Topic 3.
# Use list comprehension to create a list called passing_score_labels.
# It should include only scores greater than or equal to 70.
# Each item should use this format:
# "Passing score: <score>"
passing_score_labels = [f"Passing score: {score}" for score in scores if score >= 70]

# 6. Print passing_score_labels with a clear label.
print(f"Passing Score Labels: {passing_score_labels}")

# 7. Reuse the languages list from Topic 1.
# Use list comprehension to create a list called long_uppercase_languages.
# It should include only languages with length greater than 5.
# Each included language should be converted to uppercase.
long_uppercase_languages = [language.upper() for language in languages if len(language) > 5]

# 8. Print long_uppercase_languages with a clear label.
print(f"Long Uppercase Languages: {long_uppercase_languages}")

# 9. Use list comprehension to create a list called js_related_labels.
# It should include only languages that contain "Java" OR "Node".
# Each included language should use this format:
# "JS stack: <language>"
js_related_labels = [f"JS stack: {language}" for language in languages if "Java" in language or "Node" in language]

# 10. Print js_related_labels with a clear label.
print(f"JS Related Labels: {js_related_labels}")

# --------------------------------------------------
# Topic 5: if / else inside list comprehension
print(f"{"-" * 30}Topic 5{"-" * 30}")
# 1. Reuse the numbers list from Topic 2.
# Use list comprehension to create a list called number_types.
# For each number:
# - store "Even" if the number is even
# - otherwise store "Odd"
number_types = ["Even" if number % 2 == 0 else "Odd" for number in numbers]

# 2. Print number_types with a clear label.
print(f"Number Types: {number_types}")

# 3. Reuse the scores list from Topic 3.
# Use list comprehension to create a list called score_results.
# For each score:
# - store "Pass" if the score is greater than or equal to 70
# - otherwise store "Fail"
score_results = ["Pass" if score >= 70 else "Fail" for score in scores]

# 4. Print score_results with a clear label.
print(f"Score Results: {score_results}")

# 5. Reuse the languages list from Topic 1.
# Use list comprehension to create a list called formatted_languages.
# For each language:
# - convert it to uppercase if its length is greater than 5
# - otherwise convert it to lowercase
formatted_languages = [language.upper() if len(language) > 5 else language.lower() for language in languages]

# 6. Print formatted_languages with a clear label.
print(f"Formatted Languages: {formatted_languages}")

# 7. Use list comprehension to create a list called score_messages.
# For each score in scores:
# - store "Strong score: <score>" if the score is greater than or equal to 90
# - otherwise store "Needs improvement: <score>"
score_messages = [f"Strong score: {score}" if score >= 90 else f"Needs improvement: {score}" for score in scores]

# 8. Print score_messages with a clear label.
print(f"Score Messages: {score_messages}")

# 9. Use list comprehension to create a list called number_labels.
# For each number in numbers:
# - store "<number> is divisible by 3" if the number is divisible by 3
# - otherwise store "<number> is not divisible by 3"
number_labels = [f"{number} is divisible by 3" if number % 3 == 0 else f"{number} is not divisible by 3" for number in numbers]

# 10. Print number_labels with a clear label.
print(f"Number Labels: {number_labels}")

# --------------------------------------------------
# Topic 6: Nested List Comprehension / Flattening
print(f"{"-" * 30}Topic 6{"-" * 30}")
# 1. Create a nested list called weekly_topics with these inner lists:
# ["Dictionaries", "Conditionals"]
# ["Loops", "Functions"]
# ["Modules", "Comprehensions"]
weekly_topics = [
    ["Dictionaries", "Conditionals"],
    ["Loops", "Functions"],
    ["Modules", "Comprehensions"]
]

# 2. Create an empty list called all_topics_loop.
all_topics_loop = []

# 3. Use a normal nested for loop to flatten weekly_topics into all_topics_loop.
# Each topic from each inner list should be added to all_topics_loop.
for topics_group in weekly_topics:
    for topic in topics_group:
        all_topics_loop.append(topic)

# 4. Print all_topics_loop with a clear label.
print(f"All Topics Loop: {all_topics_loop}")

# 5. Use nested list comprehension to create a list called all_topics_comprehension.
# It should flatten weekly_topics into one list.
all_topics_comprehension = [topic for topics_group in weekly_topics for topic in topics_group]

# 6. Print all_topics_comprehension with a clear label.
print(f"All Topics Comprehension: {all_topics_comprehension}")

# 7. Use nested list comprehension to create a list called uppercase_topics.
# It should flatten weekly_topics and convert each topic to uppercase.
uppercase_topics = [topic.upper() for topics_group in weekly_topics for topic in topics_group]

# 8. Print uppercase_topics with a clear label.
print(f"Uppercase Topics: {uppercase_topics}")

# 9. Use nested list comprehension to create a list called long_topics.
# It should flatten weekly_topics and keep only topics with length greater than 7.
long_topics = [topic for topics_group in weekly_topics for topic in topics_group if len(topic) > 7]

# 10. Print long_topics with a clear label.
print(f"Long Topics: {long_topics}")

# 11. Create a nested list called score_groups with these inner lists:
# [45, 72, 88]
# [39, 100]
# [67, 91]
score_groups = [
    [45, 72, 88],
    [39, 100],
    [67, 91]
]

# 12. Use nested list comprehension to create a list called all_scores.
# It should flatten score_groups into one list.
all_scores = [score for scores_group in score_groups for score in scores_group]

# 13. Print all_scores with a clear label.
print(f"All Scores: {all_scores}")

# 14. Use nested list comprehension to create a list called passing_scores_flat.
# It should flatten score_groups and keep only scores greater than or equal to 70.
passing_scores_flat = [score for scores_group in score_groups for score in scores_group if score >= 70]

# 15. Print passing_scores_flat with a clear label.
print(f"Passing Scores Flat: {passing_scores_flat}")