# Find the value of n < 100000 for which n / totient(n) is the greatest

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def prime_factors(n):
	prime_factors = []
	for f in factors(n):
		if is_prime(f):
			prime_factors.append(f)
	return prime_factors

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

def totient(n):
	for p in prime_factors(n):
		n *= (1 - 1.0/p)
	return int(n)

def main():
	max_n = 0
	max_ratio = 0
	for n in range(1, 1000000):
		ratio = float(n) / totient(n)
		if ratio > max_ratio:
			max_n = n
			max_ratio = ratio

	return max_n


if __name__ == "__main__":

	print main()





