# How many different ways can 2 pounds be made using any number of coins?

# Coins are 1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p

# coins = [200, 100, 50, 20, 10, 5, 2, 1]
# combo_count = 0

# import itertools

# combos = []
# for p in itertools.product(coins, repeat=3):
# 	if sum(p) == 200:
# 		combos.append(p)
# 		combo_count += 1
# print combos
# print len(set(combos))
# print combo_count

# count = 0
# for p100 in range(3):
# 	total = p100 * 100
# 	if total >= 200:
# 		count += 1
# 		break
# 	for p50 in range(5):
# 		total += p50 * 50
# 		if total >= 200:
# 			count += 1
# 			break
# 		for p20 in range(11):
# 			total += p20 * 20
# 			if total >= 200:
# 				count += 1
# 				break
# 			for p10 in range(21):
# 				total += p10 * 10
# 				if total >= 200:
# 					count += 1
# 					break
# 				for p5 in range(41):
# 					total += p5 * 5
# 					if total >= 200:
# 						count += 1
# 						break
# 					for p2 in range(101):
# 						total += p2 * 2
# 						if total >= 200:
# 							count += 1
# 							break

# print count

count = 0
for p200 in range(2):
	total = 200 - 
	for p100 in range(3):
		for p50 in range(5):
			for p20 in range(11):
				for p10 in range(21):
					for p5 in range(41):
						for p2 in range(101):
							count += 1
print count



