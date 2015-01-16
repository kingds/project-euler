# Find the sum of all the primes below two million.

def is_prime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	sqr = int(n**(0.5)) + 1
	for divisor in range(3, sqr, 2):
		if n%divisor == 0:
			return False
	return True

total= 2

for i in range(3, 2000000, 2):
	if is_prime(i):
		total += i

print total





