#This file is dedicated to loops you!!

#in order to make a for loop we need to use the key works "for" and "in"
for colors in ["blue", "green", "yellow", "red", "purple"]:
    print(colors)


#creating a for loop that will print the elements of the range 10
for i in range(10):
    print(i)



#creating a range and having the for loop print them
l=list(range( 0,101,2))

for even_numbers in l:
    print(even_numbers)


#idx would be the i in a for loop for c++ and the range is how many times the loop will repeat. It is also important to notice how idx is also the condtion below
for idx in range(0,10,2):
 print(idx**2)

    
print("-------------------------------------------")

    #if else statement


a = 4
if a > 3:
   print(a)
else:
   print("wrong")


print("-------------------------------------------")

#This is an example of an else if statement

b = 7
if b == 8:
 print(True)
elif b == 7:
   print(b)
else: 
   print("None found")


print("-------------------------------------------")


#while loop

n=10

while n>-1:
   print(n)
   n-=1


print("-------------------------------------------")

#making a recursive function
#When you make a function you just need to use def and a name

m=5
def functiontest(m): 
   if m==0: return 1
   return m * functiontest(m-1)




def function(k):
   if k==0:
      return k
   
   
   print(function(0))