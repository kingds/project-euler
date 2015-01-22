# What is the sum of the digits of the number 2^1000?

n = 2**1000
n_string = str(n)
sum = 0

for i in range(len(n_string)):
	sum += int(n_string[i])

print sum