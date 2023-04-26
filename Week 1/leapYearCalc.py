# This program accepts a year input and calculates if the year is a leap year or not.
# Rules are as follows: If a year is divisible by 4, it is a leap year, unless it is divisible by 400 but not by 100

year = int(input("Which year do you want to check? "))

#Checks if number meets baseline to be included in flowchart, else it is not a leap year by default.
if (year % 4) == 0: 
    if (year % 100) == 0 and (year % 400) != 0: #Divisible by 100, but not by 400. Not leap year.
        print ("Not leap year.")
    elif (year % 100) == 0 and (year % 400) == 0: #Divisible by both 100 and 400, Leap year.
        print ("Leap year.")
    else:                                          #Divisible by 4 but not by either 100 or 400. Leap year.
        print("Leap year.")
else:                                               #Not diviisble by 4. Not leap year.
    print ("Not leap year.")