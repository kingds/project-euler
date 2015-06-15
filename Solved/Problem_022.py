# What is the total of all the names scores in the file?

def main():

    names = open("Problem_022_Names.txt").read().replace('"', "").split(",")
    names.sort()
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    total_score = 0
    for i in range(len(names)):
        score = 0
        name = names[i]
        for letter in name:
            score += letters.index(letter) + 1
        score *= i + 1
        total_score += score

    return total_score


if __name__ == "__main__":

    print main()