# How many continued fractions for the square root of N have an odd period for N <= 10000.

# Solution makes use of the algebraic method found at http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html#section7.2.3

def period(n):  
    if (n**0.5).is_integer():
        return 0
    base = int(n**0.5)
    a = 1
    b = base
    c = n - b**2
    c_reduced = c
    length = 0
    while True:
        length += 1
        base = int(a * (n**0.5 + b) / c)
        a = c_reduced
        b = -1 * (b - (c_reduced * base))
        c = n - b**2
        c_reduced = c // a
        if c == c_reduced:
            return length

def main():
    count = 0
    for n in range(10001):
        if period(n) % 2 != 0:
            count += 1

    return count


if __name__ == "__main__":

    print main()