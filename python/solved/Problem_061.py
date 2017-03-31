# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.

from itertools import permutations

def triangle(n):
    return int(0.5 * n * (n + 1))

def square(n):
    return int(n ** 2)

def pentagonal(n):
    return int(0.5 * n * (3*n - 1))

def hexagonal(n):
    return int(n * (2*n - 1))

def heptagonal(n):
    return int(0.5 * n * (5*n - 3))

def octagonal(n):
    return int(n * (3*n - 2))

def cyclic(a, b):
    if str(a)[-2:] == str(b)[:2]:
        return True
    return False

def main():

    # Create lists for all the figurative numbers
    triangles = [triangle(n) for n in range(1, 1000) if 1000<triangle(n)<10000]
    squares = [square(n) for n in range(1, 100) if 1000<square(n)<10000]
    pentagonals = [pentagonal(n) for n in range(1, 100) if 1000<pentagonal(n)<10000]
    hexagonals = [hexagonal(n) for n in range(1, 100) if 1000<hexagonal(n)<10000]
    heptagonals = [heptagonal(n) for n in range(1, 100) if 1000<heptagonal(n)<10000]
    octagonals = [octagonal(n) for n in range(1, 100) if 1000<octagonal(n)<10000]

    # Get all the permutations of the lists, so that all the possible cyclic orders will be checked
    checklist = [octagonals, heptagonals, hexagonals, pentagonals, squares, triangles]
    checklists = list(permutations(checklist))

    # Check all values
    for checklist in checklists:
        checklist = list(checklist)
        for start_value in checklist.pop(0):
            check_value = start_value
            cyclic_values = [start_value]
            for figurate_list in checklist:
                start_value = start_value
                for item in figurate_list:
                    if cyclic(check_value, item):
                        cyclic_values.append(item)
                        check_value = item
                        break
            if len(cyclic_values) == 6:
                if cyclic(cyclic_values[5], start_value):
                    return sum(cyclic_values)


if __name__ == "__main__":

    print main()