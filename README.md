## Blackjack

The game of Blackjack:

This CLI requires click library:

pip install click

the game is run from cli.py

Components
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── card.py
    ├── cli.py
    ├── dealer.py
    ├── deck.py
    └── player.py
player.py
    Class Player:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.new_deck = Deck()
        self._bust = False
    def new_card(self):
        self.new_deck.shuffle()
        new_card = self.new_deck.deck.pop()
        self.cards.append(new_card)
        self.value += self.new_deck.values[new_card.number]
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
    def ace_value(self):
        ace_value = 11
        if self.value > 21:
            ace_value = 1
        
        return ace_value

dealer.py
from deck import Deck
class Dealer:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.new_deck = Deck()
        self._bust = False

    def new_card(self):
        self.new_deck.shuffle()
        new_card = self.new_deck.deck.pop()
        self.cards.append(new_card)
        self.value += self.new_deck.values[new_card.number]

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
        if self.value < 17:
            self.new_card()
    def ace_value(self):
        ace_value = 11
        if self.value > 21:
            ace_value = 1
        return ace_value
deck.py
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
    
cli.py
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
    