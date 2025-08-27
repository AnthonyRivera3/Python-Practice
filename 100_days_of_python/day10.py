#Todays project is calculator app

# def format_name(f_name, last_name):
#     full_name = f_name.title() + " " + last_name.title()
#     return full_name


# print(format_name("anthony", "rivera"))


#---------------------------------------------------------------------------------
#calculator project

def Addition(a,b):
    return a+b

def Subtraction(a,b):
    return a-b

def Multiplication(a,b):
    return a*b

def Division(a,b):
    return a/b

def Nothing(operator):
    call()


def call():
    num1 = input("What is the first number?: ")
    num2 = input("\nWhat is the second number?: ")
    operation = input(" \n '/' \n '*' \n '+' \n '-' \n Pick an operation: ")
    if operation == '/':
        answer = Division(num1,num2)
        print("\nThis is your answer: {answer}")
    if operation == '*':
        answer = Multiplication(num1,num2)
        print("\nThis is your answer: {answer}")
    if operation == '+':
        answer = Addition(num1,num2)
        print("\nThis is your answer: {answer}")
    if operation == '-':
        answer = Subtraction(num1,num2)
        print("\nThis is your answer: {answer}")
    if operation == '':
        Nothing()
    
    result1 = input("Would you like to do anything else with that answer? 'y', 'n': ")
    if result1 == 'y':
        call(answer)
