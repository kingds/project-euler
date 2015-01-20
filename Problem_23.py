# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def factors(n):    
	factor_list = reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
	factor_list.remove(n)
	factor_list = list(set(factor_list))
	return factor_list

def factor_sum(n):
	return sum(factors(n))

abundant_numbers = []
for i in range(12, 28124):
	if factor_sum(i) > i:
		abundant_numbers.append(i)

print abundant_numbers

total = 0
for n in range(28124):
	print n
	for a in abundant_numbers:
		if a > n/2 + 1:
			total += n
			break
		try:
			abundant_numbers.index(n-a)
			break
		except Exception:
			pass

print total

