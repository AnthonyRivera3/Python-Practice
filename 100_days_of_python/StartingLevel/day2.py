#Data Types, Numbers, operations, type conversion, f-strings

#Notes:
#type() in parenthisis i can put data type or user input and the output will print the data type

print(type(2.0))
print(type(2))
print(type("hello"))
print(type(True))

#type conversion
print("345"+"456")
print(int("345")+ int("456"))

#different type erro solution

name = input("Enter your name:")
name = len(name)
#cannot just use name because its not concanated. We have to convert to a string in order to print
print("Number of letters for your name: " + str(name))

#rounding numbers
test_number = 2.211 
print(round(test_number, 2))
#           number       how many places i wanna round by


#f- strings do automatic converting
lets = 21

print(f"Hello i am anthony and I am {lets}")
#prints Hello i am anthony and I am 21


#creating a tip calculator

print("Welcome to the tip calculator!\n")
total = input("What was the total of the bill? $")
tip = input("\nHow much tip would you like to give? 10, 12, or 15? ")
amount_of_people = input("How many people to split the bill? ")
calculated_tip = (int(tip)/100)*float(total)
amount = (float(total) + calculated_tip)/int(amount_of_people)
print(f"\nEach person should pay: ${round(amount, 2)}")


