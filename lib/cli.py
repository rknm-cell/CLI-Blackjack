import ipdb
import click
from card import Card
from deck import Deck
from player import Player
from dealer import Dealer
def main():
    print('         ♣♠◆♥ Bye bye ♣♠◆♥       ')
player = Player()
# player_hand = []
dealer = Dealer()
# dealer_hand = []
choice = 0
play_deck = Deck()
cardindex = 0
blackjack = False

        
print('''                                                                                              
    ,---,.    ,--,                                   ,-.                                            ,-.  
  ,'  .'  \ ,--.'|                               ,--/ /|                                        ,--/ /|  
,---.' .' | |  | :                             ,--. :/ |        .--.                          ,--. :/ |  
|   |  |: | :  : '                             :  : ' /       .--,`|                          :  : ' /   
:   :  :  / |  ' |       ,--.--.       ,---.   |  '  /        |  |.     ,--.--.       ,---.   |  '  /    
:   |    ;  '  | |      /       \     /     \  '  |  :        '--`_    /       \     /     \  '  |  :    
|   :     \ |  | :     .--.  .-. |   /    / '  |  |   \       ,--,'|  .--.  .-. |   /    / '  |  |   \   
|   |   . | '  : |__    \__\/: . .  .    ' /   '  : |. \      |  | '   \__\/: . .  .    ' /   '  : |. \  
'   :  '; | |  | '.'|   ," .--.; |  '   ; :__  |  | ' \ \     :  | |   ," .--.; |  '   ; :__  |  | ' \ \ 
|   |  | ;  ;  :    ;  /  /  ,.  |  '   | '.'| '  : |--'    __|  : '  /  /  ,.  |  '   | '.'| '  : |--'  
|   :   /   |  ,   /  ;  :   .'   \ |   :    : ;  |,'     .'__/\_: | ;  :   .'   \ |   :    : ;  |,'     
|   | ,'     ---`-'   |  ,     .-./  \   \  /  '--'       |   :    : |  ,     .-./  \   \  /  '--'       
`----'                 `--`---'       `----'               \   \  /   `--`---'       `----'              
                                                            `--`-'                                       

                    

    ''')
print("Welcome to Blackjack Simulator 2023®")
while choice !=3:
    

    
    # print(new_deck.deck)
    # print(Deck._deck)
    # print_card(0)

    
    print("")    
    print("1) Start a game")
    print("2) Game rules")
    print("3) Quit")
    
    choice = int(input())

    if choice == 1:
        choice = None
        print("Starting game...")
        
        dealer.game_start()
        print("Dealer's cards:")
        for card in dealer.cards:
            dealer.display_card(card)
        print(f"Dealer's card value is: {dealer.value}")
        print("")

        player.game_start()
        print("Your cards:")
        
        for card in player.cards:
            player.display_card(card)

        print(f"Your hand value is {player.value}")
        
        print("")

        print("Do you want to 'hit' or 'stand'?")
        choice = str(input()) 
        #player's turn
        if dealer.value != 21 or player.value != 21:
            while choice == "hit":
                
                
                player.new_card()
                for card in player.cards:
                    player.display_card(card)
                
                player.ace_value()
                print(f"Your hand value is {player.value}")
                if player.value >= 21:
                    break
                print("Do you want to 'hit' or 'stand'?")
                choice = str(input()) 
            
            
        #dealer turn
        while player.value < 21 and dealer.value < 21:
            dealer.dealer_turn()
            dealer.ace_value()
            print("Dealers cards:")
            for card in dealer.cards:
                dealer.display_card(card)
            print(f"Dealers hand value: {dealer.value}")
        if player.value == 21:
            print("Blackjack!")
        elif dealer.value == 21:
            print("Dealer has Blackjack!")
        if player.value < 21 and dealer.value < 21:
            if player.value > dealer.value:
                print("You win!")
            elif player.value < dealer.value:
                print("Dealer wins")
            else:
                print("Push")
        elif player.bust() == True:
            print("You busted!")
            print("Game over")
        elif dealer.bust() == True:
            print("Dealer busted!")
            print("You win!")
        #clearing lists and values    
        player.cards.clear()
        dealer.cards.clear()
        player.value = 0
        dealer.value = 0
        
        
        
    elif choice == 2:
        print("Game rules:")
        print("Blackjack Game Rules:")
        print('''How do you beat the dealer?

By drawing a hand value that is higher than the dealer’s hand value
By the dealer drawing a hand value that goes over 21.
By drawing a hand value of 21 on your first two cards, when the dealer does not.

How do you lose to the dealer? 

Your hand value exceeds 21.
The dealers hand has a greater value than yours at the end of the round''')
        print("")
    elif choice == 3:
        print("Quitting program...")
print("* * * Program terminated * * *")

if __name__ == '__main__':
    main()
# ipdb.set_trace()