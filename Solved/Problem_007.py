# What is the 10 001st prime number?

def primes_sieve(limit):
    a = [True] * limit                          
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     
                a[n] = False

def main():
    count = 0
    for prime in primes_sieve(10**6):
        count += 1
        if count == 10001:
            return prime

if __name__ == "__main__":

    print main()


