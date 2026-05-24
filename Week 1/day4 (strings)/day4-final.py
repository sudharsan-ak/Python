# ---------------------------------------------------------------------
# Day 4 - Final Mixed Exercise: Strings

# 1. Create a variable called first_name and store your first name as a string
first_name = "Sudharsan"

# 2. Create a variable called last_name and store your last name as a string
last_name = "Srinivasan"

# 3. Create a variable called city and store your city as a string
city = "Lewisville"

# 4. Create a variable called language and store "Python"
language = "Python"

# 5. Create a variable called full_name by joining first_name, a space, and last_name using +
full_name = first_name + " " + last_name

# 6. Print full_name
print(full_name)

# 7. Print this using an f-string:
# My name is Sudharsan Srinivasan and I live in Lewisville.
print(f"My name is {full_name} and I live in {city}.")

# 8. Print the length of full_name
print(len(full_name))

# 9. Print the first character of first_name
print(first_name[0])

# 10. Print the last character of last_name using negative indexing
print(last_name[-1])

# 11. Print the first 3 characters of language using slicing
print(language[0:3])

# 12. Print the last 3 characters of language using negative slicing
print(language[-3:])

# 13. Create a variable called messy_city and store "   Lewisville   "
messy_city = "   Lewisville   "

# 14. Print messy_city after using strip()
print(messy_city.strip())

# 15. Print full_name in uppercase
print(full_name.upper())

# 16. Print full_name using title()
print(full_name.title())

# 17. Create a variable called sentence and store:
# I am learning JavaScript strings
sentence = "I am learning JavaScript strings"

# 18. Create a variable called updated_sentence by replacing "JavaScript" with "Python"
updated_sentence = sentence.replace("JavaScript", "Python")

# 19. Print updated_sentence
print(updated_sentence)

# 20. Print whether updated_sentence starts with "I am"
print(updated_sentence.startswith("I am"))

# 21. Print whether updated_sentence ends with "strings"
print(updated_sentence.endswith("strings"))

# 22. Print the index where "Python" starts in updated_sentence
print(updated_sentence.find("Python"))

# 23. Print how many times "Python" appears in updated_sentence
print(updated_sentence.count("Python"))

# 24. Create a variable called words by splitting updated_sentence
words = updated_sentence.split()

# 25. Print words
print(words)

# 26. Create a variable called joined_words by joining words with "-"
joined_words = "-".join(words)

# 27. Print joined_words
print(joined_words)

# 28. Create a variable called age_text and store "30"
age_text = "30"

# 29. Print whether age_text contains only digits
print(age_text.isdigit())

# 30. Create a variable called username and store "Sudharsan10"
username = "Sudharsan10"

# 31. Print whether username contains only letters and numbers
print(username.isalnum())

# 32. Create a variable called bad_username and store "Sudharsan_10"
bad_username = "Sudharsan_10"

# 33. Print whether bad_username contains only letters and numbers
print(bad_username.isalnum())

# 34. Create a variable called multi_line_summary using a triple-quoted f-string.
# It should print 3 lines:
# Name: Sudharsan Srinivasan
# City: Lewisville
# Language: Python
multi_line_summary = f"""Name: {full_name}
City: {city}
Language: {language}"""

# 35. Print multi_line_summary
print(multi_line_summary)