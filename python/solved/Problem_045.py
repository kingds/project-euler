# Find the next triagonal number after T-285 that is also pentagonal and hexagonal

def triangular(n):
    return n*(n+1)//2

def is_pentagonal(n):
    return ((((24*n) + 1)**0.5 + 1) / 6).is_integer()

def is_hexagonal(n):
    return (((8*n + 1)**0.5 + 1) / 4).is_integer()

def main():
    n = 286
    while True:
        t = triangular(n)
        if is_hexagonal(t) and is_pentagonal(t):
            return t
        n += 1

if __name__ == "__main__":

    print main()
