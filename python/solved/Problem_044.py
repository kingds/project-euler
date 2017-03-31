# Find the pair of pentagonal numbers with a pentagonal sum and difference, with the minimal different between the two. 
# What is the difference between the two numbers?

def is_pentagonal(n):
    return ((((24*n) + 1)**0.5 + 1) / 6).is_integer()

def pentagonal(n):
    return (n * (3*n - 1)) / 2

def main():
    n = 0
    pentagonals = []
    while True:
        n += 1
        a = pentagonal(n)
        pentagonals.insert(0, a)
        for b in pentagonals:
            if is_pentagonal(a - b) and is_pentagonal(a + b):
                return a - b


if __name__ == "__main__":

    print main()