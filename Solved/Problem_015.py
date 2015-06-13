# How many paths through a 20 x 20 grid by moving only down and right from the top left corner to the bottom right corner?

from math import factorial

def main():
    grid_size = 20
    paths = factorial(2 * grid_size) / (factorial(grid_size))**2

    return paths


if __name__ == "__main__":

    print main()

