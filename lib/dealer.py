from deck import Deck
from game import Game
class Dealer:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.new_deck = Deck()
        self._bust = False
        self._stalemate = False
    
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
        print(f'''
 ------ 
|      | 
|  {card}  | 
|      | 
 ------ ''')
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
    def dealer_turn(self):
        while self.value < 17:
            self.new_card()
    def ace_value(self):
        ace_value = 11
        if self.value > 21:
            ace_value = 1
        
        return ace_value
        self.new_deck = Deck()
        self._bust = False
    
    # def print_card(self, hand):
        
    #     return 
        
    def new_card(self):
        self.new_deck.shuffle()
        # for card in self.new_deck.deck:
        #     print(card.number)
        # print(self.new_deck.deck)
        if len(self.new_deck.deck) >= 1:
            new_card = self.new_deck.deck.pop()
        else:
            # ends the program
            self._stalemate = True
            return
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
        print(f'|   {card} {space}|')
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
    def dealer_turn(self):
        while self.value < 17:
            self.new_card()
    def ace_value(self):
        ace_value = 11
        if self.value > 21:
            ace_value = 1
        
        return ace_value