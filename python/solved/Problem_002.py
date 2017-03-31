# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def main():
    total = 0
    (a, b) = (1, 2)
    while b < 4000000:
        (a, b) = (b, a+b)
        if a%2 == 0:
            total += a

    return total

if __name__ == "__main__":

    print main()