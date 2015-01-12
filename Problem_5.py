# Smallest number even divisible by all numbers between 1 and 20

# Create the list of divisors
divisor_list = range(2, 21)
divisor_list.reverse()

# Create the test value
n = 0
divisible = False

# Iterate until it is divisible
while divisible == False:
	n += 20
	divisible = True
	for divisor in divisor_list:
		if n % divisor != 0:
			divisible = False
			break
	

# Print the result
print n

