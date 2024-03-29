# import ipdb
# import click

from deck import Deck
from player import Player

def main():
    print('         ♣♠◆♥ Bye bye ♣♠◆♥       ')
player = Player()
dealer = Player()
choice = 0
play_deck = Deck()
cardindex = 0


        
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
    


    print("")    
    print("1) Start a game")
    print("2) Game rules")
    print("3) Quit")
    
    choice = int(input())

    if choice == 1:
        choice = None
        print("")
        print("Starting game...")
        print("")
        dealer.game_start()
        print("Dealer's cards:")
        for card in dealer.cards:
            dealer.display_card(card)
        print("")
        print(f"Dealer's card value is: {dealer.value}")
        print("")
       
        player.game_start()
        
      
        print("Your cards:")
        
        for card in player.cards:
            player.display_card(card)
        print(f"Your hand value is {player.value}")
        print("")
        

        if dealer.value < 21 and player.value < 21:
            print("Do you want to 'hit' or 'stand'?")
            choice = str(input()) 
            while choice == "hit":
                print(len(player.new_deck.deck))
                player.new_card()
                for card in player.cards:
                    player.display_card(card)
                print(f"Your hand value is {player.value}")
                if player.value >= 21:
                    break
                print("Do you want to 'hit' or 'stand'?")
                choice = str(input()) 
            
            
        #dealer turn
        if player.value == 21:
            print("Blackjack!")
            print("You win!")
        elif dealer.value == 21:
            print("Dealer has Blackjack!")
        elif player.value > 21:
            print("You busted!")
            print("Game over")
        elif player.value < 21:
            dealer.dealer_turn()
            print("Dealers cards:")
            for card in dealer.cards:
                dealer.display_card(card)
            print(f"Dealers hand value: {dealer.value}")
            if dealer.value > 21:
                print("Dealer busted!")
                print("You win!")
            elif player.value > dealer.value:
                print("You win!")
            elif player.value < dealer.value:
                print("Dealer wins")
            else:
                print("Push")
            
        player.cards.clear()
            
        dealer.cards.clear()
        
        dealer.value = 0
        player.value = 0
        
    elif choice == 2:
        print("Game rules:")
        print("Blackjack Game Rules:")
        print('''
            Computer Dealer vs Human Player
        1. This is a game played between a Human Player and a Computer Dealer
        1. Goal is to have a value closer to 21 than the Dealer without going over 21
        2. Number cards from (2 - 10) are worth their number value.
        3. Face cards (Jack, Queen, King) are worth 10 value.
        4. Aces are worth 11 or 1, depending on what is more advantageous.
        5. Player can choose to HIT (draw another card from deck) or STAND (keep the current hand) on their turn.
        6. If Player's hand goes over 21, you BUST, then the Dealer wins.
        7. If the Player stands and hand is under 21, then its the Dealer's turn.
        8. The dealer must hit until their hand value is 17 or higher.
        9. If the dealer's hand goes over 21, they BUST, then Player wins the round.
        10. If the player's hand and the dealer's hand value both equals, it is a "TIE".
        11. If player's initial two cards adds up to 21 (ACE and a FACE card), it is BLACKJACK, and player wins the round.
        ''')

    elif choice == 3:
        print("Quitting program...")
print("   * * * Program terminated * * *")

if __name__ == '__main__':
    main()
