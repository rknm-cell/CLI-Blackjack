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
        # for card in self.new_deck.deck:
        #     print(card.number)
        # print(self.new_deck.deck)
        new_card = self.new_deck.deck.pop()
        self.cards.append(new_card)
        # print(new_card.number, "new card")
    
        
        # print(self.new_deck.values[new_card.number], "This is the value")
        self.value += self.new_deck.values[new_card.number]

        # print("Current value: ", self.value)
    
    def display_card(self, card):
        
        if len(str(card)) < 3:
            space = " "
        else:
            space = ""
        print('┌───────┐')
        print(f'| {card} {space}  |') 
        print('|       |')
        print('|       |') 
        print('|       |')
        print(f'|    {card}{space}|')
        print('└───────┘') 
    def game_start(self):
        while len(self.cards) < 2:
            self.new_card()
    
    def bust(self):
        if self.value > 21:
            self._bust = True
        else:
            self._bust = False
        return self._bust    
    # def hit(self):
    #     return self.new_card()

    def ace_value(self):
        for card in self.cards:
            if str(card)[0] == 'A' and self.value > 21:
                self.value -= 10
        return self.value
# ipdb.set_trace()
