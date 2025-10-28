#Creating a Hangman project game
import random

words = ['panda', 'chicken', 'food', 'drink', 'games', 'fried' , 'bike', 'fruit', 'strawberry', 'monday', 'jello', 'music', 'computer' ]

print("Hello Welcome player!")
print("We will be playing Hangman!")
print("Guess the word you get 5 tries:")





testcase = 5
Game_word = random.choice(words)

decoy_word = list(range(len(Game_word)))
for key in decoy_word:
    decoy_word[key] = '_'

print(Game_word)
print(decoy_word)

guessing_word=""

decoy_list = []

while testcase!=0 and Game_word != guessing_word:
    guess = input("Guess a letter lowercase only:")
    if guess in Game_word:
        position = Game_word.index(guess)
        decoy_word[position] = guess
        guessing_word += guess
        decoy_list.append(position)
        print(decoy_list)
        print(decoy_word)
    else:
        testcase-=1
        print("You have ", testcase, " lives remaining")
        print(decoy_word)

if testcase == 0:
   print("You lose sorry!")
else:
   print("Congrats you have won!")



