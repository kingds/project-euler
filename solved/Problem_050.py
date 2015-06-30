# Which prime, below one-million, can be written as the sum of the most consecutive primes?

def primes_sieve(limit):
    a = [True] * limit                          
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     
                a[n] = False

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

def main():
    limit = 5000
    primes = list(primes_sieve(limit))
    max_count = 0
    max_prime = 0
    while True:
        i = 0
        total = 0
        count = 0
        while i < len(primes):
            total += primes[i]
            count += 1
            if total > 1000000:
                break
            i += 1
        while i < len(primes):
            if is_prime(total):
                if count > max_count:
                    max_count = count
                    max_prime = total
                break
            total -= primes[i]
            count -= 1
            i -= 1
        if len(primes) == 1:
            return max_prime
        primes.pop(0)


if __name__ == "__main__":

    print main()