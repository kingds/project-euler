# Find the sum of all the primes below two million.

def primes_sieve(limit):
    a = [True] * limit                          
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     
                a[n] = False

def main():
    sum = 0
    for prime in primes_sieve(2000000):
        sum += prime

    return sum


if __name__ == "__main__":

    print main()