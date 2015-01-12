from math import sqrt

def isprime(num):
	"""checks to see if a number is prime"""
	if type(num)!=int or num<2:

		return False

	for i in range(2, int(sqrt(num))+1):
		if num%i==0:
			return False
	return True


def nthprime(n):
	"""returns the nth prime"""
	a=2
	k=0
	while k<n:
		if isprime(a)==True:
			k+=1
		a+=1
	return a-1

print nthprime(10001)