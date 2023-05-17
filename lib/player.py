class Player:
    def __init__(self):
        self.cards = []
        self.value = 0
        
        deck.draw_card(self)


    def new_card(self):
        pass

    def ace_value(self):
        ace_value = 11
        if self.value > 21:
            ace_value = 1
        pass