# How many n-digit positive integers exist which are also an nth power?

def main():
    l = []
    for a in range(1, 10):
        for b in range(100):
            if len(str(a**b)) == b:
                l.append(a**b)

    return len(set(l))


if __name__ == "__main__":

    print main()