# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

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

def primes_sieve(limit):
    a = [True] * limit                          
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     
                a[n] = False

def main():
    a_max = 0
    b_max = 0
    n_max = 0

    for a in range(-1000, 1001):
        for b in primes_sieve(1001):
            n = 0
            while is_prime(n**2 + a*n + b):
                n += 1
                if n > n_max:
                    n_max = n
                    a_max = a
                    b_max = b

    return a_max * b_max


if __name__ == "__main__":

    print main()

