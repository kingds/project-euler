# Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.

a = 0
b = 1
c = 0
k = 0

pan_set = "123456789"
while True:
	k += 1
	c = a + b
	a = b
	b = c

	if "".join(sorted(set(str(c % 1000000000)))) == pan_set:
		if "".join(sorted(set(str(c)[:9]))) == pan_set:
			print k + 1
			break

