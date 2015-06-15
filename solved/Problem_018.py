# Find the maximum total of moving on a path down the triangle through adjacent numbers

def main():
    # Create the triangle list from the raw values
    triangle_raw = open("Problem_018_Triangle.txt").read()
    triangle_rows = triangle_raw.split("\n")
    triangle = []
    for row in triangle_rows:
        triangle.append(row.split(" "))

    # Calculate the maximum total
    max_total = 0
    for path in range(2**14):
        position = 0
        total = int(triangle[0][0])
        for row in range(14):
            if not path & 2**row:
                position += 1
            total += int(triangle[row+1][position])
        if total > max_total:
            max_total = total

    return max_total


if __name__ == "__main__":

    print main()