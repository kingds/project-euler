# Problem_102_Triangles.txt contains the coordinates of 1000 triangles. Find the number of triangles for which the interior contains the origin

triangles_raw = open("Problem_102_Triangles.txt").read().split("\n")
triangles = []
for t in triangles_raw:
	triangles.append(t.split(","))

def contains_origin(t):

	p1 = (float(t[0]), float(t[1]))
	p2 = (float(t[2]), float(t[3]))
	p3 = (float(t[4]), float(t[5]))

	# y = mx + b
	y_intercepts = []
	try:
		m1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
		b1 = p2[1] - (m1 * p2[0])	
		if p1[1] <= b1 <= p2[1] or p2[1] <= b1 <= p1[1]:
			y_intercepts.append(b1)
	except Exception:
		pass

	try:
		m2 = (p3[1] - p2[1]) / (p3[0] - p2[0])
		b2 = p3[1] - (m2 * p3[0])
		if p2[1] <= b2 <= p3[1] or p3[1] <= b2 <= p2[1]:
			y_intercepts.append(b2)
	except Exception:
		pass

	try:
		m3 = (p1[1] - p2[1]) / (p1[0] - p3[0])
		b3 = p1[1] - (m3 * p1[0])
		if p1[1] <= b3 <= p3[1] or p3[1] <= b3 <= p1[1]:
			y_intercepts.append(b3)	
	except Exception:
		pass

	if len(y_intercepts) == 2:
		if y_intercepts[0] <= 0 <= y_intercepts[1] or y_intercepts[1] <= 0 <= y_intercepts[0]:
			return True
		else:
			return False
	else:
		return False


count = 0
for t in triangles:
	if contains_origin(t):
		count += 1

print count
