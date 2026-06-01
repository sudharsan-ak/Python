print(f"{'-' * 30} Day 15 Final: Order Checkout Debugging {'-' * 30}")

# Scenario:
# You are debugging a small online store checkout script.
# Run one broken line at a time, read the error/output, comment it again,
# then write the corrected version below it.

# ------------------------------------------------------------
# Task 1 - Display vs number

customer_name = "Ashwin"
order_id = 1045

# broken_order_message = customer_name + " placed order #" + order_id

# Fix it using an f-string.
# Print the fixed order message.
fixed_order_message = f"{customer_name} placed order #{order_id}"
print(f"Fixed order message: {fixed_order_message}")


# ------------------------------------------------------------
# Task 2 - Numeric string from external data

item_price = "49.99"
shipping_fee = 5

# broken_total_price = item_price + shipping_fee

# Print the type of item_price.
# Fix total_price so it becomes 54.99 as a number.
# Print total_price.
print(f"Type of item_price: {type(item_price)}")
total_price = float(item_price) + shipping_fee
print(f"Total price: {total_price}")

# ------------------------------------------------------------
# Task 3 - Wrong list access

cart_items = ["Laptop Stand", "USB-C Cable", "Wireless Mouse"]

# broken_first_item = cart_items["first"]

# Fix it by accessing the first item correctly.
# Print first_item.
print(f"First item: {cart_items[0]}")

# ------------------------------------------------------------
# Task 4 - Wrong dictionary access style

customer = {
    "name": "Ashwin",
    "email": "Ashwin@example.com",
    "membership": "Gold"
}

# broken_membership = customer("membership")

# Fix it using the correct dictionary access pattern.
# Print membership.
print(f"Membership: {customer['membership']}")

# ------------------------------------------------------------
# Task 5 - Missing dictionary key

shipping_address = {
    "city": "Dallas",
    "state": "TX"
}

# broken_zip_code = shipping_address["zip_code"]

# In comments, answer:
# 1. What error do you expect?
# 2. Why?
# Fix it using get() with fallback value "Not provided".
# Print zip_code.

# Answers: 
# 1. KeyError, since "zip_code" is not a key in shipping_address dictionary.
# 2. This error occurs because the key is not present in the dictionary, not because of wrong index type.
zip_code = shipping_address.get("zip_code", "Not provided")
print(f"Zip code: {zip_code}")

# ------------------------------------------------------------
# Task 6 - Function missing return

# def calculate_cart_total(price, tax):
#     total = price + tax

# broken_cart_total = calculate_cart_total(120, 10)
# print(broken_cart_total + 5)

# In comments, explain where None comes from.
# Fix the function so it returns the total.
# Store the result in cart_total.
# Print cart_total.

# Answers:
# None comes from the function call, because the function is not returning anything.
def calculate_cart_total(price, tax):
    return price + tax

cart_total = calculate_cart_total(120, 10)
print(f"Cart total: {cart_total}")

# ------------------------------------------------------------
# Task 7 - Method returns None

delivery_estimates = [5, 2, 7, 3]

# broken_sorted_estimates = delivery_estimates.sort()
# print(broken_sorted_estimates)

# In comments, explain why broken_sorted_estimates becomes None.
# Fix it using sorted() so the original list stays unchanged.
# Print sorted_estimates.
# Print original delivery_estimates.

# Answers:
# broken_sorted_estimates becomes None because list.sort() sorts the original list in place and returns None. It does not return the sorted list.
sorted_estimates = sorted(delivery_estimates)
print(f"Sorted estimates: {sorted_estimates}")
print(f"Original delivery estimates: {delivery_estimates}")

# ------------------------------------------------------------
# Task 8 - Append correctly

order_status_history = ["Order placed", "Payment confirmed"]

# broken_status_history = order_status_history.append("Packed")
# print(broken_status_history)

# In comments, explain why the broken variable becomes None.
# Append "Packed" correctly.
# Print order_status_history.

# Answers:
# order_status_history.append() updates the original list in place and returns None. It does not return the updated list.
order_status_history.append("Packed")
print(f"Updated order status history: {order_status_history}")

# ------------------------------------------------------------
# Task 9 - Mixed type list

item_quantities = [2, "3", 1, "4"]

# broken_total_items = sum(item_quantities)

# In comments, explain why sum(item_quantities) fails.
# Create cleaned_quantities.
# Convert only the string numbers into integers.
# Print cleaned_quantities.
# Print total_items.

# Answers:
# sum(item_quantities) fails because the item_quantities list has unsupported operand type(s).
# The operation expects a list of integers, but the list also contains strings.
cleaned_quantities = [int(quantity) if isinstance(quantity, str) else quantity for quantity in item_quantities]
print(f"Cleaned quantities: {cleaned_quantities}")
total_items = sum(cleaned_quantities)
print(f"Total items: {total_items}")

# ------------------------------------------------------------
# Task 10 - Nested data debugging

order = {
    "customer": "Ashwin",
    "summary": {
        "items_count": "4",
        "gift_wrap_count": 1
    }
}

# broken_total_units = order["items_count"] + order["gift_wrap_count"]

# In comments, explain the first mistake in the broken line.
# Access items_count from the nested summary dictionary.
# Access gift_wrap_count from the nested summary dictionary.
# Convert items_count to int.
# Print total_units.

# Answers:
# "items_count" and later "gift_wrap_count" is not a top level key inside order dictionary, hence the access fails.
items_count = int(order["summary"]["items_count"])
gift_wrap_count = order["summary"]["gift_wrap_count"]
total_units = items_count + gift_wrap_count
print(f"Total units: {total_units}")

# ------------------------------------------------------------
# Task 11 - Safe uppercase

preferences = {
    "currency": "usd"
}

# selected_country = preferences.get("country")

# broken_country = selected_country.upper()

# Fix it using get() with fallback value "us".
# Print the uppercase country.
safe_country = preferences.get("country", "us")
print(f"Safe country: {safe_country.upper()}")

# ------------------------------------------------------------
# Task 12 - Final clean summary

receipt = {
    "customer": "Ashwin",
    "order_id": 1045,
    "total": 54.99,
    "status": "Packed"
}

# broken_receipt = receipt["customer"] + " order " + receipt["order_id"] + " total $" + receipt["total"] + " is " + receipt["status"]

# Fix it using an f-string.
# Print:
# Ashwin order 1045 total $54.99 is Packed.
fixed_receipt = f"{receipt['customer']} order {receipt['order_id']} total ${receipt['total']} is {receipt['status']}."
print(fixed_receipt)