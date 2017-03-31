# How many circular primes are there below one million?

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    if not n & 1:
        return False
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

def circular(n):
    n = str(n)
    for digit in n:
        n = n[-1] + n[:-1]
        if not is_prime(int(n)):
            return False
    return True

def main():
    return len([n for n in primes_sieve(1000000) if circular(n)])


if __name__ == "__main__":

    print main()