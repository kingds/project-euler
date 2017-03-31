# Peter has 9 4-sided dice (With sides 1, 2, 3, 4)
# Colin has 6 6-sided dice (With sides 1, 2, 3, 4, 5, 6)
# If they roll their dice and compare the totals, what is the probability
# that Peter wins? (To 7 decimal places)

from itertools import product

def main():
    peter_wins = 0
    count = 0
    for colin_sum in [sum(p) for p in product([1, 2, 3, 4, 5, 6], repeat=6)]:
        print count
        for peter_sum in [sum(p) for p in product([1, 2, 3, 4], repeat=9)]:
            count += 1
            if peter_sum > colin_sum:
                peter_wins += 1

    return float(peter_wins) / float(count)


if __name__ == "__main__":

    print main()