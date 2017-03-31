# Using cipher.txt, a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
# Encryption key consists of 3 lower case characters

# Lower case ASCII characters are in the range of 97-122. 
# Bitwise XOR operator is ^

def main():
    # Open the cipher
    cipher = open("Problem_059_Cipher.txt").read().replace("\n", "").split(",")

    # It is known that key is three letters that repeat cyclically, so split the cipher into three lists
    c1 = []
    p = 0
    while p < len(cipher):
        c1.append(cipher[p])
        p += 3

    c2 = []
    p = 1
    while p < len(cipher):
        c2.append(cipher[p])
        p += 3

    c3 = []
    p = 2
    while p < len(cipher):
        c3.append(cipher[p])
        p += 3

    # Determine the "space" character for each key set.
    # This assumes that space is the most common character in the message
    c1_space = max(set(c1), key=c1.count)
    c2_space = max(set(c2), key=c2.count)
    c3_space = max(set(c3), key=c3.count)

    # Space has the ascii value 32
    ascii_character = 32

    c1_key = int(c1_space) ^ ascii_character
    c2_key = int(c2_space) ^ ascii_character
    c3_key = int(c3_space) ^ ascii_character

    decoded = ""
    keys = [c1_key, c2_key, c3_key]
    for i in range(len(cipher)):
        decoded += chr(int(cipher[i]) ^ keys[i % 3])

    print decoded

    total = 0
    for c in c1:
        total += int(c) ^ c1_key
    for c in c2:
        total += int(c) ^ c2_key
    for c in c3:
        total += int(c) ^ c3_key

    return total


if __name__ == "__main__":

    print main()