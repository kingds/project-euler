# Find the smallest cube for which exactly five permutations of its digits are cube.

def main():
    cube_dict = {}
    for n in range(10000):
        cube = n**3
        digits = "".join(sorted(str(cube)))
        try:
            cube_dict[digits].append(n)
        except KeyError:
            cube_dict[digits] = [n]

    for d in sorted(cube_dict.keys()):
        if len(cube_dict[d]) == 5:
            return min(cube_dict[d]) ** 3


if __name__ == "__main__":

    print main()