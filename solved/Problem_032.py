# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

def main():
    products = []

    for a in range(2, 100):
        for b in range(a, (10000/a)):
            c = a * b
            product_string = str(a) + str(b) + str(c)
            if not "0" in product_string and len(product_string) == 9 and len(set(product_string)) == 9:
                products.append(c)
                print a, b, c

    return sum(list(set(products)))


if __name__ == "__main__":

    print main()