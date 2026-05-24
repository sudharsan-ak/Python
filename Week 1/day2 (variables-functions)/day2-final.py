# 1. Create these variables:
# first_name
# last_name
# age
# city
# years_experience
# is_software_engineer
first_name = "Sudharsan"
last_name = "Srinivasan"
age = 30
city = "Lewisville"
years_experience = 6
is_software_engineer = True

# 2. Create full_name using f-string
full_name = f"{first_name} {last_name}"

# 3. Print:
# "My name is Sudharsan Srinivasan."
print(f"My name is {full_name}.")

# 4. Print:
# "I am 30 years old and live in Lewisville."
print(f"I am {age} years old and live in {city}.")

# 5. Print the type of age
print(type(age))

# 6. Print the length of full_name
print(len(full_name))

# 7. Ask the user for two numbers
num1 = input("Please enter first number: ")
num2 = input("Please enter second number: ")

# 8. Convert both numbers to int
num1 = int(num1)
num2 = int(num2)

# 9. Print:
# addition
# subtraction
# multiplication
# division
# modulus
print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Modulus: {num1 % num2}")

# 10. Create a list called skills with:
# JavaScript, React, Python, Node
skills = ["JavaScript", "React", "Python", "Node"]

# 11. Print the first skill
print(skills[0])

# 12. Create a dictionary called profile with:
# name
# age
# city
# skills
profile = {
    "name": full_name,
    "age": age,
    "city": city,
    "skills": skills
}

# 13. Print the name from profile
print(profile["name"])

# 14. Print the skills from profile
print(profile["skills"])

# 15. Create duplicate_numbers = [1, 2, 2, 3, 4, 4, 5]
duplicate_numbers = [1, 2, 2, 3, 4, 4, 5]

# 16. Convert duplicate_numbers into a set called unique_numbers
unique_numbers = set(duplicate_numbers)

# 17. Print unique_numbers
print(unique_numbers)

# 18. Create price = 100 and tax_rate = 0.08
price = 100
tax_rate = 0.08

# 19. Calculate final_price
tax_amount = price * tax_rate
final_price = price + tax_amount

# 20. Print:
# "Final price after tax: $108.0"
print(f"Final price after tax: ${final_price}")