

def r(a, n):
	return ((a-1)**n + (a+1)**n) % a**2

print max(max(r(a, n) for n in range(10000)) for a in range(1000, 1001))
