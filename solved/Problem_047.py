# Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

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

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))              

def prime_factor_count(n):
    count = 0
    for f in factors(n):
        if is_prime(f):
            count += 1
    return count

def primes_sieve(limit):
    a = [True] * limit                          
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     
                a[n] = False

# def main(): 
#     n = 0
#     count = 0
#     while True:
#         n += 1
#         if prime_factor_count(n) >= 4:
#             count += 1
#         else: 
#             count = 0
#         if count == 4:
#             return n - 3

def main():
    products = []
    primes = list(primes_sieve(100))
    for a in range(len(primes_sieve), 0, -1):
        for b in range(a, 0, -1):
            for c in range()


if __name__ == "__main__":

    print main()