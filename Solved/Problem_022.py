# What is the total of all the names scores in the file?

names = open("Problem_22_Names.txt").read().replace('"', "").split(",")

names.sort()

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

total_score = 0

for i in range(len(names)):
	score = 0
	for l in range(len(names[i])):
		score += letters.index(names[i][l]) + 1
	score *= i + 1
	total_score += score

print total_score