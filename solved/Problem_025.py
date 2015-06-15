# What is the first term in the Fibonacci sequence to contain 1000 digits?

a = 1
b = 1
c = 0
n = 2

while len(str(c)) < 1000:
	c = a + b
	a = b
	b = c
	n += 1

print n



