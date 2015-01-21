pandigital = set(['1','2','3','4','5','6','7','8','9'])
pset = set()
for i in range(1,10):
    for j in range(1234,9877):
        if len(str(i)) + len(str(j)) + len(str(i*j)) == 9:
            multiplicand = set(list(str(i)))
            multiplier = set(list(str(j)))
            product = set(list(str(i*j)))
            test = product.union(multiplicand)
            test = test.union(multiplier)
            if test == pandigital:
                pset.add(i*j)

for i in range(12,99):
    for j in range(123,988):
        if len(str(i)) + len(str(j)) + len(str(i*j)) == 9:
            multiplicand = set(list(str(i)))
            multiplier = set(list(str(j)))
            product = set(list(str(i*j)))
            test = product.union(multiplicand)
            test = test.union(multiplier)
            if test == pandigital:
                pset.add(i*j)


print pset
print sum(pset)