# How many Sundays fell on the first of the month in the twentieth century?

# January 1 1901 was a Tuesday

# Starting information
day_of_week = 2

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sunday_first_count = 0

for year in range(1901, 2001):
	for item in days_per_month:
		if item == 28 & year%4 == 0:
			item = 29
		day_of_week = (day_of_week + item%7) % 7
		if day_of_week == 0:
			sunday_first_count += 1

print sunday_first_count



