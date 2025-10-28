#   This script demonstrates how to round a floating-point number to a specified number of decimal places in Python.

# Method 1: Using the round() function
print("Method 1: Using the round() function for 3.14259265")
number = 3.14259265
rounded_number = round(number, 3)
print(rounded_number)
print("")

# Method 2: Using f-strings (for display)
print("Method 2: Using f-strings (for display) for 1.23456789")
number = 1.23456789
print(f"The rounded number is: {number:.3f}")
print("")

# Method 3: Using the Decimal module (for high precision
print("Method 3: Using the Decimal module (for high precision) for 1.2225")
from decimal import Decimal, ROUND_HALF_UP
number = Decimal("1.2225")
# The '0.001' sets the number of decimal places
rounded_number = number.quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)
print(rounded_number)
print("")

# Method 4: Truncating to 3 decimal places
print("Method 4: Truncating to 3 decimal places for 3.14159265 (not half-up rounding)")
import math
number = 3.14159265
truncated_number = math.trunc(number * 1000) / 1000
print(truncated_number)

