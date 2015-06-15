# Find the denominator of the product of the four fractions which might be incorrectly simplified:


fractions = []
for n in range(10, 100):
	for d in range(n + 1, 100):
		for a in [(0, 0), (0, 1), (1, 0), (1, 1)]:
			if n % 10 != 0:
				if int(str(n)[a[0]]) != 0 and int(str(d)[a[1]]) != 0:
					if int(str(n)[1 - a[0]]) == int(str(d)[1 - a[1]]):
						if float(n)/float(d) == float(str(n)[a[0]]) / float(str(d)[a[1]]):
							print "Yeeeeee"
							fractions.append((n, d))
							break

product = 1
for fraction in set(fractions):
	product *= float(fraction[0]) / float(fraction[1])

print product