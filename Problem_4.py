# Find the largest palindrome made from the product of two 3-digit numbers.

a = 999
b = 999
palindrome = 0

for a in reversed(range(100, 999)):

	for b in reversed(range(100, 999)):

		product = str(a * b)

		if product == product[::-1]:
			if int(product) > palindrome:
				palindrome = int(product)

print palindrome





