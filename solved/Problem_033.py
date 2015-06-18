# Find the denominator of the product of the four fractions which might be incorrectly simplified.

def main():
    # Create the list of fractions
    fractions = []
    for n in range(10, 100):
        for d in range(n + 1, 100):
            for a in [(0, 0), (0, 1), (1, 0), (1, 1)]:
                if n % 10 != 0:
                    if int(str(n)[a[0]]) != 0 and int(str(d)[a[1]]) != 0:
                        if int(str(n)[1 - a[0]]) == int(str(d)[1 - a[1]]):
                            if float(n)/float(d) == float(str(n)[a[0]]) / float(str(d)[a[1]]):
                                fractions.append((n, d))
                                break

    # Get the product fraction
    numerator = 1
    denominator = 1
    for fraction in set(fractions):
        numerator *= fraction[0]
        denominator *= fraction[1]

    # Return the simplified denominator
    m = 1
    while (m * denominator) % numerator != 0:
        m += 1
    return (m * denominator) / numerator


if __name__ == "__main__":

    print main()