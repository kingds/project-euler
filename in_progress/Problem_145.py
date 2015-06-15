# A number is reversible if the sum(n + reverse(n)) consists of all odd digits.
# How many reversible numbers are there below one-billion (10^9)?

def reversible(n):
	if str(n)[-1] == "0":
		return False
	for d in str(n + int(str(n)[::-1])):
		if int(d) % 2 == 0:
			return False
	return True

n = 1
count = 0
while n < 1000:
	print n
	if reversible(n):
		count += 1
	n += 1

print count