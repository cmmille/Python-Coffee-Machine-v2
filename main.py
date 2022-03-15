from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
coffee_menu = Menu()

coffee_input = ''
while not coffee_input == "off":
    coffee_input = input("What would you like? (espresso/latte/cappuccino)?\t")
    if coffee_input == "off":
        print("Turning machine off...\nGoodbye.")
    elif coffee_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = coffee_menu.find_drink(coffee_input)
        can_make = coffee_maker.is_resource_sufficient(drink)
        if can_make:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)