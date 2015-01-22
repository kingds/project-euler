# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

def factorial(n):
	product = 1
	for i in xrange(1, n+1):
		product *= i
	return product

def factorial_sum(n):
	total = 0
	for digit in str(n):
		total += factorial(int(digit))
	return total

total = 0
for i in xrange(3, 7*factorial(9)):
	print i
	if factorial_sum(i) == i:
		total += i

print total

