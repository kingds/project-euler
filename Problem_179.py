# Find the number of integers 1 < n < 107, for which n and n + 1 have the same number of positive divisors.

def factors(n):    
	return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

count = 0
f_n_1 = len(factors(2))
for n in range(2, 10**7):
	f_n = f_n_1
	f_n_1 = len(factors(n+1))
	if f_n == f_n_1:
		count += 1

print count