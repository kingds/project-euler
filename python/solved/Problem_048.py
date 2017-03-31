# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

def main():
    total = 0
    for i in range(1, 1001):
        total += i**i

    return int(str(total)[-10:])


if __name__ == "__main__":

    print main()