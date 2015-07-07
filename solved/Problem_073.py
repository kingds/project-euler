# How many fractions lie between 1/3 and 1/2 in the sorted 
# set of reduced proper fractions for d <= 12000

def main():
	value_1 = 1.0/3.0
	value_2 = 1.0/2.0
	fractions = set()
	for denominator in range(6000, 12001):
		n_1 = int(denominator * value_1) + 1
		n_2 = int(denominator * value_2)
		if denominator % 2 != 0:
			n_2 += 1
		for numerator in range(n_1, n_2):
			fractions.add(float(numerator) / float(denominator))

	return len(fractions)




if __name__ == "__main__":

	print main()
