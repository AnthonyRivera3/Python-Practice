#making a hash map is like a set but with :. Imagine element Tom has A stored inside of it. To access 

grades = {

"Tom" : "A", 
"John" : "B" ,
"Peter" : "C" ,
"Jones" : "B" ,
"Alex" : "C" ,
"Adam" : "A" ,

}

print(grades)

#When we have hash map and seperate the contents with : that is like saying element Tom has A in the set grades.
print(grades["Tom"])


#This is a how to use a hash map.
for hello in grades:
     print(hello, grades[hello])



#This is how you add an element to a hash map
grades["Jason"] = "A+" 
print(grades)


#Factorial recursive function. Base case and return

def factorial(n):
     if n==0 or n==1:
          return 1
     return n* factorial(n-1)

