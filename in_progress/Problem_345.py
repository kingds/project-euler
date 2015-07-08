# The matrix sum of a matrix is the maximum sum attained by totaling 
# only one element from each row and column. 
# Find the matrix sum for the matrix in Problem_345_Matrix.txt

from itertools import permutations

def get_matrix():
	matrix = []
	with open("Problem_345_Matrix.txt") as matrix_file:
		for line in matrix_file.readlines():
			row = []
			for i in range(0, 60, 4):
				row.append(int(line[i : i+4]))
			matrix.append(row)
	return matrix

def main():
	# Get the matrix
	matrix = get_matrix()

	# Determine the maximum value in each row
	max_columns = []
	for i in range(15):
		row_maximum = max(matrix[i])
		max_columns.append(matrix[i].index(row_maximum))

	# Find out which maximum values overlap 
	used_columns = [c if max_columns.count(c)==1 else None for c in max_columns]
	print used_columns


if __name__ == "__main__":

	print main()