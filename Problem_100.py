# Find the first arrangement of blue and red disks with over 10^12 total disks where the probablility of choosing 2 blue disks in a row is 50%. Determine the number of blue disks.

# (b / b+r)*(b-1 / b+r-1) = 0.5,  b+r > 10^12

# solutions = []
# for b in range(1, 200):
# 	for r in range(1, 200):
# 		if b == 85 and r == 35:
# 			print (float(b) / float(b+r)) * ((float(b)-1) / float(b+r-1)) == 0.5

# 		if (float(b) / (b+r)) * ((float(b)-1) / (b+r-1)) == 0.5:
# 			solutions.append((b, r))

# print solutions

def calc_r(b):
	r = r = 0.5 * ((-2*b) + (8*b**2 - 8*b + 1)**0.5 + 1)
	return r

# b = 707106781185
b = 707106781185

while True:
	r = calc_r(b)
	# print r
	if r.is_integer():
		print b, r
		print b + r
	b += 1

