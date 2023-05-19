from deck import Deck
class Game:

    def __init__(self):
        self.new_deck = Deck()
        

    def game_start(self):
        while len(self.cards) < 2:
            self.new_card()

    def new_card(self):
        self.new_deck.shuffle()
        new_card = self.new_deck.deck.pop()
        self.cards.append(new_card)
        self.value += self.new_deck.values[new_card.number]
    def game_start(self):
        while len(self.cards) < 2:
            self.new_card()