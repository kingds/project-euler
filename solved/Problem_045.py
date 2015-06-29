# Find the next triagonal number after T-285 that is also pentagonal and hexagonal

def triagonal(n):
	return n*(n+1)//2

def pentagonal(n):
	return n*(3*n - 1)//2

def hexagonal(n):
	return n*(2*n - 1)

def main():
	n = 143
	t = []
	p = []
	h = []

	while True:
		t_n = int(0.5*n*(n+1))
		if t_n in p and t_n in h and t_n != 40755:
			print t_n
			break
		p.append(int(0.5*n*(3*n - 1)))
		h.append(int(n*(2*n-1)))
		t.append(t_n)
		n += 1

if __name__ == "__main__":

	print main()
