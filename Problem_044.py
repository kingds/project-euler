# Find the pair of pentagonal numbers with a pentagonal sum and difference, with the minimal different between the two. What is the difference between the two numbers?

n = 0
p = []
a = True
while a:
	n += 1
	x = int(0.5*n*(3*n - 1))
	p.append(x)
	for i in p:
		if x - i in p:
			if ((24*(x+i) + 1)**0.5 + 1)/6 % 1 == 0.0:
				print x - i
				a = False
				break