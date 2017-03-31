
def possibly_pandigital(n):
    return len(set(str(n))) == len(str(n))
    return sorted(set(str(n)))

def definitely_pandigital(n):
    return sorted(set(str(n))) == [str(i) for i in range(10)]

def main():
    total = 0
    for a in range(17, 1000, 17):
        if not possibly_pandigital(a):
            continue
        for b in range(10):
            b = a + b*10**3
            if (b / 10**1) % 13 != 0 or not possibly_pandigital(b):
                continue
            for c in range(10):
                c = b + c*10**4
                if (c / 10**2) % 11 != 0 or not possibly_pandigital(c):
                    continue
                for d in range(10):
                    d = c + d*10**5
                    if (d / 10**3) % 7 != 0 or not possibly_pandigital(d):
                        continue
                    for e in range(10):
                        e = d + e*10**6
                        if (e / 10**4) % 5 != 0 or not possibly_pandigital(e):
                            continue
                        for f in range(10):
                            f = e + f*10**7
                            if (f / 10**5) % 3 != 0 or not possibly_pandigital(f):
                                continue
                            for g in range(10):
                                g = f + g*10**8
                                if (g / 10**6) % 2 != 0 or not possibly_pandigital(g):
                                    continue
                                for h in range(10):
                                    h = g + h*10**9
                                    if not definitely_pandigital(h):
                                        continue
                                    total += h

    return total



if __name__ == "__main__":

    print main()