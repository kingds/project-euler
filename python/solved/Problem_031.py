# How many different ways can 2 pounds be made using any number of coins?

# Coins are 1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p

def number_of_ways(target, values, value_index):
    if value_index == 0:
        return 1
    current_value = values[value_index]
    count = 0
    while target >= 0:
        count += number_of_ways(target, values, value_index - 1)
        target -= current_value
    return count 

def main():

    return number_of_ways(200, [1, 2, 5, 10, 20, 50, 100, 200], 7)

if __name__ == "__main__":

    print main()