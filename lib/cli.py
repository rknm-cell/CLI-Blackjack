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
        print("Starting game...")
        # Dealer.
        player.game_start()
        player.new_card()
        new_deck
        for card in player.cards:
            print(f'''
 ------ 
|      | 
|  {card}  | 
|      | 
 ------ ''')
            print(len(player.new_deck.deck))
        #player turn
        print("hit or stand")
        while choice != "stand":
            player_hand.hit = input()
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
ipdb.set_trace()





