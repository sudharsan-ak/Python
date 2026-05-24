# Exercise 1: Creating lists and checking length

# 1. Create an empty list called empty_list
empty_list = []

# 2. Print empty_list
print(empty_list)

# 3. Print the length of empty_list
print(len(empty_list))

# 4. Create a list called skills with these values:
# JavaScript, React, Node, Python, MongoDB
skills = ["JavaScript", "React", "Node", "Python", "MongoDB"]

# 5. Print skills
print(skills)

# 6. Print the length of skills
print(len(skills))

# 7. Create a list called cities with 5 city names
cities = ["New York", "San Francisco", "Chicago", "Dallas", "Los Angeles"]

# 8. Print cities
print(cities)

# 9. Print the length of cities
print(len(cities))

# 10. Create a list called mixed_data_types with your name, age, height, is_learning_python, and city
mixed_data_types = ["Sudharsan", 30, 5.1, True, "Lewisville"]

# 11. Print mixed_data_types
print(mixed_data_types)

# 12. Print the length of mixed_data_types
print(len(mixed_data_types))

# ---------------------------------------------------------------------
# Exercise 2: Indexing, negative indexing, and slicing lists
# 1. Print the first item from skills
print(skills[0])

# 2. Print the second item from skills
print(skills[1])

# 3. Print the last item from skills using negative indexing
print(skills[-1])

# 4. Print the second-to-last item from skills using negative indexing
print(skills[-2])

# 5. Print the first city from cities
print(cities[0])

# 6. Print the last city from cities using negative indexing
print(cities[-1])

# 7. Print the first 3 items from skills using slicing
print(skills[:3])

# 8. Print all items from skills starting from index 2
print(skills[2:])

# 9. Print the last 2 cities using slicing
print(cities[-2:])

# 10. Print a full copy of skills using slicing
print(skills[:])

# 11. Print your name from mixed_data_types using indexing
print(mixed_data_types[0])

# 12. Print your city from mixed_data_types using negative indexing
print(mixed_data_types[-1])

# ---------------------------------------------------------------------
# Exercise 3: Checking items and modifying list items
# 1. Check whether "Python" exists in skills and store the result in has_python
has_python = "Python" in skills

# 2. Print has_python
print(has_python)

# 3. Check whether "Java" exists in skills and store the result in has_java
has_java = "Java" in skills

# 4. Print has_java
print(has_java)

# 5. Check whether "Dallas" exists in cities and store the result in has_dallas
has_dallas = "Dallas" in cities

# 6. Print has_dallas
print(has_dallas)

# 7. Change "Node" in skills to "Node.js" using indexing
skills[2] = "Node.js"

# 8. Print skills
print(skills)

# 9. Change the last item in skills to "PostgreSQL" using negative indexing
skills[-1] = "PostgreSQL"

# 10. Print skills
print(skills)

# 11. Change your height in mixed_data_types to a different number using indexing
mixed_data_types[2] = 5.5

# 12. Print mixed_data_types
print(mixed_data_types)

# 13. Check whether your city exists in mixed_data_types and store the result in has_city
has_city = "Lewisville" in mixed_data_types

# 14. Print has_city
print(has_city)

# ---------------------------------------------------------------------
# Exercise 4: Adding items with append(), insert(), and extend()
# 1. Add "AWS" to the end of skills using append()
skills.append("AWS")

# 2. Print skills
print(skills)

# 3. Insert "TypeScript" at index 1 in skills
skills.insert(1, "TypeScript")

# 4. Print skills
print(skills)

# 5. Create a list called backend_skills with these values:
# Express, PostgreSQL, Docker
backend_skills = ["Express", "PostgreSQL", "Docker"]

# 6. Add all backend_skills into skills using extend()
skills.extend(backend_skills)

# 7. Print skills
print(skills)

# 8. Add "Houston" to the end of cities using append()
cities.append("Houston")

# 9. Print cities
print(cities)

# 10. Insert "Austin" at index 1 in cities
cities.insert(1, "Austin")

# 11. Print cities
print(cities)

# 12. Create a list called more_cities with these values:
# Seattle, Boston, Denver
more_cities = ["Seattle", "Boston", "Denver"]

# 13. Add all more_cities into cities using extend()
cities.extend(more_cities)

# 14. Print cities
print(cities)

# 15. Print the length of skills
print(len(skills))

# 16. Print the length of cities
print(len(cities))

# ---------------------------------------------------------------------
# Exercise 5: Removing items with remove(), pop(), del, and clear()
# 1. Remove "AWS" from skills using remove()
skills.remove("AWS")

# 2. Print skills
print(skills)

# 3. Remove "Austin" from cities using remove()
cities.remove("Austin")

# 4. Print cities
print(cities)

# 5. Remove the last item from skills using pop() and store it in removed_skill
removed_skill = skills.pop()

# 6. Print removed_skill
print(removed_skill)

# 7. Print skills
print(skills)

# 8. Remove the first item from cities using pop(0) and store it in removed_city
removed_city = cities.pop(0)

# 9. Print removed_city
print(removed_city)

# 10. Print cities
print(cities)

# 11. Delete the item at index 1 from skills using del
del skills[1]

# 12. Print skills
print(skills)

# 13. Delete the last 2 cities using del and slicing
del cities[-2:]

# 14. Print cities
print(cities)

# 15. Create a list called temporary_items with these values:
# draft, test, sample
temporary_items = ["draft", "test", "sample"]

# 16. Print temporary_items
print(temporary_items)

# 17. Clear temporary_items using clear()
temporary_items.clear()

# 18. Print temporary_items
print(temporary_items)

# 19. Print the length of temporary_items
print(len(temporary_items))

# ---------------------------------------------------------------------
# Exercise 6: Copying and joining lists
# 1. Create a copy of skills called skills_copy using copy()
skills_copy = skills.copy()

# 2. Print skills_copy
print(skills_copy)

# 3. Add "GraphQL" to skills_copy using append()
skills_copy.append("GraphQL")

# 4. Print skills_copy
print(skills_copy)

# 5. Print the original skills list to confirm it did not change
print(skills)

# 6. Create a copy of cities called cities_copy using slicing
cities_copy = cities[:]

# 7. Print cities_copy
print(cities_copy)

# 8. Add "Miami" to cities_copy using append()
cities_copy.append("Miami")

# 9. Print cities_copy
print(cities_copy)

# 10. Print the original cities list to confirm it did not change
print(cities)

# 11. Create a list called frontend_skills with:
# HTML, CSS, JavaScript, React
frontend_skills = ["HTML", "CSS", "JavaScript", "React"]

# 12. Create a list called backend_skills_v2 with:
# Node.js, Express, MongoDB, PostgreSQL
backend_skills_v2 = ["Node.js", "Express", "MongoDB", "PostgreSQL"]

# 13. Join frontend_skills and backend_skills_v2 into a new list called full_stack_skills using +
full_stack_skills = frontend_skills + backend_skills_v2

# 14. Print full_stack_skills
print(full_stack_skills)

# 15. Print frontend_skills to confirm it did not change
print(frontend_skills)

# 16. Print backend_skills_v2 to confirm it did not change
print(backend_skills_v2)

# 17. Print the length of full_stack_skills
print(len(full_stack_skills))

# ---------------------------------------------------------------------
# Exercise 7: count(), index(), reverse(), sort(), and sorted()
# 1. Count how many times "PostgreSQL" appears in skills and store it in postgres_count
postgres_count = skills.count("PostgreSQL")

# 2. Print postgres_count
print(postgres_count)

# 3. Count how many times "Java" appears in skills and store it in java_count
java_count = skills.count("Java")

# 4. Print java_count
print(java_count)

# 5. Find the index of "Python" in skills and store it in python_index
python_index = skills.index("Python")

# 6. Print python_index
print(python_index)

# 7. Find the index of "Dallas" in cities and store it in dallas_index
dallas_index = cities.index("Dallas")

# 8. Print dallas_index
print(dallas_index)

# 9. Create a list called numbers with these values:
# 42, 7, 19, 100, 3
numbers = [42, 7, 19, 100, 3]

# 10. Print numbers
print(numbers)

# 11. Create a sorted copy of numbers called sorted_numbers using sorted()
sorted_numbers = sorted(numbers)

# 12. Print sorted_numbers
print(sorted_numbers)

# 13. Print the original numbers list to confirm it did not change
print(numbers)

# 14. Sort numbers in place using sort()
numbers.sort()

# 15. Print numbers
print(numbers)

# 16. Sort numbers in descending order using sort(reverse=True)
numbers.sort(reverse=True)

# 17. Print numbers
print(numbers)

# 18. Reverse cities in place using reverse()
cities.reverse()

# 19. Print cities
print(cities)

# 20. Create a sorted copy of full_stack_skills called sorted_full_stack_skills using sorted()
sorted_full_stack_skills = sorted(full_stack_skills)

# 21. Print sorted_full_stack_skills
print(sorted_full_stack_skills)

# 22. Print full_stack_skills to confirm it did not change
print(full_stack_skills)