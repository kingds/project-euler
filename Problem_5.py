# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

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

