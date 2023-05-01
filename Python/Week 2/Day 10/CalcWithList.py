def add(first_number, second_number):
    """Adds N1 and N2, return result"""
    return first_number+second_number
def subtract(first_number, second_number):
    """Subtracts N2 from N1, return result"""
    return second_number-first_number
def multiply(first_number,second_number):
    """Multiply N1 and N2, return result"""
    return first_number*second_number
def divide(first_number,second_number):
    """Divide N1 by N2, return result. if divide by 0, prompt user for valid number."""
    while second_number == 0:
        second_number=float(input("Error! Cannot divide by 0. Please enter a valid number for division.\n"))
    return first_number/second_number
operator_list = {
    "+": add, "-": subtract, "*": multiply, "/": divide
}
number1=0
print("Welcome to the calculator!")
while True:
    continuecalcs = True
    result = 0
    if number1 == 0:
        number1 = float(input("What's the first number?\n"))
    for key in operator_list:
        print(f"{key}")
    operatorstring = input("Choose an operator from above.\n")
    while operatorstring not in operator_list:
        operatorstring = input("Please enter one of the valid operators printed above.")
    operator = operator_list[operatorstring]
    number2 = float(input("What's the second number?\n"))
    if operatorstring == '/' and number2 == 0:
        number2 = float(input("Can't divide by zero!\n"))
    result = operator(number1,number2)
    print(f"{number1} {operatorstring} {number2} = {result}")
    calcprompt=input("Do you want to perform another calculation? Enter 'yes' to continue or 'no' to exit.").lower()
    if calcprompt == "yes":
        keepresult = input("Would you like to keep calculating with your result? Yes or No\n").lower()
        if keepresult == "yes":
            number1 = result
        else:
            number1 = 0
    else:
        print("Thanks for using my calculator. Have a nice day!")
        break




