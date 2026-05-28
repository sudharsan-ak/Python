# Topic 7: Dictionary Comprehension
print(f"{'-' * 30} Topic 7 {'-' * 30}")
# 1. Use list comprehension to create a list called numbers.
# It should contain numbers from 1 to 5.
numbers = [number for number in range(1, 6)]

# 2. Print numbers with a clear label.
print(f"Numbers: {numbers}")

# 3. Use dictionary comprehension to create a dictionary called square_map.
# Each key should be a number from numbers.
# Each value should be that number squared.
square_map = {number: number ** 2 for number in numbers}

# 4. Print square_map with a clear label.
print(f"Square Map: {square_map}")

# 5. Create a list called languages with:
# "Python", "JavaScript", "React", "Node.js"
languages = ["Python", "JavaScript", "React", "Node.js"]

# 6. Use dictionary comprehension to create a dictionary called language_lengths.
# Each key should be a language.
# Each value should be the length of that language.
language_lengths = {language: len(language) for language in languages}

# 7. Print language_lengths with a clear label.
print(f"Language Lengths: {language_lengths}")

# 8. Create a dictionary called student_scores with:
# "Asha": 92
# "Ben": 67
# "Chris": 81
# "Diya": 45
# "Evan": 100
student_scores = {
    "Asha": 92,
    "Ben": 67,
    "Chris": 81,
    "Diya": 45,
    "Evan": 100
}
# 9. Use dictionary comprehension to create a dictionary called score_results.
# Each key should be the student name.
# Each value should be:
# - "Pass" if the score is greater than or equal to 70
# - otherwise "Fail"
score_results = {
    name: "Pass" if score >= 70 else "Fail"
    for name, score in student_scores.items()
}

# 10. Print score_results with a clear label.
print(f"Score Results: {score_results}")

# 11. Use dictionary comprehension to create a dictionary called passing_students.
# It should keep only students whose score is greater than or equal to 70.
# The key should be the student name.
# The value should be the score.
passing_students = {
    name: score
    for name, score in student_scores.items()
    if score >= 70
}

# 12. Print passing_students with a clear label.
print(f"Passing Students: {passing_students}")

# 13. Create a list called words with:
# "hi", "to", "sun", "book", "code"
words = ["hi", "to", "sun", "book", "code"]

# 14. Use dictionary comprehension to create a dictionary called word_length_map.
# Each key should be the word.
# Each value should be the length of the word.
word_length_map = {
    word: len(word) 
    for word in words
}

# 15. Print word_length_map with a clear label.
print(f"Word Length Map: {word_length_map}")