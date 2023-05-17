class Card:
    suits = ("♥","◆","♣","♠")
    numbers = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
    
    
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    
    def __str__(self):
        return self.number + self.suit
        
        
        

    
        
        
    
        



    