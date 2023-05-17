import ipdb
import random
from deck import Deck
class Player:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.new_deck = Deck()
        self._bust = False
    
    # def print_card(self, hand):
        
    #     return 
        
    def new_card(self):
        self.new_deck.shuffle()
        # random_card = random.random(len(self.new_deck.deck))
        new_card = self.new_deck.deck.pop()
        self.cards.append(new_card)
        self.value += self.new_deck.values in self.new_deck.values
        
    def bust(self):
        if self.value > 21:
            self._bust = True
        else:
            self._bust = False
        return self._bust

    def game_start(self):
        while len(self.cards) < 2:
            return self.new_card()

    def set_value(self):
        pass

    def hit(self):
        return self.new_card

    def ace_value(self):
        ace_value = 11
        if self.value > 21:
            ace_value = 1
        
        return ace_value
# ipdb.set_trace()