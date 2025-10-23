# day 13 debugeer

# from random import randint

# dice_images = [1,2,3,4,5,6]
# dice_num =randint(a:1, b:6)
# print(dice_images[dice_num])


from random import randint

dice_images = [1,2,3,4,5,6] 
dice_num =randint( 0, 5 ) #element 0-5 in dice images
print(dice_images[dice_num])


#Try and except is like a if staement for errors. If we get a value error meaning we cant put "string in an int"
#This error will prompt the user to countinue and try again if they messed up on their end. 
# try input twelve then 12, 19
try: 
    age  = int(input("How old are you"))
except ValueError: 
    print("type new number invalid")
    age  = int(input("How old are you"))


if age >= 18:
    print(f"You can drive at {age}. ")


    #debugger use. We use the debugger by clicking the red dot to the left of the line. debugger will start showing
    #behind the scenes what is going on and where youre variables get stored and how they change.



def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print([number])
