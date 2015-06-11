# Find the least number for which the proportion of bouncy numbers is exactly 99%.

def bouncy(n):
	if "".join(sorted(str(n))) == str(n):
		return False
	if "".join(reversed(sorted(str(n)))) == str(n):
		return False
	return True

count = 0
i = 0
while True:
	i += 1
	if bouncy(i):
		count += 1
	if float(count) / i >= 0.99:
		print i
		break