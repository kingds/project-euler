# With an anticlockwise number spiral starting at 1, how great is the side length when the ratio of primes in the diagonals drops below 10%

import random

def is_probable_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True
 
    for i in range(5):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True

def main():
    s = 2
    prime_count = 0
    count = 0
    d = 1
    while True:
        for i in range(4):
            d += s
            if is_probable_prime(d):
                prime_count += 1
            count += 1
        s += 2
        if (100 * prime_count) / count < 10:
            return s - 3


if __name__ == "__main__":

    print main()