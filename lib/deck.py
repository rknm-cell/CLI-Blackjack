
class Deck:
    def __init__(self):
        from card import Card
        self._deck = []
        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, values))

    