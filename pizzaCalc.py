# Thos code asks users for options and then calculates the price of their order. Order prices are stored on top, and can be easily modified.
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

#If prices change, change these values to reflect.
smallprice = 15
mediumprice = 20
largeprice = 25
pepperoniSmall = 2
pepperoniMediumLarge = 3
cheese = 1

if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print ("Your final bill is: $" , smallprice + pepperoniSmall + cheese , ".")
        else:
            print ("Your final bill is: $" , smallprice + pepperoniSmall , ".")
    elif extra_cheese == "Y":
        print ("Your final bill is: $" , smallprice + extra_cheese , ".")
    else:
        print ("Your final bill is: $" , smallprice , ".")

elif size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print ("Your final bill is: $" , mediumprice + pepperoniMediumLarge + cheese , ".")
        else:
            print ("Your final bill is: $" , mediumprice + pepperoniMediumLarge , ".")
    elif extra_cheese == "Y":
        print ("Your final bill is: $" , mediumprice + extra_cheese , ".")
    else:
        print ("Your final bill is: $" , mediumprice , ".")

elif size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print ("Your final bill is: $" , largeprice + pepperoniMediumLarge + cheese , ".")
        else:
            print ("Your final bill is: $" , largeprice + pepperoniMediumLarge , ".")
    elif extra_cheese == "Y":
        print ("Your final bill is: $" , largeprice + extra_cheese , ".")
    else:
        print ("Your final bill is: $" , largeprice , ".")

else:
    print("Please only aswer in single, capital letters.")
