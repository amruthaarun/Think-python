import random
class Card(object):
    
	suit_names=['Clubs','Diamonds','Hearts','Spades']
	rank_names=[None, 'Ace', '1', '2', '3', '4', '5', '6', '7', '8','9', '10', 'Jack', 'Queen', 'King']
	def __init__(self, suit=0, rank=2):
		self.suit = suit
		self.rank = rank
	
	def __str__(self):
		return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

	def __cmp__(self, other):
		t1 = self.suit, self.rank
		t2 = other.suit, other.rank
		return cmp(t1, t2)    

class Deck(object):
	def __init__(self):
		self.cards = []

        	for suit in range(4):
            		for rank in range(1, 15):
		        	card = Card(suit, rank)
		        	self.cards.append(card)

	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

	def add_card(self, card):
		self.cards.append(card)

	def pop_card(self):
		return self.cards.pop()
	
	def shuffle(self):
		random.shuffle(self.cards)
	
	def sort(self):
		self.cards.sort(Card.__cmp__)
	
	def deals_hand(self,hand_num,card_no):
		hands={}
		for i in range(hand_num):
			label="hand" +str(i+1)
			hand=Hand(label)
			hand.move_cards(self,card_no)
			hands[label]=hand
		
		return hands.items()
			
			

class Hand(Deck):
        def __init__(self, label=''):
		self.cards = []
		self.label = label

	def move_cards( hand,self, num):
		for i in range(num):
			hand.add_card(self.pop_card())
	

card1 = Card(2, 11)
print card1
deck = Deck()
print deck
deck.shuffle()
print "AFTER SHUFFLING\n", deck
print "\n\n DEALS WITH HANDS\n\n"

hands=deck.deals_hand(3,14)
for label,cards in hands:
	print label,"\n"
	print cards
	print " "
