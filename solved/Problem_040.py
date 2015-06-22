# An irrational decimal fraction is created by concatenating the positive integers
# If d_n represents the nth digit of the fractional part, find d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000

def main():
    concat = ""
    n = 1
    while len(concat) <= 1000000:
        concat += str(n)
        n += 1

    return reduce(lambda x,y:x*y, [int(concat[10**i - 1]) for i in range(7)])

if __name__ == "__main__":

    print main()