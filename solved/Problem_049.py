# Find an increasing arithmetic sequence where all three terms are prime and all are 4-digit permutations of each other. What 12 digit number is formed by concatenating these terms?

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
    answers = []
    for p in primes_sieve(10000):
        if p > 999:
            for i in range(1, (10000-p)/2):
                if is_prime(p + i) and is_prime(p + 2*i) and set(str(p)) == set(str(p + i)) == set(str(p + 2*i)):
                    answers.append((p, i))
                    break
        if len(answers) > 1:
            break

    return int(str(answers[1][0]) + str(answers[1][0] + answers[1][1]) + str(answers[1][0] + 2*answers[1][1]))


if __name__ == "__main__":

    print main()