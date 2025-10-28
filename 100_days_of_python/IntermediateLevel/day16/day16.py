#object oriented programming (OOP)

#creating a class in python
import day16_variablefile
import turtle


#When calling from another file in pyhton we need to use the file_name.vairable_name.
#Also we need to import the file name before hand
print(day16_variablefile.Random_variable)


import turtle

#Making an object. We made timmy an object in the Turtle class().
#We used turtle. to call the turtle function before we call the class

timmy = turtle.Turtle()

#This is the same as above just that when we use from the turtle function
#We import the class. Then we just set it equal without a dot operator
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("chartreuse")
timmy.forward(100)

#object.attribute
#car.speed


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


#Pyhton packages are packages of other peoples code that is developed by the community



#Using functions from pretty table to get a table
from prettytable import PrettyTable

table = PrettyTable()
#methods - using the functions inside of the class
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])
print(table)
#Attributes - changing data inside of our class
table.border = False
table.header_style = "upper"
print(table)
