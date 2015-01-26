# There is a massive non-Mersenne prime with 2,357,207 digits: 28433x2^7830457 + 1
# Find the last ten digits of this prime number.

# print str(28433 * 2**7830457 + 1)[-10:]

x = 1
total = 0
for d in reversed(str(2**7830457)[-10 :]):
	total += 28433 * int(d) * x
	x *= 10

total += 1

print str(total)[-10 :]
