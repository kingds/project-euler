# Which starting number, under one million, produces the longest Collatz chain?

def main():
    tested = {1: 1}
    max_length = 0
    max_n = 0
    for n in range(2, 1000000):
        starting_n = n
        length = 1
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = (3 * n) + 1
            tested_value = tested.get(n)
            if tested_value: 
                length += tested_value
                tested[starting_n] = length
                break
            else:
                length += 1
        tested[starting_n] = length
        if length > max_length:
            max_length = length
            max_n = starting_n

    return max_n


if __name__ == "__main__":

    print main()

