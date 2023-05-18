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


        

while choice !=3:
    print(new_deck.deck[0])
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
        choice = None
        print("Starting game...")
        dealer.game_start()
        print("Dealer's cards:")
        for card in dealer.cards:
            dealer.display_card(card)
        print(f"Dealer's card value is: {dealer.value}")
        print(len(dealer.new_deck))
        player.game_start()
        
        # player.new_card()
        # print(player.value)
        print("Your cards:")
        for card in player.cards:
            player.display_card(card)
        
        #player turn
        print(f"Your hand value is {player.value}")
        print(len(player.new_deck))
        print("Do you want to 'hit' or 'stand'?")
        choice = str(input())
        while choice != "stand":
            if choice == "hit":
                print(player.cards)
                player.new_card()
                
            
        #dealer turn
        dealer.dealer_turn()
        print("Dealers cards:")
        print(len(dealer.cards))
        for card in dealer.cards:
            dealer.display_card(card)
        print(f"Dealers hand value: {dealer.value}")
        if player.value == 21:
            print("Blackjack! You won")
        elif dealer.value == 21:
            print("Dealer has Blackjack!")
        if player.bust() or dealer.bust() == False:
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
        
        
    elif choice == 2:
        print("Game rules:")
    elif choice == 3:
        print("Quitting program...")
print("* * * Program terminated * * *")

if __name__ == '__main__':
    main()
# ipdb.set_trace()