# How many, not necessarily distinct, values of nCr, for 1 <= n <= 100, are greater than one-million?

def factorial(n):
	product = 1
	for i in xrange(1, n+1):
		product *= i
	return product

def combination(n, r):
	return factorial(n)/(factorial(r) * factorial(n-r))

count = 0
for n in range(1, 101):
	for r in range(1, n):
		if combination(n, r) > 1000000:
			count += 1
print count