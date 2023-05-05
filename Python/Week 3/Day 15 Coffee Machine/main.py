import os
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def espresso():
    global espressoprice
    """Dispense espresso or return error if insufficient resources"""
    if waterleft < 50:
        print("Sorry, there is not enough water.")
        return 1
    elif coffeeleft < 18:
        print("Sorry, there is not enough coffee.")
        return 1
    else:
        print(f"That will be {espressoprice}")


def latte():
    """Dispense latte or return error if insufficient resources"""
    global latteprice
    if waterleft < 200:
        print("Sorry, there is not enough water.")
        return 1
    elif milkleft < 150:
        print("Sorry, there is not enough milk.")
        return 1
    elif coffeeleft < 24:
        print("Sorry, there is not enough coffee.")
        return 1
    else:
        print(f"That will be {latteprice}")


def cappuccino():
    """Dispense cappuccino or return error if insufficient resources"""
    global cappuccinoprice
    if waterleft < 250:
        print("Sorry, there is not enough water.")
        return 1
    elif milkleft < 100:
        print("Sorry, there is not enough milk.")
        return 1
    elif coffeeleft < 24:
        print("Sorry, there is not enough coffee.")
        return 1
    else:
        print(f"That will be {cappuccinoprice}")

def payment():
    """Pay for the coffee"""

    global quarter
    global dime
    global nickel
    global penny
   
    
    quarterspaid = int(input("How many quarters are you paying?"))
    dimespaid = int(input("How many dimes are you paying?"))
    nickelspaid = int(input("How many nickels are you paying?"))
    penniespaid = int(input("How many pennies are you paying?"))
    amountpaid = float(quarter * quarterspaid + dime * dimespaid + nickel * nickelspaid + penny * penniespaid)
    return amountpaid

def insufficientpayment():
    print("Sorry, that's not enough money. Money refunded.")

def drainresources(coffee):
    """Drain resources according to the coffee selected"""
    global waterleft
    global milkleft
    global coffeeleft
    if coffee == "espresso":
        coffeeleft -= 18
        waterleft -= 50
    elif coffee == "latte":
        coffeeleft -= 24
        waterleft -= 100
        milkleft -= 150
    elif coffee == "cappuccino":
        coffeeleft -= 24
        waterleft -= 250
        milkleft -= 100

def returnchange(amountpaid, coffeeprice):
    if float(amountpaid) > float(coffeeprice):
        change = round(amount_paid - coffeeprice, 2)
        return change


waterleft = resources['water']
milkleft = resources['milk']
coffeeleft = resources['coffee']
    
quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01
espressoprice = MENU["espresso"]["cost"]
latteprice = MENU["latte"]["cost"]
cappuccinoprice = MENU["cappuccino"]["cost"]


while True:  
    drinkchoice = input("What would you like? (espresso/latte/cappuccino)\n").lower()
    if drinkchoice == "espresso":
        if espresso() == 1:
            drinkchoice = input("Anything else you would like?")
        drinkprice = espressoprice
            

    elif drinkchoice == "latte":
        if latte() == 1:
            drinkchoice = input("Anything else you would like?")
        drinkprice = latteprice
            

    elif drinkchoice == "cappuccino":
        if cappuccino() == 1:
            drinkchoice = input("Anything else you would like?")
        drinkprice = cappuccinoprice
    elif drinkchoice == "off":
        print("Goodbye!")
        break

    elif drinkchoice == ("report"):
        print(f"Water left: {waterleft}, Milk Left: {milkleft}, Coffee left: {coffeeleft}")
        drinkchoice = input("What coffee would you like?")

        

    amount_paid = payment()
    if amount_paid < drinkprice:
        insufficientpayment()
    change = returnchange(amount_paid, drinkprice)
    drainresources(drinkchoice)

    print(f"Here is your {drinkchoice}!")
    print(f"Returning change of {change}.")
    print(waterleft)
    input("Thanks for your purchase. please press enter to finish your transaction.")
    #    os.system("cls")


