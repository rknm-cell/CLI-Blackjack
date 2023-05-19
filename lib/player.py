import ipdb
import click
from card import Card
from deck import Deck
from player import Player
from dealer import Dealer
def main():
    print('         ♣♠◆♥ Bye bye ♣♠◆♥       ')
player = Player()
player_hand = []
dealer = Dealer()
dealer_hand = []
choice = 0
new_deck = Deck()
cardindex = 0


        
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
        print(f'|   {card} {space}|')
        print('└───────┘') 
    def game_start(self):
        while len(self.cards) < 2:
            self.new_card()
    
    # print(new_deck.deck)
    # print(Deck._deck)
    # print_card(0)

    print("Welcome to Blackjack Simulator 2023®")
    print("")    
    print("1) Start a game")
    print("2) Game rules")
    print("3) Quit")
    choice = int(input())

    if choice == 1:
        print("Starting game...")
        # Dealer.
        player.game_start()
        # player.new_card()
        print(player.value)
        print("Your cards:")
        for card in player.cards:
            print(f'''
 ------ 
|      | 
|  {card}  | 
|      | 
 ------ ''')
            
        #player turn
        print("hit or stand")
        while choice != "stand":
            if input() == "hit":
                player.new_card
                
            input()
        #dealer turn
        Dealer.dealer_turn
        # while bust_status == False:
        if Player.value > Dealer.value:
            print("You win!")
        elif Player.value < Dealer.value:
            print("Dealer wins")
        else:
            print("Push")
        
        
    elif choice == 2:
        print("Game rules:")
    elif choice == 3:
        print("Quitting program...")
print("* * * Program terminated * * *")

if __name__ == '__main__':
    main()
# ipdb.set_trace()