from deck import Deck
from player import Player
class Dealer:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.dealer_deck = Deck()
        
        
    
    def dealer_turn(self):
        while self.value > 17:
            return self.draw_card
        else:
            return print("Dealer turn over")
        
    # def draw_card(self):
    #     pass
    