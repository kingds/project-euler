# If all numbers from one to one thousand are written out, how many letters are used

def main():
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    compound_string = ""

    for i in range(1, 10):
        compound_string += units[i]
        compound_string += "\n"

    for teen in teens:
        compound_string += teen
        compound_string += "\n"

    for i in range(20, 100):
        compound_string += tens[i/10 - 1] + "-" + units[i%10]
        compound_string += "\n"

    for i in range(100, 1000):
        compound_string += units[i/100] + "-hundred"
        tens_value = i%100
        if 0 < tens_value < 10:
            compound_string += " and " + units[tens_value]
        elif 10 <= tens_value < 20:
            compound_string += " and " + teens[tens_value%10]
        elif 20 <= tens_value < 100:
            compound_string += " and " + tens[tens_value/10 - 1] + "-" + units[tens_value%10]
        compound_string += "\n"

    compound_string += "one thousand\n"

    compound_string = compound_string.replace(" ", "")
    compound_string = compound_string.replace("-", "")
    compound_string = compound_string.replace("\n", "")

    return len(compound_string)


if __name__ == "__main__":

    print main()