#This program prompts the user for a number and, by checking the remainder after dividing by 2, tells the user
#if the number is even or odd.

number = int(input("Which number do you want to check? "))

if (number % 2) == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")
