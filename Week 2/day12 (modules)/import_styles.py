# Topic 2: Specific imports, multiple imports, and aliases
# 1. Import only get_student_name from helpers
from helpers import get_student_name

# 2. Import get_current_day, get_current_topic, and get_course_name from helpers in one import line
from helpers import get_current_day, get_current_topic, get_course_name

# 3. Import the full helpers module using the alias helpers_tools
import helpers as helpers_tools

# 4. Import format_topic_summary from helpers using the alias format_summary
from helpers import format_topic_summary as format_summary

# 5. Call get_student_name directly
# Store the returned value in student_name
student_name = get_student_name()

# 6. Call get_current_day directly
# Store the returned value in current_day
current_day = get_current_day()

# 7. Call get_current_topic directly
# Store the returned value in current_topic
current_topic = get_current_topic()

# 8. Call get_course_name directly
# Store the returned value in course_name
course_name = get_course_name()

# 9. Call format_summary using current_day and current_topic
# Store the returned value in topic_summary
topic_summary = format_summary(current_day, current_topic)

# 10. Call calculate_total_minutes from the helpers_tools alias
# Pass these values: 30, 45, 60
# Store the returned value in total_minutes
total_minutes = helpers_tools.calculate_total_minutes(30, 45, 60)

# 11. Use helpers_tools.print_separator()
helpers_tools.print_separator()

# 12. Print the student name with this format:
# Student: <student_name>
print(f"Student: {student_name}")

# 13. Print the course name with this format:
# Course: <course_name>
print(f"Course: {course_name}")

# 14. Print topic_summary with this format:
# Summary: <topic_summary>
print(f"Summary: {topic_summary}")

# 15. Print total_minutes with this format:
# Total minutes: <total_minutes>
print(f"Total minutes: {total_minutes}")

# 16. Use helpers_tools.print_separator() again
helpers_tools.print_separator()