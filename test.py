
def is_prime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	sqr = int(n**(0.5)) + 1
	for divisor in range(3, sqr, 2):
		if n%divisor == 0:
			return False
	return True

limit = 2000000
number_list = range(3, limit)
sum = 2

for n in number_list:
	if is_prime(n):
		sum += n
		a = n
		while a < limit:
			print a
							number_list.remove(a)
			except Exception:
				pass
			a += n

print sum