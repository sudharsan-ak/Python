# ---------------------------------------------------------------------
# Day 6 - Final Mixed Exercise: Tuples
# 1. Create a tuple called languages with:
# "JavaScript", "TypeScript", "Python", "Java"
languages = ("JavaScript", "TypeScript", "Python", "Java")

# 2. Print the first item, last item, and first two items from languages
print(f"First item: {languages[0]}, Last item: {languages[-1]}, First 2 items: {languages[:2]}")

# 3. Check whether "Python" exists in languages and store it in has_python
has_python = "Python" in languages

# 4. Print has_python
print(f"Does Python exist: {has_python}")

# 5. Convert languages into a list called languages_list
languages_list = list(languages)

# 6. Add "Go" to languages_list and change the first item to "HTML"
languages_list.append("Go")
languages_list[0] = "HTML"

# 7. Convert languages_list back into a tuple called updated_languages
updated_languages = tuple(languages_list)

# 8. Print updated_languages and its type
print(f"Updated Languages: {updated_languages}, Type: {type(updated_languages)}")

# 9. Create frontend_skills and backend_skills tuples, then join them into full_stack_skills
frontend_skills = ("HTML", "CSS", "JavaScript", "TypeScript")
backend_skills = ("Node.js", "Python", "Java")
full_stack_skills = frontend_skills + backend_skills

# 10. Print full_stack_skills and its length
print(f"Full stack skills: {full_stack_skills}\nLength: {len(full_stack_skills)}")

# 11. Create a tuple called scores with:
# 90, 85, 90, 70, 90
scores = (90, 85, 90, 70, 90)

# 12. Print how many times 90 appears and the first index of 70
print(f"Times 90 appear in scores: {scores.count(90)}\nFirst Index of 70: {scores.index(70)}")

# 13. Create a one-item tuple called single_language with the value "Python"
single_language = ("Python",)

# 14. Print single_language and its type
print(f"Single Language Tuple: {single_language}, Type: {type(single_language)}")

# 15. Create a tuple called coordinates with values 10 and 20, then reassign it to 30 and 40
coordinates = (10, 20)
coordinates = (30, 40)

# 16. Print coordinates
print(f"Updated coordinates: {coordinates}")

# 17. Create a list called changing_tasks with "study", "practice", "review", then append "submit"
changing_tasks = ["study", "practice", "review"]
changing_tasks.append("submit")

# 18. Print changing_tasks
print(changing_tasks)

# 19. Add a comment explaining why changing_tasks should be a list
# changing_tasks should be a list because skills can change over time

# 20. Add a comment explaining why coordinates should be a tuple
# coordinates should be a tuple because it represents a fixed pair of values