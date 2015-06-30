# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

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

def main():
    family = 8
    limit = 1000000
    for prime in primes_sieve(limit):
        prime_string = str(prime)
        for digit in range(11 - family):
            count = 1
            if prime_string.count(str(digit)) > 1:
                prime_string = str(prime)
                misses = 0
                for i in range(digit + 1, 10):
                    test_value = int(prime_string.replace(str(digit), str(i)))
                                        
                    if not is_prime(test_value):
                        misses += 1
                    else:
                        count += 1
                    if misses >= 11 - family + 1:
                        break
                    if count == family:
                        
                        return prime


if __name__ == "__main__":

    print main()