# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers

def main():
    numbers = open("Problem_013_Numbers.txt").read().split("\n")
    return int(str(reduce(lambda x, y: int(x) + int(y), numbers))[0:10])

if __name__ == "__main__":

    print main()