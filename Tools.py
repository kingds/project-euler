# Tools for working with prime numbers

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

def primes_sieve(limit):
	a = [True] * limit                          
	a[0] = a[1] = False

	for (i, isprime) in enumerate(a):
		if isprime:
			yield i
			for n in xrange(i*i, limit, i):     
				a[n] = False

def circular(n):
	n = str(n)
	for digit in n:
		n = n[-1] + n[:-1]
		if not is_prime(int(n)):
			return False
	return True

def factorial(n):
	product = 1
	for i in xrange(1, n+1):
		product *= i
	return product

def pandigital(n):
	if str(n).find("0") > -1:
		return False
	for i in range(len(n)):
		if str(n).find(str(i+1)) == -1:
			return False
	return True

def permutations(iterable, r=None):
	# permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
	# permutations(range(3)) --> 012 021 102 120 201 210
	pool = tuple(iterable)
	n = len(pool)
	r = n if r is None else r
	if r > n:
		return
	indices = range(n)
	cycles = range(n, n-r, -1)
	yield tuple(pool[i] for i in indices[:r])
	while n:
		for i in reversed(range(r)):
			cycles[i] -= 1
			if cycles[i] == 0:
				indices[i:] = indices[i+1:] + indices[i:i+1]
				cycles[i] = n - i
			else:
				j = cycles[i]
				indices[i], indices[-j] = indices[-j], indices[i]
				yield tuple(pool[i] for i in indices[:r])
				break
		else:
			return



