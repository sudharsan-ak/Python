# Day 12 - Final Mixed Exercise
# Scenario: Python study session toolkit

# 1. Import math, random, datetime, os, and sys
import math, random, datetime, os, sys

# 2. Import the full day12_final_helpers module using the alias helpers
import day12_final_helpers as helpers

# 3. Import build_session_title from day12_final_helpers using the alias build_title
from day12_final_helpers import build_session_title as build_title

# 4. Import calculate_average_score directly from day12_final_helpers
from day12_final_helpers import calculate_average_score

# 5. Create a variable called current_day and set it to 12
current_day = 12

# 6. Create a variable called current_topic and set it to "Modules"
current_topic = "Modules"

# 7. Call build_title using current_day and current_topic
# Store the result in a variable called session_title
session_title = build_title(current_day, current_topic)

# 8. Create a list called review_topics with:
# "custom modules", "import styles", "math module", "random module", "datetime module"
review_topics = ["custom modules", "import styles", "math module", "random module", "datetime module"]

# 9. Use random.choice() to select one item from review_topics
# Store the result in a variable called selected_review_topic
selected_review_topic = random.choice(review_topics)

# 10. Call calculate_average_score directly with these scores:
# 88, 92, 79
# Store the result in a variable called average_score
average_score = calculate_average_score(88, 92, 79)

# 11. Use math.ceil() to round average_score upward
# Store the result in a variable called rounded_average
rounded_average = math.ceil(average_score)

# 12. Call helpers.classify_score using rounded_average
# Store the result in a variable called score_status
score_status = helpers.classify_score(rounded_average)

# 13. Call helpers.build_review_message using selected_review_topic and score_status
# Store the result in a variable called review_message
review_message = helpers.build_review_message(selected_review_topic, score_status)

# 14. Use datetime.datetime.now()
# Store the result in a variable called current_datetime
current_datetime = datetime.datetime.now()

# 15. Use os.getcwd() and sys.platform
# Store them in variables called current_folder and platform_name
current_folder = os.getcwd()
platform_name = sys.platform

# 16. Print a final report in this order:
# separator
# Session: <session_title>
# Date: <current year>-<current month>-<current day>
# Average score: <average_score>
# Rounded average: <rounded_average>
# <review_message>
# Folder: <current_folder>
# Platform: <platform_name>
# separator
helpers.print_separator()
print(f"Session: {session_title}")
print(f"Date: {current_datetime.year}-{current_datetime.month}-{current_datetime.day}")
print(f"Average score: {average_score}")
print(f"Rounded average: {rounded_average}")
print(review_message)
print(f"Folder: {current_folder}")
print(f"Platform: {platform_name}")
helpers.print_separator()
