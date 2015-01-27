# Problem_099_Base_Exp.txt contains 1000 base exponent pairs. Determine which line number has the greatest numerical value

from math import log

pairs_raw = open("Problem_099_Base_Exp.txt").read().split("\n")
pairs_dict = {}
pairs = []
for pair in pairs_raw:
	split_pair = pair.split(",")
	pairs_dict[int(split_pair[0])] = int(split_pair[1])
	pairs.append((int(split_pair[0]), int(split_pair[1])))


def greater(a, b):
	if a[1] * log(a[0]) > b[1] * log(b[0]):
		return 0
	else:
		return 1

max_pair = pairs[0]
for i in range(1, len(pairs)):
	if greater(max_pair, pairs[i]) == 1:
		max_pair = pairs[i]

print pairs.index(max_pair) + 1
	

