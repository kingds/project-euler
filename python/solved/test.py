

def winner(p1, p2):
	if p1 and p2:
		return 0
	if p1:
		return 1
	if p2: 
		return 2
	return 0

def sort(hand):
	order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
	return sorted(hand, key= lambda card: order.index(card[:-1]))
	

def sort_hand(hand):
	return sorted(hand, key=lambda card: order.index(card[:-1]))

def royal_flush(hand):
	p1 = len(set([card[-1] for card in hand[:5]])) == 1 and sorted(card[:-1] for card in hand[:5]) == ['10', 'A', 'J', 'K', 'Q']
	p2 = len(set([card[-1] for card in hand[5:]])) == 1 and sorted(card[:-1] for card in hand[5:]) == ['10', 'A', 'J', 'K', 'Q']
	
	return winner(p1, p2)

def straight_flush(hand):
	p1 = len(set([card[-1] for card in hand[:5]])) == 1 and "".join(card[:-1] for card in sort(hand)[:5]) in "23456789TQKA"
	p2 = len(set([card[-1] for card in hand[5:]])) == 1 and "".join(card[:-1] for card in sort(hand)[5:]) in "23456789TQKA"

	return winner(p1, p2)

def four_kind(hand):
	p1 = [card[-1] for card in hand[:5]]

def main():
	for hand in [hand.split(" ") for hand in open("Problem_054_Poker.txt").read().split("\n")]:
		if straight_flush(hand) > 0:
			print hand






if __name__ == "__main__":

	print main()
