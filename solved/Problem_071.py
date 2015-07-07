# By listing the set of reduced proper fractions for d <= 1,000,000 in ascending order of size, find the numeratior of the fraction immediately to the left of 3/7

def main():
    value = 3.0/7.0

    min_difference = 1
    n_target = 0
    d_target = 0
    for d in range(10**6 + 1, 2, -1):

        n = int(value * d)
        difference = value - float(n)/float(d)
        if difference < min_difference and d != 7 and difference != 0:
            min_difference = difference
            n_target = n
            d_target = d

    return n_target


if __name__ == "__main__":

    print main()