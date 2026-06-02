# ---------------------------------------------------------------------
# Day 16 - Final Mixed Exercise: Invoice due-date checker

print(f"{'-' * 30} Day 16 Final Mixed Exercise {'-' * 30}")

# Scenario:
# You are building a small invoice due-date checker.
# The invoice date comes in as text, so you need to parse it first.
# Then calculate the due date, reminder date, and invoice status.

# 1. Import datetime and timedelta from the datetime module
from datetime import datetime, timedelta

# 2. Create a variable called current_datetime
# Store this fixed datetime:
# June 22, 2026 at 10:00 AM
current_datetime = datetime(2026, 6, 22, 10, 0)

# 3. Create a variable called invoice_created_text
# Store this string:
# "2026-06-10 09:15"
invoice_created_text = "2026-06-10 09:15"

# 4. Create a variable called invoice_created_datetime
# Parse invoice_created_text into a real datetime object
invoice_created_datetime = datetime.strptime(invoice_created_text, "%Y-%m-%d %I:%M")

# 5. Create a variable called payment_terms_days
# Store the number 14
payment_terms_days = 14

# 6. Create a variable called invoice_due_datetime
# Add payment_terms_days to invoice_created_datetime
invoice_due_datetime = invoice_created_datetime + timedelta(days=payment_terms_days)

# 7. Create a variable called reminder_datetime
# Subtract 2 days from invoice_due_datetime
reminder_datetime = invoice_due_datetime - timedelta(days=2)

# 8. Create a variable called time_until_due
# Subtract current_datetime from invoice_due_datetime
time_until_due = invoice_due_datetime - current_datetime

# 9. Create a variable called is_invoice_overdue
# It should be True if current_datetime is greater than invoice_due_datetime
# Otherwise it should be False
is_invoice_overdue = current_datetime > invoice_due_datetime

# 10. Print invoice_created_datetime formatted like this:
# Invoice created: June 10, 2026 at 09:15 AM
print(f"Invoice created: {invoice_created_datetime.strftime('%B %d, %Y at %I:%M %p')}")

# 11. Print invoice_due_datetime formatted like this:
# Invoice due: June 24, 2026 at 09:15 AM
print(f"Invoice due: {invoice_due_datetime.strftime('%B %d, %Y at %I:%M %p')}")

# 12. Print reminder_datetime formatted like this:
# Reminder date: June 22, 2026 at 09:15 AM
print(f"Reminder date: {reminder_datetime.strftime('%B %d, %Y at %I:%M %p')}")

# 13. Print time_until_due.days with the label:
# Days until due:
print(f"Days until due: {time_until_due.days}")

# 14. Print is_invoice_overdue with the label:
# Is invoice overdue:
print(f"Is invoice overdue: {is_invoice_overdue}")

# 15. Use an if / else statement:
# If the invoice is overdue, print:
# Invoice status: Overdue
# Otherwise, print:
# Invoice status: Still within payment window
if is_invoice_overdue:
    print("Invoice status: Overdue")
else:
    print("Invoice status: Still within payment window")

# 16. Create a variable called invoice_summary
# It should be a clean f-string summary using the formatted due date and status.
# Example idea:
# Invoice is due on June 24, 2026 at 09:15 AM. Status: Still within payment window.
invoice_summary = f"Invoice is due on {invoice_due_datetime.strftime('%B %d, %Y at %I:%M %p')}. Status: {'Overdue' if is_invoice_overdue else 'Still within payment window'}."

# 17. Print invoice_summary with the label:
# Invoice summary:
print(f"Invoice summary: {invoice_summary}")