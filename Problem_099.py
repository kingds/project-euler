# Problem_099_Base_Exp.txt contains 1000 base exponent pairs. Determine which line number has the greatest numerical value

pairs_raw = open("Problem_099_Base_Exp.txt").read().split("\n")
pairs_dict = {}
pairs = []
for pair in pairs_raw:
	split_pair = pair.split(",")
	pairs_dict[int(split_pair[0])] = int(split_pair[1])
	pairs.append((int(split_pair[0]), int(split_pair[1])))





	

