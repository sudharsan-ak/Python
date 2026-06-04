# ---------------------------------------------------------------------
# Topic 4 - Simple Groups and Extraction

print(f"{'-' * 30} Topic 4 {'-' * 30}")

# 1. Import the re module.
import re

# 2. Create a variable called activity_log with this text:
# "User sara.khan signed in from IP 192.168.1.45. Case CASE-4821 was escalated to team OPS."
activity_log = "User sara.khan signed in from IP 192.168.1.45. Case CASE-4821 was escalated to team OPS."

# 3. Use re.search() with r"CASE-(\d{4})" to find the case ID.
# Store the result in case_result.
case_result = re.search(r"CASE-(\d{4})", activity_log)

# 4. If case_result exists:
# Print the full match using .group()
# Print only the case number using .group(1)
# Otherwise, print "No case ID found".
if case_result:
    print(f"Case result: {case_result.group()}")
    print(f"Case number: {case_result.group(1)}")
else:
    print("No case ID found")

# 5. Use re.search() with r"User ([a-z]+\.[a-z]+)" to find the username.
# Store the result in user_result.
user_result = re.search(r"User ([a-z]+\.[a-z]+)", activity_log)

# 6. If user_result exists:
# Print the full match using .group()
# Print only the username using .group(1)
# Otherwise, print "No user found".
if user_result:
    print(f"User result: {user_result.group()}")
    print(f"Username: {user_result.group(1)}")
else:
    print("No user found")

# 7. Use re.search() with r"IP (\d+\.\d+\.\d+\.\d+)" to find the IP address.
# Store the result in ip_result.
ip_result = re.search(r"IP (\d+\.\d+\.\d+\.\d+)", activity_log)

# 8. If ip_result exists:
# Print the full match using .group()
# Print only the IP address using .group(1)
# Otherwise, print "No IP address found".
if ip_result:
    print(f"IP result: {ip_result.group()}")
    print(f"IP address: {ip_result.group(1)}")
else:
    print("No IP address found")

# 9. Use re.search() with r"team ([A-Z]+)" to find the assigned team.
# Store the result in team_result.
team_result = re.search(r"team ([A-Z]+)", activity_log)

# 10. If team_result exists:
# Print the full match using .group()
# Print only the team name using .group(1)
# Otherwise, print "No team found".
if team_result:
    print(f"Team result: {team_result.group()}")
    print(f"Team name: {team_result.group(1)}")
else:
    print("No team found")

# 11. Create a variable called case_text with this text:
# "Closed cases: CASE-4821, CASE-3900, CASE-7255."
case_text = "Closed cases: CASE-4821, CASE-3900, CASE-7255."

# 12. Use re.findall() with r"CASE-\d{4}" to find all full case IDs.
# Store the result in full_case_ids and print it.
full_case_ids = re.findall(r"CASE-\d{4}", case_text)
print(f"Full case IDs: {full_case_ids}")

# 13. Use re.findall() with r"CASE-(\d{4})" to find only the case numbers.
# Store the result in case_numbers and print it.
case_numbers = re.findall(r"CASE-(\d{4})", case_text)
print(f"Case numbers: {case_numbers}")

# 14. Add one short comment explaining why the second findall returns only numbers,
# not full CASE-#### values.
# The second findall has a group, so it returns only the captured parts(case numbers in this case)
# whereas findall without group, will return full matches

# ---------------------------------------------------------------------
# Topic 5 - re.sub() for Replacement and Cleanup

print(f"{'-' * 30} Topic 5 {'-' * 30}")

# 1. Create a variable called audit_note with this text:
# "Login   failed   for   user mike.ross from IP 10.20.30.40!!! Contact mike.ross@company.com ASAP."
audit_note = "Login   failed   for   user mike.ross from IP 10.20.30.40!!! Contact mike.ross@company.com ASAP."

# 2. Use re.sub() with r"\s+" to replace multiple spaces with one space.
# Store the result in cleaned_spacing and print it.
cleaned_spacing = re.sub(r"\s+", " ", audit_note)
print(f"Cleaned spacing: {cleaned_spacing}")

# 3. Use re.sub() on cleaned_spacing to replace the email-like value
# with "[email-hidden]".
# Pattern hint: use r"\w+\.\w+@\w+\.\w+"
# Store the result in hidden_email_note and print it.
hidden_email_note = re.sub(r"\w+\.\w+@\w+\.\w+", "[email-hidden]", cleaned_spacing)
print(f"Hidden email note: {hidden_email_note}")

# 4. Use re.sub() on hidden_email_note to replace the IP address
# with "[ip-hidden]".
# Pattern hint: use r"\d+\.\d+\.\d+\.\d+"
# Store the result in hidden_ip_note and print it.
hidden_ip_note = re.sub(r"\d+\.\d+\.\d+\.\d+", "[ip-hidden]", hidden_email_note)
print(f"Hidden IP note: {hidden_ip_note}")

# 5. Use re.sub() on hidden_ip_note to remove exclamation marks.
# Replace r"!+" with an empty string.
# Store the result in cleaned_note and print it.
cleaned_note = re.sub(r"!+", "", hidden_ip_note)
print(f"Cleaned note: {cleaned_note}")

# 6. Create a variable called retry_message with this text:
# "retry retry retry needed"
retry_message = "retry retry retry needed"

# 7. Use re.sub() with count=1 to replace only the first "retry"
# with "attempt".
# Store the result in first_retry_replaced and print it.
first_retry_replaced = re.sub(r"retry", "attempt", retry_message, count=1)
print(f"First retry replaced: {first_retry_replaced}")

# 8. Add one short comment explaining why re.sub() is useful for cleanup.
# It is useful to cleanup messy unwanted space or characters or substitute characters