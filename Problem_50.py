# Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

MAX = 1000000

primes = []
for prime in primes_sieve(MAX):
	primes.append(prime)

max_total = 0
max_length = 0
for length in reversed(range(1, MAX)):
	for i in range(len(primes)-length):
		total = sum(primes[i : i+length])
		if total > MAX:
			break
		if is_prime(total):
			max_length = length
			max_total = total
			break
	if max_length > 0:
		break
print max_total







