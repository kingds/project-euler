a = 1
b = 1

sum = 0

while True:

	c = a + b
	a = b
	b = c

	if b%2 == 0:
		sum += b

	if b > 4000000:
		break

print sum