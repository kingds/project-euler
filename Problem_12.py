# What is the value of the first triangle number to have over five hundred divisors?

divisors = 500
factors = []

n = 0
i = 0

while True:
	i += 1
	n += i

	factors = []
	for d in range(1, n):
		if n % d == 0:
			factors.append(d)

	if len(factors) == divisors:
		break

print factors
print n