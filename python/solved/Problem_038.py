# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

def main():
    max_pandigital = 0
    for i in xrange(9876):
        concat = str(i)
        n = 2
        while True:
            concat += str(n * i)
            n += 1
            if concat.find("0") > -1:
                break
            if len(concat) > 9:
                break
            if len(concat) != len(set(concat)):
                break
            if len(concat) == 9:
                if concat > max_pandigital:
                    max_pandigital = concat
                break

    return int(max_pandigital)


if __name__ == "__main__":

    print main()