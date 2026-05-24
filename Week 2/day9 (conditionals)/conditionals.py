# ---------------------------------------------------------------------
# Topic 1: if, indentation, and comparison conditions
# 1. Create a variable called age and set it to your age
age = 30

# 2. If age is greater than or equal to 18, print "You are eligible to vote"
if age >= 18:
  print("You are eligible to vote")

# 3. Create a variable called score and set it to 85
score = 85

# 4. If score is greater than or equal to 80, print "Good score"
if score >= 80:
  print("Good score")

# 5. Create a variable called language and set it to "Python"
language = "Python"

# 6. If language is equal to "Python", print "You are learning Python"
if language == "Python":
  print("You are learning Python")

# 7. Create a variable called city and set it to "Lewisville"
city = "Lewisville"

# 8. If city is not equal to "Austin", print "You are not in Austin"
if city != "Austin":
  print("You are not in Austin")

# 9. Create a variable called temperature and set it to 95
temperature = 95

# 10. If temperature is greater than 90, print "It is hot today"
if temperature > 90:
  print("It is hot today")

# 11. Create a variable called completed_day_8 and set it to True
completed_day_8 = True

# 12. If completed_day_8 is True, print "Ready for Day 9"
# Write this condition in the clean Python style, not using == True
if completed_day_8:
  print("Ready for Day 9")

# ---------------------------------------------------------------------
# Topic 2: if / else and user input basics
# 1. Create a variable called user_age and set it to 16
user_age = 16

# 2. If user_age is greater than or equal to 18, print "You can vote"
# Otherwise, print "You cannot vote yet"
if user_age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")

# 3. Create a variable called exam_score and set it to 72
exam_score = 72

# 4. If exam_score is greater than or equal to 60, print "Passed"
# Otherwise, print "Failed"
if exam_score >= 60:
    print("Passed")
else:
    print("Failed")

# 5. Create a variable called is_logged_in and set it to False
is_logged_in = False

# 6. If is_logged_in is True, print "Welcome back"
# Otherwise, print "Please log in"
# Use clean Python style. Do not write == True.
if is_logged_in:
    print("Welcome back")
else:
    print("Please log in")

# 7. Ask the user to enter their age and store it in a variable called entered_age
# Convert the input to an integer
entered_age = int(input("Please enter your age: "))

# 8. If entered_age is greater than or equal to 18, print "Adult"
# Otherwise, print "Minor"
if entered_age >= 18:
    print("Adult")
else:
    print("Minor")

# 9. Ask the user to enter their favorite language and store it in favorite_language
# Use strip() to remove extra spaces
favorite_language = input("Please enter your favorite language: ").strip()

# 10. If favorite_language is equal to "Python", print "Python is a solid choice"
# Otherwise, print "Today we are still practicing Python"
if favorite_language == "Python":
    print(f"{favorite_language} is a solid choice")
else:
    print("Today we are still practicing Python")

# ---------------------------------------------------------------------
# Topic 3: if / elif / else
# 1. Create a variable called final_score and set it to 92
final_score = 92

# 2. Use if / elif / else to print:
# "Grade A" if final_score is greater than or equal to 90
# "Grade B" if final_score is greater than or equal to 80
# "Grade C" if final_score is greater than or equal to 70
# "Needs improvement" otherwise
if final_score >= 90:
    print("Grade A")
elif final_score >= 80:
    print("Grade B")
elif final_score >= 70:
    print("Grade C")
else:
    print("Needs improvement")

# 3. Create a variable called account_status and set it to "pending"
account_status = "pending"

# 4. Use if / elif / else to print:
# "Account is active" if account_status is "active"
# "Account is waiting for approval" if account_status is "pending"
# "Account is disabled" if account_status is "disabled"
# "Unknown account status" otherwise
if account_status == "active":
    print("Account is active")
elif account_status == "pending":
    print("Account is waiting for approval")
elif account_status == "disabled":
    print("Account is disabled")
else:
    print("Unknown account status")

# 5. Ask the user to enter a number from 1 to 3
# Store it in a variable called menu_choice
# Convert the input to an integer
menu_choice = int(input("Please enter a number from 1 to 3: "))

# 6. Use if / elif / else to print:
# "You selected Profile" if menu_choice is 1
# "You selected Settings" if menu_choice is 2
# "You selected Logout" if menu_choice is 3
# "Invalid menu choice" otherwise
if menu_choice == 1:
    print("You selected Profile")
elif menu_choice == 2:
    print("You selected Settings")
elif menu_choice == 3:
    print("You selected Logout")
else:
    print("Invalid menu choice")

# 7. Create a variable called temperature and set it to 72
temperature = 72

# 8. Use if / elif / else to print:
# "Hot" if temperature is greater than or equal to 90
# "Warm" if temperature is greater than or equal to 70
# "Cool" if temperature is greater than or equal to 50
# "Cold" otherwise
if temperature >= 90:
    print("Hot")
elif temperature >= 70:
    print("Warm")
elif temperature >= 50:
    print("Cool")
else:
    print("Cold")

# ---------------------------------------------------------------------
# Topic 4: logical conditions with and / or
# 1. Create a variable called applicant_age and set it to 25
applicant_age = 25

# 2. Create a variable called has_work_permit and set it to True
has_work_permit = True

# 3. If applicant_age is greater than or equal to 18 AND has_work_permit is True,
# print "Applicant can work"
# Otherwise, print "Applicant cannot work"
if applicant_age >= 18 and has_work_permit:
    print("Applicant can work")
else:
    print("Applicant cannot work")

# 4. Create a variable called has_coupon and set it to False
has_coupon = False

# 5. Create a variable called is_premium_member and set it to True
is_premium_member = True

# 6. If has_coupon is True OR is_premium_member is True,
# print "Discount applied"
# Otherwise, print "No discount available"
if has_coupon or is_premium_member:
    print("Discount applied")
else:
    print("No discount available")

# 7. Create a variable called username and set it to "admin"
username = "Admin"

# 8. Create a variable called password and set it to "python123"
password = "python123"

# 9. If username is equal to "admin" AND password is equal to "python123",
# print "Login successful"
# Otherwise, print "Invalid credentials"
if username == "Admin" and password == "python123":
    print("Login successful")
else:
    print("Invalid credentials")

# 10. Ask the user to enter their preferred language
# Store it in a variable called preferred_language
# Use strip()
preferred_language = input("Please enter your preferred language: ").strip()

# 11. If preferred_language is "Python" OR preferred_language is "JavaScript",
# print "Good language choice"
# Otherwise, print "We will still focus on Python today"
if preferred_language in ["Python", "JavaScript"]:
    print("Good language choice")
else:
    print("We will still focus on Python today")

# 12. Create a variable called user_age and set it to 20
user_age = 20

# 13. Create a variable called has_ticket and set it to False
has_ticket = False

# 14. Create a variable called is_vip and set it to True
is_vip = True

# 15. If user_age is greater than or equal to 18 AND has_ticket is True OR is_vip is True,
# print "Event entry allowed"
# Otherwise, print "Event entry denied"
# Use parentheses to make the logic clear
if (user_age >= 18 and has_ticket) or is_vip:
    print("Event entry allowed")
else:    
    print("Event entry denied")

# ---------------------------------------------------------------------
# Topic 5: nested conditionals vs cleaner logical conditions
# 1. Create a variable called customer_age and set it to 22
customer_age = 22

# 2. Create a variable called has_membership_card and set it to True
has_membership_card = True

# 3. Write a nested conditional:
# If customer_age is greater than or equal to 18:
#     If has_membership_card is True, print "Member access granted"
#     Otherwise, print "Membership card required"
# Otherwise, print "Must be at least 18"
if customer_age >= 18:
   if has_membership_card:
       print("Member access granted")
   else:
       print("Membership card required")
else:
    print("Must be at least 18")

# 4. Create a variable called account_balance and set it to 500
account_balance = 500

# 5. Create a variable called withdrawal_amount and set it to 200
withdrawal_amount = 200

# 6. Create a variable called account_active and set it to True
account_active = True

# 7. Write a simple condition using and:
# If account_active is True AND account_balance is greater than or equal to withdrawal_amount,
# print "Withdrawal approved"
# Otherwise, print "Withdrawal denied"
if account_active and account_balance >= withdrawal_amount:
    print("Withdrawal approved")
else:
    print("Withdrawal denied")

# 8. Create a variable called login_username and set it to "admin"
login_username = "admin"

# 9. Create a variable called login_password and set it to "wrongpass"
login_password = "wrongpass"

# 10. Create a variable called account_locked and set it to False
account_locked = False

# 11. Write a cleaner if / elif / else chain:
# If account_locked is True, print "Account is locked"
# Else if login_username is not equal to "admin", print "Invalid username"
# Else if login_password is not equal to "python123", print "Invalid password"
# Otherwise, print "Login successful"
if account_locked:
    print("Account is locked")
elif login_username != "admin":
    print("Invalid username")
elif login_password != "python123":
    print("Invalid password")
else:
    print("Login successful")

# 12. Create a variable called order_total and set it to 120
order_total = 120

# 13. Create a variable called has_free_shipping_coupon and set it to False
has_free_shipping_coupon = False

# 14. Write a condition using parentheses:
# If order_total is greater than or equal to 100 OR has_free_shipping_coupon is True,
# print "Free shipping applied"
# Otherwise, print "Shipping fee applied"
if (order_total >= 100 or has_free_shipping_coupon):
    print("Free shipping applied") 
else:
    print("Shipping fee applied")

# 15. Create a variable called employee_role and set it to "manager"
employee_role = "manager"

# 16. Create a variable called has_security_badge and set it to False
has_security_badge = False

# 17. Write a cleaner if / elif / else chain:
# If employee_role is not "manager" and not "admin", print "Access denied: role not allowed"
# Else if has_security_badge is False, print "Access denied: badge required"
# Otherwise, print "Secure area access granted"
if employee_role not in ["manager", "admin"]:
    print("Access denied: role not allowed")
elif not has_security_badge:
    print("Access denied: badge required")
else:
    print("Secure area access granted")

# ---------------------------------------------------------------------
# Topic 6: truthy/falsy values with strings, lists, and dictionaries
# 1. Create a variable called username and set it to an empty string
username = ""

# 2. If username has a value, print "Username provided"
# Otherwise, print "Username is missing"
if username:
    print("Username provided")
else:
    print("Username is missing")

# 3. Create a variable called cleaned_username and set it to "   admin   ".strip()
cleaned_username = "   admin   ".strip()

# 4. If cleaned_username has a value, print "Clean username received"
# Otherwise, print "Clean username is missing"
if cleaned_username:
    print("Clean username received")
else:
    print("Clean username is missing")

# 5. Create a list called cart_items and set it to an empty list
cart_items = []

# 6. If cart_items has items, print "Cart has items"
# Otherwise, print "Cart is empty"
if cart_items:
    print("Cart has items")
else:
    print("Cart is empty")

# 7. Add "keyboard" and "mouse" to cart_items using extend()
cart_items.extend(["keyboard", "mouse"])

# 8. If cart_items has items, print "Cart has items now"
# Otherwise, print "Cart is still empty"
if cart_items:
    print("Cart has items now")
else:
    print("Cart is still empty")

# 9. Create a dictionary called user_profile and set it to an empty dictionary
user_profile = {}

# 10. If user_profile has data, print "Profile exists"
# Otherwise, print "Profile is empty"
if user_profile:
    print("Profile exists")
else:
    print("Profile is empty")

# 11. Add these key-value pairs to user_profile:
# "name" -> "Sudharsan"
# "role" -> "Developer"
user_profile["name"] = "Sudharsan"
user_profile["role"] = "Developer"

# 12. If user_profile has data, print "Profile exists now"
# Otherwise, print "Profile is still empty"
if user_profile:
    print("Profile exists now")
else:
    print("Profile is still empty")

# 13. If "role" exists as a key in user_profile, print "Role is available"
# Otherwise, print "Role is missing"
if "role" in user_profile:
    print("Role is available")
else:
    print("Role is missing")

# 14. Ask the user to enter a project name
# Store it in project_name
# Use strip()
project_name = input("Please enter a project name: ").strip()

# 15. If project_name is empty, print "Project name is required"
# Otherwise, print "Project name saved"
if not project_name:
    print("Project name is required")
else:
    print("Project name saved")

# 16. Create a variable called score and set it to 0
score = 0

# 17. If score has a truthy value, print "Score exists"
# Otherwise, print "Score is zero"
if score:
    print("Score exists")
else:
    print("Score is zero")

# ---------------------------------------------------------------------
# Topic 7: short-hand conditionals
# 1. Create a variable called age and set it to 21
age = 21

# 2. Create a variable called age_status using a short-hand if / else:
# "Adult" if age is greater than or equal to 18
# "Minor" otherwise
age_status = "Adult" if age >=18 else "Minor"

# 3. Print age_status
print(f"Age status: {age_status}")

# 4. Create a variable called score and set it to 58
score = 58

# 5. Create a variable called exam_result using a short-hand if / else:
# "Passed" if score is greater than or equal to 60
# "Failed" otherwise
exam_result = "Passed" if score >= 60 else "Failed"

# 6. Print exam_result
print(f"Exam result: {exam_result}")

# 7. Create a variable called is_logged_in and set it to False
is_logged_in = False

# 8. Create a variable called login_message using a short-hand if / else:
# "Welcome back" if is_logged_in is True
# "Please log in" otherwise
# Use clean Python boolean style. Do not write == True.
login_message = "Welcome back" if is_logged_in else "Please log in"

# 9. Print login_message
print(f"Login message: {login_message}")

# 10. Create a list called cart_items and set it to ["laptop"]
cart_items = ["laptop"]

# 11. Create a variable called cart_status using a short-hand if / else:
# "Cart has items" if cart_items has data
# "Cart is empty" otherwise
cart_status = "Cart has items" if cart_items else "Cart is empty"

# 12. Print cart_status
print(f"Cart status: {cart_status}")

# 13. Create a dictionary called profile and set it to an empty dictionary
profile = {}

# 14. Create a variable called profile_status using a short-hand if / else:
# "Profile exists" if profile has data
# "Profile missing" otherwise
profile_status = "Profile exists" if profile else "Profile missing"

# 15. Print profile_status
print(f"Profile status: {profile_status}")

# 16. Create a variable called temperature and set it to 95
temperature = 95

# 17. Use a normal if / else, not short-hand:
# If temperature is greater than or equal to 90, print "Hot day"
# Otherwise, print "Not too hot"
# This is to prove you know when normal if / else is still cleaner for direct actions.
if temperature >= 90:
    print("Hot day")
else:
    print("Not too hot")