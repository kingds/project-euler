# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

from fractions import Fraction
from decimal import Decimal

def e_fraction(n):
	n = n + 1
	x = 0.0
	for i in range(n, 0, -1):
		if i % 3 == 1:
			j = int(i / 3) * 2
		else:
			j = 1

		x = Fraction(1 / (x + j))
	return x + 1

total = 0
for d in str(e_fraction(100)).split("/")[0]:
	total += int(d)

print total


