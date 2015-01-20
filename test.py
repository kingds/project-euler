from math import *

limit = 28123

def divisors(n):
    ds = set(d for d in range(2, int(sqrt(n))+1) if n%d == 0)
    ds |= set(n//d for d in ds)
    ds.add(1)
    return ds

abundants = [0]+[sum(divisors(i))>i for i in range(1, limit+1)]

sum2ab = set(i+j for i in range(1, limit+1) if abundants[i]
                 for j in range(i,limit-i+1) if abundants[j])

notsum2ab = set(range(1, limit+1)) - sum2ab

print sum(notsum2ab)