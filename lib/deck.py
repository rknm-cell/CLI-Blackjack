import ipdb
import random
from card import Card

class Deck:
    
    def __init__(self):
    
        self.deck = []
        self.suits = ("♥","◆","♣","♠")
        self.values = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")    
        
        # build our deck and add to our deck list
        for suit in self.suits:
            for value in self.values:
                created_card = Card(suit, value) 
                self.deck.append(created_card)

    # display our deck
    def show(self):
        for d in self.deck:
            d.show()
    
    # shuffle our deck
    def shuffle(self):
        random.shuffle(self.deck)

    # draw a card from the deck
    def draw(self):
        return self.deck.pop()
    
    def count(self):
        return len(self.deck)
# ipdb.set_trace()
    


    