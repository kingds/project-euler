

a = ""
i = 1
while len(a) < 1000001:
	a += str(i)
	i += 1

product = 1
i = 1
while i <= 1000000:
	product *= int(a[i - 1])
	i *= 10

print product