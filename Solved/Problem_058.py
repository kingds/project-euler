# With an anticlockwise number spiral starting at 1, how great is the side length when the ratio of primes in the diagonals drops below 10%

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

s = 1
primes = [False]
d = 1
while True:
	s += 2
	for i in range(4):
		d += s-1
		primes.append(is_prime(d))
	if float(primes.count(True)) / len(primes) < 0.10:
		print s
		break

