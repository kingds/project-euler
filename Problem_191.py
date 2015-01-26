import itertools

base_string = ""
base_string += "L" * 30 
base_string += "O" * 30 
base_string += "A" * 30

for p in itertools.permutations(base_string, 30):
	print p