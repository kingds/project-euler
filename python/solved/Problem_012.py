# What is the value of the first triangle number to have over five hundred divisors?

def number_of_factors(n):    
    return len(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def triangle(n):
    return (n * (n + 1)) // 2 


def main():
    n = 0
    while True:
        n += 1
        t = triangle(n)
        if t % 2 != 0:
            continue
        if number_of_factors(t) > 500:
            break
        if t > 76576500:
            break        

    return triangle(n)


if __name__ == "__main__":

    print main()



