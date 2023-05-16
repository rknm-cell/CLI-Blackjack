import click
from card import Card
def main():
    print('         ♣♠Bye bye◆♥       ')

choice = 0
while choice !=3:
    print("*Blackjack*")
    print(Card.number)
    print(" ----    ----")
    print(f"| {Card.number[0]}{Card.suit[0]} |  | {Card.number[12]}{Card.suit[2]} |")
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