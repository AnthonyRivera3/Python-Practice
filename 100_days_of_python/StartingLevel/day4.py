#randomizer and lists
#this is the library for random number function
import random

#random numbers from a-b inculsive
#random.randint(a,b)

random_int = random.randint(10,20)
print(random_int)

#if I want to use information from other files in python all i have to do is import. 
#Lets say day1.py. I have to type import day1 . Then with the functions from day one if
#I want to use them all I have to do is do day1.functionname 

#This functions has 0 as inculsive and 1 as exculsive. It will only print numbers 0-0.99999etc. We could multiple it to get bigger floating point numbers
test = random.random() # * 10
print(test)

#prints a floating point value where A is <= N and N <=B. In other words inclusive a and b
test2 = random.uniform(1,2)
print(test2)

#Exercise 1

randomint = random.randint(0,1)
choice = input("Pick heads or Tails: ")

if randomint==0: 
    print("Heads wins")
else:
    print("Tails wins")

    #<------------------------------------------------------------------->

    #Lists: 
    ten = [".",".",".","."]
    
    ten.append("Hi")#adds 1 to a list

    ten.extend(["Hello","Hi"])#adds multiple values to the lists 
    print(ten)


#<------------------------------------------------------------------->

#Excerise 2

friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]

#random.choice() will print out a random element from the list inside the parenthisis
print(random.choice(friends))


#Nested list

#adding lists together

#Nested_list = [friends , ten]
#print(Nested_list)
#This prints out list in element 1 of nested_list and prints out position one inside that list
#print(Nested_list[1][1])

#Final project: 

choice1 = int(input("What do you choose? Type 0 for rock, 1 for Paper, 2 for Sissors.\n"))
computer_choices = [0, 1, 2]
CPU = random.choice(computer_choices)

if choice1 == CPU: 
    print(f"Computer chose: {CPU} ")
    print("draw!")
elif choice1 == 0 and CPU == 1:
    print(f"Computer chose: {CPU} ")
    print("Computer wins!")
elif choice1 == 1 and CPU == 2:
    print(f"Computer chose: {CPU} ")
    print("Computer wins!")
elif choice1 == 2 and CPU == 0:
    print(f"Computer chose: {CPU} ")
    print("Computer wins")
else:
    print(f"Computer chose: {CPU} ")
    print("Player wins!")
