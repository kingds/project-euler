# File poker.txt contains 1000 poker hands. First five cards are player 1. Next five are player 2.
# How many hands does player 1 win?

hands = []
for hand in open("Problem_054_Poker.txt").read().split("\n"):
	hands.append(hand.split(" "))

order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def winner(hand):
	p1 = hand[:5]
	p2 = hand[5:]

def sort(hand):
	return sorted(hand, key=lambda card: order.index(card[:-1]))

def straight_flush(hand):
	for i in range(len(hand) - 1):
		if order.index(hand[i+1][:-1]) - order.index(hand[i][:-1]) != 1 or hand[i][-1] != hand[i+1][-1:]:
			return False 
	return True

def royal_flush(hand):
	for i in range

print straight_flush(["9C", "TC", "JC", "QC", "KS"])

