# What is the largest n-digit pandigital prime that exists?

def primes_sieve(limit):
	a = [True] * limit                          
	a[0] = a[1] = False

	for (i, isprime) in enumerate(a):
		if isprime:
			yield i
			for n in xrange(i*i, limit, i):     
				a[n] = False
def pandigital(n):
	if str(n).find("0") > -1:
		return False
	for i in range(len(str(n))):
		if str(n).find(str(i+1)) == -1:
			return False
	return True

largest = 0
for n in primes_sieve(10000000):
	if pandigital(n):
		largest = n

print largest
