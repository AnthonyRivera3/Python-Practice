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

















player_money = 2000
print("Welcome to my game of BlackJack!!!!!\n\n")
answer = input("Are you ready to gamble??!??!?! 'y' or 'n': ")
if answer == 'y':
    print("\n\nGreat Lets get Started!")
    gambling_money = int(input(f"You have a total of ${player_money} to gamble: How much would you like to put on this round?: "))
else:
    print("See ya next time!")


