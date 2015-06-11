# How many different ways can one hundred be written as a sum of at least two positive integers?

integers = range(1, 100)
ways = [0 for i in range(101)]
for i in integers:
    ways[i] += 1
    for a in range(i+1, 101):
        ways[a] += ways[a-i]
print ways
print ways[100]
