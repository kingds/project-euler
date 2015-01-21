# What is the value of the first triangle number to have over five hundred divisors?

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

n = 28
i = 8

while True:
	n += i
	i += 1
	if len(factors(n)) > 500:
		print n
		break



