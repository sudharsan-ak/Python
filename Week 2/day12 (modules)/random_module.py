# Day 12 - Topic 4: Built-in random module
print(f"{"-" * 30}Topic 4{"-" * 30}")
# 1. Import the random module
import random

# 2. Create a list called study_topics with:
# "Modules", "Functions", "Loops", "Dictionaries", "Conditionals"
study_topics = ["Modules", "Functions", "Loops", "Dictionaries", "Conditionals"]

# 3. Use random.choice() to select one topic from study_topics
# Store the result in a variable called selected_topic
selected_topic = random.choice(study_topics)

# 4. Print selected_topic with this format:
# Selected topic: <selected_topic>
print(f"Selected topic: {selected_topic}")

# 5. Use random.randint() to generate a random study score between 70 and 100
# Store the result in a variable called study_score
study_score = random.randint(70, 100)

# 6. Print study_score with this format:
# Study score: <study_score>
print(f"Study score: {study_score}")

# 7. Use random.random() to generate a random decimal
# Store the result in a variable called random_decimal
random_decimal = random.random()

# 8. Print random_decimal with this format:
# Random decimal: <random_decimal>
print(f"Random decimal: {random_decimal}")

# 9. Create a list called review_tasks with:
# "Read notes", "Practice code", "Fix mistakes", "Review output"
review_tasks = ["Read notes", "Practice code", "Fix mistakes", "Review output"]

# 10. Use random.shuffle() to shuffle review_tasks
random.shuffle(review_tasks)

# 11. Print review_tasks with this format:
# Shuffled tasks: <review_tasks>
print(f"Shuffled tasks: {review_tasks}")

# 12. Print the type of study_score with this format:
# Study score type: <type>
print(f"Study score type: {type(study_score)}")

# 13. Print the type of random_decimal with this format:
# Random decimal type: <type>
print(f"Random decimal type: {type(random_decimal)}")