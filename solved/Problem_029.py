# How many distinct terms are in the sequence generated by a^b for 2 <= a <= 100 and 2 <= b <= 100?

def main():

    return len(set([x**y for x in range(2,101) for y in range(2,101)]))


if __name__ == "__main__":

    print main()