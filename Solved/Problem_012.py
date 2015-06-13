# What is the value of the first triangle number to have over five hundred divisors?

def number_of_factors(n):    
    return len(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))


def triangle(n):
    return (n * (n + 1)) // 2 


def main():
    n = 1
    while True:
        print triangle(n), number_of_factors(triangle(n))
        if number_of_factors(triangle(n)) > 500:
            break
        n += 1

    return triangle(n)


if __name__ == "__main__":

    print main()



