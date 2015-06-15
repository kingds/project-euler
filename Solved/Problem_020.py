# Find the sum of the digits of 100!

def factorial_digit_sum(n):
    n_factorial = reduce(lambda x, y: x*y, range(1, n+1))
    return reduce(lambda x, y: x+y, [int(a) for a in str(n_factorial)])

def main():
    return factorial_digit_sum(100)


if __name__ == "__main__":

    print main()