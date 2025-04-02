#This is for Arrays in python]
#Lines 4-87 is lists practice

 
#A list in python starts from elements 0... In order to make one you just need a name for it and []
 #I can also put any data type inside of the List. A list can have different data types
MyfirstList = [1, "Hello", " \"Hi\"" ,3.7 , "27"]
#              0     1           2      3      4     

#When I print the length of the list it will print 5 because it starts from 1,2,3...
print(len(MyfirstList))



#When I print elements from the list one by one I use brackets and that is when you start from 0
print(MyfirstList[0])
print(MyfirstList[1])
print(MyfirstList[2])
print(MyfirstList[3])
print(MyfirstList[4])

#This will print starting from element 0. The 2 indicates to print 2 outputs moving up the List including 0. 0 is inclusive and 2 is exculsive
print(MyfirstList[0:2])

#This will print the rest of the list starting from the element selected. In this case it will start at element 2 then go to 3.4...end
print(MyfirstList[2:])

#This will print up to an end point. It will go up to the 4th element startign from the begining
print(MyfirstList[:4])

#This will print the whole List
print(MyfirstList[:])

print("\n")
print("\n")
print("\n")

print("-------------------------------------------")
#Deeper into Lists
#Lists will always be traversable by the other side I will show you an example

MySecondList = [1, 2, 3 ,4 , 5 , 6, 7, 8]
#Elements       0  1  2  3   4   5  6  7
#Elements      -8 -7 -6 -5  -4  -3 -2 -1
#The negative elements will always go start from the left and end on -1.

#The first number before the : is inclusive and the one after it exclusive
print(MySecondList[1:-2])
print(MySecondList[-6:-4])

print("-------------------------------------------")


#Im going to introduce another list where there is a thrid number. The third number is just to print every element in a skipping.
#So i can do every other element and that would 1 or every other other would be 2. Here is an example

MyThirdList = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 11, 12]

#these two are the same. They both indicate to iclude all elements 0-11. But notice how it is skipping by two elements inclusive
print(MyThirdList[0:12:2])
print(MyThirdList[0::2])

#This is indicating to traverse the list backwards from element 11 inclusive to the whole array by 2.
#Note: We have to use - when going backwards. In this case it was -2
print(MyThirdList[11::-2])


#Because it is starting incrementing by -1 it will print the array backwards. 
#If it is positive it will print it from begining to end
print(MyThirdList[::-1])
print(MyThirdList[::1])

#This gets the size of the array and divides it by 2. The answer is 6. So then it goes from element 6 to the beginning of the array backwards
print(MyThirdList[len(MyThirdList)//2::-1])


print("-------------------------------------------")

#Pulling specific characters out of a string using the list references

Stringlist = "abcdefghijklmnopqrstuvwxyz"
print(len(Stringlist))

print(Stringlist[0:])
print(Stringlist[0::2])

#printing alphabet backwards  
print(Stringlist[::-1]) 

print("-------------------------------------------")

#Range practice
#When you make a range it is like your making a list but without manually typing it
#Ranges are made with a name = list(range(...)) 
#A range has the same ideology a list main differnece is how you create one. Instead of ":" it is ","

MyfirstRange = list(range(10))
print(MyfirstRange)


#Im going to make a range that has elements starting from 1000 to 1100 going by 10's

PracticeRange = list(range(1000, 1101, 10 ))
print(PracticeRange)

print("-------------------------------------------")


