import click
from card import Card
from deck import Deck
from player import Player
from dealer import Dealer
def main():
    print('         ♣♠◆♥ Bye bye ♣♠◆♥       ')
player_hand = Player()
dealer_hand = Dealer()
choice = 0

cardindex = 0


        

while choice !=3:
    print('''                                                                                              
88888888ba   88                          88            88                          88         
88      "8b  88                          88            ""                          88         
88      ,8P  88                          88                                        88         
88aaaaaa8P'  88  ,adPPYYba,   ,adPPYba,  88   ,d8      88  ,adPPYYba,   ,adPPYba,  88   ,d8   
88""""""8b,  88  ""     `Y8  a8"     ""  88 ,a8"       88  ""     `Y8  a8"     ""  88 ,a8"    
88      `8b  88  ,adPPPPP88  8b          8888[         88  ,adPPPPP88  8b          8888[      
88      a8P  88  88,    ,88  "8a,   ,aa  88`"Yba,      88  88,    ,88  "8a,   ,aa  88`"Yba,   
88888888P"   88  `"8bbdP"Y8   `"Ybbd8"'  88   `Y8a     88  `"8bbdP"Y8   `"Ybbd8"'  88   `Y8a  
                                                    ,88                                     
                                                    888P"                                     
                    

    ''')
    
    # print(new_deck.deck)
    # print(Deck._deck)
    # print_card(0)

    
    print("1) Start a game")
    print("2) Game rules")
    print("3) Quit")
    choice = int(input())

    if choice == 1:
        print("Starting game...")
        Dealer.game_start
        Player.game_start
        #player turn
        print("hit or stand")
        while choice != "stand":
            Player.hit = input("hit")
            input()
        #dealer turn
        Dealer.dealer_turn
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