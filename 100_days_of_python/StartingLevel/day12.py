import random

def game_entry():
    return input("Type 'easy' or 'hard' or if you wish to not play enter 1: ")

def play_round(max_try, random_number):
    guess = int(input("Make a guess: "))

    if guess == random_number:
        print("\nYou got it correct!!! 🎉\n")
        return -1  # special value means "win"
    
    max_try -= 1
    if max_try == 0:
        print(f"You lost 😢 The number was {random_number}")
        return 0  # no attempts left

    if guess > random_number:
        print("Too High. Try again.\n")
    else:
        print("Too Low. Try again.\n")

    print(f"You have {max_try} attempts left.\n")
    return max_try


# --- Main Program ---
print("Welcome to the number guessing game!\n")
print("I'm thinking of a number between 1 and 100.\n")

difficulty = game_entry()

if difficulty == 'hard':
    attempts = 5
elif difficulty == 'easy':
    attempts = 10
else:
    print("Exiting game.")
    exit()

random_number = random.randint(1, 100)

while attempts > 0:
    print(f"\nYou have {attempts} attempts remaining to guess the number.\n")
    attempts = play_round(attempts, random_number)

    if attempts == -1:  # player won
        break
