# Day 5 Final Mixed Exercise - Lists
# Scenario: Manage a small software engineer profile
# 1. Create a list called skills with these values:
# JavaScript, React, Node.js, Python, MongoDB
skills = ["JavaScript", "React", "Node.js", "Python", "MongoDB"]

# 2. Print the full skills list
print(skills)

# 3. Print the length of skills
print(len(skills))

# 4. Print the first skill
print(skills[0])

# 5. Print the last skill using negative indexing
print(skills[-1])

# 6. Print the first 3 skills using slicing
print(skills[:3])

# 7. Check whether "Python" exists in skills and store the result in has_python
has_python = "Python" in skills

# 8. Print has_python
print(has_python)

# 9. Change "MongoDB" to "PostgreSQL" using negative indexing
skills[-1] = "PostgreSQL"

# 10. Print skills
print(skills)

# 11. Add "AWS" to the end of skills using append()
skills.append("AWS")

# 12. Insert "TypeScript" at index 1
skills.insert(1, "TypeScript")

# 13. Create a list called backend_skills with:
# Express, Docker, PostgreSQL
backend_skills = ["Express", "Docker", "PostgreSQL"]

# 14. Add all backend_skills into skills using extend()
skills.extend(backend_skills)

# 15. Remove "AWS" from skills using remove()
skills.remove("AWS")

# 16. Remove the last item from skills using pop() and store it in removed_skill
removed_skill = skills.pop()

# 17. Print removed_skill
print(removed_skill)

# 18. Create a copy of skills called skills_copy using copy()
skills_copy = skills.copy()

# 19. Sort skills_copy alphabetically using sort()
skills_copy.sort()

# 20. Print both skills and skills_copy to prove the original order did not change
print("Original skills- ", skills)
print("Copied and Sorted skills- ", skills_copy)