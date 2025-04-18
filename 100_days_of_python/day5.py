#for loops, range and code blocks

#sum function that allows you to get sum of list
#Exercise 1: Replicating the max function


nums = list(range(0,1502,2))

key = 0

for numbers in nums: 
    if numbers>0:
        key=numbers
#print(key)

#print("<---------------------------------------------------------------------------------->")

#Exercise 2 the guas challenge. Add all numbers up from a range of 1-100

number = 0
for gaus in range(1, 101):
 number +=gaus
 #print(number)

print("<---------------------------------------------------------------------------------->")


#Password generator final project

import random

Uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','10']
Signs = ['!','#','$''!','@','%','&','*']

password = []

U = int(input( "How many uppercase characters would you like in your password?: "))
amount = list(range(U))
L = int(input( "How many lowercase characters would you like in your password?: "))
amount1 = list(range(L))
S = int(input( "How many symbols characters would you like in your password?: "))
amount2 = list(range(S))
N = int(input("How many numbers would you like in your password?: "))
amount3 = list(range(N))

for key in amount:
   password += random.choice(Uppercase[::])


for key in amount1:
   password += random.choice(Lowercase[::])

for key in amount2:
   password += random.choice(Signs[::])

for key in amount3:
    password += random.choice(numbers[::])

random.shuffle(password)
realpassword = ""
for key in password:
    realpassword+=key

print("Your password is: ")
print(realpassword)


'''
print("<---------------------------------------------------------------------------------->")
print("\n")
print("\n")
print("\n")

#Creating same project with random order of charachters. Gone wrong corrdcted at top

All_possibilities = [Uppercase, Lowercase, Signs, numbers]

password = ""

U = int(input( "How many uppercase characters would you like in your password?: "))
amount = list(range(U))
L = int(input( "How many lowercase characters would you like in your password?: "))
amount1 = list(range(L))

N = int(input("How many numbers would you like in your password?: "))
amount3 = list(range(N))

S = int(input( "How many symbols characters would you like in your password?: "))
amount2 = list(range(S))

TotalChar = U + L + S + N

Testcase = list(range(0,TotalChar))
print(Testcase)
for key in Testcase:
    for key in All_possibilities:
        answer = random.choice(All_possibilities)
        if answer == Uppercase:
            for key in amount:
                Testcase[key] = random.choice(Uppercase[::])
        if answer == Lowercase:
            for key in amount1:
                Testcase[key] = random.choice(Lowercase[::])
        if answer == Signs:
            for key in amount2:
                Testcase[key] = random.choice(Signs[::])
        if answer == numbers: 
            for key in amount3: 
                Testcase[key]=random.choice(numbers[::])

print("Your password is: ")
print(Testcase)
print(password)
      
'''