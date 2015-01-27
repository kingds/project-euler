# How many different ways can one hundred be written as a sum of at least two positive integers?

coin = range(1, 100)
s = {i:0 for i in range(101)}
for c in coin:
    s[c] += 1
    for i in range(c+1, 101):
        s[i] += s[i-c]
print(s[100])