# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# (9**5)*6 = 354295. (9**5)*7=413343. So it's not possible for the number to be greater than 354295.

def main():

    return reduce(lambda x,y:x+y, [a for a in range(2, 354295) if a == reduce(lambda x, y: x+y, [int(d)**5 for d in str(a)])])


if __name__ == "__main__":

    print main()