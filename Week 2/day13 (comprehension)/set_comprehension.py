# Topic 8: Set Comprehension
print(f"{'-' * 30} Topic 8 {'-' * 30}")

# 1. Create a list called languages with:
# "Python", "JavaScript", "React", "Node.js", "Python", "React"
languages = ["Python", "JavaScript", "React", "Node.js", "Python", "React"]

# 2. Use set comprehension to create a set called unique_languages.
# It should contain each language only once.
unique_languages = {language for language in languages}

# 3. Print unique_languages with a clear label.
print(f"Unique Languages: {unique_languages}")

# 4. Use set comprehension to create a set called unique_language_lengths.
# It should contain the unique length values of each language.
unique_language_lengths = {len(language) for language in languages}

# 5. Print unique_language_lengths with a clear label.
print(f"Unique Language Lengths: {unique_language_lengths}")

# 6. Create a list called tools with:
# "Docker", "Django", "Postman", "Python", "Git", "GitHub"
tools = ["Docker", "Django", "Postman", "Python", "Git", "GitHub"]

# 7. Use set comprehension to create a set called first_letters.
# It should contain the first letter of each tool.
first_letters = {tool[0] for tool in tools}

# 8. Print first_letters with a clear label.
print(f"First Letters: {first_letters}")

# 9. Create a list called scores with:
# 45, 72, 88, 39, 100, 67, 91, 72, 100
scores = [45, 72, 88, 39, 100, 67, 91, 72, 100]

# 10. Use set comprehension to create a set called passing_score_set.
# It should keep only scores greater than or equal to 70.
passing_score_set = {score for score in scores if score >= 70}

# 11. Print passing_score_set with a clear label.
print(f"Passing Score Set: {passing_score_set}")

# 12. Create a list called words with:
# "apple", "angle", "banana", "berry", "cherry", "code"
words = ["apple", "angle", "banana", "berry", "cherry", "code"]

# 13. Use set comprehension to create a set called starting_letters.
# It should contain the first letter of each word.
starting_letters = {word[0] for word in words}

# 14. Print starting_letters with a clear label.
print(f"Starting Letters: {starting_letters}")

# 15. Use set comprehension to create a set called long_word_lengths.
# It should keep only words with length greater than 5.
# Store the length of each matching word, not the word itself.
long_word_lengths = {
    len(word)
    for word in words 
    if len(word) > 5
}

# 16. Print long_word_lengths with a clear label.
print(f"Long Word Lengths: {long_word_lengths}")