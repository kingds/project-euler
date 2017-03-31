# How many Lychrel numbers are there below ten-thousand?

def palindrome(n):
    for i in range(len(str(n))):
        if str(n)[i] != str(n)[-i - 1]:
            return False
    return True

def lychrel(n):
    i = 0
    while i < 50:
        i += 1
        n = int(str(n)) + int(str(n)[:: -1])
        if palindrome(n):
            return False
    return True

def main():
    count = 0
    for i in range(1, 10000):
        if lychrel(i):
            count += 1

    return count


if __name__ == "__main__":

    print main()