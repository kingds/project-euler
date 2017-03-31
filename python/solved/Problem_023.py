# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def factors(n):    
    factor_list = reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
    return list(set(factor_list))

def abundant(n):
    return sum(factors(n)) - n > n

def sum_between(a, b):
    return int(0.5 * (b + a) * (b - a + 1)) - b - a

def main():
    # Create a list of abundant numbers and sums
    n = 12
    sums = []
    abundants = []
    while n < 20162:
        if abundant(n):
            abundants.append(n)
            for a in abundants:
                sum = a + n 
                if sum > 20162:
                    break
                sums.append(a + n)
        n += 1

    # Sort the list
    sums = sorted(list(set(sums)))
    sums.insert(0, 0)

    # Calculate the total of all integers not in the sums list
    total = 0
    for i in range(len(sums) - 1):
        if sums[i] > 28124:
            break
        total += sum_between(sums[i], sums[i+1])

    return total


if __name__ == "__main__":

    print main()