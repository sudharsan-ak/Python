# Topic 1 - Built-in functions
print(f"{'-' * 30}Topic 1{'-' * 30}")
# 1. Create a variable called name and store your name
name = "Sudharsan"
# 2. Print the length of your name
print(len(name))
# 3. Create age = 30 and print its type
age = 30
print(type(age))
# 4. Ask the user for their age using input()
user_age = input("Please enter your age: ")
# 5. Convert that input into an integer
user_age = int(user_age) + 1
# 6. Print:
# "Next year, you will be X years old"
print(f"Next year, you will be {user_age} years old")

# ---------------------------------------------------------------------
# Topic 2: Variable Naming Rules
print(f"{'-' * 30}Topic 2{'-' * 30}")
# 1. Create variables:
# first_name
# last_name
# current_city
# years_experience
# is_software_engineer
# can_relocate
first_name = "Sudharsan"
last_name = "Srinivasan"
current_city = "Lewisville"
years_experience = 6
is_software_engineer = True
can_relocate = True

# 2. Create full_name using f-string
full_name = f"{first_name} {last_name}"
# 3. Print this:
# "Sudharsan Srinivasan is a software engineer with 6 years of experience."
print(f"{full_name} is a software engineer with {years_experience} years of experience.")

# 4. Print this:
# "Current city: Lewisville"
print(f"Current city: {current_city}")

# 5. Print this:
# "Can relocate: True"
print(f"Can relocate: {can_relocate}")

# ---------------------------------------------------------------------
# Topic 3: multiple variable assignment and assignment shortcuts.
print(f"{'-' * 30}Topic 3{'-' * 30}")
# 1. Assign first_name, last_name, and age in one line
first_name, last_name, age = "Sudharsan", "Srinivasan", 30
# 2. Print each variable
print(first_name)
print(last_name)
print(age)
# 3. Assign x = 100 and y = 200
x, y = 100, 200
# 4. Swap x and y using Python's swapping syntax
x, y = y, x
# 5. Print x and y after swapping
print(x)
print(y)
# 6. Create a list:
# skills = ["JavaScript", "React", "Python"]
skills = ["JavaScript", "React", "Python"]

# 7. Unpack the list into three variables:
# skill_one, skill_two, skill_three
skill_one, skill_two, skill_three = skills
# 8. Print all three skills
print(skill_one)
print(skill_two)
print(skill_three)

# ---------------------------------------------------------------------
# Topic 4: Python Data Types
print(f"{'-' * 30}Topic 4{'-' * 30}")
# 1. Create a string variable called name
name = "Sudharsan"

# 2. Create an integer variable called age
age = 30

# 3. Create a float variable called rating
rating = 4.9

# 4. Create a boolean variable called is_learning_python
is_learning_python = True

# 5. Create a list called skills with 3 skills
skills = ["JavaScript", "React", "Python"]

# 6. Create a dictionary called profile with:
# name
# age
# city
# skills
profile = {
  "name"   : name,
  "age"    : age,
  "city"   : "Lewisville",
  "skills" : skills
}

# 7. Create a tuple called coordinates with two numbers
coordinates = (2, 3)

# 8. Create a set called unique_numbers with duplicate values inside it
unique_numbers = {1, 2, 3, 2, 4, 6, 4}

print(unique_numbers)
# 9. Print the type of each variable
print(type(name))
print(type(age))
print(type(rating))
print(type(is_learning_python))
print(type(skills))
print(type(profile))
print(type(coordinates))
print(type(unique_numbers))

# 10. Print the first skill from the skills list
print(skills[0])

# 11. Print the name from the profile dictionary
print(profile["name"])

# ---------------------------------------------------------------------
# Topic 5: Type Conversion / Casting
print(f"{'-' * 30}Topic 5{'-' * 30}")
# 1. Ask the user for their age
# 2. Convert it to int
# 3. Print their age next year
user_age = int(input("Please enter your current age: ")) 
new_age = user_age + 1
print(new_age)

# 4. Ask the user for a product price
# 5. Convert it to float
# 6. Add 10 dollars to the price
# 7. Print the final price
price = float(input("Enter the price of this item: "))
new_price = price + 10
print(f"New Price: {new_price}")

# 8. Create a list with duplicate numbers
# 9. Convert it to a set
# 10. Print the set
duplicate_numbers = [1, 2, 3, 4, 4, 3, 5, 8, 9, 9, 6]
unique_numbers = set(duplicate_numbers)
print(unique_numbers)

# 11. Convert your name into a list of letters
# 12. Print the list
name = "Sudharsan"
print(list(name))

# ---------------------------------------------------------------------
# Topic 6: Numbers and Arithmetic
print(f"{'-' * 30}Topic 6{'-' * 30}")
# 1. Create two variables:
# num1 = 20
# num2 = 6
num1, num2 = 20, 6

# 2. Print:
# addition
# subtraction
# multiplication
# division
# floor division
# modulus
# exponent
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)

# 3. Create a variable called score = 50
# 4. Add 10 using +=
# 5. Subtract 5 using -=
# 6. Multiply by 2 using *=
# 7. Print final score
score = 50
score += 10
score -= 5
score *= 2
print(f"Final Score: {score}")

# 8. Create a variable called number
# 9. Print number % 2
# This will help us see whether the number is even or odd
number = int(input("Please enter a number: "))
print(number % 2)

# 10. Calculate final price:
# price = 100
# tax_rate = 0.08
# final_price = price + tax amount
# Print final price using f-string
price, tax_rate = 100, 0.08

tax_amount = price * tax_rate
final_price = price + tax_amount
print(f"Final Price after tax rate: {final_price}")