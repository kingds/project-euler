# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

def factorial(n):
    product = 1
    for i in xrange(1, n+1):
        product *= i
    return product


def main():
    digit_factorials = [factorial(n) for n in range(10)]
    checked_combos = []
    total = 0
    for n in xrange(3, 7*factorial(9)):
        unique_list = sorted(str(n))
        if not unique_list in checked_combos:
            checked_combos.append(unique_list)
            if n == sum([digit_factorials[int(d)] for d in str(n)]):
                total += n

    return total


if __name__ == "__main__":
    
    print main()

