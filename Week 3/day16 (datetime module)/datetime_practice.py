# ---------------------------------------------------------------------
# Topic 1 Exercise: datetime module + current date/time

print(f"{'-' * 30} Topic 1 {'-' * 30}")

# 1. Import the datetime module using the full module import style
import datetime

# 2. Create a variable called current_datetime
# Store the current date and time using datetime.datetime.now()
current_datetime = datetime.datetime.now()

# 3. Print current_datetime with the label:
# Current date and time:
print(f"Current date and time: {current_datetime}")

# 4. Print the type of current_datetime with the label:
# Type of current_datetime:
print(f"Type of current_datetime: {type(current_datetime)}")

# 5. Now use the specific import style:
# from datetime import datetime
# (Added at the top)
from datetime import datetime

# 6. Create a variable called current_datetime_short
# Store the current date and time using datetime.now()
current_datetime_short = datetime.now()

# 7. Print current_datetime_short with the label:
# Current date and time using specific import:
print(f"Current date and time using specific import: {current_datetime_short}")

# 8. Print the type of current_datetime_short with the label:
# Type of current_datetime_short:
print(f"Type of current_datetime_short: {type(current_datetime_short)}")

# ---------------------------------------------------------------------
# Topic 2 Exercise: date, time, and datetime objects

print(f"{'-' * 30} Topic 2 {'-' * 30}")

# 1. Import date, time, and datetime from the datetime module
from datetime import date, time, datetime

# 2. Create a variable called delivery_date
# Store this date: June 25, 2026
delivery_date = date(2026, 6, 25)

# 3. Print delivery_date with the label:
# Delivery date:
print(f"Delivery date: {delivery_date}")

# 4. Print the type of delivery_date with the label:
# Type of delivery_date:
print(f"Type of delivery_date: {type(delivery_date)}")

# 5. Create a variable called delivery_time
# Store this time: 3:45 PM
# Hint: use 24-hour format
delivery_time = time(15, 45)

# 6. Print delivery_time with the label:
# Delivery time:
print(f"Delivery time: {delivery_time}")

# 7. Print the type of delivery_time with the label:
# Type of delivery_time:
print(f"Type of delivery_time: {type(delivery_time)}")

# 8. Create a variable called delivery_datetime
# Store this full date and time:
# June 25, 2026 at 3:45 PM
delivery_datetime = datetime(2026, 6, 25, 15, 45)

# 9. Print delivery_datetime with the label:
# Delivery datetime:
print(f"Delivery datetime: {delivery_datetime}")

# 10. Print the type of delivery_datetime with the label:
# Type of delivery_datetime:
print(f"Type of delivery_datetime: {type(delivery_datetime)}")

# 11. Create a variable called current_datetime
# Store the current date and time using datetime.now()
current_datetime = datetime.now()

# 12. From current_datetime, print:
# Current year:
# Current month:
# Current day:
# Current hour:
# Current minute:
# Current second:
print(f"Current year: {current_datetime.year}")
print(f"Current month: {current_datetime.month}")
print(f"Current day: {current_datetime.day}")
print(f"Current hour: {current_datetime.hour}")
print(f"Current minute: {current_datetime.minute}")
print(f"Current second: {current_datetime.second}")

# 13. Create a variable called current_date_only
# Store only the date part from current_datetime
current_date_only = current_datetime.date()

# 14. Create a variable called current_time_only
# Store only the time part from current_datetime
current_time_only = current_datetime.time()

# 15. Print current_date_only with the label:
# Current date only:
print(f"Current date only: {current_date_only}")

# 16. Print current_time_only with the label:
# Current time only:
print(f"Current time only: {current_time_only}")

# ---------------------------------------------------------------------
# Topic 3 Exercise: Formatting and parsing dates

print(f"{'-' * 30} Topic 3 {'-' * 30}")

# 1. Create a variable called formatted_delivery_date
# Use delivery_datetime from Topic 2
# Format it like this:
# June 25, 2026
formatted_delivery_date = delivery_datetime.strftime("%B %d, %Y")

# 2. Print formatted_delivery_date with the label:
# Formatted delivery date:
print(f"Formatted delivery date: {formatted_delivery_date}")

# 3. Create a variable called formatted_delivery_time
# Use delivery_datetime from Topic 2
# Format it like this:
# 03:45 PM
formatted_delivery_time = delivery_datetime.strftime("%I:%M %p")

# 4. Print formatted_delivery_time with the label:
# Formatted delivery time:
print(f"Formatted delivery time: {formatted_delivery_time}")

# 5. Create a variable called formatted_delivery_summary
# Use delivery_datetime from Topic 2
# Format it like this:
# Thursday, June 25, 2026 at 03:45 PM
formatted_delivery_summary = delivery_datetime.strftime("%A, %B %d, %Y at %I:%M %p")

# 6. Print formatted_delivery_summary with the label:
# Delivery summary:
print(f"Delivery summary: {formatted_delivery_summary}")

# 7. Create a variable called order_datetime_text
# Store this string:
# "2026-07-04 18:30"
order_datetime_text = "2026-07-04 18:30"

# 8. Create a variable called parsed_order_datetime
# Convert order_datetime_text into a real datetime object using datetime.strptime()
parsed_order_datetime = datetime.strptime(order_datetime_text, "%Y-%m-%d %H:%M")

# 9. Print parsed_order_datetime with the label:
# Parsed order datetime:
print(f"Parsed order datetime: {parsed_order_datetime}")

# 10. Print the type of parsed_order_datetime with the label:
# Type of parsed_order_datetime:
print(f"Type of parsed_order_datetime: {type(parsed_order_datetime)}")

# 11. Create a variable called readable_order_datetime
# Format parsed_order_datetime like this:
# July 04, 2026 at 06:30 PM
readable_order_datetime = parsed_order_datetime.strftime("%B %d, %Y at %I:%M %p")

# 12. Print readable_order_datetime with the label:
# Readable order datetime:
print(f"Readable order datetime: {readable_order_datetime}")

# ---------------------------------------------------------------------
# Topic 4 Exercise: timedelta and date/time differences

print(f"{'-' * 30} Topic 4 {'-' * 30}")

# 1. Import timedelta from the datetime module
from datetime import timedelta

# 2. Create a variable called order_created_datetime
# Store this datetime:
# June 20, 2026 at 10:30 AM
order_created_datetime = datetime(2026, 6, 20, 10, 30)

# 3. Create a variable called estimated_delivery_datetime
# Add 5 days to order_created_datetime
estimated_delivery_datetime = order_created_datetime + timedelta(days=5)

# 4. Print order_created_datetime with the label:
# Order created datetime:
print(f"Order created datetime: {order_created_datetime}")

# 5. Print estimated_delivery_datetime with the label:
# Estimated delivery datetime:
print(f"Estimated delivery datetime: {estimated_delivery_datetime}")

# 6. Create a variable called reminder_datetime
# Subtract 1 day from estimated_delivery_datetime
reminder_datetime = estimated_delivery_datetime - timedelta(days=1)

# 7. Print reminder_datetime with the label:
# Reminder datetime:
print(f"Reminder datetime: {reminder_datetime}")

# 8. Create a variable called support_deadline
# Add 2 days, 4 hours, and 30 minutes to order_created_datetime
support_deadline = order_created_datetime + timedelta(days=2, hours=4, minutes=30)

# 9. Print support_deadline with the label:
# Support deadline:
print(f"Support deadline: {support_deadline}")

# 10. Create a variable called delivery_duration
# Subtract order_created_datetime from estimated_delivery_datetime
delivery_duration = estimated_delivery_datetime - order_created_datetime

# 11. Print delivery_duration with the label:
# Delivery duration:
print(f"Delivery duration: {delivery_duration}")

# 12. Print delivery_duration.days with the label:
# Delivery duration days:
print(f"Delivery duration days: {delivery_duration.days}")

# 13. Print delivery_duration.total_seconds() with the label:
# Delivery duration total seconds:
print(f"Delivery duration total seconds: {delivery_duration.total_seconds()}")

# 14. Create a variable called payment_date
# Store this date:
# June 18, 2026
payment_date = date(2026, 6, 18)

# 15. Create a variable called shipping_date
# Store this date:
# June 21, 2026
shipping_date = date(2026, 6, 21)

# 16. Create a variable called payment_to_shipping_days
# Subtract payment_date from shipping_date
payment_to_shipping_days = shipping_date - payment_date

# 17. Print payment_to_shipping_days with the label:
# Payment to shipping duration:
print(f"Payment to shipping duration: {payment_to_shipping_days}")

# 18. Print payment_to_shipping_days.days with the label:
# Payment to shipping days:
print(f"Payment to shipping days: {payment_to_shipping_days.days}")