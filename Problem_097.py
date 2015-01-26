# There is a massive non-Mersenne prime with 2,357,207 digits: 28433x2^7830457 + 1
# Find the last ten digits of this prime number.

n = 2 ** 7830457
n *= 28433
n += 1

print n % 10000000000
