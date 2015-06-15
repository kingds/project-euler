# In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator? 

n0 = 1
n1 = 3
d0 = 1
d1 = 2

count = 0
for i in range(1000):
	n2 = 2*n1 + n0
	n0 = n1
	n1 = n2
	d2 = 2*d1 + d0
	d0 = d1
	d1 = d2
	if len(str(n2)) > len(str(d2)):
		count += 1

print count
