import random

class Card(object):
    def __init__(self, suit, number):
        self.suit=suit
        self.number=number
        self.visib=False

    def flip(self):
        if self.visib==True:
            self.visib=False
        else:
            self.visib=True
        return self

    def displayCard(self):
        print self.suit, str(self.number)
        return ""


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        self.cards=[]
        suits = ['s','h','d','c']
        types = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        for card_suit in suits:
            for card_value in types:
                self.cards.append(Card(card_suit, card_value))
                # print card_suit, card_value
        return self
    def shuffle(self):
        random.shuffle(self.cards)
        return self
    def deal(self, player):
        if len(self.cards)==0:
            print "No more cards."
            return self
        player.hand.append(self.cards[-1])
        print player.hand
        self.cards.pop()
        return self

    def show_Deck(self):
        for i in self.cards:
            i.displayCard()
        return self

class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = []

    def draw(self,deck):
        if len(deck.cards)==0:
            print "No more cards."
            return self
        self.hand.append(deck.cards[-1])
        deck.cards.pop()
        return self

    def discard(self):
        self.hand.pop()

    def show_hand(self):
        for i in self.hand:
            i.displayCard()












Elliot_deck = Deck()

Elliot_deck.shuffle() #Deck.shuffle()

print "Cards in Deck:", len(Elliot_deck.cards)
ricky = Player("ricky")
Elliot_deck.deal(ricky).deal(ricky).deal(ricky)
print "---------------------"
print "Below is Ricky's Hand:"
print "---------------------"
ricky.show_hand()
print len(ricky.hand)
print "---------------------"
print "Cards in Deck:", len(Elliot_deck.cards)
print "---------------------", "below is the new deck"
Elliot_deck.build()
print len(Elliot_deck.cards)
