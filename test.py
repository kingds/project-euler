from itertools import combinations_with_replacement

def isPrime(n):
    if n <= 3:
        return n >= 2
    if n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

digits = []
cirque = set()
for i in range(1,7):
    digits.extend(['1','3','7','9'])
    for j in combinations_with_replacement(digits,i):
        num =''.join(j)
        if isPrime(int(num)):
            cyc = list(j)
            circular = True
            for k in j:
                cyc.append(k)
                cyc.pop(0)
                if not isPrime(int(''.join(cyc))):
                    circular = False
            if circular == True:
                cirque.add(int(''.join(cyc)))
print cirque
print len(cirque)