"""
Calculates the minimum amount of change necessary for a monetary amount.

Expects a starting input of USD$. Rounds down on fractional pennies.
"""
from __future__ import print_function
from decimal import Decimal
import sys

# Define the denominations to be used
denominations = ['100', '50', '20', '10', '5', '2', '1', '0.25', '0.10', '0.05', '0.01']
names = {'0.25': "quarters", '0.10': "dimes", '0.05': "nickels", '0.01': "pennies"}

# Usage
if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " <monetary_amount>", file=sys.stderr)
    sys.exit(1)

# Read the amount as a command-line argument, stripping the dollar sign if it was passed
try:
    amount = Decimal(sys.argv[1].strip('$'))
except ValueError:
    print("Amount provided must be numeric!\nProvided '" + sys.argv[1] + "'", file=sys.stderr)
    sys.exit(2)

# Calculate the least amount of change
for den in denominations:
    num = Decimal(amount // Decimal(den))
    amount -= num * Decimal(den)
    if num:
        print(str(num) + " " + names[den] if den in names else str(num) + " $" + str(den) + " dollar bills")

