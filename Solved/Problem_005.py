# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def main():
    # Create the list of divisors
    divisor_list = [19, 18, 17, 16, 15, 14, 13, 12, 11]

    # Calculate the multiple of the prime factors. The value must be a multiple of this number
    prime_divisor = 1
    for d in [19, 17, 13, 11, 7, 5, 3, 2]:
        prime_divisor *= d
    print prime_divisor

    # Iterate until divisible
    n = prime_divisor
    divisible = False
    while divisible == False:
        n += prime_divisor
        divisible = True
        for divisor in divisor_list:
            if n % divisor != 0:
                divisible = False
                break       

    # Print the result
    return  n

if __name__ == "__main__":

    print main()


