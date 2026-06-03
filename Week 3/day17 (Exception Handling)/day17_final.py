# ---------------------------------------------------------------------
# Day 17 - Final Mixed Exercise: Warehouse Shipment Intake Checker

print(f"{'-' * 30} Day 17 Final Exercise {'-' * 30}")

# Scenario:
# A warehouse system receives shipment request data as text.
# Your job is to safely validate the data without crashing the program.

# 1. Import datetime from the datetime module.

from datetime import datetime

# 2. Create a dictionary called shipment_request with:
# "tracking_id" -> "SHIP-2048"
# "ship_date" -> "2026-09-15"
# "package_weight" -> "12.5"
# "shipping_option_index" -> "1"
# Do NOT include "destination_zip" yet.

shipment_request = {
    "ship_date": "2026-09-15",
    "tracking_id": "SHIP-2048",
    "package_weight": "12.5",
    "shipping_option_index": "1"
}

# shipment_request = {
    # "ship_date": "September 15, 2026",
    # "package_weight": "twelve",
    # "destination_zip": "12345",
    # "shipping_option_index": "1",
    # "shipping_option_index": "5",
    # "shipping_option_index": "five"
# }

# 3. Create a list called shipping_options with: "Standard", "Express", "Overnight"
shipping_options = ["Standard", "Express", "Overnight"]

# 4. Try to read shipment_request["destination_zip"].
# If it is missing, catch KeyError as error and print:
# Missing required shipment field: <error message>

try:
    destination_zip = shipment_request["destination_zip"]
except KeyError as error:
    print(f"Missing required shipment field: {error}")

# 5. Safely parse shipment_request["ship_date"] using datetime.strptime()
# with the format "%Y-%m-%d".
# If parsing succeeds, print:
# Ship date: September 15, 2026
# If parsing fails, print:
# Invalid ship date format

try:
    ship_date = datetime.strptime(shipment_request["ship_date"], "%Y-%m-%d")
except ValueError:
    print("Invalid ship date format")
else:
    print(f"Ship date: {ship_date.strftime('%B %d, %Y')}")

# 6. Safely convert shipment_request["package_weight"] into a float.
# If conversion succeeds:
# - if weight is greater than 50, print: Heavy package
# - otherwise, print: Standard package weight
# If conversion fails, print:
# Package weight must be a valid number

try:
    package_weight = float(shipment_request["package_weight"])
except ValueError:
    print("Package weight must be a valid number")
else:
    if package_weight > 50:
        print("Heavy package")
    else:
        print("Standard package weight")

# 7. Safely convert shipment_request["shipping_option_index"] into an integer.
# Use it to select the shipping option from shipping_options.
# If successful, print:
# Selected shipping option: Express
# If the index text is not numeric, print:
# Shipping option index must be a number
# If the index does not exist, print:
# Selected shipping option does not exist

try:
    shipping_option_index = int(shipment_request["shipping_option_index"])
    selected_shipping_option = shipping_options[shipping_option_index]
except ValueError:
    print("Shipping option index must be a number")
except IndexError:
    print("Selected shipping option does not exist")
else:
    print(f"Selected shipping option: {selected_shipping_option}")
finally:
    print("Shipping option check completed")

# 8. Add a finally block to the shipping option check that always prints:
# Shipping option check completed

# 9. Test these failure paths one at a time:
# - Change "ship_date" to "September 15, 2026"
# - Change "package_weight" to "twelve"
# - Change "shipping_option_index" to "five"
# - Change "shipping_option_index" to "5"

# 10. After testing, return the file to the original valid values from step 2.