import ipdb
from deck import Deck

values = {"A":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
class Player:
    def __init__(self):

        self.cards = []
        self.score = 0
        self.aces = 0

    def new_card(self, card):
        self.cards.append(card)
        self.score += values[card.number]
        if card.number == "A":
            self.aces += 1 # add to self.aces

    def ace_value(self):
        while self.score > 21 and self.aces:
            self.score -= 10
            self.aces -= 1
            

ipdb.set_trace()