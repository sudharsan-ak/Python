# ---------------------------------------------------------------------
# Topic 6 - Practical Validation and Search Mini-Scenarios

print(f"{'-' * 30} Topic 6 {'-' * 30}")

# 1. Import the re module.
import re

# 2. Create a variable called deployment_log with this text:
# "Deploy DEP-4582 finished on server app_01. Failed checks: CHECK-17, CHECK-22. Owner email: release.team@company.com."
deployment_log = "Deploy DEP-4582 finished on server app_01. Failed checks: CHECK-17, CHECK-22. Owner email: release.team@company.com."

# 3. Create a variable called deployment_id and set it to "DEP-4582".
deployment_id = "DEP-4582"

# 4. Use re.search() with r"^DEP-\d{4}$" to validate deployment_id.
# Store the result in valid_deployment_result.
# If it exists, print "Valid deployment ID".
# Otherwise, print "Invalid deployment ID".
valid_deployment_result = re.search(r"^DEP-\d{4}$", deployment_id)
if valid_deployment_result:
    print("Valid deployment ID")
else:
    print("Invalid deployment ID")

# 5. Create a variable called bad_deployment_id and set it to "Deploy DEP-4582".
bad_deployment_id = "Deploy DEP-4582"

# 6. Use the same validation pattern to check bad_deployment_id.
# Store the result in bad_deployment_result.
# If it exists, print "Valid bad deployment ID".
# Otherwise, print "Invalid bad deployment ID".
bad_deployment_result = re.search(r"^DEP-\d{4}$", bad_deployment_id)
if bad_deployment_result:
    print("Valid bad deployment ID")
else:
    print("Invalid bad deployment ID")

# 7. Use re.search() with r"server ([a-z]+_\d+)" to extract the server name
# from deployment_log.
# Store the result in server_result.
# If it exists, print only the server name using .group(1).
server_result = re.search(r"server ([a-z]+_\d+)", deployment_log)
if server_result:
    print(f"Server name: {server_result.group(1)}")

# 8. Use re.findall() with r"CHECK-\d+" to find all failed check IDs
# from deployment_log.
# Store the result in failed_checks and print it.
failed_checks = re.findall(r"CHECK-\d+", deployment_log)
print(f"Failed checks: {failed_checks}")

# 9. Use re.search() with r"([\w.]+)@(\w+\.\w+)" to extract the owner email.
# Store the result in email_result.
# If it exists:
# Print the full email using .group()
# Print the username part using .group(1)
# Print the domain using .group(2)
email_result = re.search(r"([\w.]+)@(\w+\.\w+)", deployment_log)
if email_result:
    print(f"Full email: {email_result.group()}")
    print(f"Username: {email_result.group(1)}")
    print(f"Domain: {email_result.group(2)}")


# 10. Use re.sub() to hide the email in deployment_log.
# Replace r"[\w.]+@\w+\.\w+" with "[email-hidden]".
# Store the result in safe_deployment_log and print it.
safe_deployment_log = re.sub(r"([\w.]+)@\w+\.\w+", r"[email-hidden]", deployment_log)
print(f"Safe deployment log: {safe_deployment_log}")

# 11. Add one short comment explaining why validation uses ^ and $,
# but searching inside deployment_log does not.
# validation is done to match a pattern so anchor is important whereas
# search is done to find the presence of character(s)