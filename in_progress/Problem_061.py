# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.

from itertools import permutations

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
while triangle(n) < 100000:
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
	n += 1

all = []
types = [tri, squ, pen, hex, hep, oct]
for a in types:
	for b in a:
		all.append(b)

print len(tri)

for types_perm in permutations([tri, squ, pen, hex, hep, oct]):
	for a in all:
		types = list(types_perm)
		for t in types:
			if a in t:
				types.remove(t)
				break
		solution = [a]
		for b in all:
			if len(types) == 1:
				if b in types[0]:
					if cyclic(solution[-1], b) and cyclic(b, a):
						solution.append(b)
						print sum(solution)
						print solution
						quit()
			else:
				if cyclic(solution[-1], b):
					for t in types:
						if b in t:
							types.remove(t)
							solution.append(b)
							break

