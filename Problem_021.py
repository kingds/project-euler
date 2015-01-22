# Evaluate the sum of all amicable numbers under 10000

def factors(n):    
	factor_list = reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
	factor_list.remove(n)
	return factor_list

def factor_sum(n):
	return sum(factors(n))

sums = [0]
for i in range(1, 10000):
	sums.append(factor_sum(i))

amicable_numbers = []

for i in range(len(sums)):
	try:
		if i == sums[sums[i]] and i != sums[i]:
			amicable_numbers.append(i)
	except Exception:
		pass

print amicable_numbers
print sum(amicable_numbers)









