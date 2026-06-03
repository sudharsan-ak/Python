# Day 17 Notes - Exception Handling

Status: Cleared

Source backbone:
https://github.com/Asabeneh/30-Days-Of-Python

## Main goal

Day 17 focused on handling runtime errors cleanly so a program can recover instead of crashing.

Core idea:

```text
Use exception handling around risky operations, not around lazy or messy code.
```

Common risky operations practiced:

```text
text -> int conversion
text -> float conversion
text -> datetime parsing
dictionary required-key access
list index access
division by zero
```

---

# Topic 1 - Exception basics and try / except

## What an exception is

An exception is an error that happens while the program is running.

Example:

```python
age = int("twenty")
```

Python understands the operation, but the value cannot be converted into an integer, so it raises `ValueError`.

## Basic shape

```python
try:
    age = int(age_text)
except ValueError:
    print("Invalid age value")
```

Mental model:

```text
try    -> risky code
except -> recovery path when that specific error happens
```

Avoid using a bare `except` as a habit because it catches too much and can hide real bugs.

---

# Topic 2 - Specific exceptions and error messages

## Why specific exceptions matter

Specific exception handling makes the expected failure clear.

```python
try:
    score = int(score_text)
    divisor = int(divisor_text)
    result = score / divisor
except ValueError:
    print("Score and divisor must be valid numbers")
except ZeroDivisionError:
    print("Divisor cannot be zero")
```

Common exceptions practiced:

| Exception | When it happens |
|---|---|
| `ValueError` | Correct type, bad value, like `int("abc")` |
| `TypeError` | Wrong type for an operation |
| `ZeroDivisionError` | Dividing by zero |
| `KeyError` | Missing dictionary key |
| `IndexError` | Invalid list/string index |

## Reading the exception message

Use `as error` when the original Python error message is useful.

```python
try:
    city = profile["city"]
except KeyError as error:
    print(f"Missing profile field: {error}")
```

---

# Topic 3 - else and finally blocks

## else block

`else` runs only when the `try` block succeeds.

```python
try:
    payment = float(payment_text)
except ValueError:
    print("Invalid payment amount")
else:
    print(f"Payment accepted: ${payment:.2f}")
```

Use `else` for success logic when you want the `try` block to stay focused on risky code.

## finally block

`finally` always runs, whether an exception happened or not.

```python
try:
    discount = int(discount_text)
except ValueError:
    print("Invalid discount value")
else:
    print("Discount accepted")
finally:
    print("Discount check completed")
```

Best mental model:

```text
try     -> risky code
except  -> failure path
else    -> success path
finally -> always path
```

---

# Topic 4 - Safe input and conversion patterns

## Safe conversion

Use exception handling when text must become a stricter type.

```python
try:
    age = int(age_text)
except ValueError:
    print("Age must be a valid number")
else:
    print(f"Age next year: {age + 1}")
```

## Fallback value pattern

Sometimes invalid input should fall back to a safe default.

```python
try:
    quantity = int(quantity_text)
except ValueError:
    quantity = 0

print(f"Quantity used: {quantity}")
```

Use fallback values carefully. If bad data should be rejected, print an error instead of silently replacing it.

## Keep try blocks tight

Better:

```python
try:
    price = float(price_text)
except ValueError:
    print("Price must be a valid number")
else:
    final_price = price + tax_amount
    print(f"Final price with tax: ${final_price:.2f}")
```

Risky conversion stays in `try`; success logic stays in `else`.

---

# Topic 5 - Practical exception handling patterns

## Date parsing

Day 16 parsing connects naturally to exception handling.

```python
from datetime import datetime

try:
    event_date = datetime.strptime(event_date_text, "%Y-%m-%d")
except ValueError:
    print("Invalid event date format")
else:
    print(event_date.strftime("%B %d, %Y"))
```

`strptime()` raises `ValueError` when the text does not match the expected format.

## Dictionary access

Use `.get()` for optional fields:

```python
company = profile.get("company", "Not provided")
```

Use `try / except KeyError` when a missing key is a required-field error:

```python
try:
    ticket_id = profile["ticket_id"]
except KeyError as error:
    print(f"Missing required field: {error}")
```

## List index access

```python
try:
    selected_index = int(selected_index_text)
    selected_session = sessions[selected_index]
except ValueError:
    print("Session index must be a number")
except IndexError:
    print("Selected session does not exist")
else:
    print(f"Selected session: {selected_session}")
```

This handles both invalid conversion and invalid index separately.

---

# Final mixed exercise summary

Final scenario:

```text
Warehouse shipment intake checker
```

Practiced:

```text
required dictionary field handling with KeyError
date parsing with ValueError
float conversion with ValueError
list index selection with ValueError and IndexError
success handling with else
completion handling with finally
focused real-world validation without bloated tasks
```

Final result:

```text
Day 17 final mixed exercise cleared.
```

---

# Mistakes and corrections from Day 17

Important corrections:

```text
Use specific exceptions instead of bare except.
Use else for success-only logic.
Use finally for code that must always run.
Keep try blocks focused on risky operations.
Use .get() for optional dictionary fields.
Use KeyError handling for required missing dictionary fields.
Use formatted money output like :.2f when exact two-decimal display is required.
When testing alternate dictionary values, keep the active dictionary clean.
Avoid over-fragmenting exercise tasks into too many tiny numbered steps.
```

---

# Day 17 status

```text
Day 17 - Exception Handling: Cleared
Week 3 Day 3: Cleared
Next: Day 18 - Regular Expressions
```

## What to remember before Day 18

```text
Read the exact error type before deciding what to catch.
Catch the smallest useful exception, not everything.
Use else for successful conversions or lookups.
Use finally only when something must always happen.
Do not replace simple .get() usage with unnecessary try / except.
Date parsing and numeric conversion are common places where exception handling is useful.
```
