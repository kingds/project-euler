# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

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

def truncatable(n):
    if n < 10:
        return False
    n = str(n)
    for i in range(1, len(n)):
        if not is_prime(int(n[i:])):
            return False
        if not is_prime(int(n[:i])):
            return False
    return True

def main():
    count = 0
    total = 0
    for n in primes_sieve(1000000):
        if truncatable(n):
            total += n
            count += 1
            if count == 11:
                return total


if __name__ == "__main__":

    print main()

