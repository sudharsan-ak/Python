# ---------------------------------------------------------------------
# Topic 5 - Practical Exception Handling Patterns

print(f"{'-' * 30} Topic 5 {'-' * 30}")

# 1. Import datetime from the datetime module.
# Create event_date_text = "2026-08-20".
# Safely parse it using datetime.strptime() with the format "%Y-%m-%d".
# If parsing succeeds, print the date as:
# Event date: August 20, 2026
# If parsing fails, print:
# Invalid event date format
# Then test with event_date_text = "August 20, 2026".

from datetime import datetime

event_date_text = "2026-08-20"
# event_date_text = "August 20, 2026"

try:
    event_date = datetime.strptime(event_date_text, "%Y-%m-%d")
except ValueError:
    print("Invalid event date format")
else:
    print(f"Event date: {event_date.strftime('%B %d, %Y')}")

# 2. Create registration_profile with:
# "name" -> "Sudharsan"
# "email" -> "sudharsan@example.com"
# Use .get() to read optional "company" with fallback "Not provided".
# Print:
# Company: Not provided

registration_profile = {
    "name": "Sudharsan",
    "email": "sudharsan@example.com",
    # "company": "Google"
}

company = registration_profile.get("company", "Not provided")
print(f"Company: {company}")

# 3. In registration_profile, try to read required "ticket_id".
# Catch KeyError as error and print:
# Missing required field: <error message>

try:
    ticket_id = registration_profile["ticket_id"]
except KeyError as error:
    print(f"Missing required field: {error}")

# 4. Create available_sessions with:
# "Python Basics", "Date Time", "Exception Handling"
# Create selected_index_text = "2".
# Safely convert selected_index_text into an integer and use it to access available_sessions.
# If successful, print:
# Selected session: Exception Handling
# If selected_index_text is not numeric, print:
# Session index must be a number
# If the index does not exist, print:
# Selected session does not exist
# Test with selected_index_text = "five" and selected_index_text = "5".

available_sessions = ["Python Basics", "Date Time", "Exception Handling"]
selected_index_text = "2"
# selected_index_text = "five"
# selected_index_text = "5"

try:
    selected_index = int(selected_index_text)
    selected_session = available_sessions[selected_index]
except ValueError:
    print("Session index must be a number")
except IndexError:
    print("Selected session does not exist")
else:
    print(f"Selected session: {selected_session}")