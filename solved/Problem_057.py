# In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator? 

def main():
    (n0, n1, d0, d1) = (1, 3, 1, 2)
    count = 0
    for i in range(1000):
        n2 = 2*n1 + n0
        d2 = 2*d1 + d0
        (n0, n1, d0, d1) = (n1, n2, d1, d2)
        if len(str(n2)) > len(str(d2)):
            count += 1

    return count


if __name__ == "__main__":

    print main()