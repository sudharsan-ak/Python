# Day 13 - Final Mixed Exercise: Comprehensions
# Scenario: Python bootcamp analytics cleanup

print(f"{'-' * 30} Day 13 Final {'-' * 30}")

# 1. Create a list called raw_topics with:
# "strings", "lists", "loops", "functions", "modules", "comprehensions"
raw_topics = ["strings", "lists", "loops", "functions", "modules", "comprehensions"]

# 2. Use list comprehension to create a list called formatted_topics.
# Each topic should be title case.
# Example: "strings" -> "Strings"
formatted_topics = [topic.title() for topic in raw_topics]

# 3. Print formatted_topics with a clear label.
print(f"Formatted topics: {formatted_topics}")

# 4. Create a list called study_minutes with:
# 25, 40, 15, 60, 35, 80, 20
study_minutes = [25, 40, 15, 60, 35, 80, 20]

# 5. Use list comprehension to create a list called long_sessions.
# It should keep only study minutes greater than or equal to 40.
long_sessions = [minutes for minutes in study_minutes if minutes >= 40]

# 6. Print long_sessions with a clear label.
print(f"Long sessions: {long_sessions}")

# 7. Use list comprehension with if / else to create a list called session_labels.
# For each value in study_minutes:
# - store "Long session" if minutes are greater than or equal to 40
# - otherwise store "Short session"
session_labels = ["Long session" if minutes >= 40 else "Short session" for minutes in study_minutes]

# 8. Print session_labels with a clear label.
print(f"Session labels: {session_labels}")

# 9. Create a nested list called weekly_scores with:
# [72, 88, 45]
# [91, 67]
# [100, 39, 84]
weekly_scores = [
    [72, 88, 45],
    [91, 67],
    [100, 39, 84]
]

# 10. Use nested list comprehension to create a list called all_scores.
# It should flatten weekly_scores into one list.
all_scores = [score for scores_group in weekly_scores for score in scores_group]

# 11. Print all_scores with a clear label.
print(f"All scores: {all_scores}")

# 12. Use dictionary comprehension to create a dictionary called score_status.
# Each key should be a score from all_scores.
# Each value should be:
# - "Pass" if the score is greater than or equal to 70
# - otherwise "Fail"
score_status = {
    score: "Pass" if score >= 70 else "Fail"
    for score in all_scores
}

# 13. Print score_status with a clear label.
print(f"Score status: {score_status}")

# 14. Use set comprehension to create a set called unique_statuses.
# It should contain the unique values from score_status.
# Expected idea: {"Pass", "Fail"}
unique_statuses = {status for status in score_status.values()}

# 15. Print unique_statuses with a clear label.
print(f"Unique Statuses: {unique_statuses}")

# 16. Create a generator expression called passing_score_generator.
# It should generate only scores from all_scores that are greater than or equal to 70.
# Convert it to a tuple called passing_scores_tuple.
passing_score_generator = (score for score in all_scores if score >= 70)
passing_scores_tuple = tuple(passing_score_generator)

# 17. Print passing_scores_tuple with a clear label.
print(f"Passing scores tuple: {passing_scores_tuple}")

# 18. Create a lambda function called is_strong_score.
# It should accept one parameter called score.
# It should return True if score is greater than or equal to 90.
is_strong_score = lambda score: score >= 90

# 19. Use list comprehension to create a list called strong_scores.
# It should keep only scores from all_scores where is_strong_score(score) is True.
strong_scores = [score for score in all_scores if is_strong_score(score)]

# 20. Print strong_scores with a clear label.
print(f"Strong scores: {strong_scores}")