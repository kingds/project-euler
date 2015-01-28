# Find the first arrangement of blue and red disks with over 10^12 total disks where the probablility of choosing 2 blue disks in a row is 50%. Determine the number of blue disks.

# (b / b+r)*(b-1 / b+r-1) = 0.5,  b+r > 10^12

solutions = []
for b in range(1, 100):
	for r in range(1, 100):
		if (float(b) / (b+r)) * ((float(b)-1) / (b+r-1)) == 0.5:
			solutions.append((b, r))

print solutions

