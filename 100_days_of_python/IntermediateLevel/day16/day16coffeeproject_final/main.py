from menu import Menu
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



#Objects
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()



var = True



while var:
    options = menu.get_items()
    choice = input(f"What would you like ({options}: )")
    if choice == 'off':
        var == False
    elif choice == "report":
        print(money_machine.report())
        print(coffee_maker.report())
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink): 
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

