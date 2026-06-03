# Topic 1 - Exception Handling Basics

print(f"{'-' * 30} Topic 1 {'-' * 30}")

# 1. Create a variable called age_text and set it to "28"
age_text = "28"
# age_text = "twenty-eight"

# 2. Use try / except to convert age_text into an integer
# 3. Inside the try block, print:
# Age next year: 29

# 4. Inside the except block, print:
# Invalid age value
try:
    age = int(age_text)
    print(f"Age next year: {age + 1}")
except ValueError:
    print("Invalid age value")

# 5. Change age_text to "twenty-eight" and run the same try / except again

# 6. Confirm that the program prints:
# Invalid age value

# Confirmed that this invalid msg prints when age_text cannot become an integer

# 7. Create a variable called quantity_text and set it to "3"
quantity_text = "3"
# quantity_text = "three"

# 8. Use try / except to convert quantity_text into an integer

# 9. Inside the try block, create total_items by adding 2 to the converted quantity

# 10. Print:
# Total items: 5
try:
    quantity = int(quantity_text)
    total_items = quantity + 2
    print(f"Total items: {total_items}")
except ValueError:
    print("Invalid quantity value")

# 11. Change quantity_text to "three" and run the same try / except again

# 12. Confirm that the program prints:
# Invalid quantity value

# Confirmed that this invalid msg prints when quantity_text cannot become an integer

# ---------------------------------------------------------------------
# Topic 2 - Catching Specific Exceptions and Reading Error Messages

print(f"{'-' * 30} Topic 2 {'-' * 30}")

# 1. Create score_text = "90" and divisor_text = "3".
# Use try / except to convert both values into integers.
# Divide score by divisor, store it in result, and print:
# Result: 30.0
score_text = "90"
divisor_text = "3"

# 2. Add specific exception handling:
# ValueError should print:
# Score and divisor must be valid numbers
# ZeroDivisionError should print:
# Divisor cannot be zero
try:
    score = int(score_text)
    divisor = int(divisor_text)
    result = score / divisor
    print(f"Result: {result}")
except ValueError:
    print("Score and divisor must be valid numbers")
except ZeroDivisionError:
    print("Divisor cannot be zero")

# 3. Test both error paths:
# Change score_text to "ninety" and confirm the ValueError message prints.
# Then change score_text back to "90", change divisor_text to "0",
# and confirm the ZeroDivisionError message prints.

# Both error types print as expected when input is changed

# 4. Create a dictionary called user_profile with:
# "name" -> "Sudharsan"
# "role" -> "Software Engineer"
# Try to print user_profile["city"].
# Catch KeyError as error and print:
# Missing profile field: <error message>
user_profile = {
    "name": "Sudharsan",
    "role": "Software Engineer"
}

try:
    print(user_profile["city"])
except KeyError as error:
    print(f"Missing profile field: {error}")

# 5. Create a list called course_topics with:
# "Type Errors", "Date Time", "Exception Handling"
# Try to print the item at index 5.
# Catch IndexError as error and print:
# Invalid topic index: <error message>
course_topics = ["Type Errors", "Date Time", "Exception Handling"]

try:
    print(course_topics[5])
except IndexError as error:
    print(f"Invalid topic index: {error}")

# ---------------------------------------------------------------------
# Topic 3 - Else and Finally Blocks

print(f"{'-' * 30} Topic 3 {'-' * 30}")

# 1. Create payment_text = "125.50".
# Use try / except / else / finally to convert it into a float.
# If conversion fails, print:
# Invalid payment amount
# If conversion succeeds, print:
# Payment accepted: $125.50
# Finally, always print:
# Payment check completed

payment_text = "125.50"
# payment_text = "one twenty five"

try:
    payment = float(payment_text)
except ValueError:
    print("Invalid payment amount")
else:
    print(f"Payment accepted: ${payment:.2f}")
finally:
    print("Payment check completed")

# 2. Change payment_text to "one twenty five" and confirm:
# - the invalid payment message prints
# - the finally message still prints

# 3. Create discount_text = "10" and original_price = 80.
# Use try / except / else / finally to convert discount_text into an integer.
# In the else block, calculate final_price by subtracting discount from original_price.
# Print:
# Final price after discount: $70
# If conversion fails, print:
# Invalid discount value
# Finally, always print:
# Discount check completed

discount_text = "10"
# discount_text = "ten"
original_price = 80

try:
    discount = int(discount_text)
except ValueError:
    print("Invalid discount value")
else:
    final_price = original_price - discount
    print(f"Final price after discount: ${final_price}")
finally:
    print("Discount check completed")

# 4. Change discount_text to "ten" and confirm:
# - the invalid discount message prints
# - the final price message does not print
# - the finally message still prints

# ---------------------------------------------------------------------
# Topic 4 - Safe Input and Conversion Patterns

print(f"{'-' * 30} Topic 4 {'-' * 30}")

# 1. Create age_text = "31".
# Use try / except / else to safely convert it into an integer.
# If conversion succeeds, print:
# Age next year: 32
# If conversion fails, print:
# Age must be a valid number
# Then test with age_text = "thirty-one" and confirm the error message prints.

age_text = "31"
# age_text = "thirty-one"

try:
    age = int(age_text)
except ValueError:
    print("Age must be a valid number")
else:
    print(f"Age next year: {age + 1}")

# 2. Create price_text = "49.99".
# Use try / except / else to safely convert it into a float.
# If conversion succeeds, print:
# Final price with tax: $54.99
# Use tax_amount = 5.
# If conversion fails, print:
# Price must be a valid number
# Then test with price_text = "forty-nine" and confirm the error message prints.

price_text = "49.99"
# price_text = "forty-nine"

try:
    price = float(price_text)
except ValueError:
    print("Price must be a valid number")
else:
    tax_amount = 5
    final_price = price + tax_amount
    print(f"Final price with tax: ${final_price}")

# 3. Create quantity_text = "4".
# Use a fallback value pattern:
# Try to convert quantity_text into an integer.
# If conversion fails, set quantity to 0.
# Print:
# Quantity used: 4
# Then test with quantity_text = "four" and confirm it prints:
# Quantity used: 0

quantity_text = "4"
# quantity_text = "four"

try:
    quantity = int(quantity_text)
except ValueError:
    quantity = 0

print(f"Quantity used: {quantity}")


# 4. Create signup_year_text = "2026".
# Safely convert it into an integer.
# If conversion succeeds, check whether signup_year is greater than or equal to 2024.
# Print:
# Recent signup
# Otherwise print:
# Older signup
# If conversion fails, print:
# Signup year must be a valid number

signup_year_text = "2026"
# signup_year_text = "twenty-twenty-six"

try:
    signup_year = int(signup_year_text)
except ValueError:
    print("Signup year must be a valid number")
else:
    if signup_year >= 2024:
        print("Recent signup")
    else:
        print("Older signup")
