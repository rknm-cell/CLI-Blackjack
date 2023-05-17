import ipdb
from deck import Deck
class Player:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.new_deck = Deck()
    
    
    def print_card(self, hand, cardindex):
        
        return print(f'''
 ------ 
|      | 
|  {hand.deck[cardindex]}  | 
|      | 
 ------ ''')
        
    def new_card(self):
        new_card = self.new_deck.pop()
        self.cards.append(new_card)

    def game_start(self):
        if len(self.cards) < 2:
            return self.new_card
    def hit(self):
        if self.value < 21:
            return self.new_card

    def ace_value(self):
        ace_value = 11
        if self.value > 21:
            ace_value = 1
        
        return ace_value
# ipdb.set_trace()
