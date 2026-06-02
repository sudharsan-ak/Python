# ---------------------------------------------------------------------
# Day 16 - Topic 5 Exercise: Practical datetime mini-scenarios

print(f"{'-' * 30} Topic 5 {'-' * 30}")

# 1. Import datetime and timedelta from the datetime module
from datetime import datetime, timedelta

# 2. Create a variable called current_datetime
# Store this fixed datetime:
# June 20, 2026 at 9:30 AM
current_datetime = datetime(2026, 6, 20, 9, 30)

# ---------------------------------------------------------------------
# Scenario 1: Subscription renewal tracker

# 3. Create a variable called renewal_datetime
# Store this datetime:
# June 25, 2026 at 9:30 AM
renewal_datetime = datetime(2026, 6, 25, 9, 30)

# 4. Create a variable called renewal_time_left
# Subtract current_datetime from renewal_datetime
renewal_time_left = renewal_datetime - current_datetime

# 5. Print renewal_time_left.days with the label:
# Days until renewal:
print(f"Days until renewal: {renewal_time_left.days}")

# 6. Create a variable called formatted_renewal_datetime
# Format renewal_datetime like this:
# June 25, 2026 at 09:30 AM
formatted_renewal_datetime = renewal_datetime.strftime("%B %d, %Y at %I:%M %p")

# 7. Print formatted_renewal_datetime with the label:
# Renewal date:
print(f"Renewal date: {formatted_renewal_datetime}")

# 8. Create a variable called is_renewal_past_due
# It should be True if current_datetime is greater than renewal_datetime
# Otherwise it should be False
is_renewal_past_due = current_datetime > renewal_datetime

# 9. Print is_renewal_past_due with the label:
# Is renewal past due:
print(f"Is renewal past due: {is_renewal_past_due}")

# ---------------------------------------------------------------------
# Scenario 2: Appointment reminder

# 10. Create a variable called appointment_datetime
# Store this datetime:
# June 22, 2026 at 2:00 PM
appointment_datetime = datetime(2026, 6, 22, 14, 0)

# 11. Create a variable called appointment_reminder
# Subtract 2 hours from appointment_datetime
appointment_reminder = appointment_datetime - timedelta(hours=2)

# 12. Create a variable called formatted_appointment
# Format appointment_datetime like this:
# June 22, 2026 at 02:00 PM
formatted_appointment = appointment_datetime.strftime("%B %d, %Y at %I:%M %p")

# 13. Create a variable called formatted_reminder
# Format appointment_reminder like this:
# June 22, 2026 at 12:00 PM
formatted_reminder = appointment_reminder.strftime("%B %d, %Y at %I:%M %p")

# 14. Print formatted_appointment with the label:
# Appointment:
print(f"Appointment: {formatted_appointment}")

# 15. Print formatted_reminder with the label:
# Reminder:
print(f"Reminder: {formatted_reminder}")

# 16. Create a variable called hours_until_appointment
# Subtract current_datetime from appointment_datetime
hours_until_appointment = appointment_datetime - current_datetime

# 17. Print hours_until_appointment.total_seconds() with the label:
# Seconds until appointment:
print(f"Seconds until appointment: {hours_until_appointment.total_seconds()}")