# What is the 10 001st prime number?

def is_prime(number):
	if number == 2:
		return True
	elif number % 2 == 0:
		return False
	else:
		i = 3
		while i < number/2:
			if number % i == 0:
				return False
			i += 2
	return True

n = 10001
count = 0
i = 2

while count != n:
	if is_prime(i):
		count += 1
	i += 1


print i-1


