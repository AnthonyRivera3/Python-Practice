#coffee Vending machine maker program

#Element 0 = water, Element 1 = coffee,  #Element 2 = milk
Coffee_choices = {
    '1': [50,18],
    '2': [200,24,150],
    '3': [250,24,100]
}










#prompting user to pick a flavor
ans = str(input(f"Welcome to Anthony's Coffee machine! What would you like? ('1' for Espresso/ '2' for Latte/ '3' for Cappuccino):"))
print(ans)
while (ans != '1') and (ans !='2') and (ans!='3'):
    ans = input("Invalid answer please try again. ('1' for Espresso/ '2' for Latte/ '3' for Cappuccino):")


