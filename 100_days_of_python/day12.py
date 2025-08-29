#There is no block scope in python.
#If I wanna change global variables I can return the changed variables
attempts = []
wanna_play = 0

def game_entry():
    difficulty = input("Type 'easy' or 'hard' or if you wish to not play enter 1: ")


print("Welcome to the number guessing game!\n")
print("Im thinking of a number between 1 and 100.\n")
difficulty = game_entry()


while difficulty != 1:
    if difficulty == "hard":
        print("\n You have 5 attempts remaining to guess the number.\n")
        guess = input("Make a guess: ")
        
    elif difficulty == "easy":
        print("\n You have 10 attempts remaining to guess the number.\n")
        guess = input("Make a guess: ")
        
    else:
        difficulty = game_entry()
