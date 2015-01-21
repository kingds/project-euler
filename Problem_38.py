# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

pan = []

for i in xrange(100000):
	string = ""
	n = 1
	while True:
		string += str(n * i)
		n += 1
		if string.find("0") > -1:
			break
		if len(string) > 9:
			break
		if len(string) == 9:
			if len(set(string)) == 9:
				pan.append(string)
				break

print max(pan)