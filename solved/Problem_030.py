# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

total_total = 0

for i in range(2, 354295):
	total = 0
	for digit in str(i):
		total += int(digit) ** 5
	if total == i:
		print i
		total_total += i

print total_total


