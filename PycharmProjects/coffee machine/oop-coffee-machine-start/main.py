from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
mencard = Menu()
money = MoneyMachine()
cof = CoffeeMaker()
while 1:
    choice = input(f"Enter your flavor {mencard.get_items()}:")
    if choice.lower() == "report":
        cof.report()
        money.report()
    elif choice.lower() == "off":
        break
    else:
        coff_type = mencard.find_drink(choice.lower())
        if coff_type is not None:
            if cof.is_resource_sufficient(coff_type):
                if money.make_payment(coff_type.cost):
                    cof.make_coffee(coff_type)
                    print("Enjoy your Drink:")
                else:
                    print("Insufficient money!refunded: ")
            else:
                print("Insufficient resources!Money refunded:")
