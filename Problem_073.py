# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 12000

value_1 = 1.0/3.0
value_2 = 1.0/2.0

fractions = []
count = 0
for d in range(2, 12001):
	n_1 = int(d * value_1) + 1
	n_2 = int(d * value_2)
	for n in range(n_1, n_2 + 1):
		f = float(n) / float(d)
		if f != value_1 and f != value_2:
			fractions.append(f)

print len(set(fractions))
