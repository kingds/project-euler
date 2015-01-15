# Which starting number, under one million, produces the longest Collatz chain?

def create_chain(starting_value):
	n = starting_value
	chain = [n]
	while n != 1:
		if n % 2 == 0:
			n = n/2
		else:
			n = (3*n) + 1
		chain.append(n)
	return chain

max_length = 0
max_starting_value = 0

for i in range(1, 1000000):
	print i
	chain = create_chain(i)
	if len(chain) > max_length:
		max_length = len(chain)
		max_starting_value = i

print max_starting_value

