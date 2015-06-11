# What is the largest prime factor of the number 600851475143 ?

n = 600851475143
primes = [2]

def is_prime(number):
	if number == 2:
		return True
	if number % 2 == 0:
		return False
	else:
		i = 3
		while i < number/2:
			if number % i == 0:
				return False
			i += 2
	return True

divisor = 3

while True:
	if is_prime(divisor):
		if n % divisor == 0:
			n = n / divisor
			if n == 1:
				break
			factor = n
	divisor += 2

print factor
	


