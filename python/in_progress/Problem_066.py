# x^2 + D*y^2 = 1
# Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained

def squares(max):
	n = 1
	square = 1
	while square < max:
		square = n**2
		yield square
		n += 1

sub_1000_squares = list(squares(1000))

x_max = 0

for d in range(2, 1001):
	print d
	if d not in sub_1000_squares:
		solved = False
		for x in squares(1000000):
			if solved:
				break
			for y in squares(x):
				if x - (d * y) == 1:
					if x**0.5 > x_max:
						x_max = int(x)
					solved = True
					break

print x_max
