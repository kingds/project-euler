# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

products = []
for n in permutations("123456789"):
	n = "".join(n)
	if int(str(n)[0]) * int(str(n)[1:5]) == int(str(n)[5:9]):
		products.append(int(str(n)[5:9]))
	if int(str(n)[0:2]) * int(str(n)[2:5]) == int(str(n)[5:9]):
		products.append(int(str(n)[5:9]))

print sum(set(products))