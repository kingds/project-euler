# How many words in Problem_42_Words.txt are triangle words?

words = open("Problem_42_Words.txt").read().replace('"', "").split(",")

def word_score(word):
	letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	score = 0
	word = word.upper()
	for l in word:
		score += letters.index(l) + 1
	return score

def triangle_numbers(limit):
	triangle_numbers = []
	n = 1
	t = 0
	while t < limit:
		t = int(0.5*n*(n+1))
		triangle_numbers.append(t)
		n += 1
	return triangle_numbers

t = triangle_numbers(1000)
count = 0
for w in words:
	if word_score(w) in t:
		count += 1

print count