# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

from itertools import combinations

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

# checked = []
# for p in primes_sieve(100000):
# 	if p >= 10000:
# 		p = str(p)
# 		if p[2] == p[3]:
# 			checked.append(p[:2] + p[-1])

# for c in checked:
# 	if checked.count(c) == 8:
# 		print c
# 		break

for d in combinations("012345", 2):
	print d
	checked = []
	for p in primes_sieve(1000000):
		if p >= 100000:
			p = list(str(p))
			if p[int(d[0])] == p[int(d[1])]:
				p.pop(int(d[0])) 
				p.pop(int(d[1]) - 1)
				checked.append("".join(p))
	for c in checked:
		if checked.count(c) == 8:
			print d, c
			c = list(c)
			c.insert(int(d[0]), 0)
			c.insert(int(d[1]), 0)
			print c
			quit()

for d in combinations("012345", 3):
	print d
	checked = []
	for p in primes_sieve(1000000):
		if p >= 100000:
			p = list(str(p))
			if p[int(d[0])] == p[int(d[1])] == p[int(d[2])]:
				p.pop(int(d[0])) 
				p.pop(int(d[1]) - 1)
				p.pop(int(d[2]) - 2)
				checked.append("".join(p))
	for c in checked:
		if checked.count(c) == 8:
			print d, c
			c = list(c)
			c.insert(int(d[0]), 0)
			c.insert(int(d[1]), 0)
			c.insert(int(d[2]), 0)
			print c
			quit()




	