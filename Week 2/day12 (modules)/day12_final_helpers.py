# Day 12 - Final Mixed Exercise helper module
# Scenario: Python study session toolkit

# 1. Create a function called print_separator
# It should print 35 hyphens using string multiplication
def print_separator():
    print("-" * 35)

# 2. Create a function called build_session_title
# It should accept two parameters: day and topic
# It should return this exact format:
# Day <day> Final Review - <topic>
def build_session_title(day, topic):
    return f"Day {day} Final Review - {topic}"

# 3. Create a function called calculate_average_score
# It should accept any number of scores using *scores
# If no scores are passed, return 0
# Otherwise, return the average score
def calculate_average_score(*scores):
    if not scores:
        return 0
    total = sum(scores)
    return total / len(scores)

# 4. Create a function called classify_score
# It should accept one parameter called score
# If score is greater than or equal to 90, return "Strong"
# Else if score is greater than or equal to 75, return "Good"
# Otherwise, return "Needs review"
def classify_score(score):
    if score >= 90:
        return "Strong"
    elif score >= 75:
        return "Good"
    else:
        return "Needs review"

# 5. Create a function called build_review_message
# It should accept two parameters: topic and status
# It should return this exact format:
# Review focus: <topic> - <status>
def build_review_message(topic, status):
    return f"Review focus: {topic} - {status}"