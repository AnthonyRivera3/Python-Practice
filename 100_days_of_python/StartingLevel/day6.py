#Todays task is functions, code blocks and while loops

#to create your own function you use def function_name(): 

def myfunc():
    print("Hello")
    print("Bye")

myfunc()


#function inside of a function

def myfuncX2():
    myfunc()
    myfunc()


print(myfuncX2())

num = 5

while num<10:
    num+=1
    print(True)
print(False)