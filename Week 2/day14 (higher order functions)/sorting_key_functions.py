# Topic 5: Sorting with key functions

print(f"{'-' * 30} Topic 5 {'-' * 30}")

# 1. Create a list called numbers with values:
# 45, 12, 89, 33, 7
numbers = [45, 12, 89, 33, 7]

# 2. Use sorted() to create sorted_numbers
# Print: Sorted numbers: <list>
sorted_numbers = sorted(numbers)
print(f"Sorted numbers: {sorted_numbers}")

# 3. Print the original numbers list
# Print: Original numbers: <list>
print(f"Original numbers: {numbers}")

# 4. Create a list called names with values:
# "Sudharsan", "Ashwin", "Python", "AI", "Lambda"
names = ["Sudharsan", "Ashwin", "Python", "AI", "Lambda"]

# 5. Use sorted() with key=len to create names_by_length
# Print: Names by length: <list>
names_by_length = sorted(names, key=len)
print(f"Names by length: {names_by_length}")

# 6. Use sorted() with key=len and reverse=True
# Store the result in names_by_length_desc
# Print: Names by length desc: <list>
names_by_length_desc = sorted(names, key=len, reverse=True)
print(f"Names by length desc: {names_by_length_desc}")

# 7. Create a list called students with these dictionaries:
# {"name": "Sudharsan", "score": 88}
# {"name": "Ashwin", "score": 95}
# {"name": "Python Learner", "score": 72}
# {"name": "Lambda Student", "score": 88}
students = [
    {"name": "Sudharsan", "score": 88},
    {"name": "Ashwin", "score": 95},
    {"name": "Python Learner", "score": 72},
    {"name": "Lambda Student", "score": 88}
]

# 8. Use sorted() with a lambda to sort students by score
# Store the result in students_by_score
# Print: Students by score: <list>
students_by_score = sorted(students, key=lambda student: student["score"])
print(f"Students by score: {students_by_score}")

# 9. Use sorted() with a lambda and reverse=True
# Sort students by score from highest to lowest
# Store the result in students_by_score_desc
# Print: Students by score desc: <list>
students_by_score_desc = sorted(students, key=lambda student: student["score"], reverse=True)
print(f"Students by score desc: {students_by_score_desc}")

# 10. Create a normal function called get_student_name
# It should accept one parameter called student
# It should return student["name"]
def get_student_name(student):
    return student["name"]

# 11. Use sorted() with get_student_name to sort students by name
# Store the result in students_by_name
# Print: Students by name: <list>
students_by_name = sorted(students, key=get_student_name)
print(f"Students by name: {students_by_name}")

# 12. Use sorted() with a lambda to sort students by:
# first score
# then name
# Store the result in students_by_score_then_name
# Print: Students by score then name: <list>
students_by_score_then_name = sorted(students, key=lambda student: (student["score"], student["name"]))
print(f"Students by score then name: {students_by_score_then_name}")

# 13. Create a list called jobs with these dictionaries:
# {"title": "Frontend Engineer", "match_score": 82, "applications": 40}
# {"title": "Backend Engineer", "match_score": 75, "applications": 25}
# {"title": "Full Stack Engineer", "match_score": 91, "applications": 55}
# {"title": "Python Developer", "match_score": 68, "applications": 15}
jobs = [
    {"title": "Frontend Engineer", "match_score": 82, "applications": 40},
    {"title": "Backend Engineer", "match_score": 75, "applications": 25},
    {"title": "Full Stack Engineer", "match_score": 91, "applications": 55},
    {"title": "Python Developer", "match_score": 68, "applications": 15}
]

# 14. Use sorted() with a lambda and reverse=True
# Sort jobs by match_score from highest to lowest
# Store the result in jobs_by_match
# Print: Jobs by match: <list>
jobs_by_match = sorted(jobs, key=lambda job: job["match_score"], reverse=True)
print(f"Jobs by match: {jobs_by_match}")

# 15. Create a normal function called get_application_count
# It should accept one parameter called job
# It should return job["applications"]
def get_application_count(job):
    return job["applications"]

# 16. Use sorted() with get_application_count
# Sort jobs by applications from lowest to highest
# Store the result in jobs_by_applications
# Print: Jobs by applications: <list>
jobs_by_applications = sorted(jobs, key=get_application_count)
print(f"Jobs by applications: {jobs_by_applications}")

# 17. Create a copy of numbers called numbers_copy
numbers_copy = numbers.copy()

# 18. Use .sort() on numbers_copy
# Print: Numbers copy after sort: <list>
numbers_copy.sort()
print(f"Numbers copy after sort: {numbers_copy}")

# 19. Print the original numbers list again
# Print: Original numbers after copy sort: <list>
print(f"Original numbers after copy sort: {numbers}")

# 20. Add a comment explaining the difference between sorted() and .sort()
# sort() modifies the original list whereas sorted() creates a new sorted list

# 21. Add a comment explaining when lambda is okay for key=
# when the key is tiny and the logic will not grow or reused, then key=lambda is better, if not use a def function