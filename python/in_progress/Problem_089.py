# Find the number of characters saved by writing each of the roman numerals in Problem_089_Roman.txt in their minimal form

def int_to_roman(n):
	r = n
	M = r / 1000
	r = r % 1000
	C = r / 100
	r = r % 100
	X = r / 10
	r = r % 10
	numeral = ""
	numeral += M * "M"
	numeral += C * "C"
	numeral += X * "X"
	numeral += r * "I"
	numeral = numeral.replace("CCCCC", "D")
	numeral = numeral.replace("XXXXX", "L")
	numeral = numeral.replace("IIIII", "V")
	return numeral

def roman_to_int(r):
	n = 0
	n += r.count("M") * 1000
	n += r.count("D") * 500
	n += r.count("C") * 100
	n += r.count("L") * 50
	n += r.count("X") * 10
	n += r.count("V") * 5
	n += r.count("I")
	return n

numerals = open("Problem_089_Roman.txt").read().split("\n")

# original_length = len("".join(numerals))

# new_length = 0
# for r in numerals:
# 	new_length += len(int_to_roman(roman_to_int(r)))

# print original_length
# print new_length
# print original_length - new_length

for r in numerals:
	if int_to_roman(roman_to_int(r)) != r:
		print roman_to_int(r), r, int_to_roman(roman_to_int(r))



