# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

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


# for a in primes_sieve(1000):
# 	print a
# 	for b in primes_sieve(1000):
# 		for c in primes_sieve(1000):
# 			if b < a:
# 				break
# 			for d in primes_sieve(1000):
# 				if c < b:
# 					break
# 				if d > c:
# 					all_prime = True
# 					for p in permutations([a, b, c, d], r=2):
# 						if not is_prime(int(str(p[0]) + str(p[1]))):
# 							all_prime = False
# 							break
# 					if all_prime:
# 						print a, b, c, d
# 						quit()

two_sets = []
for b in primes_sieve(3000):
	print "B: ", b
	for a in primes_sieve(b):
		if is_prime(int(str(a) + str(b))):
			if is_prime(int(str(b) + str(a))):
				two_sets.append([a, b])


three_sets = []
for c in primes_sieve(3000):
	print "C: ", c
	for t in two_sets:
		if c > t[1]:
			all_prime = True
			for p in permutations([t[0], t[1], c], r=2):
				if not is_prime(int(str(p[0]) + str(p[1]))):
					all_prime = False
					break
			if all_prime:
				three_sets.append([t[0], t[1], c])

four_sets = []
for d in primes_sieve(15000):
	print "D: ", d
	for t in three_sets:
		if d > t[2]:
			all_prime = True
			for p in permutations([t[0], t[1], t[2], d], r=2):
				if not is_prime(int(str(p[0]) + str(p[1]))):
					all_prime = False
					break
			if all_prime:
				# print t[0], t[1], t[2], d
				four_sets.append([t[0], t[1], t[2], d])

print four_sets

for e in primes_sieve(100000):
	print "E: ", e
	for f in four_sets:
		if e > f[3]:
			all_prime = True
			for p in permutations([f[0], f[1], f[2], f[3], e], r=2):
				if not is_prime(int(str(p[0]) + str(p[1]))):
					all_prime = False
					break
			if all_prime:
				print f[0], f[1], f[2], f[3], e
				print sum([f[0], f[1], f[2], f[3], e])
				quit()




			