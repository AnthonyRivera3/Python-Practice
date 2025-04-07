#conditional statements, logical operations, code blocks and scope


#exercise 1

num = int(input("Enter a number and I will check if it is odd or even: #"))

if (num % 2) == 0:
    print("/nThe number is even")
else:
    print("/nThe number is odd")

print("\n\n\n<--------------------------------------------------------------------------->")

#pizza pie exercise 2

bill = 0
print("""Hello welcome to Tony's pie's! 
      A large pie is $25
      A medium pie is $20
      A small pie is $15
      """)

pie_size = input("\nWhat can I get for you? S M or L: ")
if pie_size == "S":
    bill=15
elif pie_size == "M":
    bill=20
else:
    bill=25
    
toppings = input("Would you like to add toppings? Y or N: ")
if(toppings=="Y"):
    if pie_size == "S":
        bill+=2
    elif pie_size == "M":
             bill+=3
    elif pie_size == "L":
                bill+=3

extra_cheese = input("Would you like to add any extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill+=1

print(f"Your total will be: ${bill}")

print("\n\n\n<--------------------------------------------------------------------------->")

#final exercise:

print("""              ______________________
           .-'|     |     |     |   `-.
         .'   |     |     |     |     `.
        /_____|_____|_____|_____|_______\
       |     ___                   ___   |
       |    |___|=================|___|  |
       |    |___|                 |___|  |
       |    |___|                 |___|  |
       |    |___|                 |___|  |
       |    |___|                 |___|  |
       |    |___|                 |___|  |
       |_______________________________|
       |_______________________________|
      /_________________________________\
     /___________________________________\
    |_____________________________________|
   /_______________________________________\
  (_________________________________________)
\n\n\n""")

print("Welcome to treasure Island, your mission is to find the treasure!")
decision = input("Do you wish to travel left or right?: ")
if decision == "left":
     decision = input("Would you like to swim or wait?: ")
     if decision == "wait":
        decision = input("Which door would you like to go through? red, yellow or blue: ")
     if decision == "yellow":
          print("You win you found the treasure!!")
     else:
          print("Game Over!")
else:
     print("Game Over!")
