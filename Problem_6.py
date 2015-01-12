# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

number_list = range(1, 101)

square_of_sum = sum(number_list) * sum(number_list)

squares = []
for number in number_list:
	squares.append(number * number)

sum_of_squares = sum(squares)

difference = square_of_sum - sum_of_squares

print difference