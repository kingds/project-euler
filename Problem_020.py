# Find the sum of the digits of 100!

def factorial_digit_sum(n):
	n_fac = 1
	for i in range(1, n+1):
		n_fac *= i
	digit_sum = 0
	n_fac_string = str(n_fac)
	for i in range(len(n_fac_string)):
		digit_sum += int(n_fac_string[i])

	return digit_sum

print factorial_digit_sum(100)

