# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0
# where each _ is a single digit

# Since the square ends in 0 it must be a multiple of 10, this means we know
# the ending of the square will be 900.
# Thus, n must end in 30 or 70

def check(n):
    n_squared = str(n**2)
    digits = "1020304050607080900"
    for i in range(0, 20, 2):
        if n_squared[i] != digits[i]:
            return False
    return True

def main():
    for d in range(10):
        min_range = int(int("1%s20304050607080900" % str(d)) ** 0.5) / 100 * 100 + 30
        max_range = int(int("1%s29394959697989990" % str(d)) ** 0.5) / 100 * 100
        n = min_range
        while n < max_range:
            if check(n):
                return n
            n += 40
            if check(n):
                return n
            n += 60

if __name__ == "__main__":

    print main()