

def diagonal_sum(side_length):
	total = 1
	l = 3
	while l < side_length + 1:
		total += 4*l**2 - 6*l + 6
		l += 2
	return total

print diagonal_sum(1001)
