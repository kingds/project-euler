# What is the sum of the numbers on the diagonals of a 1001 by 1001 spiral formed by
# starting with the number 1 and moving to the right in a clockwise direction?

def diagonal_sum(side_length):
    total = 1
    l = 3
    while l < side_length + 1:
        total += 4*l**2 - 6*l + 6
        l += 2
    return total

def main():
    return diagonal_sum(1001)


if __name__ == "__main__":

    print main()