from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneymachine = MoneyMachine()
coffeemaker = CoffeeMaker()
coffee_menu = Menu()

while True:
    options = coffee_menu.get_items()
    print("Welcome to our coffee machine.")
    choice = input(f"What would you like? ({options})\n").lower()

    if choice == "off":
        print("Turning off. See you later.")
        break
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()

    else:
        chosen_coffee = coffee_menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(chosen_coffee) == False:
            print("Sorry, not enough ingredients.")
        else:
            if moneymachine.make_payment(chosen_coffee.cost) == False:
                print("Sorry, not enough money. Refunded.")
            else:
                coffeemaker.make_coffee(chosen_coffee)



