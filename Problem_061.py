# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.

def triangle(n):
	return int(0.5 * n * (n + 1))

def square(n):
	return int(n ** 2)

def pentagonal(n):
	return int(0.5 * n * (3*n - 1))

def hexagonal(n):
	return int(n * (2*n - 1))

def heptagonal(n):
	return int(0.5 * n * (5*n - 3))

def octagonal(n):
	return int(n * (3*n - 2))

def cyclic(a, b):
	if str(a)[-2:] == str(b)[:2]:
		return True
	return False	

tri = []
squ = []
pen = []
hex = []
hep = []
oct = []
n = 0
while triangle(n) < 10000:
	n += 1
	if 999 < triangle(n) < 10000:
		tri.append(triangle(n))
	if 999 < square(n) < 10000:
		squ.append(square(n))
	if 999 < pentagonal(n) < 10000:
		pen.append(pentagonal(n))
	if 999 < hexagonal(n) < 10000:
		hex.append(hexagonal(n))
	if 999 < heptagonal(n) < 10000:
		hep.append(heptagonal(n))
	if 999 < octagonal(n) < 10000:
		oct.append(octagonal(n))

all = []
for a in [tri, squ, pen, hex, hep, oct]:
	for b in a:
		all.append(b)



first_round = []
for a in all:
	solution = [a]
	for b in all:
		if cyclic(solution[-1], b):
			solution.append(b)
			if len(solution) == 6:
				if cyclic(solution[5], solution[0]):
					first_round.append(solution)
					break

print 1281 in all
print 8128 in all
print 2882 in all
