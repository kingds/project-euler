# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

def digit_sum(n):
	return sum(int(d) for d in str(n))

max_sum = 0
for a in range(1, 100):
	for b in range(1, 100):
		d_sum = digit_sum(a**b)
		if d_sum > max_sum:
			max_sum = d_sum

print max_sum