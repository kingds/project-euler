# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

total = 0
for i in range(1, 1001):
	total += i**i

print str(total)[-10:]