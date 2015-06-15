# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


from decimal import *

getcontext().prec = 2000

longest_d = 1
repeated_length = 0

def fractional(n, d):
	return str(Decimal(n)/Decimal(d)).replace("0.", "")


def repeater(n, d):
	f = fractional(n, d)
	r = ""
	if len(f) >= 2000:
		for i in range(1, 1000):
			if f[5:5 + i] == f[5 + i:5 + 2*i]:
				r = f[0:i]
				break
	return r


max_length = 0
max_d = 0
for d in range(1, 1001):
	if len(repeater(1, d)) > max_length:
		max_length = len(repeater(1, d))
		max_d = d

print max_d
