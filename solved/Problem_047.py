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

def main(): 
    n = 0
    count = 0
    while True:
        n += 1
        if prime_factor_count(n) == 4:
            count += 1
        else: 
            count = 0
        if count == 4:
            return n - 3


if __name__ == "__main__":

    print main()