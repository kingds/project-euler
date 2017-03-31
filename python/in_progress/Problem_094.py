# Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).

def area(a, b):
	return 0.5 * (b * (a**2 - (float(b)/2)**2)**0.5)

print area(5, 6).is_integer()

almost_equilaterals = []
for a in range(2, 10**9 / 3):
	print a
	b = a + 1
	if area(a, b).is_integer():
		almost_equilaterals.append((a, b))
	b = a - 1
	if area(a, b).is_integer():
		almost_equilaterals.append((a, b))

print almost_equilaterals