# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

def primes_sieve(limit):
	a = [True] * limit                          
	a[0] = a[1] = False

	for (i, isprime) in enumerate(a):
		if isprime:
			yield i
			for n in xrange(i*i, limit, i):     
				a[n] = False

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


n = 33

while True:
	answer = True
	if not is_prime(n):
		for p in primes_sieve(n):
			if ((n - p)/2)**0.5 % 1 == 0:
				answer = False
				break
		if answer:
			print n
			break
	n += 2