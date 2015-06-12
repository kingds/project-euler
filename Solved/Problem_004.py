# Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    palindrome = 0
    for a in range(999, 100, -1):
        for b in range(999, a, -1):
            product = str(a * b)
            if product == product[::-1]:
                if int(product) > palindrome:
                    palindrome = int(product)
                else:
                    break

    return palindrome

if __name__ == "__main__":

    print main()