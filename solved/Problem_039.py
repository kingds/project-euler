# If p is the perimeter of a right triangle, and p <= 1000, which value of p gives the most possible triangles with integer length sides?

max_solutions = 0
p_max = 0

for p in range(3, 1001):
	solutions = 0
	for c in range(p - 3):
		for b in range(1, c):
			a = p - c - b
			if a**2 + b**2 == c**2:
				solutions += 1
	if solutions > max_solutions:
		max_solutions = solutions
		p_max = p

print p_max