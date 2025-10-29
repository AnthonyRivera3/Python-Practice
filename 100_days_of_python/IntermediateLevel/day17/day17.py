#Creating classes and using them in our final project

class User:
    #constructor
    def __init__(self):
        print("New user being created...")




#object
user_1 = User()
user_2 = User()
#attribute
user_1.id = "001"
user_1.username = "Anthony"

print(user_1.username)

#Attrubutes
user_2.id = "002"
user_2.username = "james"


print(user_2.username)




