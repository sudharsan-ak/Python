# ---------------------------------------------------------------------
# Day 8 - Final Mixed Exercise: Dictionaries

# 1. Create a dictionary called enrollment with:
# "student" -> your full name
# "course" -> "Backend Development"
# "level" -> "Beginner"
# "active" -> True
# "completed_lessons" -> 4
enrollment = {
    "student": "Sudharsan Srinivasan",
    "course": "Backend Development",
    "level": "Beginner",
    "active": True,
    "completed_lessons": 4
}

# 2. Print the whole enrollment dictionary with a clear label
print(f"Enrollment dictionary: {enrollment}")

# 3. Print the length and type of enrollment
print(f"Enrollment dictionary length: {len(enrollment)}, and type: {type(enrollment)}")

# 4. Print the student and course values using square bracket access
print(f"Enrollment Student: {enrollment['student']}, Enrollment course: {enrollment['course']}")

# 5. Safely get "certificate_status" from enrollment using get()
# Use "Not started" as the default value
# Store it in certificate_status
certificate_status = enrollment.get("certificate_status", "Not started")

# 6. Print certificate_status with a clear label
print(f"Certificate status: {certificate_status}")

# 7. Check whether "active" exists as a key in enrollment
# Store the result in has_active_status
has_active_status = "active" in enrollment

# 8. Print has_active_status with a clear label
print(f'Is "active" key present in enrollment: {has_active_status}')

# 9. Add a new key called "platform" with the value "Self-paced"
enrollment["platform"] = "Self-paced"

# 10. Update "completed_lessons" to 8
enrollment["completed_lessons"] = 8

# 11. Use update() to add:
# "language" -> "Python"
# "practice_file" -> "day8_final.py"
enrollment.update({
    "language": "Python",
    "practice_file": "day8_final.py"
})

# 12. Print enrollment after the additions and updates
print(f"Enrollment after addition and updates: {enrollment}")

# 13. Remove "level" using pop()
# Store the removed value in removed_level
removed_level = enrollment.pop("level")

# 14. Print removed_level and enrollment after removing level
print(f"Removed level from enrollment: {removed_level} and enrollment: {enrollment}")

# 15. Store enrollment keys, values, and items in separate variables:
# enrollment_keys
# enrollment_values
# enrollment_items
enrollment_keys = enrollment.keys()
enrollment_values = enrollment.values()
enrollment_items = enrollment.items()

# 16. Convert enrollment_keys into a list called enrollment_keys_list
# Print enrollment_keys_list and the first key from that list
enrollment_keys_list = list(enrollment_keys)
print(f"Enrollment keys list: {enrollment_keys_list}")
print(f"First key in Enrollment keys list: {enrollment_keys_list[0]}")

# 17. Create a copy of enrollment called enrollment_copy using copy()
# Update enrollment_copy["completed_lessons"] to 10
# Print both enrollment_copy and the original enrollment
enrollment_copy = enrollment.copy()
enrollment_copy["completed_lessons"] = 10
print(f"Enrollment copy: {enrollment_copy}")
print(f"Original Enrollment: {enrollment}")

# 18. Create a nested dictionary called course_progress with:
# "student" -> your full name
# "progress" -> another dictionary with:
#     "current_day" -> 8
#     "topic" -> "Dictionaries"
#     "status" -> "Final exercise"
# "review" -> another dictionary with:
#     "needs_review" -> True
#     "mistakes_found" -> 0
course_progress = {
    "student": "Sudharsan Srinivasan",
    "progress": {
        "current_day": 8,
        "topic": "Dictionaries",
        "status": "Final exercise"
    },
    "review": {
        "needs_review": True,
        "mistakes_found": 0
    }
}

# 19. Print the nested progress topic using square bracket access
print(f"Topic progress: {course_progress['progress']['topic']}")

# 20. Update the nested review "mistakes_found" to 1
course_progress["review"]["mistakes_found"] = 1

# 21. Safely get "next_topic" from the nested "progress" dictionary using get()
# Use "Conditionals" as the default value
# Store it in next_topic
progress = course_progress.get("progress", {})
next_topic = progress.get("next_topic", "Conditionals")

# 22. Print next_topic with a clear label
print(f"Next topic: {next_topic}")

# 23. Print the final course_progress dictionary
print(f"Final course progress dictionary: {course_progress}")