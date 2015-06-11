# Find the sum of all the multiples of 3 or 5 below 1000.

def main():

    list = []

    for i in range(1000):
        if i%3 == 0 or i%5 == 0:
            list.append(i)

    return sum(list)

if __name__ == "__main__":

    main()

