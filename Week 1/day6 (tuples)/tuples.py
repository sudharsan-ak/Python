# Topic 1 - Creating tuples, len(), and type()
# 1. Create a tuple called languages with these values:
# "JavaScript", "TypeScript", "Python", "Java"
languages = ("JavaScript", "TypeScript", "Python", "Java")

# 2. Print the languages tuple
print(languages)

# 3. Print the length of languages using len()
print(len(languages))

# 4. Print the type of languages using type()
print(type(languages))

# 5. Create a tuple called profile with these values:
# "Sudharsan", 30, "Lewisville", True
profile = ("Sudharsan", 30, "Lewisville", True)

# 6. Print the profile tuple
print(profile)

# 7. Print the length of profile
print(len(profile))

# 8. Create an empty tuple called empty_tuple
empty_tuple = ()

# 9. Print the empty_tuple
print(empty_tuple)

# 10. Print the length of empty_tuple
print(len(empty_tuple))

# 11. Create a one-item tuple called favorite_language with the value "Python"
favorite_language = ("Python",)

# 12. Print favorite_language
print(favorite_language)

# 13. Print the type of favorite_language
print(type(favorite_language))

# ---------------------------------------------------------------------
# Topic 2 - Accessing tuple items
# 1. Print the first item from languages
print(languages[0])

# 2. Print the second item from languages
print(languages[1])

# 3. Print the last item from languages using negative indexing
print(languages[-1])

# 4. Print the second-to-last item from languages using negative indexing
print(languages[-2])

# 5. Print the first two items from languages using slicing
print(languages[:2])

# 6. Print everything from index 2 to the end from languages
print(languages[2:])

# 7. Print the last two items from languages using slicing
print(languages[-2:])

# 8. Print a full copy of languages using slicing
print(languages[:])

# 9. Print the first item from profile
print(profile[0])

# 10. Print the last item from profile using negative indexing
print(profile[-1])

# 11. Print the middle two items from profile using slicing
print(profile[1:-1])

# ---------------------------------------------------------------------
# Topic 3 - Checking items and tuple immutability
# 1. Check whether "Python" exists in languages and store the result in has_python
has_python = "Python" in languages

# 2. Print has_python
print(has_python)

# 3. Check whether "Go" exists in languages and store the result in has_go
has_go = "Go" in languages

# 4. Print has_go
print(has_go)

# 5. Check whether "JavaScript" exists in languages and print the result directly
print("JavaScript" in languages)

# 6. Create a tuple called week_days with these values:
# "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

# 7. Print week_days
print(week_days)

# 8. Print whether "Saturday" exists in week_days
print("Saturday" in week_days)

# 9. Print whether "Monday" exists in week_days
print("Monday" in week_days)

# 10. Create a tuple called coordinates with the values 10 and 20
coordinates = (10, 20)

# 11. Print coordinates
print(coordinates)

# 12. Reassign coordinates to a new tuple with values 30 and 40
coordinates = (30, 40)

# 13. Print coordinates again
print(coordinates)

# 14. Add this as a comment only:
# coordinates[0] = 100 would fail because tuples cannot be changed directly

# ---------------------------------------------------------------------
# Topic 4 - Tuple to list and list to tuple conversion
# 1. Convert languages into a list and store it in languages_list
languages_list = list(languages)

# 2. Print languages_list
print(languages_list)

# 3. Print the type of languages_list
print(type(languages_list))

# 4. Change the first item in languages_list to "HTML"
languages_list[0] = "HTML"

# 5. Append "Go" to languages_list
languages_list.append("Go")

# 6. Print languages_list again
print(languages_list)

# 7. Convert languages_list back into a tuple and store it in updated_languages
updated_languages = tuple(languages_list)

# 8. Print updated_languages
print(updated_languages)

# 9. Print the type of updated_languages
print(type(updated_languages))

# 10. Create a tuple called frontend_skills with:
# "HTML", "CSS", "JavaScript"
frontend_skills = ("HTML", "CSS", "JavaScript")

# 11. Convert frontend_skills into a list called frontend_skills_list
frontend_skills_list = list(frontend_skills)

# 12. Append "React" to frontend_skills_list
frontend_skills_list.append("React")

# 13. Convert frontend_skills_list back into a tuple called updated_frontend_skills
updated_frontend_skills = tuple(frontend_skills_list)

# 14. Print updated_frontend_skills
print(updated_frontend_skills)

# ---------------------------------------------------------------------
# Topic 5 - Joining and deleting tuples
# 1. Create a tuple called backend_skills with:
# "Node.js", "Express", "MongoDB", "PostgreSQL"
backend_skills = ("Node.js", "Express", "MongoDB", "PostgreSQL")

# 2. Print backend_skills
print(backend_skills)

# 3. Join frontend_skills and backend_skills into a new tuple called full_stack_skills
full_stack_skills = frontend_skills + backend_skills

# 4. Print full_stack_skills
print(full_stack_skills)

# 5. Print the length of full_stack_skills
print(len(full_stack_skills))

# 6. Create a tuple called cloud_skills with:
# "AWS", "Docker"
cloud_skills = ("AWS", "Docker")

# 7. Join full_stack_skills and cloud_skills into a new tuple called complete_skills
complete_skills = full_stack_skills + cloud_skills

# 8. Print complete_skills
print("Complete Skills: ", complete_skills)

# 9. Create a tuple called numbers with values 1 and 2
numbers = (1, 2)

# 10. Create a tuple called repeated_numbers by repeating numbers 3 times
repeated_numbers = numbers * 3

# 11. Print repeated_numbers
print(repeated_numbers)

# 12. Create a tuple called temporary_tuple with:
# "draft", "test", "sample"
temporary_tuple = ("draft", "test", "sample")

# 13. Print temporary_tuple
print(f"Temporary tuple is- {temporary_tuple}")

# 14. Delete temporary_tuple using del
del temporary_tuple

# 15. Add this as a comment only:
# print(temporary_tuple) would fail because temporary_tuple was deleted

# 16. Add this as a comment only:
# del complete_skills[0] would fail because tuple items cannot be deleted directly

# ---------------------------------------------------------------------
# Topic 6 - Tuple use cases and beginner gotchas
# 1. Create a tuple called rgb_color with values 255, 255, 255
rgb_color = (255, 255, 255)

# 2. Print rgb_color
print(rgb_color)

# 3. Print the length of rgb_color
print(len(rgb_color))

# 4. Create a tuple called date_parts with values 2026, 5, 18
date_parts = (2026, 5, 18)

# 5. Print date_parts
print(date_parts)

# 6. Print the year from date_parts using indexing
print(date_parts[0])

# 7. Create a tuple called repeated_scores with values:
# 90, 85, 90, 70, 90
repeated_scores = (90, 85, 90, 70, 90)

# 8. Print how many times 90 appears in repeated_scores using count()
print(repeated_scores.count(90))

# 9. Print the first index of 70 using index()
print(repeated_scores.index(70))

# 10. Check whether 100 exists in repeated_scores and store it in has_100
has_100 = 100 in repeated_scores

# 11. Print has_100
print(f"Is 100 present: {has_100}")

# 12. Create a one-item tuple called single_skill with the value "Python"
single_skill = ("Python",)

# 13. Print single_skill
print(single_skill)

# 14. Print the type of single_skill
print(type(single_skill))

# 15. Create a list called changing_skills with:
# "JavaScript", "React", "Node.js"
changing_skills = ["JavaScript", "React", "Node.js"]

# 16. Append "Python" to changing_skills
changing_skills.append("Python")

# 17. Print changing_skills
print(changing_skills)

# 18. Add this as a comment only:
# changing_skills should be a list because skills can change over time

# 19. Add this as a comment only:
# rgb_color should be a tuple because it represents a fixed group of color values