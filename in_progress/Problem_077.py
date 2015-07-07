# What is the first value that can be written as the sum of primes in over 
# five thousand different ways?

def primes_sieve(limit):
	a = [True] * limit                          
	a[0] = a[1] = False

	for (i, isprime) in enumerate(a):
		if isprime:
			yield i
			for n in xrange(i*i, limit, i):     
				a[n] = False

def number_of_ways( total, coins):
    if not coins: return 0
    c, coins = coins[0], coins[1:]
    count = 0 
    if total % c == 0: count += 1    
    for amount in xrange( 0, total, c):
        count += number_of_ways(total - amount, coins)    
    return count

def main():
	# checked_values = [0] * 250
	# for a in primes_sieve(50):
	# 	for b in primes_sieve(50):
	# 		for c in primes_sieve(50):
	# 			for d in primes_sieve(50):
	# 				for e in primes_sieve(50):
	# 					total = a + b + c + d + e
	# 					checked_values[total] += 1


	# print checked_values
	# for i in range(250):
	# 	if checked_values[i] > 5000:
	# 		return i

	for i in xrange(10, 10000):
		print i
		if number_of_ways(i + 1, list(primes_sieve(i))) >= 5000:
			return i

if __name__ == "__main__":

	print main()

