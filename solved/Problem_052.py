# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def check_value(x):
    for a in range(1, 7):
        if sorted(list(str(x))) != sorted(list(str(a * x))):
            return False
    return True

def main():
    x = 10
    while not check_value(x):
        x += 1

    return x


if __name__ == "__main__":

    print main()

