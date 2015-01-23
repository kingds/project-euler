# Using cipher.txt, a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
# Encryption key consists of 3 lower case characters

# Lower case ASCII characters are in the range of 97-122. 



# Bitwise XOR operator is ^

cipher = open("Problem_059_Cipher.txt").read().replace("\n", "").split(",")

c_1 = []
p = 0
while p < len(cipher):
	c_1.append(cipher[p])
	p += 3

c_2 = []
p = 1
while p < len(cipher):
	c_2.append(cipher[p])
	p += 3

c_3 = []
p = 2
while p < len(cipher):
	c_3.append(cipher[p])
	p += 3

# for item in set(c_1):
# 	print item, c_1.count(item)
# print "fjsdfsdklsjldjghdfhdkljhsljdsl"

# for item in set(c_2):
# 	print item, c_2.count(item)
# print "fjsdfsdklsjldjghdfhdkljhsljdsl"

# for item in set(c_3):
# 	print item, c_3.count(item)
# print "fjsdfsdklsjldjghdfhdkljhsljdsl"

# c_1_space = 71
# c_2_space = 79
# c_3_space = 69

# for i in range(97, 123):
# 	if c_1_space ^ i == 32:
# 		print i
# 		break

# for i in range(97, 123):
# 	if c_2_space ^ i == 32:
# 		print i
# 		break

# for i in range(97, 123):
# 	if c_3_space ^ i == 32:
# 		print i
# 		break

c_1_key = 103
c_2_key = 111
c_3_key = 101

total = 0
for c in c_1:
	total += int(c) ^ c_1_key
for c in c_2:
	total += int(c) ^ c_2_key
for c in c_3:
	total += int(c) ^ c_3_key

print total


