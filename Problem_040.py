# An irrational decimal fraction is created by concatenating the positive integers
# If d_n represents the nth digit of the fractional part, find d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000

c = ""
n = 1
while len(c) <= 1000000:
	c += str(n)
	n += 1

product = 1
for i in range(7):
	product *= int(c[10**i - 1])

print product