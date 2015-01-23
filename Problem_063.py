# How many n-digit positive integers exist which are also an nth power?

l = []
for a in range(1, 10):
	for b in range(100):
		if len(str(a**b)) == b:
			l.append(a**b)

print len(set(l))


