# Topic 2: Lambda in Detail

print(f"{'-' * 30} Topic 2 {'-' * 30}")

# 1. Create a lambda called double_number
# It should accept one parameter called number
# It should return number * 2
double_number = lambda number: number * 2

# 2. Call double_number with 12
# Store the result in doubled_value
# Print: Doubled value: <value>
doubled_value = double_number(12)
print(f"Doubled value: {doubled_value}")

# 3. Create a lambda called triple_number
# It should accept one parameter called number
# It should return number * 3
triple_number = lambda number: number * 3

# 4. Call triple_number with 8
# Store the result in tripled_value
# Print: Tripled value: <value>
tripled_value = triple_number(8)
print(f"Tripled value: {tripled_value}")

# 5. Create a lambda called add_numbers
# It should accept two parameters:
# first_number
# second_number
# It should return their sum
add_numbers = lambda first_number, second_number: first_number + second_number

# 6. Call add_numbers with 15 and 25
# Store the result in total
# Print: Total: <value>
total = add_numbers(15, 25)
print(f"Total: {total}")

# 7. Create a lambda called format_name
# It should accept one parameter called name
# It should return name.title()
format_name = lambda name: name.title()

# 8. Call format_name with "sudharsan srinivasan"
# Store the result in formatted_name
# Print: Formatted name: <value>
formatted_name = format_name("sudharsan srinivasan")
print(f"Formatted name: {formatted_name}")

# 9. Create a lambda called check_pass_status
# It should accept one parameter called score
# It should return "Pass" if score is greater than or equal to 70
# Otherwise, it should return "Fail"
check_pass_status = lambda score: "Pass" if score >= 70 else "Fail"

# 10. Call check_pass_status with 85
# Store the result in first_result
# Print: First result: <value>
first_result = check_pass_status(85)
print(f"First result: {first_result}")

# 11. Call check_pass_status with 55
# Store the result in second_result
# Print: Second result: <value>
second_result = check_pass_status(55)
print(f"Second result: {second_result}")

# 12. Create a normal function called apply_operation
# It should accept two parameters:
# operation
# value
# Inside the function:
# - call operation(value)
# - store the result in a variable called result
# - return result
def apply_operation(operation, value):
    result = operation(value)
    return result

# 13. Call apply_operation with an inline lambda
# The lambda should accept number and return number + 10
# Pass 40 as the value
# Store the result in increased_value
# Print: Increased value: <value>
increased_value = apply_operation(lambda number: number + 10, 40)
print(f"Increased value: {increased_value}")

# 14. Call apply_operation with another inline lambda
# The lambda should accept text and return text.upper()
# Pass "python lambda" as the value
# Store the result in uppercase_text
# Print: Uppercase text: <value>
uppercase_text = apply_operation(lambda text: text.upper(), "python lambda")
print(f"Uppercase text: {uppercase_text}")

# 15. Create a normal def function called clean_and_format_name
# It should accept one parameter called name
# Inside the function:
# - strip the name
# - convert it to title case
# - return the cleaned result
def clean_and_format_name(name):
    cleaned_name = name.strip().title()
    return cleaned_name

# 16. Call clean_and_format_name with "   ashwin python learner   "
# Store the result in clean_name
# Print: Clean name: <value>
clean_name = clean_and_format_name("   ashwin python learner   ")
print(f"Clean name: {clean_name}")

# 17. Add a comment explaining why clean_and_format_name should use def instead of lambda
# Use def here because name cleanup is clearer as named reusable logic, and it may grow later if more formatting rules are added.