def sum_between(a, b):
	return int(0.5 * (b + a) * (b - a + 1)) - b - a

def sum_between_list(a, b):
	total = 0
	for i in range(a+1, b):
		total += i
	return total



for (a, b) in ((3, 5), (10, 30), (4, 10), (0, 24)):
	print sum_between(a, b) , sum_between_list(a, b)