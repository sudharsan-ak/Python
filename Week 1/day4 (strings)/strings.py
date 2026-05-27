# Topic 1: Creating Strings
print(f"{'-' * 30}Topic 1{'-' * 30}")
# 1. Create a variable called first_name and store your first name as a string
first_name = "Sudharsan"

# 2. Create a variable called last_name and store your last name as a string
last_name = "Srinivasan"

# 3. Create a variable called city and store your city as a string
city = "Lewisville"

# 4. Create a variable called language and store "Python" as a string
language = "Python"

# 5. Create a variable called message and store this text:
# I'm learning Python strings today
message = "I'm learning Python strings today"

# 6. Create a variable called quote and store this text:
# He said "Python is beginner friendly"
quote = 'He said "Python is beginner friendly"'

# 7. Create a variable called short_bio using triple quotes.
# The bio should have 3 lines:
# Your name
# Your city
# The programming language you are learning
short_bio = f"""My name is {first_name}.
My city is {city}.
I'm currently learning {language}."""

# 8. Print first_name
print(first_name)

# 9. Print last_name
print(last_name)

# 10. Print city
print(city)

# 11. Print language
print(language)

# 12. Print message
print(message)

# 13. Print quote
print(quote)

# 14. Print short_bio
print(short_bio)

# 15. Print the length of first_name using len()
print(len(first_name))

# 16. Print the length of language using len()
print(len(language))

# ---------------------------------------------------------------------
# Topic 2: Concatenation, Repetition, Escape Characters
print(f"{'-' * 30}Topic 2{'-' * 30}")
# Existing variables available:
# first_name
# last_name
# city
# language

# 1. Create a variable called full_name by joining first_name, a space, and last_name using +
full_name = first_name + " " + last_name

# 2. Print full_name
print(full_name)

# 3. Create a variable called intro by joining full_name, " lives in ", and city using +
intro = full_name + " lives in " + city

# 4. Print intro
print(intro)

# 5. Create a variable called age and store your age as a number
age = 30

# 6. Print this using an f-string:
# Sudharsan Srinivasan is 30 years old
print(f"{full_name} is {age} years old")

# 7. Create a variable called separator and store "-"
separator = "-"

# 8. Print separator repeated 20 times
print(separator * 20)

# 9. Create a variable called laugh and store "ha"
laugh = "ha"

# 10. Print laugh repeated 4 times
print(laugh * 4)

# 11. Create a variable called multi_line_message using \n
# It should print:
# Python
# Strings
# Practice
multi_line_message = "Python\nStrings\nPractice"

# 12. Print multi_line_message
print(multi_line_message)

# 13. Create a variable called tab_message using \t
# It should print something like:
# Name:    Sudharsan
tab_message = "Name:\tSudharsan"

# 14. Print tab_message
print(tab_message)

# 15. Create a variable called escaped_quote that stores:
# He said, "Python is fun"
escaped_quote = 'He said, "Python is fun"'

# 16. Print escaped_quote
print(escaped_quote)


# ---------------------------------------------------------------------
# Topic 3: String Formatting
print(f"{'-' * 30}Topic 3{'-' * 30}")
# Existing variables available:
# first_name
# last_name
# city
# language
# full_name
# age

# 1. Create a variable called profile_sentence using an f-string.
# It should say:
# Sudharsan Srinivasan lives in Lewisville.
profile_sentence = f"{full_name} lives in {city}."

# 2. Print profile_sentence
print(profile_sentence)

# 3. Create a variable called learning_sentence using an f-string.
# It should say:
# Sudharsan is learning Python.
learning_sentence = f"{first_name} is learning {language}."

# 4. Print learning_sentence
print(learning_sentence)

# 5. Create a variable called years_to_40 and store 40 - age
years_to_40 = 40 - age

# 6. Print this using an f-string:
# Sudharsan will be 40 in 10 years.
print(f"{first_name} will be 40 in {years_to_40} years.")

# 7. Create two variables:
# hourly_rate = 50
# hours_worked = 8
hourly_rate = 50
hours_worked = 8

# 8. Create a variable called total_pay and store hourly_rate * hours_worked
total_pay = hourly_rate * hours_worked

# 9. Print this using an f-string:
# Total pay is $400
print(f"Total pay is ${total_pay}")

# 10. Create a variable called summary using a triple-quoted f-string.
# It should print 3 lines:
# Name: Sudharsan Srinivasan
# City: Lewisville
# Language: Python
summary = f"""Name: {full_name}
City: {city}
Language: {language}"""

# 11. Print summary
print(summary)

# ---------------------------------------------------------------------
# Topic 4: String Indexing
print(f"{'-' * 30}Topic 4{'-' * 30}")
# Existing variables available:
# first_name
# last_name
# city
# language
# full_name

# 1. Print the first character of first_name
print(first_name[0])

# 2. Print the second character of first_name
print(first_name[1])

# 3. Print the last character of first_name using negative indexing
print(first_name[-1])

# 4. Print the first character of language
print(language[0])

# 5. Print the last character of language using negative indexing
print(language[-1])

# 6. Create a variable called first_city_letter and store the first character of city
first_city_letter = city[0]

# 7. Print first_city_letter
print(first_city_letter)

# 8. Create a variable called last_city_letter and store the last character of city using negative indexing
last_city_letter = city[-1]

# 9. Print last_city_letter
print(last_city_letter)

# 10. Create a variable called full_name_length and store the length of full_name
full_name_length = len(full_name)

# 11. Print full_name_length
print(full_name_length)

# 12. Create a variable called last_index and store len(full_name) - 1
last_index = len(full_name) - 1

# 13. Print the last character of full_name using last_index
print(full_name[last_index])

# 14. Print the last character of full_name again using negative indexing
print(full_name[-1])

# ---------------------------------------------------------------------
# Topic 5: String Slicing
print(f"{'-' * 30}Topic 5{'-' * 30}")
# Existing variables available:
# first_name
# last_name
# city
# language
# full_name

# 1. Print the first 3 characters of first_name using slicing
print(first_name[0:3])

# 2. Print the first 5 characters of last_name using slicing
print(last_name[0:5])

# 3. Print the first 3 characters of language using slicing
print(language[0:3])

# 4. Print characters from index 3 to the end of language
print(language[3:])

# 5. Print the last 3 characters of language using negative slicing
print(language[-3:])

# 6. Create a variable called first_name_start and store the first 4 characters of first_name
first_name_start = first_name[0:4]

# 7. Print first_name_start
print(first_name_start)

# 8. Create a variable called city_start and store the first 5 characters of city
city_start = city[0:5]

# 9. Print city_start
print(city_start)

# 10. Create a variable called city_end and store the last 5 characters of city using negative slicing
city_end = city[-5:]

# 11. Print city_end
print(city_end)

# 12. Create a variable called full_name_first_part and store the first 9 characters of full_name
full_name_first_part = full_name[0:9]

# 13. Print full_name_first_part
print(full_name_first_part)

# 14. Create a variable called full_name_last_part and store the last 10 characters of full_name
full_name_last_part = full_name[10:]

# 15. Print full_name_last_part
print(full_name_last_part)

# 16. Print the full language string using slicing with [:]
print(language[:])

# ---------------------------------------------------------------------
# Topic 6: String Methods - Case, Strip, Replace
print(f"{'-' * 30}Topic 6{'-' * 30}")
# Existing variables available:
# first_name
# last_name
# city
# language
# full_name

# 1. Print first_name in uppercase
print(first_name.upper())

# 2. Print last_name in lowercase
print(last_name.lower())

# 3. Print full_name using title()
print(full_name.title())

# 4. Create a variable called messy_name and store "   Sudharsan   "
messy_name = "   Sudharsan   "

# 5. Print messy_name
print(messy_name)

# 6. Print messy_name after using strip()
print(messy_name.strip())

# 7. Create a variable called sentence and store:
# I am learning JavaScript
sentence = "I am learning JavaScript"

# 8. Create a variable called updated_sentence by replacing "JavaScript" with "Python"
updated_sentence = sentence.replace("JavaScript", "Python")

# 9. Print updated_sentence
print(updated_sentence)

# 10. Create a variable called city_sentence using an f-string:
# I live in Lewisville
city_sentence = f"I live in {city}"

# 11. Replace "Lewisville" with "Dallas" and store it in a variable called new_city_sentence
new_city_sentence = city_sentence.replace("Lewisville", "Dallas")

# 12. Print new_city_sentence
print(new_city_sentence)

# 13. Create a variable called lowercase_language and store language in lowercase
lowercase_language = language.lower()

# 14. Print lowercase_language
print(lowercase_language)

# 15. Create a variable called uppercase_city and store city in uppercase
uppercase_city = city.upper()

# 16. Print uppercase_city
print(uppercase_city)

# ---------------------------------------------------------------------
# Topic 7: String Search and Check Methods
print(f"{'-' * 30}Topic 7{'-' * 30}")
# Existing variables available:
# first_name
# last_name
# city
# language
# full_name

# 1. Print whether first_name starts with "Sud"
print(first_name.startswith("Sud"))

# 2. Print whether first_name ends with "san"
print(first_name.endswith("san"))

# 3. Print whether city starts with "Lew"
print(city.startswith("Lew"))

# 4. Print whether city ends with "ville"
print(city.endswith("ville"))

# 5. Create a variable called search_sentence and store:
# I am learning Python because Python is useful
search_sentence = "I am learning Python because Python is useful"

# 6. Print how many times "Python" appears in search_sentence
print(search_sentence.count("Python"))

# 7. Print the index where "learning" starts in search_sentence
print(search_sentence.find("learning"))

# 8. Print the index where "JavaScript" starts in search_sentence
print(search_sentence.find("JavaScript"))

# 9. Create a variable called has_python and store whether search_sentence contains "Python" using find()
# Hint: find() should not equal -1
has_python = search_sentence.find("Python") != -1

# 10. Print has_python
print(has_python)

# 11. Create a variable called has_javascript and store whether search_sentence contains "JavaScript" using find()
has_javascript = search_sentence.find("JavaScript") != -1

# 12. Print has_javascript
print(has_javascript)

# 13. Print whether full_name starts with first_name
print(full_name.startswith(first_name))

# 14. Print whether full_name ends with last_name
print(full_name.endswith(last_name))

# ---------------------------------------------------------------------
# Topic 8: split() and join()
print(f"{'-' * 30}Topic 8{'-' * 30}")
# Existing variables available:
# first_name
# last_name
# city
# language
# full_name

# 1. Create a variable called sentence and store:
# I am learning Python strings
sentence = "I am learning Python strings"

# 2. Create a variable called words by splitting sentence
words = sentence.split()
# 3. Print words
print(words)

# 4. Create a variable called full_name_parts by splitting full_name
full_name_parts = full_name.split()

# 5. Print full_name_parts
print(full_name_parts)

# 6. Print the first item from full_name_parts
print(full_name_parts[0])

# 7. Print the second item from full_name_parts
print(full_name_parts[1])

# 8. Create a variable called skills_text and store:
# JavaScript,React,Python,Node
skills_text = "JavaScript,React,Python,Node"

# 9. Create a variable called skills_list by splitting skills_text using ","
skills_list = skills_text.split(",")

# 10. Print skills_list
print(skills_list)

# 11. Create a variable called joined_skills by joining skills_list with ", "
joined_skills = ", ".join(skills_list)

# 12. Print joined_skills
print(joined_skills)

# 13. Create a variable called name_letters by converting first_name into a list using list()
name_letters = list(first_name)

# 14. Print name_letters
print(name_letters)

# 15. Create a variable called joined_letters by joining name_letters with "-"
joined_letters = "-".join(name_letters)

# 16. Print joined_letters
print(joined_letters)

# ---------------------------------------------------------------------
# Topic 9: Character Check Methods
print(f"{'-' * 30}Topic 9{'-' * 30}")
# Existing variables available:
# first_name
# last_name
# city
# language
# full_name

# 1. Print whether first_name contains only alphabetic characters using isalpha()
print(first_name.isalpha())

# 2. Print whether full_name contains only alphabetic characters using isalpha()
print(full_name.isalpha())

# 3. Create a variable called age_text and store "30"
age_text = "30"

# 4. Print whether age_text contains only digits using isdigit()
print(age_text.isdigit())

# 5. Create a variable called username and store "Sudharsan10"
username = "Sudharsan10"

# 6. Print whether username contains only letters and numbers using isalnum()
print(username.isalnum())

# 7. Create a variable called bad_username and store "Sudharsan_10"
bad_username = "Sudharsan_10"

# 8. Print whether bad_username contains only letters and numbers using isalnum()
print(bad_username.isalnum())

# 9. Create a variable called lowercase_name and store first_name in lowercase
lowercase_name = first_name.lower()

# 10. Print whether lowercase_name is lowercase using islower()
print(lowercase_name.islower())

# 11. Create a variable called uppercase_city and store city in uppercase
uppercase_city = city.upper()

# 12. Print whether uppercase_city is uppercase using isupper()
print(uppercase_city.isupper())

# 13. Print whether language is uppercase using isupper()
print(language.isupper())

# 14. Print whether language is lowercase using islower()
print(language.islower())