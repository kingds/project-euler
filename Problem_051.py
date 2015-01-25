# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

def is_prime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	if not n & 1:
		return False
	sqr = int(n**(0.5)) + 1
	for divisor in range(3, sqr, 2):
		if n%divisor == 0:
			return False
	return True

def primes_sieve(limit):
	a = [True] * limit                          
	a[0] = a[1] = False

	for (i, isprime) in enumerate(a):
		if isprime:
			yield i
			for n in xrange(i*i, limit, i):     
				a[n] = False

for p in primes_sieve(1000000):
	print p

	