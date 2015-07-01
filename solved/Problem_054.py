# File poker.txt contains 1000 poker hands. First five cards are player 1. Next five are player 2.
# How many hands does player 1 win?

order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def sort_hand(hand):
	return sorted(hand, key=lambda card: order.index(card[:-1]))

def royal_flush(hand):
	p1 = sort_hand(hand[:5])
	p2 = sort_hand(hand[5:])
	results = []
	for p in [p1, p2]:
		suit = p[0][-1]
		result = True
		for i in range(len(hand)):
			if p[i][:-1] != order[i+8] or p[i][-1] != suit:
				result =  False
				break
		results.append(result)
	if results.count(True) == 1:
		return results.index(True) + 1
	elif results.count(True) == 0:
		return 0
	elif results.count(True) == 2:
		if order.index(p1[-1][-1]) > order.index(p2[-1][-1]):
			return 1
		else:
			return 2

def straight_flush(hand):
	p1 = sort_hand(hand[:5])
	p2 = sort_hand(hand[5:])
	results = []
	for p in [p1, p2]:
		result = True
		for i in range(len(p) - 1):
			if order.index(p[i+1][:-1]) - order.index(p[i][:-1]) != 1 or p[i][-1] != p[i+1][-1:]:
				result = False 
				break
		results.append(result)
	if results.count(True) == 1:
		return results.index(True) + 1
	elif results.count(True) == 0:
		return 0
	elif results.count(True) == 2:
		if order.index(p1[-1][:-1]) > order.index(p2[-1][:-1]):
			return 1
		else:
			return 2

def four_kind(hand):
	p1 = sort_hand(hand[:5])
	p2 = sort_hand(hand[5:])
	results = []
	for p in [p1, p2]:
		result = True
		values = []
		for card in p:
			values.append(card[:-1])
		if max(values.count(value) for value in values) < 4:
			result = False
			break
		results.append[result]
	if results.count(True) == 1:
		return results.index(True) + 1
	elif results.count(True) == 0:
		return 0
	elif results.count(True) == 2:
		if order.index(p1[-2][:-1]) > order.index(p2[-2][:-2]):
			return 1
		else:
			return 2


def full_house(hand):
	p1 = sort_hand(hand[:5])
	p2 = sort_hand(hand[5:])
	results = []
	for p in [p1, p2]:
		result = False
		values = []
		for card in p:
			values.append(card[:-1])
		if len(set(values)) == 2 and values.count(values[0]) > 1:
			result = True
		results.append(result)
	if results.count(True) == 1:
		return results.index(True) + 1
	elif results.count(True) == 0:
		return 0
	elif results.count(True) == 2:
		if order.index(p1[-3][:-1]) > order.index(p2[-3][:-1]):
			return 1
		else:
			return 2	

def flush(hand):
	p1 = sort_hand(hand[:5])
	p2 = sort_hand(hand[5:])
	results = []
	for p in [p1, p2]:
		result = True
		suit = p[0][-1]
		for card in p:
			if card[-1] != suit:
				result = False
				break
		results.append(result)
	if results.count(True) == 1:
		return results.index(True) + 1
	elif results.count(True) == 0:
		return 0
	elif results.count(True) == 2:
		if order.index(p1[-1][:-1]) > order.index(p2[-1][:-1]):
			return 1
		else:
			return 2

def straight(hand):
	p1 = sort_hand(hand[:5])
	p2 = sort_hand(hand[5:])
	results = []
	for p in [p1, p2]:
		result = True
		for i in range(4):
			if order.index(p[i+1][:-1]) - order.index(p[i][:-1]) != 1:
				result = False
				break
		results.append(result)
	if results.count(True) == 1:
		return results.index(True) + 1
	elif results.count(True) == 0:
		return 0
	elif results.count(True) == 2:
		if order.index(p1[-1][:-1]) > order.index(p2[-1][:-1]):
			return 1
		else:
			return 2

def three_kind(hand):
	p1 = sort_hand(hand[:5])
	p2 = sort_hand(hand[5:])
	results = []
	for p in [p1, p2]:
		result = False	
		values = []
		for card in p:
			values.append(card[:-1])
		if len(set(values)) == 3 and max(values.count(value) for value in values) == 3:
			result = True
		results.append(result)
	if results.count(True) == 1:
		return results.index(True) + 1
	elif results.count(True) == 0:
		return 0
	elif results.count(True) == 2:
		if order.index(p1[-3][:-1]) > order.index(p2[-3][:-1]):
			return 1
		else:
			return 2

def two_pair(hand):
	p1 = sort_hand(hand[:5])
	p2 = sort_hand(hand[5:])
	results = []
	pair_values = []
	for p in [p1, p2]:
		result = False
		values = []
		for card in p:
			values.append(card[:-1])
		if len(set(values)) == 3 and max(values.count(value) for value in values) == 2:
			result = True
		i = 4
		while i > -1:
			if values.count(values[i]) == 2:
				pair_values.append(values[i])
				break
			i -= 1
		results.append(result)
	if results.count(True) == 1:
		return results.index(True) + 1
	elif results.count(True) == 0:
		return 0
	elif results.count(True) == 2:
		if pair_values[0] > pair_values[1]:
			return 1
		else:
			return 2

def pair(hand):
	p1 = sort_hand(hand[:5])
	p2 = sort_hand(hand[5:])
	results = []
	pair_values = []
	for p in [p1, p2]:
		result = False
		values = []
		for card in p:
			values.append(card[:-1])
		if len(set(values)) == 4 and max(values.count(value) for value in values) == 2:
			for value in values:
				if values.count(value) == 2:
					pair_values.append(value)
					break
			result = True
		results.append(result)
	if results.count(True) == 1:
		return results.index(True) + 1
	elif results.count(True) == 0:
		return 0
	elif results.count(True) == 2:
		if pair_values[0] > pair_values[1]:
			return 1
		else:
			return 2



def winner(hand):
	if royal_flush(hand) != 0:
		return royal_flush(hand)
	if straight_flush(hand) != 0:
		return straight_flush(hand)
	if four_kind(hand) != 0:
		return four_kind(hand)
	if full_house(hand) != 0:
		return full_house(hand)
	if flush(hand) != 0:
		return flush(hand)
	if straight(hand) != 0:
		return straight(hand)
	if three_kind(hand) != 0:
		return three_kind(hand)
	if two_pair(hand) != 0:
		return two_pair(hand)
	if pair(hand) != 0:
		print hand
		return pair(hand)
	p1 = sort_hand(hand[:5])
	p2 = sort_hand(hand[5:])
	if order.index(p1[-1][:-1]) > order.index(p2[-1][:-1]):
		return 1
	else:
		return 2

def main():
	hands = []
	for hand in open("Problem_054_Poker.txt").read().split("\n"):
		hands.append(hand.split(" "))
	order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
	p1_wins = 0
	p2_wins = 0
	for hand in hands:
		if winner(hand) == 1:
			p1_wins += 1
		elif winner(hand) == 2:
			p2_wins += 1

	return p1_wins


if __name__ == "__main__":

	print main()











