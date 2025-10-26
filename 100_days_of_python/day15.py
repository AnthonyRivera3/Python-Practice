#coffee Vending machine maker program
import sys

def report():
    print(f"Total Money Collected:{money}")
    print(f"Total  Water Left:{water}")
    print(f"Total Coffee Left:{coffee}")
    print(f"Total Milk Left:{milk}")
    print("\n"*5)


def price_calculator(coffee_type):
    pennie = 1
    nickel = 5
    dime   = 10
    quarter = 25
    total = 0

    espresso = 200
    latte = 250
    cappuccino = 300


    #espresso price calculator
    if coffee_type == '1':
        print("Your total is $2.00 enter change:\n")
        penny_total = int(input("Amount of pennies: "))
        nickel_total = int(input("Amount of nickels: "))
        dime_total = int(input("Amount of dime: "))
        quarter_total = int(input("Amount of quarter: "))
        total += (pennie*penny_total)
        total += (nickel*nickel_total)
        total += (dime*dime_total)
        total += (quarter*quarter_total)
        while total < espresso:
            print(f"You put in {total}. Your price is $2.00\n")
            penny_total = int(input("Amount of pennies: "))
            nickel_total = int(input("Amount of nickels: "))
            dime_total = int(input("Amount of dime: "))
            quarter_total = int(input("Amount of quarter: "))
            total += (pennie*penny_total)
            total += (nickel*nickel_total)
            total += (dime*dime_total)
            total += (quarter*quarter_total)
            if total > espresso:
                change = total-espresso
                print(f"You gave us more your change is: {change}\n")
                money += (total-change)
            elif total == espresso:
                money += total
        
    
    #latte price calculator
    elif coffee_type == '2':
    
        while total < latte:
            print(f"You put in {total}. Your price is $2.50\n")
            penny_total = int(input("Amount of pennies: "))
            nickel_total = int(input("Amount of nickels: "))
            dime_total = int(input("Amount of dime: "))
            quarter_total = int(input("Amount of quarter: "))
            total += (pennie*penny_total)
            total += (nickel*nickel_total)
            total += (dime*dime_total)
            total += (quarter*quarter_total)
            if total > latte:
                change = total-latte
                print(f"You gave us more your change is: {change}\n")
                money += (total-change)
            elif total == latte:
                money += total

    #cappuncino price calculator
    elif coffee_type == '3':
        while total < cappuccino:
            print(f"You put in {total}. Your price is $2.50\n")
            penny_total = int(input("Amount of pennies: "))
            nickel_total = int(input("Amount of nickels: "))
            dime_total = int(input("Amount of dime: "))
            quarter_total = int(input("Amount of quarter: "))
            total += (pennie*penny_total)
            total += (nickel*nickel_total)
            total += (dime*dime_total)
            total += (quarter*quarter_total)
            if total > cappuccino:
                change = total-cappuccino
                print(f"You gave us more your change is: {change}\n")
                money += (total-change)
            elif total == cappuccino:
                money += total

water = 1000
coffee = 1000
milk = 1000
money = 0
final_ans = 1

#Element 0 = water, Element 1 = coffee,  #Element 2 = milk
Coffee_choices = {
    'espresso': [50,18],
    'latte': [200,24,150],
    'cappuccino': [250,24,100]
}


while final_ans != 0:

    ans = str(input(f"Welcome to Anthony's Coffee machine! What would you like? ('1' for Espresso/ '2' for Latte/ '3' for Cappuccino / 'off' to turn off machine):"))
    print(ans)

    if ans == 'off':
        print("Coffee maching powering off")
        print("........\n"*10)
        sys.exit(0)

    if ans == 'report':
        report()
    
    while (ans != '1') and (ans !='2') and (ans!='3'):
        ans = input("Invalid answer please try again. ('1' for Espresso/ '2' for Latte/ '3' for Cappuccino / 'off' to turn off machine):")
        if ans == 'off':
            print("Coffee maching powering off")
            print("........\n"*10)
            sys.exit(0)
        elif ans == 'report':
            report()

    if ans == '1':
        water -= Coffee_choices["espresso"][0]
        coffee -= Coffee_choices["espresso"][1]
        price_calculator('1')
        print("\n"*5)
        print("Transaction complete:")
        print("Thankyou for your purchase enjoy!")
        print("\n"*5)

    elif ans == '2':
        water -= Coffee_choices["latte"][0]
        coffee -= Coffee_choices["latte"][1]
        milk -= Coffee_choices["latte"][2]
        price_calculator('2')
        print("\n"*5)
        print("Transaction complete:")
        print("Thankyou for your purchase enjoy!")
        print("\n"*5)

    elif ans == '3':
        water -= Coffee_choices["cappuccino"][0]
        coffee -= Coffee_choices["cappuccino"][1]
        milk -= Coffee_choices["cappuccino"][2]
        price_calculator('3')
        print("\n"*5)
        print("Transaction complete:")
        print("Thankyou for your purchase enjoy!")
        print("\n"*5)
    
    final_ans = int(input("\nWould you like anything else? ('0' for NO and '1' for YES)\n"))
    while (final_ans != 1) and (final_ans !=0):
        final_ans = (input("\nInput a possible choice ('0' for NO and '1' for YES)\n"))
        if final_ans == 0:
            sys.exit(0)
        if final_ans == 'report':
            report()


    
    




        
        
    

