# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def main():

    a = 1
    b = 1

    sum = 0

    while True:

        c = a + b
        a = b
        b = c

        if b%2 == 0:
            sum += b

        if b > 4000000:
            break

    return sum

if __name__ == "__main__":

    main()