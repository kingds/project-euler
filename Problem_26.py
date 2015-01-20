# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

from decimal import *

getcontext().prec = 1000

longest_d = 1
repeated_length = 0


def decimalize(denominator):
	fractional = str(Decimal(1)/Decimal(denominator)).replace("0.", "")

	return "0." + fractional

print max(list())





