# ---------------------------------------------------------------------
# Topic 1 - Regex Basics, Raw Strings, and re Module

print(f"{'-' * 30} Topic 1 {'-' * 30}")

# 1. Import the re module.
import re

# 2. Create a variable called message with this text:
# "Order INV-2045 was created for customer ashwin@example.com on June 4."
message = "Order INV-2045 was created for customer ashwin@example.com on June 4."

# 3. Create a variable called word_pattern and store the raw string pattern for:
# "Order"
word_pattern = r"Order"

# 4. Use re.search() to search for word_pattern inside message.
# Store the result in a variable called word_result.
word_result = re.search(word_pattern, message)

# 5. Print word_result with a clear label.
print(f"Word result: {word_result}")

# 6. Create a variable called missing_pattern and store the raw string pattern for:
# "Refund"
missing_pattern = r"Refund"

# 7. Use re.search() to search for missing_pattern inside message.
# Store the result in a variable called missing_result.
missing_result = re.search(missing_pattern, message)

# 8. Print missing_result with a clear label.
print(f"Missing result: {missing_result}")

# 9. Create a variable called digit_pattern and store the raw string pattern:
# r"\d"
digit_pattern = r"\d"

# 10. Use re.search() to search for digit_pattern inside message.
# Store the result in a variable called digit_result.
digit_result = re.search(digit_pattern, message)

# 11. Print digit_result with a clear label.
print(f"Digit result: {digit_result}")

# 12. Add one short comment explaining why we use r"\d" instead of "\d" for regex patterns.
# "\d" sometimes works but is a bad habit, prefixing them with r tells the code to treat as normal regex backslashes.
# Do not treat them like Python escape characters first.

# ---------------------------------------------------------------------
# Topic 2 - re.search(), .group(), re.findall(), and re.match()

print(f"{'-' * 30} Topic 2 {'-' * 30}")

# 1. Create a variable called support_message with this text:
# "Ticket TICKET was opened by customer. Ticket TICKET was assigned to support. Refund request is pending."
support_message = "Ticket TICKET was opened by customer. Ticket TICKET was assigned to support. Refund request is pending."

# 2. Create a variable called ticket_pattern and store the raw string pattern:
# r"TICKET"
ticket_pattern = r"TICKET"

# 3. Use re.search() to search for ticket_pattern inside support_message.
# Store the result in a variable called first_ticket_result.
first_ticket_result = re.search(ticket_pattern, support_message)

# 4. Print first_ticket_result with a clear label so you can see the full match object.
print(f"First ticket result: {first_ticket_result}")

# 5. If first_ticket_result exists, use .group() to print only the matched text.
# Otherwise, print "No ticket found".
if first_ticket_result:
    print(f"First ticket result: {first_ticket_result.group()}")
else:
    print("No ticket found")

# 6. Use re.findall() to find all ticket_pattern matches inside support_message.
# Store the result in a variable called all_ticket_results.
all_ticket_results = re.findall(ticket_pattern, support_message)

# 7. Print all_ticket_results with a clear label.
print(f"All ticket results: {all_ticket_results}")

# 8. Use re.match() to check whether support_message starts with the pattern:
# r"Ticket"
# Store the result in a variable called starts_with_ticket.
starts_with_ticket = re.match(r"Ticket", support_message)

# 9. Print starts_with_ticket with a clear label.
print(f"Starts with ticket: {starts_with_ticket}")

# 10. Use re.match() to check whether support_message starts with the pattern:
# r"Refund"
# Store the result in a variable called starts_with_refund.
starts_with_refund = re.match(r"Refund", support_message)

# 11. Print starts_with_refund with a clear label.
print(f"Starts with refund: {starts_with_refund}")

# 12. Add one short comment explaining why re.match(r"Refund", support_message)
# returns None even though "Refund" exists later in the message.
# re.match() checks only the beginning of the support_message and since it doesn't start with Refund, it returns None
# unlike re.search() which finds first match anywhere or re.findall() which finds all matches

# ---------------------------------------------------------------------
# Topic 3 - Character Classes, Quantifiers, and Anchors

print(f"{'-' * 30} Topic 3 {'-' * 30}")

# 1. Create a variable called log_message with this text:
# "Order INV-2045 was assigned to agent ALEX and ticket TICKET-789 is still open."
log_message = "Order INV-2045 was assigned to agent ALEX and ticket TICKET-789 is still open."

# 2. Use re.search() with r"\d" to find the first single digit in log_message.
# Store it in first_digit_result and print only the matched text using .group()
# if the result exists.
first_digit_result = re.search(r"\d", log_message)
if first_digit_result:
    print(f"First digit result: {first_digit_result.group()}")
else:
    print("No digit found")

# 3. Use re.search() with r"\d+" to find the first full number in log_message.
# Store it in first_number_result and print only the matched text using .group()
# if the result exists.
first_number_result = re.search(r"\d+", log_message)
if first_number_result:
    print(f"First number result: {first_number_result.group()}")
else:
    print("No number found")

# 4. Use re.findall() with r"\d+" to find all full numbers in log_message.
# Store the result in all_numbers and print it with a clear label.
all_numbers = re.findall(r"\d+", log_message)
print(f"All numbers: {all_numbers}")

# 5. Use re.search() with r"INV-\d{4}" to find the invoice code.
# Store it in invoice_result and print only the matched text if it exists.
invoice_result = re.search(r"INV-\d{4}", log_message)
if invoice_result:
    print(f"Invoice result: {invoice_result.group()}")
else:
    print("No invoice found")

# 6. Use re.search() with r"TICKET-\d+" to find the ticket code.
# Store it in ticket_result and print only the matched text if it exists.
ticket_result = re.search(r"TICKET-\d+", log_message)
if ticket_result:
    print(f"Ticket result: {ticket_result.group()}")
else:
    print("No ticket found")

# 7. Create a variable called invoice_code and set it to "INV-2045".
invoice_code = "INV-2045"

# 8. Use re.search() with r"^INV-\d{4}$" to check whether invoice_code
# fully matches the invoice format.
# Store it in valid_invoice_result and print it with a clear label.
valid_invoice_result = re.search(r"^INV-\d{4}$", invoice_code)
print(f"Valid invoice result: {valid_invoice_result}")

# 9. Create another variable called bad_invoice_code and set it to "Order INV-2045".
bad_invoice_code = "Order INV-2045"

# 10. Use the same r"^INV-\d{4}$" pattern to check bad_invoice_code.
# Store it in bad_invoice_result and print it with a clear label.
bad_invoice_result = re.search(r"^INV-\d{4}$", bad_invoice_code)
print(f"Bad invoice result: {bad_invoice_result}")

# 11. Add one short comment explaining why bad_invoice_result is None.
# The code doesn't strictly start and end with pattern we were checking for, 
# since anchors force the entire text to follow the pattern