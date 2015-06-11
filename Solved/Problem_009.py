# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for a in range(1, 998):
	for b in range(1, 998):
		c = 1000 - a - b
		if (a*a) + (b*b) == c*c:
			print a * b * c
			break



