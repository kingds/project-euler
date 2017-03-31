# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

def factorial(n):
    product = 1
    for i in xrange(1, n+1):
        product *= i
    return product

def main():
    digit_factorials = [factorial(n) for n in range(10)]
    checked = {}
    total = 0
    for n in xrange(3, 50000):
        unique_string = "".join(sorted(str(n)))
        checked_sum = checked.get(unique_string)
        if checked_sum:
            if n == checked_sum:
                total += n
        else:
            n_sum = sum(digit_factorials[int(d)] for d in str(n))
            checked[unique_string] = n_sum
            if n == n_sum:
                total += n

    return total


if __name__ == "__main__":
    
    print main()
