# Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

def rectangle_count(x, y):
	count = 0
	area = x * y
	for a in range(1, x+1):
		for b in range(1, y+1):
			count += (x - a + 1) * (y - b + 1)
	return count

count_dict = {}
for x in range(100):
	for y in range(100):
		count = rectangle_count(x, y)
		count_dict[count] = (x, y)

closest = min(abs(2000000 - count) for count in count_dict.keys())
area = 0
try:
	size = count_dict[2000000 - closest]
except Exception:
	pass
try:
	size = count_dict[2000000 + closest]
except Exception:
	pass
print size

print rectangle_count(size[0], size[1])













