# 70 colored balls are placed in an urn, 10 for each color of the rainbow
# What is the expected number of distinct colors in 20 randomly picked balls?

from itertools import combinations

def main():
	all_balls = []
	for i in range(1, 8):
		all_balls += [i] * 10

