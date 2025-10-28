import numpy as np
import math
x = math.pi / 2
y = np.sin(x)
print(y)
x*=2
y = np.sin(x)
print(round(y,5))

from decimal import Decimal, ROUND_HALF_UP

number = Decimal("1.2225")
# The '0.001' sets the number of decimal places
rounded_number = number.quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)
print(rounded_number)
