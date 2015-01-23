# Tools for working with prime numbers

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

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def most_common_element(iterable):
	return max(set(iterable), key=iterable.count)

def prime_factors(n):
	prime_factors = []
	for f in factors(n):
		if is_prime(f):
			prime_factors.append(f)
	return prime_factors

def prime_factor_count(n):
	count = 0
	for f in factors(n):
		if is_prime(f):
			count += 1
	return count    		

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

def palindrome(n):
	for i in range(len(str(n))):
		if str(n)[i] != str(n)[-i - 1]:
			return False
	return True

def lychrel(n):
	i = 0
	while i < 50:
		i += 1
		n = int(str(n)) + int(str(n)[:: -1])
		if palindrome(n):
			return False
	return True

def digit_sum(n):
	return sum(int(d) for d in str(n))


