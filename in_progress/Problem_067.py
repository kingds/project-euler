# Find the maximum total of moving on a path down the triangle through adjacent numbers

import itertools

# Create the triangle list from the raw values
triangle_raw = open("Problem_067_Triangle.txt").read()
triangle_rows = triangle_raw.split("\n")
triangle = []
for row in triangle_rows:
	triangle.append(row.split(" "))

sub_triangles = []
for i in range(len(triangle_rows) / 5):
	



max_total = 0
for path in xrange(2**14):
	position = 0
	total = int(triangle[0][0])
	for row in range(14):
		if not path & 2**row:
			position += 1
		total += int(triangle[row+1][position])
	if total > max_total:
		max_total = total

print max_total