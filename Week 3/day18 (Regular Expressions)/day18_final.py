# ---------------------------------------------------------------------
# Day 18 - Final Mixed Exercise: Regular Expressions
# Scenario: Event registration intake parser

print(f"{'-' * 30} Day 18 Final {'-' * 30}")

# Goal:
# Build a small parser for an event registration message.
# Practice validation, search, groups, findall, and re.sub() cleanup.

# 1. Import re.
import re

# 2. Create this registration_message:
# "Registration REG-5839 submitted by Maya Patel. Contact: maya.patel@events.com. Sessions: SES-101, SES-205, SES-310. Backup phone: 555-812-4090!!!"
registration_message = "Registration REG-5839 submitted by Maya Patel. Contact: maya.patel@events.com. Sessions: SES-101, SES-205, SES-310. Backup phone: 555-812-4090!!!"

# 3. Create registration_id = "REG-5839" and bad_registration_id = "New REG-5839".
# Validate both using the same full-string regex pattern.
# Print whether each one is valid or invalid.
registration_id = "REG-5839"
bad_registration_id = "New REG-5839"

valid_registration_id = re.search(r"^REG-\d{4}$", registration_id)
if valid_registration_id:
    print("Valid registration ID")
else:
    print("Invalid registration ID")

valid_bad_registration_id = re.search(r"^REG-\d{4}$", bad_registration_id)
if valid_bad_registration_id:
    print("Valid bad registration ID")
else:
    print("Invalid bad registration ID")

# 4. Extract the registrant name from registration_message.
# Expected extracted name: Maya Patel
registrant_name = re.search(r"submitted by ([A-Za-z ]+)\.", registration_message)
if registrant_name:
    print(f"Registrant name: {registrant_name.group(1)}")
else:
    print("No registrant name found")

# 5. Extract the email and print:
# - full email
# - username part
# - domain part
email_result = re.search(r"([\w.]+)@(\w+\.\w+)", registration_message)
if email_result:
    print(f"Full email: {email_result.group()}")
    print(f"Username: {email_result.group(1)}")
    print(f"Domain: {email_result.group(2)}")

# 6. Find all selected session IDs.
# Expected result: ["SES-101", "SES-205", "SES-310"]
session_ids = re.findall(r"SES-\d+", registration_message)
print(f"Session IDs: {session_ids}")

# 7. Extract the backup phone number.
# Expected result: 555-812-4090
backup_phone = re.search(r"\d{3}-\d{3}-\d{4}", registration_message)
if backup_phone:
    print(f"Backup phone: {backup_phone.group()}")

# 8. Create a safe version of registration_message by:
# - replacing the email with [email-hidden]
# - replacing the phone number with [phone-hidden]
# - removing extra exclamation marks
# Print the final safe message.
safe_message = re.sub(r"([\w.]+)@(\w+\.\w+)", r"[email-hidden]", registration_message)
safe_message = re.sub(r"\d{3}-\d{3}-\d{4}", r"[phone-hidden]", safe_message)
safe_message = re.sub(r"!+", "", safe_message)
print(f"Safe message: {safe_message}")

# 9. Add 2 short comments at the bottom:
# - why validation needs anchors
# - why groups are useful for extraction
# Validation matches a pattern, so it requires anchors.
# Groups are useful because they let us extract only the specific part we need from a larger full match.