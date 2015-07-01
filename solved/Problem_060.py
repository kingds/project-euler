# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

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

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def concat_prime(a, b):
    if not is_prime(int(str(a) + str(b))):
        return False
    if not is_prime(int(str(b) + str(a))):
        return False
    return True

def main():
    for a in primes_sieve(10000):
        concat = [a]
        for b in primes_sieve(10000):
            if len(concat) == 5:
                return sum(concat)
                quit()
            match = True
            for c in concat:
                if not concat_prime(b, c):
                    match = False
                    break
            if match:
                concat.append(b)


if __name__ == "__main__":

    print main()