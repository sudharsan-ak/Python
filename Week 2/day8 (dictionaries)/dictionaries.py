# Topic 1: Dictionary Basics
# 1. Create a dictionary called profile with these key-value pairs:
# "first_name" -> your first name
# "last_name" -> your last name
# "age" -> your age as a number
# "city" -> your city
# "is_learning_python" -> True
profile = {
    "first_name": "Sudharsan",
    "last_name": "Srinivasan",
    "age": 30,
    "city": "Lewisville",
    "is_learning_python": True
}

# 2. Print the whole profile dictionary
print(f"Profile: {profile}")

# 3. Print the length of profile
print(f"Length of profile: {len(profile)}")

# 4. Print the type of profile
print(f"Type of profile: {type(profile)}")

# 5. Create an empty dictionary called empty_profile
empty_profile = {}

# 6. Print the type of empty_profile
print(f"Type of Empty profile: {type(empty_profile)}")

# 7. Create a dictionary called developer_profile with:
# "primary_language" -> "JavaScript"
# "learning_now" -> "Python"
# "years_experience" -> your years of experience as a number
# "skills" -> a list with "JavaScript", "React", "Node.js", "Python"
developer_profile = {
    "primary_language": "JavaScript",
    "learning_now": "Python",
    "years_experience": 6,
    "skills": ["JavaScript", "React", "Node.js", "Python"]
}

# 8. Print developer_profile
print(f"Developer Profile: {developer_profile}")

# 9. Print the length of developer_profile
print(f"Length of Developer Profile: {len(developer_profile)}")

# ---------------------------------------------------------------------
# Topic 2: Accessing Values Safely
# 1. Print the first_name from profile using square bracket access
print(f"First name: {profile['first_name']}")

# 2. Print the city from profile using square bracket access
print(f"City: {profile['city']}")

# 3. Store the age from profile in a variable called profile_age
profile_age = profile['age']

# 4. Print profile_age with a clear label
print(f"Profile Age: {profile_age}")

# 5. Try to get "country" from profile using get() and store it in profile_country
profile_country = profile.get("country")

# 6. Print profile_country
print(f"Profile country without default: {profile_country}")

# 7. Use get() again to get "country", but this time provide "Not provided" as the default value.
# Store it in profile_country_with_default
profile_country_with_default = profile.get("country", "Not provided")

# 8. Print profile_country_with_default
print(f"Profile country with default: {profile_country_with_default}")

# 9. Check whether "city" exists as a key in profile.
# Store the result in has_city
has_city = "city" in profile

# 10. Check whether "country" exists as a key in profile.
# Store the result in has_country
has_country = "country" in profile

# 11. Print has_city and has_country with clear labels
print(f"Is city present: {has_city}")
print(f"Is country present: {has_country}")

# 12. From developer_profile, print the primary_language using square bracket access
print(f"Primary language from Developer Profile: {developer_profile['primary_language']}")

# 13. From developer_profile, safely get "current_company" using get()
# Use "Not provided" as the default value
current_company = developer_profile.get("current_company", "Not provided")

# 14. Print the current_company result
print(f"Current company: {current_company}")

# ---------------------------------------------------------------------
# Topic 3: Adding and Updating Dictionary Data
# 1. Add a new key called "country" to profile with the value "USA"
profile["country"] = "USA"

# 2. Print profile with a clear label
print(f"Profile with country added: {profile}")

# 3. Update the "city" in profile to "Dallas"
profile["city"] = "Dallas"

# 4. Print the updated city using square bracket access
print(f"Updated city: {profile['city']}")

# 5. Add a new key called "favorite_language" to profile with the value "JavaScript"
profile["favorite_language"] = "JavaScript"

# 6. Print profile again
print(f"Updated profile: {profile}")

# 7. In developer_profile, update "learning_now" to "Python Dictionaries"
developer_profile["learning_now"] = "Python Dictionaries"

# 8. Add a new key to developer_profile called "current_topic" with the value "Adding and updating dictionaries"
developer_profile["current_topic"] = "Adding and updating dictionaries"

# 9. Print developer_profile
print(f"Developer Profile updated: {developer_profile}")
print(f"Developer Profile Length before Update : {len(developer_profile)}") # added on my own

# 10. Use update() on developer_profile to add/update these key-value pairs:
# "backend_runtime" -> "Node.js"
# "database" -> "MongoDB"
# "learning_day" -> 8
developer_profile.update({
    "backend_runtime": "Node.js",
    "database": "MongoDB",
    "learning_day": 8
})

# 11. Print developer_profile after update()
print(f"Developer profile after updates: {developer_profile}")

# 12. Print the length of developer_profile after all additions
print(f"Developer Profile Length after Update : {len(developer_profile)}")

# ---------------------------------------------------------------------
# Topic 4: Removing Dictionary Items
# 1. Remove "favorite_language" from profile using pop()
# Store the removed value in removed_favorite_language
removed_favorite_language = profile.pop("favorite_language")

# 2. Print removed_favorite_language with a clear label
print(f"Removed Language from profile: {removed_favorite_language}");

# 3. Print profile after removing favorite_language
print(f"Profile after removing favorite language: {profile}")

# 4. Try to remove "state" from profile using pop()
# Use "Not found" as the default value
# Store the result in removed_state
removed_state = profile.pop("state", "Not found")

# 5. Print removed_state with a clear label
print(f"Removed state: {removed_state}")

# 6. Remove the "country" key from profile using del
del profile["country"]

# 7. Print profile after deleting country
print(f"Profile after country deleted: {profile}")

# 8. Add a new key to profile called "temporary_status" with the value "Testing"
profile["temporary_status"] = "Testing"

# 9. Use popitem() on profile and store the result in removed_last_item
removed_last_item = profile.popitem()

# 10. Print removed_last_item with a clear label
print(f"Removed Last Item: {removed_last_item}")

# 11. Print profile after popitem()
print(f"Profile after last removed item: {profile}")

# 12. Create a dictionary called temporary_profile with:
# "name" -> "Test User"
# "status" -> "Draft"
# "type" -> "Temporary"
temporary_profile = {
    "name": "Test User",
    "status": "Draft",
    "type": "Temporary"
}

# 13. Print temporary_profile
print(f"Temporary profile: {temporary_profile}")

# 14. Clear temporary_profile using clear()
temporary_profile.clear()

# 15. Print temporary_profile after clear()
print(f"Temporary profile after clear: {temporary_profile}")

# ---------------------------------------------------------------------
# Topic 5: Dictionary Views - keys(), values(), items()
# 1. Store all keys from profile in a variable called profile_keys
profile_keys = profile.keys()

# 2. Print profile_keys with a clear label
print(f"Profile Keys: {profile_keys}")

# 3. Store all values from profile in a variable called profile_values
profile_values = profile.values()

# 4. Print profile_values with a clear label
print(f"Profile values: {profile_values}")

# 5. Store all key-value pairs from profile in a variable called profile_items
profile_items = profile.items()

# 6. Print profile_items with a clear label
print(f"Profile items: {profile_items}")

# 7. Convert profile_keys into a list called profile_keys_list
profile_keys_list = list(profile_keys)

# 8. Print profile_keys_list
print(f"Profile Keys List: {profile_keys_list}")

# 9. Print the first key from profile_keys_list
print(f"First key from profile keys list: {profile_keys_list[0]}")

# 10. Store all keys from developer_profile in developer_profile_keys
developer_profile_keys = developer_profile.keys()

# 11. Store all values from developer_profile in developer_profile_values
developer_profile_values = developer_profile.values()

# 12. Store all key-value pairs from developer_profile in developer_profile_items
developer_profile_items = developer_profile.items()

# 13. Print developer_profile_keys, developer_profile_values, and developer_profile_items with clear labels
print(f"Developer profile keys: {developer_profile_keys}")
print(f"Developer profile values: {developer_profile_values}")
print(f"Developer profile items: {developer_profile_items}")

# ---------------------------------------------------------------------
# Topic 6: Copying Dictionaries
# 1. Create a copy of profile using copy()
# Store it in profile_copy
profile_copy = profile.copy()

# 2. Print profile_copy with a clear label
print(f"Profile copy: {profile_copy}")

# 3. Update the "city" in profile_copy to "Austin"
profile_copy["city"] = "Austin"

# 4. Print profile_copy after updating city
print(f"Profile copy after city update: {profile_copy}")

# 5. Print the original profile after updating profile_copy
# Confirm the original profile city did not change
print(f"Original Profile after city update on profile copy: {profile}")

# 6. Create a direct assignment copy of developer_profile called developer_profile_reference
developer_profile_reference = developer_profile

# 7. Update "learning_day" in developer_profile_reference to 80
developer_profile_reference["learning_day"] = 80

# 8. Print developer_profile_reference
print(f"Developer profile reference: {developer_profile_reference}")

# 9. Print developer_profile
# Notice whether developer_profile also changed
print(f"Developer profile after profile reference changes: {developer_profile}")


# 10. Create a real copy of developer_profile using copy()
# Store it in developer_profile_copy
developer_profile_copy = developer_profile.copy()

# 11. Update "learning_day" in developer_profile_copy to 8
developer_profile_copy["learning_day"] = 8

# 12. Print developer_profile_copy
print(f"Developer profile copy: {developer_profile_copy}")

# 13. Print developer_profile
# Notice whether developer_profile changed this time
print(f"Original Developer profile after copy updates: {developer_profile}")

# ---------------------------------------------------------------------
# Topic 7: Nested Dictionaries
# 1. Create a dictionary called learning_profile with:
# "student_name" -> your name
# "current_day" -> 8
# "course" -> another dictionary with:
#     "name" -> "Python from Scratch"
#     "topic" -> "Dictionaries"
#     "status" -> "In progress"
learning_profile = {
    "student_name": "Sudharsan Srinivasan",
    "current_day": 8,
    "course": {
        "name": "Python from Scratch",
        "topic": "Dictionaries",
        "status": "In progress"
    }
}

# 2. Print the whole learning_profile dictionary
print(f"Learning Profile Dictionary: {learning_profile}")

# 3. Print the course name using nested square bracket access
print(f"Course name: {learning_profile['course']['name']}")

# 4. Print the course topic using nested square bracket access
print(f"Course topic: {learning_profile['course']['topic']}")

# 5. Update the nested course "status" to "Almost done"
learning_profile['course']['status'] = "Almost done"

# 6. Print the updated course status
print(f"Updated Course status: {learning_profile['course']['status']}")

# 7. Add a new nested key inside "course" called "source"
# Set it to "30 Days of Python"
learning_profile["course"]["source"] = "30 Days of Python"

# 8. Print the full nested "course" dictionary
print(f"Full nested course dictionary: {learning_profile['course']}")

# 9. Add a new top-level key called "practice"
# The value should be another dictionary with:
#     "file_name" -> "day8_dictionaries.py"
#     "exercise_count" -> 7
#     "needs_review" -> True
learning_profile["practice"] = {
    "file_name": "day8_dictionaries.py",
    "exercise_count": 7,
    "needs_review": True
} 

# 10. Print the practice file_name using nested square bracket access
print(f"Practice file name: {learning_profile['practice']['file_name']}")

# 11. Print the practice needs_review value using nested square bracket access
print(f"Practice needs review: {learning_profile['practice']['needs_review']}")

# 12. Safely get "mentor" from learning_profile using get()
# Use "Not provided" as the default value
# Store it in mentor_name
mentor_name = learning_profile.get("mentor", "Not provided")

# 13. Print mentor_name with a clear label
print(f"Mentor name: {mentor_name}")

# 14. Safely get "difficulty" from the nested "course" dictionary using get()
# Use "Beginner" as the default value
# Store it in course_difficulty
learning_profile_course = learning_profile.get("course", {})
course_difficulty = learning_profile_course.get("difficulty", "Beginner")

# 15. Print course_difficulty with a clear label
print(f"Course difficulty: {course_difficulty}")