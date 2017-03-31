# What is the sum of the digits of the number 2^1000?

def main():
    return sum([int(digit) for digit in str(2**1000)])


if __name__ == "__main__":

    print main()