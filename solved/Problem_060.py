# Find the lowest sum for a set of five primes for which any two 
# primes concatenate to produce another prime.

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


def concat_prime(a, b):
    if not is_prime(int(str(a) + str(b))):
        return False
    if not is_prime(int(str(b) + str(a))):
        return False
    return True

def main():
    for a in primes_sieve(10000):
        print a
        concat = [a]
        for b in primes_sieve(10000):
            if len(concat) == 5:
                print concat
                return sum(concat)
            match = True
            for c in concat:
                if not concat_prime(b, c):
                    match = False
                    break
            if match:
                concat.append(b)


    # primes = list(primes_sieve(10000))
    # concat_dict = {}

    # for a in primes_sieve(50):
    #     print a
    #     concat_list = concat_dict.get(a)
    #     if concat_list == None:
    #         concat_list = []
    #     for b in primes:
    #         if concat_prime(a, b):
    #             concat_list.append(b)
    #     concat_dict[a] = concat_list


    # for a in concat_dict:
    #     concat_list = 




# [5701, 13, 5197, 6733, 8389]

if __name__ == "__main__":

    print main()