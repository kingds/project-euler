# How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

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


limit = int(50000000**0.5)
squares = []
cubes = []
fourths = []
for p in primes_sieve(limit):
	p_2 = p**2
	p_3 = p**3
	p_4 = p**4
	squares.append(p_2)
	if p_3 < 50000000:
		cubes.append(p_3)
	if p_4 < 50000000:	
		fourths.append(p_4)

sums = []
for s in squares:
	for c in cubes:
		for f in fourths:
			if s + c + f < 50000000:
				sums.append(s + c + f)

print len(set(sums))
