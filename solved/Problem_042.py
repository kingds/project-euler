# How many words in Problem_42_Words.txt are triangle words?

def word_score(word):
    return sum("ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter) + 1 for letter in word.upper())

def triangle_numbers(limit):
    triangle_numbers = []
    n = 1
    t = 0
    while t < limit:
        t = int(0.5*n*(n+1))
        triangle_numbers.append(t)
        n += 1
    return triangle_numbers

def main():
    words = open("Problem_042_Words.txt").read().replace('"', "").split(",")
    triangle_list = triangle_numbers(max(len(word) for word in words) * 26)
    count = 0
    for word in words:
        if word_score(word) in triangle_list:
            count += 1

    return count


if __name__ == "__main__":

    print main()