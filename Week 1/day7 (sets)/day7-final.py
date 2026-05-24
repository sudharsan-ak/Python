# ---------------------------------------------------------------------
# Day 7 - Final Mixed Exercise: Sets
# 1. Create a set called languages with:
# "JavaScript", "Python", "Java", "Python", "TypeScript"
languages = {"JavaScript", "Python", "Java", "Python", "TypeScript"}

# 2. Print languages and its length
print(f"Languages: {languages}, Length: {len(languages)}")

# 3. Create an empty set called empty_tools using set()
empty_tools = set()

# 4. Print the type of empty_tools
print(f"Type of Empty tools: {type(empty_tools)}")

# 5. Check whether "Python" exists in languages and store it in has_python
has_python = "Python" in languages

# 6. Check whether "Go" does not exist in languages and store it in missing_go
missing_go = "Go" not in languages

# 7. Print has_python and missing_go
print(f"Does Python exist in languages: {has_python}, and is Go missing in languages: {missing_go}")

# 8. Add "Go" to languages using add()
languages.add("Go")

# 9. Update languages with this list:
# ["Rust", "JavaScript", "C#"]
languages.update(["Rust", "JavaScript", "C#"])

# 10. Print languages
print(f"Updated Languages: {languages}")

# 11. Remove "Java" from languages using remove()
languages.remove("Java")

# 12. Discard "Ruby" from languages using discard()
languages.discard("Ruby")

# 13. Print languages
print(f"Languages after modifications: {languages}")

# 14. Create a list called skill_list with:
# "React", "Node.js", "React", "MongoDB", "Node.js", "Docker"
skill_list = ["React", "Node.js", "React", "MongoDB", "Node.js", "Docker"]

# 15. Convert skill_list into a set called unique_skills and print it
unique_skills = set(skill_list)
print(f"Unique Skills: {unique_skills}")

# 16. Create two sets:
# frontend_skills = {"HTML", "CSS", "JavaScript", "React"}
# backend_skills = {"JavaScript", "Node.js", "Express", "MongoDB"}
frontend_skills = {"HTML", "CSS", "JavaScript", "React"}
backend_skills = {"JavaScript", "Node.js", "Express", "MongoDB"}

# 17. Create and print:
# all_skills using union()
# common_skills using intersection()
# frontend_only using difference()
# not_shared using symmetric_difference()
all_skills = frontend_skills.union(backend_skills)
common_skills = frontend_skills.intersection(backend_skills)
frontend_only = frontend_skills.difference(backend_skills)
not_shared = frontend_skills.symmetric_difference(backend_skills)

print(f"All Skills: {all_skills}")
print(f"Common Skills: {common_skills}")
print(f"Frontend Only Skills: {frontend_only}")
print(f"Skills not shared between frontend and backend: {not_shared}")

# 18. Create:
# required_skills = {"JavaScript", "React"}
# candidate_skills = {"JavaScript", "React", "Node.js", "MongoDB"}
required_skills = {"JavaScript", "React"}
candidate_skills = {"JavaScript", "React", "Node.js", "MongoDB"}

# 19. Check and print whether required_skills is a subset of candidate_skills
required_is_subset = required_skills.issubset(candidate_skills)
print(f"Is required_skills a subset of candidate_skills? {required_is_subset}")

# 20. Check and print whether candidate_skills is a superset of required_skills
candidate_is_superset = candidate_skills.issuperset(required_skills)
print(f"Is candidate_skills a superset of required_skills? {candidate_is_superset}")

# 21. Add a comment explaining when you would choose a set over a list
# A set is ideal when you need to store unique items and perform operations like union, intersection, and difference efficiently. It is also faster for membership testing compared to a list. 
# A list is better when you need to maintain the order of elements or allow duplicates.