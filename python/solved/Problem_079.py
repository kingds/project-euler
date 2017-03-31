# Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

keys = open("Problem_079_Keylog.txt").read().split("\n")

character_set = sorted(list(set("".join(keys))))
character_positions = []
for c in character_set:
	character_positions.append(0)

c1 = character_set[0]
for key in keys:
	if key.find(c1) > 0:
		c1 = key[0]

character_set.remove(c1)
c2 = character_set[0]
for key in keys:
	if key.find(c1) == -1 and key.find(c2) > 0:
		c2 = key[0]

character_set.remove(c2)
c3 = character_set[0]
for key in keys:
	if key.find(c1) == -1 and key.find(c2) == -1 and key.find(c3) > 0:
		c3 = key[0]

character_set.remove(c3)
c4 = character_set[0]
for key in keys:
	if key.find(c1) == -1 and key.find(c2) == -1 and key.find(c3) == -1 and key.find(c4) > 0:
		c4 = key[0]

character_set.remove(c4)
c8 = character_set[0]
for key in keys:
	if -1 < key.find(c8) < 2:
		c8 = key[2]


character_set.remove(c8)
c7 = character_set[0]
for key in keys:
	if -1 < key.find(c7) < 2 and key.find(c8) == -1:
		c7 = key[2]


character_set.remove(c7)
c6 = character_set[0]
for key in keys:
	if -1 < key.find(c6) < 2 and key.find(c7) == -1 and key.find(c8) == -1:
		c6 = key[2]

character_set.remove(c6)
c5 = character_set[0]

print c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8
