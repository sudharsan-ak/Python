# ---------------------------------------------------------------------
# Topic 1: Set Basics
# 1. Create a set called languages with:
# "JavaScript", "TypeScript", "Python", "Java", "Python"
languages = {"JavaScript", "TypeScript", "Python", "Java", "Python"}

# 2. Print languages
print(languages)

# 3. Print the length of languages
print(len(languages))

# 4. Print the type of languages
print(type(languages))

# 5. Create an empty set called empty_skills using set()
empty_skills = set()

# 6. Print empty_skills
print(empty_skills)

# 7. Print the type of empty_skills
print(type(empty_skills))

# 8. Create a set called duplicate_numbers with:
# 10, 20, 20, 30, 30, 40
duplicate_numbers = {10, 20, 20, 30, 30, 40}

# 9. Print duplicate_numbers
print(duplicate_numbers)

# 10. Print the length of duplicate_numbers
print(len(duplicate_numbers))

# 11. Create a variable called empty_data and set it to {}
empty_data = {}

# 12. Print the type of empty_data
print(type(empty_data))

# ---------------------------------------------------------------------
# Topic 2: Membership Checks + No Indexing
# 1. Check whether "Python" exists in languages and store it in has_python
has_python = "Python" in languages

# 2. Print has_python
print(f"Does Python exist: {has_python}")

# 3. Check whether "Go" exists in languages and store it in has_go
has_go = "Go" in languages

# 4. Print has_go
print(f"Does Go exist: {has_go}")

# 5. Check whether "Rust" does not exist in languages and store it in missing_rust
missing_rust = "Rust" not in languages

# 6. Print missing_rust
print(f"Is Rust missing: {missing_rust}")

# 7. Create a set called frontend_skills with:
# "HTML", "CSS", "JavaScript", "React"
frontend_skills = {"HTML", "CSS", "JavaScript", "React"}

# 8. Check whether "React" exists in frontend_skills and store it in has_react
has_react = "React" in frontend_skills

# 9. Print has_react
print(f"Does React exist in frontend skills: {has_react}")

# 10. Check whether "Node.js" does not exist in frontend_skills and store it in missing_node
missing_node = "Node.js" not in frontend_skills

# 11. Print missing_node
print(f"Is Node.js missing from frontend skills: {missing_node}")

# 12. Add a comment explaining why we should not use frontend_skills[0]
# Because frontend_skills is a set, and sets do not support indexing because they do not have a reliable order.

# ---------------------------------------------------------------------
# Topic 3: Adding and Updating Sets
# 1. Add "TypeScript" to frontend_skills using add()
frontend_skills.add("TypeScript")

# 2. Print frontend_skills
print(f"TypeScript Added: {frontend_skills}")

# 3. Add "React" again using add()
frontend_skills.add("React")

# 4. Print frontend_skills and notice that "React" is not duplicated
print(f"React Added: {frontend_skills}")

# 5. Create a set called backend_skills with:
# "Node.js", "Express", "MongoDB"
backend_skills = {"Node.js", "Express", "MongoDB"}

# 6. Add "PostgreSQL" to backend_skills using add()
backend_skills.add("PostgreSQL")

# 7. Print backend_skills
print(f"Backend Skills: {backend_skills}")

# 8. Update backend_skills with this list:
# ["Docker", "AWS Lambda", "Node.js"]
backend_skills.update(["Docker", "AWS Lambda", "Node.js"])

# 9. Print backend_skills
print(f"Updated backend skills: {backend_skills}")

# 10. Create a set called full_stack_skills with:
# "JavaScript", "React"
full_stack_skills = {"JavaScript", "React"}

# 11. Update full_stack_skills using frontend_skills
full_stack_skills.update(frontend_skills)

# 12. Update full_stack_skills using backend_skills
full_stack_skills.update(backend_skills)

# 13. Print full_stack_skills
print(f"Final Updated Full Stack Skills: {full_stack_skills}")

# 14. Add a comment explaining the difference between add() and update()
# add() is used to add one item/value to a set, update() is to add multiple items

# ---------------------------------------------------------------------
# Topic 4: Removing, Clearing, and Deleting Sets
# 1. Remove "Express" from backend_skills using remove()
backend_skills.remove("Express")

# 2. Print backend_skills
print(f"Backend Skills after Express removed: {backend_skills}")

# 3. Discard "Java" from backend_skills using discard()
backend_skills.discard("Java")

# 4. Print backend_skills
print(f"Backend Skills after Java discarded: {backend_skills}")

# 5. Discard "MongoDB" from backend_skills using discard()
backend_skills.discard("MongoDB")

# 6. Print backend_skills
print(f"Backend Skills after MongoDB discarded: {backend_skills}")

# 7. Use pop() on full_stack_skills and store the removed item in removed_skill
removed_skill = full_stack_skills.pop()

# 8. Print removed_skill
print(f"Removed skill from Full stack skills: {removed_skill}")

# 9. Print full_stack_skills
print(f"Full stack skills after pop: {full_stack_skills}")

# 10. Create a set called temporary_skills with:
# "Draft", "Test", "Sample"
temporary_skills = {"Draft", "Test", "Sample"}

# 11. Clear temporary_skills using clear()
temporary_skills.clear()

# 12. Print temporary_skills
print(f"Temporary skills cleared: {temporary_skills}")

# 13. Create a set called old_skills with:
# "COBOL", "Mainframe"
old_skills = {"COBOL", "Mainframe"}

# 14. Delete old_skills using del
del old_skills

# 15. Add a comment explaining why printing old_skills after del would fail
# since we used del to remove the entire variable, it doesnt exist anymore and therefore print would fail

# 16. Add a comment explaining the difference between remove() and discard()
# Both are use to remove item from set. Remove throws an error when the item to be removed isnt present in the set whereas discard safely removes it without crashing

# ---------------------------------------------------------------------
# Topic 5: Converting Lists/Tuples to Sets
# 1. Create a list called skills_list with:
# "JavaScript", "React", "Python", "React", "JavaScript", "Node.js"
skills_list = ["JavaScript", "React", "Python", "React", "JavaScript", "Node.js"]

# 2. Convert skills_list into a set called unique_skills
unique_skills = set(skills_list)

# 3. Print unique_skills
print(f"Unique Skills set: {unique_skills}")

# 4. Print the length of skills_list
print(f"Length of skills list: {len(skills_list)}")

# 5. Print the length of unique_skills
print(f"Length of unique skills set: {len(unique_skills)}")

# 6. Create a tuple called scores_tuple with:
# 90, 85, 90, 70, 85, 100
scores_tuple = (90, 85, 90, 70, 85, 100)

# 7. Convert scores_tuple into a set called unique_scores
unique_scores = set(scores_tuple)

# 8. Print unique_scores
print(f"Unique Scores: {unique_scores}")

# 9. Print the type of unique_scores
print(f"Type of unique scores: {type(unique_scores)}")

# 10. Convert unique_skills back into a list called unique_skills_list
unique_skills_list = list(unique_skills)

# 11. Print unique_skills_list
print(f"Final converted List: {unique_skills_list}")

# 12. Add a comment explaining why the order of unique_skills_list should not be trusted
# The order should not be trusted because converting to a set removes dependable ordering.

# ---------------------------------------------------------------------
# Topic 6: Core Set Operations
# 1. Create a set called frontend_required with:
# "HTML", "CSS", "JavaScript", "React"
frontend_required = {"HTML", "CSS", "JavaScript", "React"}

# 2. Create a set called backend_required with:
# "JavaScript", "Node.js", "Express", "MongoDB"
backend_required = {"JavaScript", "Node.js", "Express", "MongoDB"}

# 3. Create a variable called all_required_skills using union()
all_required_skills = frontend_required.union(backend_required)

# 4. Print all_required_skills
print(f"All required skills: {all_required_skills}")

# 5. Create a variable called common_required_skills using intersection()
common_required_skills = frontend_required.intersection(backend_required)

# 6. Print common_required_skills
print(f"Common skills: {common_required_skills}")

# 7. Create a variable called frontend_only_skills using difference()
frontend_only_skills = frontend_required.difference(backend_required)

# 8. Print frontend_only_skills
print(f"Frontend only: {frontend_only_skills}")

# 9. Create a variable called backend_only_skills using difference()
backend_only_skills = backend_required.difference(frontend_required)

# 10. Print backend_only_skills
print(f"Backend only: {backend_only_skills}")

# 11. Create a variable called not_shared_skills using symmetric_difference()
not_shared_skills = frontend_required.symmetric_difference(backend_required)

# 12. Print not_shared_skills
print(f"Not shared skills: {not_shared_skills}")

# 13. Add a comment explaining why difference() direction matters
# Because difference gives the items in first set not in second, if direction changes then output differs

# 14. Add a comment explaining the difference between intersection() and symmetric_difference()
# intersection gives the common item between 2 sets, whereas symmetric_difference gives only the items that are in either sets but not both

# ---------------------------------------------------------------------
# Topic 7: Set Relationship Checks
# 1. Create a set called required_skills with:
# "JavaScript", "React", "Node.js"
required_skills = {"JavaScript", "React", "Node.js"}

# 2. Create a set called candidate_skills with:
# "JavaScript", "React", "Node.js", "MongoDB", "Docker"
candidate_skills = {"JavaScript", "React", "Node.js", "MongoDB", "Docker"}

# 3. Check whether required_skills is a subset of candidate_skills
# Store the result in required_is_subset
required_is_subset = required_skills.issubset(candidate_skills)

# 4. Print required_is_subset
print(f"Is Required a subset of candidate skills: {required_is_subset}")

# 5. Check whether candidate_skills is a superset of required_skills
# Store the result in candidate_is_superset
candidate_is_superset = candidate_skills.issuperset(required_skills)

# 6. Print candidate_is_superset
print(f"Is Candidate a superset of required skills: {candidate_is_superset}")

# 7. Create a set called frontend_skills_check with:
# "HTML", "CSS", "React"
frontend_skills_check = {"HTML", "CSS", "React"}

# 8. Create a set called database_skills_check with:
# "MongoDB", "PostgreSQL"
database_skills_check = {"MongoDB", "PostgreSQL"}

# 9. Check whether frontend_skills_check and database_skills_check are disjoint
# Store the result in frontend_database_disjoint
frontend_database_disjoint = frontend_skills_check.isdisjoint(database_skills_check)

# 10. Print frontend_database_disjoint
print(f"Frontend database disjoint: {frontend_database_disjoint}")

# 11. Create a set called full_stack_skills_check with:
# "React", "Node.js", "MongoDB"
full_stack_skills_check = {"React", "Node.js", "MongoDB"}

# 12. Check whether frontend_skills_check and full_stack_skills_check are disjoint
# Store the result in frontend_full_stack_disjoint
frontend_full_stack_disjoint = frontend_skills_check.isdisjoint(full_stack_skills_check)

# 13. Print frontend_full_stack_disjoint
print(f"Frontend full stack disjoint: {frontend_full_stack_disjoint}")

# 14. Add a comment explaining the difference between issubset() and issuperset()
# A.issubset(B) -> is everything in A inside B, A.issuperset(B) -> does A contain everything in B

# 15. Add a comment explaining what isdisjoint() checks
# Disjoint checks to see if 2 sets have zero overlap