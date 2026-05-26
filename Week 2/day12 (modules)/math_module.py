# Topic 3: Built-in math module
# 1. Import the math module
import math

# 2. Create a variable called radius and set it to 7
radius = 7

# 3. Calculate the area of a circle using math.pi and radius ** 2
# Store the result in a variable called circle_area
circle_area = math.pi * radius ** 2

# 4. Print circle_area with this format:
# Circle area: <circle_area>
print(f"Circle area: {circle_area}")

# 5. Create a variable called number and set it to 81
number = 81

# 6. Use math.sqrt() to calculate the square root of number
# Store the result in a variable called square_root
square_root = math.sqrt(number)

# 7. Print square_root with this format:
# Square root: <square_root>
print(f"Square root: {square_root}")

# 8. Create a variable called price and set it to 19.25
price = 19.25

# 9. Use math.ceil() on price
# Store the result in a variable called rounded_up_price
rounded_up_price = math.ceil(price)

# 10. Use math.floor() on price
# Store the result in a variable called rounded_down_price
rounded_down_price = math.floor(price)

# 11. Print rounded_up_price with this format:
# Rounded up price: <rounded_up_price>
print(f"Rounded up price: {rounded_up_price}")

# 12. Print rounded_down_price with this format:
# Rounded down price: <rounded_down_price>
print(f"Rounded down price: {rounded_down_price}")

# 13. Create a variable called base and set it to 3
base = 3

# 14. Create a variable called exponent and set it to 4
exponent = 4

# 15. Use the ** operator to calculate base to the exponent
# Store the result in a variable called power_result
power_result = base ** exponent

# 16. Print power_result with this format:
# Power result: <power_result>
print(f"Power result: {power_result}")

# 17. Use math.pow() to calculate base to the exponent
# Store the result in a variable called math_power_result
math_power_result = math.pow(base, exponent)

# 18. Print math_power_result with this format:
# Math power result: <math_power_result>
print(f"Math power result: {math_power_result}")

# 19. Print the type of power_result with this format:
# Power result type: <type>
print(f"Power result type: {type(power_result)}")

# 20. Print the type of math_power_result with this format:
# Math power result type: <type>
print(f"Math power result type: {type(math_power_result)}")