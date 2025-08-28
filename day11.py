"""
This is a blackJack game!
Rules Listed below:

-Goal add up your cards to the largest number without going over 21.
if you go over 21 it is considered a bust.
-Whoever hits 21 first wins or whoever loses first loses and the other person wins.
-J,Q,K = 10 
-ACE = 1 or 11 You decide weather or not you want 1 or 11.
-Dealer only has two cards and you can take as much as you want.
-If the dealer ends up with a hand smaller than 17 then they have to take another card
-The player has an option to hit or stand.

"""
import random

cards = {
    "A": [1,11],
    "Q": 10, 
    "K": 10,
    "J": 10,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10
} 










dealer = 100000000
player_money = 2000
print("Welcome to my game of BlackJack!!!!!\n\n")
answer = input("Are you ready to gamble??!??!?! 'y' or 'n': ")
if answer == 'y':
    print("\n\nGreat Lets get Started!")
    gambling_money = int(input(f"You have a total of ${player_money} to gamble: How much would you like to put on this round?: "))
else:
    print("See ya next time!")



def Round(player1, player2):    
    player1_stack = []
    dealer_stack = []

    print("\nPlayer 1:")
    player1 = RandomCardGenerator()
    print(f"Here is your card: {player1}\n")
    player1_stack.appened(player1)
    print("\nPlayer 1:")
    player1 = RandomCardGenerator()
    print(f"Here is your second card: {player1}\n")
    player1_stack.appened(player1)
    print("\nDealer:")
    player2 = RandomCardGenerator()
    print(f"Here is your card: {player2}\n")
    dealer_stack.appened(player2)
    player2 = RandomCardGenerator()
    dealer_stack.appened(player2)
    print(f"\nPlayer cards: {player1_stack}")
    print(f"\ndealer cards: {dealer_stack[0]}")
    player_1_sum = player1_stack[0] + player1_stack[1]
    dealer_sum = dealer_stack[0] + dealer_stack[1]
    
    if over_21_check(player_1_sum) == 1:
        print("player1 has hit over 21 You lost")

    if over_21_check(dealer_sum) == 1:
        print("Dealer has hit over 21 You Won")
        





    
    
    answer = print("player would you like to hit? 'y' or 'n': ")
    if answer == 'y':


def RandomCardGenerator():
    list_of_cards = list(cards.keys())
    random_card = random.choice(list_of_cards)
    return random_card

def over_21_check(player):
    if player > 21: 
        return 1
    else:
        return 0


def ace():
   answer = input("\nWould you like turn the Ace into a 1 or 11?: ")
   for 
