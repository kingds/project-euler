# How many digit factorial chains, with a starting number below one million, contain exactly sixty non-repeating terms?

from math import factorial

digit_factorials = []
for i in range(10):
	digit_factorials.append(factorial(i))

def factorial_digit_sum(n):
	return sum(digit_factorials[int(d)] for d in str(n))

def count_terms(n):
	count = 0
	while True:
		count += 1
		n_prev = n
		n = factorial_digit_sum(n)
		if n == n_prev:
			break
		if n == 145:
			break
		if n == 871:
			count += 1
			break
		if n == 872:
			count += 1
			break
		if n == 169:
			count += 2
			break
	return count

c_count = 0
for i in range(10, 1000000):
	c = count_terms(i)
	if c > 58:
		print i, c
		c_count += 1

print c_count
