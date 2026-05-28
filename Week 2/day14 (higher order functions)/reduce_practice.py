# Topic 4: reduce()

print(f"{'-' * 30} Topic 4 {'-' * 30}")

# 1. Import reduce from functools
from functools import reduce

# 2. Create a list called numbers with values:
# 1, 2, 3, 4, 5
numbers = [1, 2, 3, 4, 5]

# 3. Use reduce() with a lambda to create total_sum
# Add all numbers together
# Print: Total sum: <value>
total_sum = reduce(lambda accumulator, number: accumulator + number, numbers)
print(f"Total sum: {total_sum}")

# 4. Use reduce() with a lambda to create product
# Multiply all numbers together
# Print: Product: <value>
product = reduce(lambda accumulator, number: accumulator * number, numbers)
print(f"Product: {product}")

# 5. Create a normal function called add_scores
# It should accept two parameters:
# accumulator
# score
# It should return accumulator + score
def add_scores(accumulator, score):
    return accumulator + score

# 6. Create a list called scores with values:
# 80, 90, 75, 85
scores = [80, 90, 75, 85]

# 7. Use reduce() with add_scores to create total_score
# Print: Total score: <value>
total_score = reduce(add_scores, scores)
print(f"Total score: {total_score}")

# 8. Use reduce() with a lambda and an initial value of 100
# Add all numbers from numbers starting from 100
# Store the result in total_with_bonus
# Print: Total with bonus: <value>
total_with_bonus = reduce(lambda accumulator, number: accumulator + number, numbers, 100)
print(f"Total with bonus: {total_with_bonus}")

# 9. Create a list called words with values:
# "Python", "higher", "order", "functions"
words = ["Python", "higher", "order", "functions"]

# 10. Use reduce() with a lambda to combine the words into one string
# The final result should be:
# Python higher order functions
# Store it in sentence
# Print: Sentence: <value>
sentence = reduce(lambda accumulator, word: accumulator + " " + word, words)
print(f"Sentence: {sentence}")

# 11. Create a list called name_lengths_source with values:
# "Sudharsan", "Ashwin", "Python"
name_lengths_source = ["Sudharsan", "Ashwin", "Python"]

# 12. Use reduce() with a lambda to calculate the total number of characters
# Hint: accumulator starts at 0
# Use an initial value of 0
# Store the result in total_characters
# Print: Total characters: <value>
total_characters = reduce(lambda accumulator, name: accumulator + len(name), name_lengths_source, 0)
print(f"Total characters: {total_characters}")

# 13. Create a list called prices with values:
# 19.99, 5.50, 10.00
prices = [19.99, 5.50, 10.00]

# 14. Use reduce() with a lambda to calculate the total price
# Store the result in total_price
# Print: Total price: <value>
total_price = reduce(lambda accumulator, price: accumulator + price, prices)
print(f"Total price: {total_price}")

# 15. Also calculate the same total price using sum()
# Store the result in total_price_with_sum
# Print: Total price with sum: <value>
total_price_with_sum = sum(prices)
print(f"Total price with sum: {total_price_with_sum}")

# 16. Add a comment explaining which is cleaner for prices:
# reduce() or sum()
# for simple totals like prices, sum() is cleaner than reduce()