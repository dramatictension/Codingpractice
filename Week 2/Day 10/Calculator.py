def add(n1, n2):
    """Adds two values and returns the sum"""
    return n1+n2
def subtract(n1, n2):
    """Subtracts n2 from n1 and returns the result"""
    return n2-n1
def multiply(n1, n2):
    """Multiplies n1 and n2 and returns the result"""
    return n1*n2
def divide (n1, n2):
    """divides n1 by n2 and returns the result"""
    while n2 == 0:
        print("Syntax error! Please do not try to divide by 0!")
        n2 = float(input("Divide by what? "))
    return n1/n2
number1 = 0

while True:
    if number1 == 0:
        number1 = float(input("What's the first number? "))
    operation = str(input("+\n-\n/\n*\nchoose an operation: "))
    number2 = float(input("What's the second number? "))
    result = ""
    morecalcs = "".lower()
    if operation == ("+"):
        result = add(number1, number2)
    elif operation ==("-"):
        result = subtract(number1, number2)
    elif operation ==("*"):
        result = multiply(number1, number2)
    elif operation ==("/"):
        result = divide(number1, number2)
    else:
        operation=str(input("Please enter one of the four operations."))
    print(f"{number1} {operation} {number2} = {result}")
    morecalcs = input("Want to keep going? Y or N\n")
    if morecalcs == "y":
        keepnumber1 = input("Would you like to keep calculating using your result? Y or N" ).lower()
        if keepnumber1 == "y":
            number1 = result  
        else:
            number1 = 0
    if morecalcs == "n":
        print("Thanks for using the calculator. Have a nice day!")
        break
