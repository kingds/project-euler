# Find the value of n < 100000 for which n / totient(n) is the greatest

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def prime_factors(n):
	prime_factors = []
	for f in factors(n):
		if is_prime(f):
			prime_factors.append(f)
	return prime_factors

def totient(n):
	f = sorted(list(factors(n)))
	non_coprimes = []
	for i in range(1, len(f)):
		a = f[i]
		b = a
		while b < n:
			non_coprimes.append(b)
			b += a
	coprimes = [1]
	for i in range(2, n):
		if i not in non_coprimes:
			coprimes.append(i)
	return len(coprimes)

cube_dict = {}
for n in range(10000):
	cube = n**3
	digits = "".join(sorted(str(cube)))
	try:
		cube_dict[digits].append(n)
	except KeyError:
		cube_dict[digits] = [n]

for d in sorted(cube_dict.keys()):
	if len(cube_dict[d]) == 5:
		print min(cube_dict[d]) ** 3


