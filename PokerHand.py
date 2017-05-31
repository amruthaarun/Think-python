"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *


class PokerHand(Hand):
    
    labels = ["has_none", "two_pair", "three_of_a_kind", "straight", "flush", "full_house", "four_of_a_kind", "straight_flush"]

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    def rank_hist(self):
	self.ranks={}
	for card in self.cards:
	    self.ranks[card.rank]=self.ranks.get(card.rank,0)+1

    def has_pair(self):
	self.rank_hist()
	for val in self.ranks.values():
	    if val==2:
		return True
	return False
	
    def has_twopair(self):
	count=0
	self.rank_hist()
	for val in self.ranks.values():
	    if val==2:
		count+=1
	if count==2:
	    return True
	return False
    def has_three_of_kind(self):
	self.rank_hist()
	for val in self.ranks.values():
	    if val==3:
		return True
	return False
    def has_full_house(self):
	self.rank_hist()
	count=0
	for val1 in self.ranks.values():
	    for val2 in self.ranks.values():
		if val1>=3 and val2>=2:
		    return True
	return False
    


    def has_four_of_kind(self):
	self.rank_hist()
	for val in self.ranks.values():
	    if val==4:
		return True
	return False


    def has_straight(self):
	self.rank_hist()
	
    def classify(self):
	self.sas_hands=[]

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
	print "HAND ",i+1
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        print "HAS FLUSH\t:",hand.has_flush()
	print "HAS A PAIR OF CARDS\t:",hand.has_pair()
	print "HAS TWO PAIR OF CARDS\t:",hand.has_twopair()
	print "HAS THREE OF A KIND\t:",hand.has_three_of_kind()
	print "HAS FOUR OF A KIND\t:",hand.has_four_of_kind()
	print "HAS FULL HOUSE\t:",hand.has_full_house()

