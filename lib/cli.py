import click
from card import Card
from deck import Deck
def main():
    print('         ♣♠Bye bye◆♥       ')
new_deck = Deck()
choice = 0
while choice !=3:
    print("*Blackjack*")
    
    # print(new_deck.deck)
    # print(Deck._deck)
    print(" ----    ----")
    print(f"| {new_deck.deck[0]} |  | {new_deck.deck[12]} |")
    print("|    |  |    |")
    print(" ----    ----")
    print("1) Start a game")
    print("2) Game rules")
    print("3) Quit")
    choice = int(input())

    if choice == 1:
        print("Starting game...")
    elif choice == 2:
        print("Game rules:")
    elif choice == 3:
        print("Quitting program...")
print("* * * Program terminated * * *")

if __name__ == '__main__':
    main()