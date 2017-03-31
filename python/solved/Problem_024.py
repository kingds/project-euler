# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def factorial(n):
	if n == 0:
		return 1
	return reduce(lambda x,y: x*y, range(1, n+1))

def main():
	digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	remaining = 999999
	answer = ""
	while len(digits) > 0:
		permutations = factorial(len(digits))
		i = int(float(remaining) / float(permutations) * float(len(digits)))
		d = digits[i]
		remaining -= int((float(i) / float(len(digits))) * permutations)
		digits.remove(d)
		answer += d

	return int(answer)


if __name__ == "__main__":

    print main()