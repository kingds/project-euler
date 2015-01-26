# How many starting numbers below ten million will arrive at 89 when a square digit chain is created?

def final_value(n):
	while n != 1 and n != 89:
		n = sum(int(d)**2 for d in str(n))
	return n

count = 0
for i in range(1, 100001):
	if final_value(i) == 89:
		count += 1
	if i == 10 or i == 100 or i == 10000 or i == 100000:
		print i, count

print count
