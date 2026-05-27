# Topic 1 - Boolean
print(f"{'-' * 30}Topic 1{'-' * 30}")
# 1. Create a variable called is_software_engineer and set it to True
is_software_engineer = True

# 2. Create a variable called is_learning_python and set it to True
is_learning_python = True

# 3. Create a variable called has_finished_day_3 and set it to False
has_finished_day_3 = False

# 4. Print all three variables
print(is_software_engineer)
print(is_learning_python)
print(has_finished_day_3)

# 5. Print the type of one boolean variable
print(type(has_finished_day_3))

# ---------------------------------------------------------------------
# Topic 2: Assignment Operators
print(f"{'-' * 30}Topic 2{'-' * 30}")
# 1. Create a variable called score and set it to 50
score = 50

# 2. Add 10 to score using +=
score += 10

# 3. Print score
print(score)

# 4. Subtract 5 from score using -=
score -= 5

# 5. Print score
print(score)

# 6. Multiply score by 2 using *=
score *= 2

# 7. Print score
print(score)

# 8. Divide score by 10 using /=
score /= 10

# 9. Print score
print(score)

# 10. Create a variable called counter and set it to 0
counter = 0

# 11. Increase counter by 1 using +=
counter += 1

# 12. Print counter
print(counter)

# ---------------------------------------------------------------------
# Topic 3: Comparison Operators
print(f"{'-' * 30}Topic 3{'-' * 30}")
# 1. Create a variable called age and set it to 30
age = 30

# 2. Print whether age is equal to 30 using ==
print(age == 30)

# 3. Print whether age is not equal to 25 using !=
print(age != 25)

# 4. Print whether age is greater than 18 using >
print(age > 18)

# 5. Print whether age is less than 40 using <
print(age < 40)

# 6. Print whether age is greater than or equal to 30 using >=
print(age >= 30)

# 7. Print whether age is less than or equal to 29 using <=
print(age <= 29)

# 8. Create two variables:
# score = 85
# passing_score = 70
score, passing_score = 85, 70

# 9. Print whether score is greater than or equal to passing_score
print(score >= passing_score)

# 10. Print whether score is less than passing_score
print(score < passing_score)

# ---------------------------------------------------------------------
# Topic 4 - Logical Operators
print(f"{'-' * 30}Topic 4{'-' * 30}")
# 1. Create a variable called age and set it to 30
age = 30

# 2. Create a variable called has_experience and set it to True
has_experience = True

# 3. Print whether age is greater than or equal to 18 AND has_experience is True
print(age >= 18 and has_experience)

# 4. Create a variable called has_degree and set it to False
has_degree = False

# 5. Print whether has_degree OR has_experience is True
print(has_degree or has_experience)

# 6. Create a variable called is_blocked and set it to False
is_blocked = False

# 7. Print the opposite of is_blocked using not
print(not is_blocked)

# 8. Create a variable called score and set it to 85
score = 85

# 9. Print whether score is greater than 70 AND less than 100
print(score > 70 and score < 100)

# 10. Create a variable called is_weekend and set it to False
is_weekend = False

# 11. Create a variable called is_holiday and set it to True
is_holiday = True

# 12. Print whether it is either weekend OR holiday
print(is_weekend or is_holiday)

# ---------------------------------------------------------------------
# Topic 5 - Operator Precedence
print(f"{'-' * 30}Topic 5{'-' * 30}")
# 1. Create a variable called result1 and store 10 + 5 * 2
result1 = 10 + 5 * 2

# 2. Print result1
print(result1)

# 3. Create a variable called result2 and store (10 + 5) * 2
result2 = (10 + 5) * 2

# 4. Print result2
print(result2)

# 5. Create a variable called result3 and store 2 ** 3 * 4
result3 = 2 ** 3 * 4

# 6. Print result3
print(result3)

# 7. Create these variables:
# age = 30
# score = 85
# is_holiday = False
age = 30
score = 85
is_holiday = False

# 8. Print whether age is at least 18 AND score is greater than 70
print(age >= 18 and score > 70)

# 9. Print this expression using parentheses:
# age is at least 18 AND either score is greater than 90 OR is_holiday is True
print(age >= 18 and (score > 90 or is_holiday))

# 10. Create a variable called final_result and store (20 + 10) / 5
final_result = (20 + 10) / 5

# 11. Print final_result
print(final_result)