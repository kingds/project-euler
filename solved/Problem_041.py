# What is the largest n-digit pandigital prime that exists?

# If the sum of the digits of a n is divisible by 3, then n is divisible by 3
# For an 8 digit pandigital: 1+2+3+4+5+6+7+8 = 36, divisible by 3
# For a 9 digit pandigital: 1+2+3+4+5+6+7+8+9 = 45, divisible by 3

def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    else:
        i = 3
        while i < number/2:
            if number % i == 0:
                return False
            i += 2
    return True

def permutations(iterable):
    pool = tuple(iterable)
    n = len(pool)
    r = n
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield int("".join(str(pool[i]) for i in indices[:r]))
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield int("".join(str(pool[i]) for i in indices[:r]))
                break
        else:
            return

def main():
    for n in range(7, 2, -1):
        for pandigital in permutations(range(n, 0, -1)):
            if is_prime(int(pandigital)):
                return pandigital


if __name__ == "__main__":

    print main()
