#Count from a to b-1, replace disivible by 3 but not 5 with "Fizz"
#divisible by 5 but not 3 with "Buzz"
#Divisible by both with "FizzBuzz"

a = 1
b = 101

hundred = range(int(a), int(b))
numbercurrent = 0

for number in hundred:
    if (number % 3) == 0 and (number % 5) == 0:
        print("FizzBuzz")
    elif (number % 3) == 0:
        print("Fizz")
    elif (number % 5) == 0:
        print("Buzz")

    else:
        print(str(number))
