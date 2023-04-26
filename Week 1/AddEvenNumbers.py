#This code counts even numbers between chosen integers a and b

a = 0
b = 101

totalnumber = range(int(a), int(b))
evensum = 0

for number in totalnumber:
    if (number % 2) == 0:
        evensum += number

print(evensum)