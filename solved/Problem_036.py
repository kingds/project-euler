# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def is_palindrome(a):
	a = str(a)
	for i in range(len(a)/2):
		if a[i] != a[-1 * (i+1)]:
			return False
	return True

total = 0
for i in range(1000000):
	if is_palindrome(str(i)) and is_palindrome(bin(i).replace("0b", "")):
		total += i

print total