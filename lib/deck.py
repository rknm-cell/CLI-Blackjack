import ipdb
import random
from card import Card

class Deck:
    
    def __init__(self):
    
        self.deck = []
        self.suits = ("♥","◆","♣","♠")
        self.numbers = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")    
        self.values = {"A":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}

        for suit in self.suits:
            for number in self.numbers:
                created_card = Card(suit, number)
                self.deck.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    
# ipdb.set_trace()
    


    