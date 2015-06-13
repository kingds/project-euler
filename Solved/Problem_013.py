# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers

def main():
    numbers = open("Problem_013_Numbers.txt").read().split("\n")
    sum = 0
    for number in numbers:
        sum += int(number)

    return int(str(sum)[0:10])


if __name__ == "__main__":

    print main()