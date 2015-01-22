# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers

numbers = open("Problem_13_Numbers.txt").read().split("\n")

sum = 0

for number in numbers:
	sum += int(number)

print str(sum)[0:10]