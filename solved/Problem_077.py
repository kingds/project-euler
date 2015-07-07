# What is the first value that can be written as the sum of primes in over 
# five thousand different ways?

def primes_sieve(limit):
    a = [True] * limit                          
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     
                a[n] = False

def number_of_ways(total, values):
    if not values: 
        return 0
    current_value, values = values[0], values[1:]
    count = 0 
    if total % current_value == 0: 
        count = 1    
    for amount in xrange(0, total, current_value):
        count += number_of_ways(total - amount, values)    
    return count

def main():
    i = 10
    while True:
        i += 10
        if number_of_ways(i, list(primes_sieve(i))) >= 5000:
            i -= 10
            for a in range(10):
                i += 1
                if number_of_ways(i, list(primes_sieve(i))) >= 5000:
                    return i


if __name__ == "__main__":

    print main()