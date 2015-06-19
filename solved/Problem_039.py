# If p is the perimeter of a right triangle, and p <= 1000, which value of p gives the most possible triangles with integer length sides?

def main():
	max_solutions = 0
	p_max = 0
	for p in xrange(12, 1001, 2):
		solutions = 0
		for a in xrange(p//3, p//2):
			for b in xrange(1, a):
				if a**2 + b**2 == (p - a - b)**2:
					solutions += 1
		if solutions > max_solutions:
			max_solutions = solutions
			p_max = p

	return p_max


# def main():
# 	triples_dict = {}
# 	for a in range(1, 500):
# 		for b in range(a, 500):
# 			c = (a**2 + b)

if __name__ == "__main__":

	print main()