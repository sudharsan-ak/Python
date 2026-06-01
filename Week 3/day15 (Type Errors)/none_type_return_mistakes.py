print(f"{'-' * 30} Topic 4: NoneType and Return Mistakes {'-' * 30}")

# ------------------------------------------------------------
# Exercise 1
# This function prints a value but does not return it.

def show_student_name():
    print("Sudharsan")

# broken_student_name = show_student_name()
# print(f"Student name from function: {broken_student_name}")

# Fix it by creating a new function called get_student_name.
# It should return "Sudharsan".
# Store the returned value in student_name.
# Print student_name.
def get_student_name():
    return "Sudharsan"

student_name = get_student_name()
print(f"Student name from function: {student_name}")

# ------------------------------------------------------------
# Exercise 2
# This function calculates a total but forgets to return it.

def calculate_total(score, bonus):
    total = score + bonus

# broken_total = calculate_total(80, 10)
# print(broken_total + 5)

# Fix calculate_total by creating a corrected function called get_total_score.
# It should return the total.
# Store the result in total_score.
# Print total_score.
def get_total_score(score, bonus):
    return score + bonus

total_score = get_total_score(80, 10)
print(f"Total score: {total_score}")

# ------------------------------------------------------------
# Exercise 3
# The broken code assigns the result of .sort().

scores = [88, 95, 72, 100]

# sorted_scores = scores.sort()
# print(sorted_scores)

# Fix it two ways:
# 1. Sort scores in place and print scores.
# 2. Create a new sorted list using sorted() and print it.

# Method 1:
scores.sort()
print(f"Sorted scores Method 1: {scores}")

# Method 2:
sorted_scores = sorted(scores)
print(f"Sorted scores Method 2: {sorted_scores}")

# ------------------------------------------------------------
# Exercise 4
# The broken code assigns the result of .append().

skills = ["Python", "React"]

# updated_skills = skills.append("Node.js")
# print(updated_skills)

# Fix it by appending "Node.js" correctly.
# Then print skills.

# If we want to update skills variable directly, then
skills.append("Node.js")
print(f"Updated Original skills: {skills}")

# If we don't want to affect the original skills, then
# updated_skills = skills + ["Node.js"]
# print(f"Updated skills: {updated_skills}")

# ------------------------------------------------------------
# Exercise 5
# The broken line tries to call a string method on None.

student_city = None

# city_upper = student_city.upper()

# Do not force a fake fix.
# Write a comment explaining why this fails.
# Then create a new variable safe_city with the fallback value "Not provided".
# Print safe_city.

# Answer: This throws an AttributeError because a NonType object has no attribute 'upper'
safe_city = student_city.upper() if student_city else "Not provided"
print(f"Safe city: {safe_city}")

# ------------------------------------------------------------
# Exercise 6
# Dictionary get() can return None if no fallback is given.

profile = {
    "name": "Sudharsan",
    "role": "Software Engineer"
}

# city = profile.get("city")

# broken_city = city.upper()

# Fix it by using get() with a fallback value of "Not provided".
# Then print the uppercase version of the fixed city value.
fixed_city = profile.get("city", "Not provided")
print(f"Fixed city: {fixed_city.upper()}")